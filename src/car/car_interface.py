# coding: utf-8

class CarInterface( ):
    def __init__(self, state, config):
        self.state = state
        self.config = config

    def start(self):
        pass

    def get_data(self):
        pass

    def send_action(self):
        pass

    def stop(self):
        pass
