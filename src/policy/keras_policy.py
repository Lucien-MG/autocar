from policy.policy_interface import PolicyInterface

from os import environ

import numpy as np
import tensorflow as tf

# The keras Controller Class.
class KerasPolicy(PolicyInterface):
    def __init__(self, state, config):
        super().__init__(state, config)

        # Avoid using GPU
        environ['CUDA_VISIBLE_DEVICES'] = '-1'

        self.model = tf.keras.models.load_model(self.config['path'])

    def __grayscale__(self, image):
        return tf.image.rgb_to_grayscale(image)

    def __transform__(self, image):
        return (image / 127.5) - 1

    def start(self):
        pass

    def step(self):
        data = self.state['data']

        image = tf.convert_to_tensor(np.array([data['image']]), dtype=tf.float32)
        speed = tf.convert_to_tensor([np.array([data['speed']])], dtype=tf.float32)

        args = { 'image': self.__transform__(self.__grayscale__(image)), 'speed': speed }

        result = self.model.call(args)

        self.state['action'] = result[0].numpy()
        self.state['action'][2] = 0.0

        print(self.state['action'])

    def stop(self):
        pass
