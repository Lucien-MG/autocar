#!/bin/usr/python3
# coding: utf-8

from config import config
from donkey_car import DonkeyCar

car = DonkeyCar(config)

car.load_modules()

car.start()

car.run()

car.stop()