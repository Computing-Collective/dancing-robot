# SPDX-FileCopyrightText: 2021 jedgarpark for Adafruit Industries
# SPDX-License-Identifier: MIT

# Pico servo demo
# Hardware setup:
#   Servo on GP0 with external 5V power supply
#   Button on GP3 and ground

import time
import board
from digitalio import DigitalInOut, Direction, Pull
import pwmio
from adafruit_motor import servo

print("Servo test")

led = DigitalInOut(board.LED)
led.direction = Direction.OUTPUT
led.value = True

### RANGE FROM 5 TO 170
def set_right_angle(angle: int):
    angle -= 15
    if angle < 5:
        angle = 5
    if angle > 170:
        angle = 170
    servo_right_foot.angle = angle


def set_left_angle(angle: int):
    angle -= 10
    if angle < 5:
        angle = 5
    if angle > 170:
        angle = 170
    servo_left_foot.angle = angle


def reset():
    set_right_angle(90)
    set_left_angle(90)


# Servo setup
pwm_right_foot = pwmio.PWMOut(board.GP3, duty_cycle=2**15, frequency=50)
servo_right_foot = servo.Servo(
    pwm_right_foot, actuation_range=180, min_pulse=1000, max_pulse=2000
)  # tune pulse for specific servo

pwm_left_foot = pwmio.PWMOut(board.GP2, duty_cycle=2**15, frequency=50)
servo_left_foot = servo.Servo(
    pwm_left_foot, actuation_range=180, min_pulse=1000, max_pulse=2000
)

# while True:
#     for angle in range(0, 50, 5):
#         servo_right_foot = angle
#         servo_left_foot = angle
# time.sleep(1)

# while True:
#     time.sleep(2)
def wobble():
    for _ in range(2):
        # for angle in range(5, 170, 15):
        # servo_left_foot.angle = 5
        # servo_right_foot.angle = 5
        set_left_angle(5)
        set_right_angle(5)
        time.sleep(0.5)
        set_left_angle(170)
        set_right_angle(165)
        time.sleep(0.5)
    reset()


wobble()
