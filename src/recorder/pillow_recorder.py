from recorder.recorder_interface import RecorderInterface

import os
import json

from PIL import Image

class PillowRecorder(RecorderInterface):
    def __init__(self, state, config):
        self.state = state
        self.config = config

        self.count = 0

    def __save_image__(self, path, image):
        image.save(path, self.config['format'])

    def __save_json__(self, path, json_obj):
        with open(path, 'w') as outfile: json.dump(json_obj, outfile)

    def start(self):
        os.makedirs(self.config['path'], exist_ok=True)

    def record(self):
        image = Image.fromarray(self.state['data']['image'])
        data = {
                'steering': self.state['action'][0],
                'throttle': self.state['action'][1],
                'break': self.state['action'][2],
                'speed': self.state['data']['speed']
            }

        image_name = 'image_{:05d}.{}'.format(self.count, self.config['format'])
        json_name = 'json_{:05d}.json'.format(self.count)

        image_name = os.path.join(self.config['path'], image_name)
        json_name = os.path.join(self.config['path'], json_name)

        self.__save_image__(image_name, image)
        self.__save_json__(json_name, data)

        self.count += 1

    def stop(self):
        print("number of image recorded:", self.count)