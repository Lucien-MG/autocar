# coding: utf-8

import sys
import time
import importlib

from car.car_interface import CarInterface
from policy.policy_interface import PolicyInterface
from recorder.recorder_interface import RecorderInterface
from communication.communication_interface import CommunicationInterface

class DonkeyCar():

    def __init__(self, config):
        self.config = config

        self.state = {
            'run': True,
            'action': [0, 0, 0],
            'data': None,
            'record': False,
            'policy': False,
        }

        self.module = {
            'car': CarInterface(self.state, self.config),
            'policy': PolicyInterface(self.state, self.config),
            'recorder': RecorderInterface(self.state, self.config),
            'communication': CommunicationInterface(self.state, self.config),
        }

    def __start_module__(self, module_name):
        self.module[module_name].start()

    def __stop_module__(self, module_name):
        self.module[module_name].stop()

    def __load_module__(self, module_name):
        module_path = module_name + '.' + self.config[module_name]['module']
        module = None

        try:
            module = importlib.import_module(module_path)
        except BaseException as e:
            print("Error to load the module '" + module_path + "': " + str(e))

        constructor = getattr(module, self.config[module_name]['constructor'])
        self.module[module_name] = constructor(self.state, self.config[module_name]['config'])

    def start(self):
        for mod in self.module: self.__start_module__(mod)

    def stop(self):
        for mod in self.module: self.__stop_module__(mod)

    def load_modules(self):
        for mod in self.config: self.__load_module__(mod)

    def run(self):
        fps = 0
        start = time.time()

        while self.state['run']:
            self.module['car'].get_data()

            if self.state['policy']:
                self.module['policy'].step()

            if self.state['record']:
                self.module['recorder'].record()

            self.module['car'].send_action()

            self.module['communication'].send_data()

            fps += 1

        stop = time.time()
        delta = stop - start

        print("fps:", fps / delta)

