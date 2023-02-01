from adafruit_motor import servo

from constants import *


class Robot:
    """
    The robot class that controls the robot. It has 4 servos, 2 for each foot.

    The class contains methods to set the angle of each foot, and a refresh
    method to make the robot dance.

    @param servo_right_lower_foot: The servo for the lower right foot
    @param servo_left_lower_foot: The servo for the lower left foot
    @param servo_right_upper_foot: The servo for the upper right foot
    @param servo_left_upper_foot: The servo for the upper left foot
    """

    def __init__(self, servo_right_lower_foot, servo_left_lower_foot, servo_right_upper_foot, servo_left_upper_foot):
        """Initialize the robot"""
        self.servo_right_lower_foot: servo.Servo = servo_right_lower_foot
        self.servo_left_lower_foot: servo.Servo = servo_left_lower_foot
        self.servo_right_upper_foot: servo.Servo = servo_right_upper_foot
        self.servo_left_upper_foot: servo.Servo = servo_left_upper_foot
        self.ticks = 0  # Timing counter
        self.move_count = 1  # Move counter

    def refresh(self):
        """Increment the robot timing and make it dance accordingly"""
        print(self.move_count)
        print(self.ticks)
        if self.move_count == 1:
            self._wobble()
        elif self.move_count == 2:
            self._inward_push()
        elif self.move_count == 3:
            self.sideways_slide()
        elif self.move_count == 4:
            self._move4()
        elif self.move_count == 5:
            self._move5()
        elif self.move_count == 6:
            self._move6()
        self.ticks += 1

    def _wobble(self):
        '''
        total position = 2
        change position every 0.5 seconds
        total cycles = 5
        '''
        if self.ticks % (REFRESH_RATE / 2) == 0 and self.ticks % REFRESH_RATE != 0:
            self._set_lower_angles(5, 5)
        elif self.ticks % REFRESH_RATE == 0:
            self._set_lower_angles(170, 170)

        # Finish after 5 cycles
        if self.ticks != 0 and self.ticks % (REFRESH_RATE * 5) == 0:
            self.reset()
            self.ticks = 0
            self.move_count += 1

    def _inward_push(self):
        '''
        total position = 2
        change position every 0.5 seconds
        total cycles = 5
        '''
        if self.ticks % (REFRESH_RATE / 2) == 0 and self.ticks % REFRESH_RATE != 0:
            self._set_lower_angles(5, 170)
        elif self.ticks % REFRESH_RATE == 0:
            self._set_lower_angles(170, 5)

        # Finish after 5 cycles
        if self.ticks != 0 and self.ticks % (REFRESH_RATE * 5) == 0:
            self.reset()
            self.ticks = 0
            self.move_count += 1

    def sideways_slide(self):
        '''
        total position = 2
        change position every 0.5 seconds
        total cycles = 5
        '''
        if self.ticks % (REFRESH_RATE / 2) == 0 and self.ticks % REFRESH_RATE != 0:
            self._set_upper_angles(5, 5)
        elif self.ticks % REFRESH_RATE == 0:
            self._set_upper_angles(170, 170)

        # Finish after 5 cycles
        if self.ticks != 0 and self.ticks % (REFRESH_RATE * 5) == 0:
            self.reset()
            self.ticks = 0
            self.move_count += 1

    def _move4(self):
        self.move_count += 1

    def _move5(self):
        self.move_count += 1

    def _move6(self):
        self.move_count += 1

    # Servo range is from 5 to 170 for lower servos
    # Servos are individually tuned

    def _set_lower_angles(self, angle_left: int, angle_right: int):
        """
        Set the lower foot angles

        @param angle_left: The angle to set the lower left foot servo to
        @param angle_right: The angle to set the lower right foot servo to
        """
        angle_left -= 10
        if angle_left < 5:
            angle_left = 5
        if angle_left > 170:
            angle_left = 170
        self.servo_left_lower_foot.angle = angle_left

        angle_right -= 15
        if angle_right < 5:
            angle_right = 5
        if angle_right > 170:
            angle_right = 170
        self.servo_right_lower_foot.angle = angle_right

    def _set_upper_angles(self, angle_left: int, angle_right: int):
        """
        Set the upper foot angles

        @param angle_left: The angle to set the upper left foot servo to
        @param angle_right: The angle to set the upper right foot servo to
        """
        angle_left -= 20
        if angle_left < 0:
            angle_left = 0
        if angle_left > 180:
            angle_left = 180
        self.servo_left_upper_foot.angle = angle_left

        angle_right -= 5
        if angle_right < 0:
            angle_right = 0
        if angle_right > 180:
            angle_right = 180
        self.servo_right_upper_foot.angle = angle_right

    def reset(self):
        """Reset the robot to the starting position"""
        self._set_lower_angles(90, 90)
        self._set_upper_angles(90, 90)
