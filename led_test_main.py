# temporary file for led output functions that will be called during the dances

import adafruit_rgbled
import board
from digitalio import DigitalInOut, Direction
import time

LEFT_ARM_RED_LED = board.GP
LEFT_ARM_GREEN_LED = board.GP
LEFT_ARM_BLUE_LED = board.GP
led_left_arm = adafruit_rgbled.RGBLED(LEFT_ARM_RED_LED, LEFT_ARM_GREEN_LED, LEFT_ARM_BLUE_LED)
led_left_arm.color = (255, 255, 255)

RIGHT_ARM_RED_LED = board.GP
RIGHT_ARM_GREEN_LED = board.GP
RIGHT_ARM_BLUE_LED = board.GP
led_right_arm = adafruit_rgbled.RGBLED(RIGHT_ARM_RED_LED, RIGHT_ARM_GREEN_LED, RIGHT_ARM_BLUE_LED)
led_right_arm.color = (255, 255, 255)

led_top_left = DigitalInOut(board.GP2)
led_top_right = DigitalInOut(board.GP3)
led_top_mid = DigitalInOut(board.GP4)

led_top_left.direction = Direction.OUTPUT
led_top_right.direction = Direction.OUTPUT
led_top_mid.direction = Direction.OUTPUT

def main():

    # starting conditions all off
    led_top_left.value = False
    led_top_right.value = False
    led_top_mid.value = False
    led_left_arm.color = (0, 0, 0)
    led_right_arm.color = (0, 0, 0)
    time.sleep(0.5)

    led_top_left.value = True
    led_top_right.value = True
    led_top_mid.value = True

    time.sleep(0.5)

    led_top_left.value = False
    led_top_right.value = False
    led_top_mid.value = False

    time.sleep(0.5)

    for i in range(255):
        led_left_arm.color = (i, i, i)
        led_right_arm.color = (i, i, i)
        time.sleep(0.01) # 0.01 * 255 -> 2.5 seconds total

    time.sleep(0.5)

if __name__ == "__main__":
    main()
