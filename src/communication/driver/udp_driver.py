# coding: utf-8

from socket import socket, AF_INET, SOCK_DGRAM
from pickle import loads, dumps
from threading import Thread

class UdpServer():

    def __init__(self, config, state):
        self.ip_server = config['host_server']
        self.port_server = config['port_server']

        self.ip_client = config['host_client']
        self.port_client = config['port_client']

        self.bufferSize  = 512

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

            (ip, port) = packet[1]

            if ip != self.ip_client:
                continue

            msg = loads(packet[0])

            if self.state['policy']:
                msg["action"] = self.state["action"]

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
