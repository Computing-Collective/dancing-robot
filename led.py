from constants import *


class LED:
    def __init__(self, led_arm_right, led_arm_left, led_top_left, led_top_right, led_top_mid):
        # RGB leds
        self.led_arm_right = led_arm_right
        self.led_arm_left = led_arm_left

        """
        single color leds
        these are all connected to the same ground
        so all of them will be on at the same time wiht the same brightness
        The brightness is controlled by number of leds that are on
        Brigness range = [0, 3]
        """
        self.led_top_left = led_top_left
        self.led_top_right = led_top_right
        self.led_top_mid = led_top_mid
        self.ticks = 0

    def refresh(self):
        if self.ticks == 1:
            # both red
            self.led_arm_left[0].value = True
            self.led_arm_left[1].value = False
            self.led_arm_left[2].value = False
            self.led_arm_right[0].value = True
            self.led_arm_right[1].value = False
            self.led_arm_right[2].value = False
            # brightness = 1
            self.led_top_left.value = True
            self.led_top_right.value = False
            self.led_top_mid.value = False

        elif self.ticks == REFRESH_RATE:
            # both green
            self.led_arm_left[0].value = False
            self.led_arm_left[1].value = True
            self.led_arm_left[2].value = False
            self.led_arm_right[0].value = False
            self.led_arm_right[1].value = True
            self.led_arm_right[2].value = False
            # brightness = 2
            self.led_top_left.value = True
            self.led_top_right.value = True
            self.led_top_mid.value = False
        
        elif self.ticks == REFRESH_RATE * 2:
            # both blue
            self.led_arm_left[0].value = False
            self.led_arm_left[1].value = False
            self.led_arm_left[2].value = True
            self.led_arm_right[0].value = False
            self.led_arm_right[1].value = False
            self.led_arm_right[2].value = True
            # brightness = 3
            self.led_top_left.value = True
            self.led_top_right.value = True
            self.led_top_mid.value = True

        elif self.ticks == REFRESH_RATE * 3:
            # both white
            self.led_arm_left[0].value = True
            self.led_arm_left[1].value = True
            self.led_arm_left[2].value = True
            self.led_arm_right[0].value = True
            self.led_arm_right[1].value = True
            self.led_arm_right[2].value = True
            # brightness = 0
            self.led_top_left.value = False
            self.led_top_right.value = False
            self.led_top_mid.value = False
            
        elif self.ticks == REFRESH_RATE * 4:
            self.ticks = 0


        self.ticks += 1
