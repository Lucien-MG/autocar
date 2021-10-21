# coding: utf-8

from car.car_interface import CarInterface 
from car.driver.donkey_mono_pi import SimClient

class DonkeyPi(CarInterface):
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
