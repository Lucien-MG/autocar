# coding: utf-8

class CommunicationInterface():
    def __init__(self, state, config):
        self.state = state
        self.config = config 

    def start(self):
        pass

    def recv(self):
        pass

    def send_data(self):
        pass

    def stop(self):
        pass
