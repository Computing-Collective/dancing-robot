import serial
import sys
import glob
import time
import requests
from constants import *


class PicoConnector:
    def __init__(self, serialPort=""):
        self.pico = None
        self.findPayload(
            serialPort
        )  # We need to establish a serial connection with the Pico

        if self.pico is None:
            print("[ERROR]    Divy     Couldn't find payload")
            raise Exception("Payload not found")

    def findPayload(self, serialPort):
        ports = []
        if serialPort == "":  # If no port is forced, get all the ports
            ports = self.getSerialPorts()
        else:
            ports.append(serialPort)
        print("[ALERT]    Divy     Serial Ports:", ports)

        for portName in ports:
            print("[ALERT]    Divy     Trying port", portName)
            pico = serial.Serial(
                port=portName, baudrate=9600, timeout=1.5, write_timeout=1.5
            )
            time.sleep(10)  # Giving time to Pico to wake up

            try:
                pico.write(
                    bytes("hello world", "utf-8")
                )  # Sending 'hello world' and expecting to get not throw an exception back
            except (
                serial.SerialTimeoutException
            ):  # If we get an exception, the port is not open
                continue

            data = pico.readline()
            data = data.decode("utf-8")
            data = data.rstrip()

            if data == "*":
                print("[ALERT]    Divy     Found Payload on port", portName)
                self.pico = pico
                return

    def getSerialPorts(self):
        """Lists serial port names
        :raises EnvironmentError:
            On unsupported or unknown platforms
        :returns:
            A list of the serial ports available on the system
        """
        if sys.platform.startswith("win"):
            ports = ["COM%s" % (i + 1) for i in range(256)]
        elif sys.platform.startswith("linux") or sys.platform.startswith("cygwin"):
            # this excludes your current terminal "/dev/tty"
            ports = glob.glob("/dev/tty[A-Za-z]*")
        elif sys.platform.startswith("darwin"):
            ports = glob.glob("/dev/tty.*")
        else:
            raise EnvironmentError("Unsupported platform")

        result = []
        for port in ports:
            try:
                s = serial.Serial(port)
                s.close()
                result.append(port)
            except (OSError, serial.SerialException):
                pass
        return result

    def listenSuccessMessage(self):
        while True:
            data = self.pico.readline()
            data = data.decode("utf-8")
            data = data.strip("\n")
            data = data.strip("\r")

            # '#' is -1
            if data == "#":
                data = -1

            # if data is sent
            if data != "" and data != "*":
                print(f"[REQUEST]    Divy    Sent: {data}")
                requests.post(url=MOVE_URL, json={"move": int(data)})


if __name__ == "__main__":
    try:
        pico = PicoConnector()
        pico.listenSuccessMessage()
    except Exception as ex:
        print(ex)
