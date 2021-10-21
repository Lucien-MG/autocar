# coding: utf-8

class PolicyInterface():
    def __init__(self, state, config):
        self.config = config
        self.state = state

    def start(self):
        pass

    def step(self):
        pass

    def stop(self):
        pass