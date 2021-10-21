# coding: utf-8

from communication.communication_interface import CommunicationInterface
from fastapi import FastAPI

class WebCommunication():
    def __init__(self, state, config):
        self.state = state
        self.config = config

    def start(self):
        app = FastAPI()


        @app.get("/")
        async def root():
    return {"message": "Hello World"}

    def send_data(self):
        self.udp_server.send_msg(self.state['data'])

    def stop(self):
        self.udp_server.close()