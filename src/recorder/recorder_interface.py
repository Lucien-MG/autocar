# coding: utf-8

class RecorderInterface():
    def __init__(self, state, config):
        self.state = state
        self.config = config 

    def start(self):
        pass

    def record(self):
        pass

    def stop(self):
        pass
