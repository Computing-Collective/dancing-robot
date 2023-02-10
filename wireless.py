# Group: 24
# Names: Divy, Elio, Kelvin, Matthew

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
            return -1