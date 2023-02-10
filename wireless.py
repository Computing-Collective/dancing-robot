import os
import time
import ssl
import wifi
import socketpool
import adafruit_requests
from constants import *

# https://learn.adafruit.com/pico-w-wifi-with-circuitpython/pico-w-requests-test-adafruit-quotes


class Wireless:
    """Class to handle wireless communication with the server for demoing specific moves"""
    def __init__(self, requests):
        self.requests = requests

    def request_move(self):
        print("Requesting move from server")
        try:
            response = self.requests.get(MOVE_URL)
            output = response.text
            print(output)
            response.close()
            return int(output)
        except Exception as e:
            print("Error requesting move: {}".format(e))
            return None