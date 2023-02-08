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
        self.cycles = 0  # Cycle counter for each move

    def refresh(self):
        """Increment the robot timing and make it dance accordingly"""
        print("Move: ", self.move_count)
        if self.move_count == 1:
            self._wobble()
        elif self.move_count == 2:
            self._inward_push()
        elif self.move_count == 3:
            self._the_sweep()
        elif self.move_count == 4:
            self._balancing_act()
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
        if self.ticks == REFRESH_RATE / 2:
            self._set_lower_angles(35, 35)
        elif self.ticks == REFRESH_RATE:
            self._set_lower_angles(140, 140)
            self.cycles += 1
            self.ticks = 0

        # Finish after 5 cycles
        if self.cycles == 5:
            self.reset()
            self.ticks = 0
            self.cycles = 0
            self.move_count += 1

    def _inward_push(self):
        '''
        total position = 2
        change position every 0.5 seconds
        total cycles = 5
        '''
        if self.ticks == REFRESH_RATE / 2:
            self._set_lower_angles(5, 170)
        elif self.ticks == REFRESH_RATE:
            self._set_lower_angles(90, 90)
            self.cycles += 1
            self.ticks = 0

        # Finish after 5 cycles
        if self.cycles == 5:
            self.reset()
            self.ticks = 0
            self.cycles = 0
            self.move_count += 1

    def _the_sweep(self):
        '''
        total position = 2
        change position every 0.5 seconds
        total cycles = 5
        '''
        if self.ticks == REFRESH_RATE / 2:
            self._set_upper_angles(5, 5)
        elif self.ticks == REFRESH_RATE:
            self._set_upper_angles(170, 170)
            self.cycles += 1
            self.ticks = 0

        # Finish after 5 cycles
        if self.cycles == 5:
            self.reset()
            self.ticks = 0
            self.cycles = 0
            self.move_count += 1

    def _balancing_act(self):
        '''
        total position = 8
        change position every 0.5 seconds
        total cycles = 2
        '''
        # balance on left foot
        if self.ticks == REFRESH_RATE / 2:
            self._set_lower_angles(120, 180)
        elif self.ticks == REFRESH_RATE:
            self._set_lower_angles(180, 180)
        elif self.ticks == REFRESH_RATE * 3 / 2:
            self._set_lower_angles(180, 0)
            self._set_upper_angles(90, 0)
        elif self.ticks == REFRESH_RATE * 2:
            self._set_lower_angles(180, 180)
            self._set_upper_angles(90, 180)
        elif self.ticks == REFRESH_RATE * 5 / 2:
            self.reset()

        # balance on right foot
        elif self.ticks == REFRESH_RATE * 3:
            self._set_lower_angles(0, 90)
        elif self.ticks == REFRESH_RATE * 7 / 2:
            self._set_lower_angles(0, 0)
        elif self.ticks == REFRESH_RATE * 4:
            self._set_lower_angles(180, 0)
            self._set_upper_angles(0, 90)
        elif self.ticks == REFRESH_RATE * 9 / 2:
            self._set_lower_angles(0, 0)
            self._set_upper_angles(180, 90)
        elif self.ticks == REFRESH_RATE * 5:
            self.reset()
            self.ticks = 0
            self.cycles += 1

        # Finish after 2 cycles
        if self.cycles == 2:
            self.reset()
            self.ticks = 0
            self.cycles = 0
            self.move_count += 1

    def _walk(self):
        '''
        Lift left foot, move it forward, then lower it
        Lift right foot, move it forward, then lower it
        total position = 6
        total cycles = 2
        '''
        if self.ticks == REFRESH_RATE / 2:
            self._set_lower_angles(90, 180)
            self._set_upper_angles(90, 0)
        elif self.ticks == REFRESH_RATE:
            self.reset()
            self.ticks = 0
            self.cycles += 1
        
        if self.cycles == 2:
            self.reset()
            self.ticks = 0
            self.cycles = 0
            self.move_count += 1

    def _move6(self):
        self.move_count += 1

    # Servo range is from 5 to 170 for lower servos
    # Servos are individually tuned

    def _set_lower_angles(self, angle_left: int, angle_right: int):
        """
        Set the lower foot angles

        @param angle_left: The angle to set the lower left foot servo to
                           0 is inwards, 180 is outwards
        @param angle_right: The angle to set the lower right foot servo to
                            0 is outwards, 180 is inwards
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
                           0 is outwards, 180 is inwards
        @param angle_right: The angle to set the upper right foot servo to
                            0 is inwards, 180 is outwards
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
