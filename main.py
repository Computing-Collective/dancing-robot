# Group: 24
# Names: Divy, Elio, Kelvin, Matthew

# Project 1: Dancing Robot
# Hardware setup:
#   Servo left foot lower on GP19
#   Servo right foot lower on GP20
#   Servo left foot upper on GP18
#   Servo right foot upper on GP21

import time
import board
from digitalio import DigitalInOut, Direction, Pull
import pwmio
from adafruit_motor import servo

import board
import displayio  # https://docs.circuitpython.org/en/latest/shared-bindings/displayio/index.html

import busio

import digitalio
import time

import terminalio  # https://docs.circuitpython.org/en/latest/shared-bindings/terminalio/index.html

from adafruit_st7789 import (
    ST7789,
)  # https://docs.circuitpython.org/projects/st7789/en/latest/
from adafruit_display_text import (
    label,
)  # https://docs.circuitpython.org/projects/display_text/en/latest/api.html#adafruit_display_text.bitmap_label.Label
import vectorio


from robot import Robot
from constants import *
from lcd import *


def main():
    print("Setting up the robot...")
    # Set the onboard LED to on
    # Note: Onboard LED only works with our Pico H (Not W)
    led = DigitalInOut(board.LED)
    led.direction = Direction.OUTPUT
    led.value = True

    # Servo setup
    # Note: Tune pulse for specific servos
    pwm_lower_right_foot = pwmio.PWMOut(board.GP20, duty_cycle=DUTY_CYCLE, frequency=50)
    servo_lower_right_foot = servo.Servo(
        pwm_lower_right_foot, actuation_range=180, min_pulse=1000, max_pulse=2000
    )

    pwm_lower_left_foot = pwmio.PWMOut(board.GP19, duty_cycle=DUTY_CYCLE, frequency=50)
    servo_lower_left_foot = servo.Servo(
        pwm_lower_left_foot, actuation_range=180, min_pulse=1000, max_pulse=2000
    )

    pwm_upper_right_foot = pwmio.PWMOut(board.GP21, duty_cycle=DUTY_CYCLE, frequency=50)
    servo_upper_right_foot = servo.Servo(
        pwm_upper_right_foot, actuation_range=180, min_pulse=1000, max_pulse=2000
    )

    pwm_upper_left_foot = pwmio.PWMOut(board.GP18, duty_cycle=DUTY_CYCLE, frequency=50)
    servo_upper_left_foot = servo.Servo(
        pwm_upper_left_foot, actuation_range=180, min_pulse=1000, max_pulse=2000
    )

    """
    Instantiate the LCD
    """

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

    robot = Robot(
        servo_lower_right_foot,
        servo_lower_left_foot,
        servo_upper_right_foot,
        servo_upper_left_foot,
        LCDObj,
    )

    # Main logic loop
    print("Dancing Robot Started!")
    robot.reset()
    while True:
        robot.refresh()
        time.sleep(1 / REFRESH_RATE)


if __name__ == "__main__":
    main()
