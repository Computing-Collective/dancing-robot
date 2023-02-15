# Group: 24
# Names: Divy, Elio, Kelvin, Matthew

# Project 1: Dancing Robot
# Hardware setup:
#   Servo left foot lower on GP19
#   Servo right foot lower on GP20
#   Servo left foot upper on GP18
#   Servo right foot upper on GP21

import time
from digitalio import DigitalInOut, Direction
import pwmio
from adafruit_motor import servo
import board
# https://docs.circuitpython.org/en/latest/shared-bindings/displayio/index.html
import displayio
import busio
import os
import ssl
import wifi
import socketpool
import adafruit_requests

from robot import Robot
from constants import *
from lcd import *
from led import *


def main():
    print("Setting up the robot...")
    # Set the onboard LED to on
    led = DigitalInOut(board.LED)
    led.direction = Direction.OUTPUT
    led.value = True
    frequency = 100

    # Servo setup
    # Note: Tune pulse for specific servos
    pwm_lower_right_foot = pwmio.PWMOut(
        board.GP20, duty_cycle=DUTY_CYCLE, frequency=frequency
    )
    servo_lower_right_foot = servo.Servo(
        pwm_lower_right_foot, actuation_range=180, min_pulse=1000, max_pulse=2000
    )

    pwm_lower_left_foot = pwmio.PWMOut(
        board.GP19, duty_cycle=DUTY_CYCLE, frequency=frequency
    )
    servo_lower_left_foot = servo.Servo(
        pwm_lower_left_foot, actuation_range=180, min_pulse=1000, max_pulse=2000
    )

    pwm_upper_right_foot = pwmio.PWMOut(
        board.GP21, duty_cycle=DUTY_CYCLE, frequency=frequency
    )
    servo_upper_right_foot = servo.Servo(
        pwm_upper_right_foot, actuation_range=180, min_pulse=1000, max_pulse=2000
    )

    pwm_upper_left_foot = pwmio.PWMOut(
        board.GP18, duty_cycle=DUTY_CYCLE, frequency=frequency
    )
    servo_upper_left_foot = servo.Servo(
        pwm_upper_left_foot, actuation_range=180, min_pulse=1000, max_pulse=2000
    )

    # Wifi setup

    wifi.radio.connect(
        os.getenv("CIRCUITPY_WIFI_SSID"), os.getenv("CIRCUITPY_WIFI_PASSWORD")
    )
    pool = socketpool.SocketPool(wifi.radio)
    requests = adafruit_requests.Session(pool, ssl.create_default_context())

    """
    Setup led outputs
    """

    # arms
    led_arm_right_red = DigitalInOut(board.GP6)
    led_arm_right_green = DigitalInOut(board.GP7)
    led_arm_right_blue = DigitalInOut(board.GP5)

    led_arm_right = (led_arm_right_red, led_arm_right_green, led_arm_right_blue)

    led_arm_left_red = DigitalInOut(board.GP26)
    led_arm_left_green = DigitalInOut(board.GP27)
    led_arm_left_blue = DigitalInOut(board.GP28)

    led_arm_left = (led_arm_left_red, led_arm_left_green, led_arm_left_blue)

    # from birds eye
    led_top_left = DigitalInOut(board.GP0)
    led_top_right = DigitalInOut(board.GP2)
    led_top_mid = DigitalInOut(board.GP1)

    # set pins as output
    led_arm_right_red.direction = Direction.OUTPUT
    led_arm_right_green.direction = Direction.OUTPUT
    led_arm_right_blue.direction = Direction.OUTPUT

    led_arm_left_red.direction = Direction.OUTPUT
    led_arm_left_green.direction = Direction.OUTPUT
    led_arm_left_blue.direction = Direction.OUTPUT

    led_top_left.direction = Direction.OUTPUT
    led_top_right.direction = Direction.OUTPUT
    led_top_mid.direction = Direction.OUTPUT

    # set initial values to all off
    led_top_left.value = False
    led_top_right.value = False
    led_top_mid.value = False

    led_arm_right[0].value = False
    led_arm_right[1].value = False
    led_arm_right[2].value = False

    led_arm_left[0].value = False
    led_arm_left[1].value = False
    led_arm_left[2].value = False

    """
    Instantiate the LED
    """
    led = LED(led_arm_right, led_arm_left, led_top_left, led_top_right, led_top_mid)


    # Release any resources currently in use for the displays
    displayio.release_displays()

    # set up GPIO
    tft_dc = board.GP8
    tft_cs = board.GP9
    spi_clk = board.GP10
    spi_mosi = board.GP11
    tft_res = board.GP12

    spi = busio.SPI(spi_clk, MOSI=spi_mosi)

    while not spi.try_lock():
        pass
    spi.configure(baudrate=24000000)  # Configure SPI for 24MHz
    spi.unlock()

    display_bus = displayio.FourWire(
        spi, command=tft_dc, chip_select=tft_cs, reset=tft_res
    )

    LCDObj = LCD(display_bus)

    """
    Instantiate the robot
    """

    robot = Robot(
        servo_lower_right_foot,
        servo_lower_left_foot,
        servo_upper_right_foot,
        servo_upper_left_foot,
        LCDObj,
        requests,
    )

    ########################################
    #           Main logic loop            #
    ########################################
    print("Dancing Robot Started!")
    robot.reset()
    while True:
        robot.refresh()  # Increment the robot counter
        led.refresh()  # Increment the led counter
        time.sleep(1 / REFRESH_RATE)


if __name__ == "__main__":
    main()
