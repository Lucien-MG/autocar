# coding: utf-8

from car.car_interface import CarInterface 
from car.driver.donkey_mono_pi import PiVideoStream

import pigpio

class DonkeyPi(CarInterface):
    def __init__(self, state, config):
        self.state = state
        self.config = config

    def start(self):
        self.video = PiVideoStream()
        self.video.start()

        self.pi = pigpio.pi()

        self.steering = 18
        self.throtling = 12

    def get_data(self):
        frame = self.video.read()
        self.state["data"] = {"image": frame}

    def send_action(self):
        steer = (self.state['action'][0] + 1.5) * 1000
        throt = (self.state['action'][1] + 1.5) * 1000

        self.pi.set_servo_pulsewidth(self.steering, steer)
        self.pi.set_servo_pulsewidth(self.throtling, throt)

    def stop(self):
        pass
