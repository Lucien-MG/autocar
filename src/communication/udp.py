# coding: utf-8

from communication.communication_interface import CommunicationInterface
from communication.driver.udp_driver import UdpServer

class UdpCommunication(CommunicationInterface):
    def __init__(self, state, config):
        self.state = state
        self.config = config

    def start(self):
        self.udp_server = UdpServer(self.config, self.state)

    def send_data(self):
        # self.udp_server.send_msg(self.state['data'])
        self.udp_server.send_msg({"image": "test"})

    def stop(self):
        self.udp_server.close()
