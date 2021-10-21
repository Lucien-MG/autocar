from car.car_interface import CarInterface 
from car.driver.donkey_simulation_driver import SimClient

from io import BytesIO
from PIL.Image import open
from base64 import b64decode
from numpy import asarray
from json import loads, dumps

class DonkeySimulation(CarInterface):
    def __init__(self, state, config):
        super().__init__(state, config)

    def start(self):
        self.client = SimClient((self.config['host'], self.config['port']))

    def get_data(self):
        self.state['data'] = self.client.get_msg()

    def send_action(self):
        action = self.state['action']

        json_control = dumps({'msg_type': 'control',
                              'steering': str(action[0]),
                              'throttle': str(action[1]),
                              'brake': str(action[2])})

        self.client.send_control(json_control)

    def pause(self):
        pass

    def stop(self):
        self.client.close()
