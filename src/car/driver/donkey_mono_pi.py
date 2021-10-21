# coding: utf-8

# import the necessary packages
import io
import time
import picamera

import numpy as np

from picamera.array import PiRGBArray
from threading import Thread

class PiVideoStream:
    def __init__(self, resolution=(320, 224), framerate=10):
        self.resolution = resolution
        self.framerate = framerate

        self.frame = np.zeros(resolution)
        self.stopped = False

    def start(self):
        Thread(target=self.update, args=()).start()
    
    def update(self):
        with picamera.PiCamera() as camera:
            camera.resolution = self.resolution
            camera.framerate = self.framerate

            rawCapture = PiRGBArray(camera, size=self.resolution)

            for f in camera.capture_continuous(rawCapture, format="rgb", use_video_port=True):
                self.frame = f.array[:,:,0]
                rawCapture.truncate(0)

                if self.stopped:
                    break

    def read(self):
        return np.asarray(self.frame, dtype=np.uint8)

    def stop(self):
        self.stopped = True
