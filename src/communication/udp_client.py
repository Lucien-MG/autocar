# coding: utf-8

import socket
import cv2
import time

from socket import socket, AF_INET, SOCK_DGRAM
from threading import Thread
from pickle import loads, dumps

class UdpServer():

    def __init__(self, config, state):
        self.ip_server = config['host_server']
        self.port_server = config['port_server']

        self.ip_client = config['host_client']
        self.port_client = config['port_client']

        self.bufferSize  = 65536

        self.run = True
        self.state = state

        try:
            self.socket_client = socket(family=AF_INET, type=SOCK_DGRAM)
            self.socket_server = socket(family=AF_INET, type=SOCK_DGRAM)
            self.socket_server.bind((self.ip_server, self.port_server))
        except Exception as e:
            raise(Exception("Could not launch the server: " + str(e)))

        self.msg_recv = [None, None]
        self.client = (None, None)

        self.listener_thread = Thread(target=self.__listener__)
        self.listener_thread.start()

    def __listener__(self):
        while self.run:
            packet = self.socket_server.recvfrom(self.bufferSize)

            ip, port = packet[1]

            if ip != self.ip_client:
                continue

            msg = loads(packet[0])

            for state in msg:
                self.state[state] = msg[state]

    def send_msg(self, msg):
        self.socket_client.sendto(dumps(msg), (self.ip_client, self.port_client))

    def close(self):
        self.run = False

        self.socket_client.sendto(b"close", (self.ip_server, self.port_server))

        self.listener_thread.join()

        self.socket_server.close()
        self.socket_client.close()

config = {
    'host_server': '127.0.0.1',
    'port_server': 9195,
    'host_client': '127.0.0.1',
    'port_client': 9196,
}

state = {}

client = UdpServer(config, state)

while not 'image' in state:
    time.sleep(1)

while True:
    image = cv2.cvtColor(state['image'], cv2.COLOR_BGR2RGB)
    image = cv2.resize(image, (854, 480))
    cv2.imshow('frame',image)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        client.send_msg({"run": False})
        break

    client.send_msg({
            "run": True,
            "action": [0.1, 0.6, 0.0]
        })

cv2.destroyAllWindows()