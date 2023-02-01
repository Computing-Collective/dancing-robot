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
            self._move2()
        elif self.move_count == 3:
            self._move3()
        elif self.move_count == 4:
            self._move4()
        elif self.move_count == 5:
            self._move5()
        elif self.move_count == 6:
            self._move6()
        self.ticks += 1

    def _wobble(self):
        '''
        Every 30 ticks (0.5 seconds), we do a move
        So change position a REFRESH_RATE/2 and REFRESH_RATE
        '''
        if self.ticks % (REFRESH_RATE / 2) == 0 and self.ticks % REFRESH_RATE != 0:
            self._set_left_lower_angle(5)
            self._set_right_lower_angle(5)
        elif self.ticks % REFRESH_RATE == 0:
            self._set_left_lower_angle(170)
            self._set_right_lower_angle(165)

        # Finish after 5 cycles
        if self.ticks != 0 and self.ticks % (REFRESH_RATE * 5) == 0:
            self.reset()
            self.ticks = 0
            self.move_count += 1

    def _move2(self):
        self.move_count += 1
        return

    def _move3(self):
        self.move_count += 1
        return

    def _move4(self):
        self.move_count += 1
        return

    def _move5(self):
        self.move_count += 1
        return

    def _move6(self):
        self.move_count += 1
        return

    # Servo range is from 5 to 170
    # Servos are individually tuned

    def _set_right_lower_angle(self, angle: int):
        """
        Set the lower right foot angle

        @param angle: The angle to set the lower left foot servo to
        """
        angle -= 15
        if angle < 5:
            angle = 5
        if angle > 170:
            angle = 170
        self.servo_right_lower_foot.angle = angle

    def _set_left_lower_angle(self, angle: int):
        """
        Set the lower left foot angle

        @param angle: The angle to set the lower left foot servo to
        """
        angle -= 10
        if angle < 5:
            angle = 5
        if angle > 170:
            angle = 170
        self.servo_left_lower_foot.angle = angle

    def reset(self):
        """Reset the robot to the starting position"""
        self._set_right_lower_angle(90)
        self._set_left_lower_angle(90)
