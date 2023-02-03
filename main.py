# Group: 24
# Names: Divy, Elio, Kelvin, Matthew

# Project 1: Dancing Robot
# Hardware setup:
#   Servo left foot lower on GP2
#   Servo right foot lower on GP3
#   Servo left foot upper on GP13
#   Servo right foot upper on GP12

import time
import board
from digitalio import DigitalInOut, Direction, Pull
import pwmio
from adafruit_motor import servo

from robot import Robot
from constants import *


def main():
    print("Setting up the robot...")
    # Set the onboard LED to on
    # Note: Onboard LED only works with our Pico H (Not W)
    led = DigitalInOut(board.LED)
    led.direction = Direction.OUTPUT
    led.value = True

    # Servo setup
    # Note: Tune pulse for specific servos
    pwm_lower_right_foot = pwmio.PWMOut(
        board.GP3, duty_cycle=DUTY_CYCLE, frequency=50)
    servo_lower_right_foot = servo.Servo(
        pwm_lower_right_foot, actuation_range=180, min_pulse=1000, max_pulse=2000)

    pwm_lower_left_foot = pwmio.PWMOut(
        board.GP2, duty_cycle=DUTY_CYCLE, frequency=50)
    servo_lower_left_foot = servo.Servo(
        pwm_lower_left_foot, actuation_range=180, min_pulse=1000, max_pulse=2000)

    pwm_upper_right_foot = pwmio.PWMOut(
        board.GP12, duty_cycle=DUTY_CYCLE, frequency=50)
    servo_upper_right_foot = servo.Servo(
        pwm_upper_right_foot, actuation_range=180, min_pulse=1000, max_pulse=2000)

    pwm_upper_left_foot = pwmio.PWMOut(
        board.GP13, duty_cycle=DUTY_CYCLE, frequency=50)
    servo_upper_left_foot = servo.Servo(
        pwm_upper_left_foot, actuation_range=180, min_pulse=1000, max_pulse=2000)

    robot = Robot(servo_lower_right_foot, servo_lower_left_foot,
                  servo_upper_right_foot, servo_upper_left_foot)

    # Main logic loop
    print("Dancing Robot Started!")
    robot.reset()
    while True:
        robot.refresh()
        time.sleep(1 / REFRESH_RATE)


if __name__ == "__main__":
    main()
