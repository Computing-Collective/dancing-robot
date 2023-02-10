import os
import time
import ssl
import wifi
import socketpool
import microcontroller
import adafruit_requests
from constants import *


class Wireless:
    def __init__(self):
        wifi.radio.connect(os.getenv('CIRCUITPY_WIFI_SSID'), os.getenv('CIRCUITPY_WIFI_PASSWORD'))
        pool = socketpool.SocketPool(wifi.radio)
        self.requests = adafruit_requests.Session(pool, ssl.create_default_context())

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