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
        
        # constants
        self.SLOW_MOVE = int(REFRESH_RATE / 4)
        self.MEDIUM_MOVE = int(REFRESH_RATE / 8)
        self.FAST_MOVE = int(REFRESH_RATE / 12)
        
        # tracking info
        self.ticks = 0  # Timing counter
        self.counter = 0  # Counter for changing angles incrementally
        self.move_count = 1  # Move counter
        self.cycles = 0  # Cycle counter for each move

    def refresh(self):
        """Increment the robot timing and make it dance accordingly"""
        print("Move: ", self.move_count)
        if self.move_count == 1:
            self._balancing_act(2)
        elif self.move_count == 2:
            self._swim(3)
        elif self.move_count == 3:
            self._walk_forwards(2)
        elif self.move_count == 4:
            self._the_sweep(3)
        elif self.move_count == 5:
            self._walk_backwards(2)
        elif self.move_count == 6:
            self._circle(5)
        self.ticks += 1
        self.counter += 1
            
    def _swim(self, cycles: int):
        speed = self.MEDIUM_MOVE
        if self.ticks < speed:
            self._move_to_angles_incrementally(90, 90, 90, 90, 90, 90, 160, 0, self.counter, speed)
        elif self.ticks == speed:
            self.counter = 0
        elif self.ticks < speed * 2:
            self._move_to_angles_incrementally(90, 90, 160, 0, 0, 180, 160, 0, self.counter, speed)
        elif self.ticks == speed * 2:
            self.counter = 0
        elif self.ticks < speed * 3:
            self._move_to_angles_incrementally(0, 180, 160, 0, 0, 180, 90, 90, self.counter, speed)
        elif self.ticks == speed * 3:
            self.counter = 0
        elif self.ticks < speed * 4:
            self._move_to_angles_incrementally(0, 180, 90, 90, 90, 90, 90, 90, self.counter, speed)
        elif self.ticks == speed * 4:
            self.counter = 0
            self.cycles += 1
            self.ticks = 0

        if self.cycles == cycles:
            self.reset()
            self.ticks = 0
            self.cycles = 0
            self.counter = 0
            self.move_count += 1

    def _the_sweep(self, cycles: int):
        speed = self.MEDIUM_MOVE
        if self.ticks < speed:
            # upper angles from 90, 90 to 0, 0
            self._move_to_angles_incrementally(90, 90, 90, 90, 0, 0, 90, 90, self.counter, speed)
        elif self.ticks == speed:
            self.counter = 0
        elif self.ticks < speed * 2:
            # upper angles from 0, 0 to 90, 90
            self._move_to_angles_incrementally(0, 0, 90, 90, 90, 90, 90, 90, self.counter, speed)
        elif self.ticks == speed * 2:
            self.counter = 0
        elif self.ticks < speed * 3:
            # upper angles from 90, 90 to 180, 180
            self._move_to_angles_incrementally(90, 90, 90, 90, 180, 180, 90, 90, self.counter, speed)
        elif self.ticks == speed * 3:
            self.counter = 0
        elif self.ticks < speed * 4:
            # upper angles from 180, 180 to 90, 90
            self._move_to_angles_incrementally(180, 180, 90, 90, 90, 90, 90, 90, self.counter, speed)
        elif self.ticks == speed * 4:
            self.counter = 0
            self.cycles += 1
            self.ticks = 0

        if self.cycles == cycles:
            self.reset()
            self.ticks = 0
            self.cycles = 0
            self.counter = 0
            self.move_count += 1

    def _balancing_act(self, cycles: int):
        speed = self.MEDIUM_MOVE
        
        # balance on left foot
        if self.ticks < speed:
            self._move_to_angles_incrementally(90, 90, 90, 90, 90, 90, 120, 180, self.counter, speed)
        elif self.ticks == speed:
            self.counter = 0
        elif self.ticks < speed * 2:
            self._move_to_angles_incrementally(90, 90, 120, 180, 90, 90, 160, 180, self.counter, speed)
        elif self.ticks == speed * 2:
            self.counter = 0

        # move right foot in air
        elif self.ticks < speed * 3:
            self._move_to_angles_incrementally(90, 90, 160, 180, 90, 0, 160, 0, self.counter, speed)
        elif self.ticks == speed * 3:
            self.counter = 0
        elif self.ticks < speed * 4:
            self._move_to_angles_incrementally(90, 0, 160, 0, 90, 180, 160, 180, self.counter, speed)
        elif self.ticks == speed * 4:
            self.counter = 0
        elif self.ticks < speed * 5:
            self._move_to_angles_incrementally(90, 180, 160, 180, 90, 0, 160, 0, self.counter, speed)
        elif self.ticks == speed * 5:
            self.counter = 0
        elif self.ticks < speed * 6:
            self._move_to_angles_incrementally(90, 0, 160, 0, 90, 180, 160, 180, self.counter, speed)
        elif self.ticks == speed * 6:
            self.counter = 0

        # back on ground
        elif self.ticks < speed * 7:
            self._move_to_angles_incrementally(90, 180, 160, 180, 90, 90, 90, 90, self.counter, speed)
        elif self.ticks == speed * 7:
            self.counter = 0
        
        # balance on right foot
        elif self.ticks < speed * 8:
            self._move_to_angles_incrementally(90, 90, 90, 90, 90, 90, 90, 50, self.counter, speed)
        elif self.ticks == speed * 8:
            self.counter = 0
        elif self.ticks < speed * 9:
            self._move_to_angles_incrementally(90, 90, 90, 50, 110, 90, 0, 50, self.counter, speed)
        elif self.ticks == speed * 9:
            self.counter = 0
        elif self.ticks < speed * 10:
            self._move_to_angles_incrementally(110, 90, 0, 50, 90, 90, 0, 0, self.counter, speed)
        elif self.ticks == speed * 10:
            self.counter = 0
        
        # move left foot in air
        elif self.ticks < speed * 11:
            self._move_to_angles_incrementally(90, 90, 0, 0, 0, 90, 180, 0, self.counter, speed)
        elif self.ticks == speed * 11:
            self.counter = 0
        elif self.ticks < speed * 12:
            self._move_to_angles_incrementally(0, 90, 180, 0, 150, 90, 0, 0, self.counter, speed)
        elif self.ticks == speed * 12:
            self.counter = 0
        elif self.ticks < speed * 13:
            self._move_to_angles_incrementally(150, 90, 0, 0, 0, 90, 180, 0, self.counter, speed)
        elif self.ticks == speed * 13:
            self.counter = 0
        elif self.ticks < speed * 14:
            self._move_to_angles_incrementally(0, 90, 180, 0, 150, 90, 0, 0, self.counter, speed)
        elif self.ticks == speed * 14:
            self.counter = 0
        
        # back on ground
        elif self.ticks < speed * 15:
            self._move_to_angles_incrementally(150, 90, 0, 0, 90, 90, 90, 90, self.counter, speed)
        elif self.ticks == speed * 15:
            self.counter = 0
            self.cycles += 1
            self.ticks = 0

        if self.cycles == cycles:
            self.reset()
            self.ticks = 0
            self.cycles = 0
            self.move_count += 1

    def _walk_backwards(self, cycles: int):
        '''
        Lift left foot, move it backwards, then lower it
        Lift right foot, move it backwards, then lower it
        '''
        speed = self.FAST_MOVE
        
        # balance on left foot
        if self.ticks < speed:
            self._move_to_angles_incrementally(90, 90, 90, 90, 90, 90, 120, 180, self.counter, speed)
        elif self.ticks == speed:
            self.counter = 0
        elif self.ticks < speed * 2:
            self._move_to_angles_incrementally(90, 90, 120, 180, 90, 90, 160, 180, self.counter, speed)
        elif self.ticks == speed * 2:
            self.counter = 0
        
        # move right foot back
        elif self.ticks < speed * 3:
            self._move_to_angles_incrementally(90, 90, 160, 180, 90, 30, 160, 180, self.counter, speed)
        elif self.ticks == speed * 3:
            self.counter = 0
        elif self.ticks < speed * 4:
            self._move_to_angles_incrementally(90, 30, 160, 180, 30, 90, 160, 180, self.counter, speed)
        elif self.ticks == speed * 4:
            self.counter = 0
        
        # set right foot down
        elif self.ticks < speed * 5:
            self._move_to_angles_incrementally(30, 90, 160, 180, 30, 90, 90, 90, self.counter, speed)
        elif self.ticks == speed * 5:
            self.counter = 0
        elif self.ticks < speed * 6:
            self._move_to_angles_incrementally(30, 90, 90, 90, 90, 90, 90, 90, self.counter, speed)
        elif self.ticks == speed * 6:
            self.counter = 0

        # balance on right foot
        elif self.ticks < speed * 7:
            self._move_to_angles_incrementally(90, 90, 90, 90, 90, 90, 90, 50, self.counter, speed)
        elif self.ticks == speed * 7:
            self.counter = 0
        elif self.ticks < speed * 8:
            self._move_to_angles_incrementally(90, 90, 90, 50, 110, 90, 0, 50, self.counter, speed)
        elif self.ticks == speed * 8:
            self.counter = 0
        elif self.ticks < speed * 9:
            self._move_to_angles_incrementally(110, 90, 0, 50, 90, 90, 0, 0, self.counter, speed)
        elif self.ticks == speed * 9:
            self.counter = 0
            
        # move left foot back
        elif self.ticks < speed * 10:
            self._move_to_angles_incrementally(90, 90, 0, 0, 40, 90, 0, 0, self.counter, speed)
        elif self.ticks == speed * 10:
            self.counter = 0
        elif self.ticks < speed * 11:
            self._move_to_angles_incrementally(40, 90, 0, 0, 90, 140, 0, 0, self.counter, speed)
        elif self.ticks == speed * 11:
            self.counter = 0
        
        # set left foot down
        elif self.ticks < speed * 12:
            self._move_to_angles_incrementally(90, 140, 0, 0, 90, 140, 90, 90, self.counter, speed)
        elif self.ticks == speed * 12:
            self.counter = 0
        elif self.ticks < speed * 13:
            self._move_to_angles_incrementally(90, 140, 90, 90, 90, 90, 90, 90, self.counter, speed)
        elif self.ticks == speed * 13:
            self.counter = 0
            self.cycles += 1
            self.ticks = 0
        
        if self.cycles == cycles:
            self.reset()
            self.ticks = 0
            self.cycles = 0
            self.move_count += 1
        
    def _circle(self, cycles: int):
        '''
        Circle around the center of the robot
        - Lift right foot, move it forward, then lower it and adjust the left foot
        '''
        speed = self.MEDIUM_MOVE
        
        # balance on left foot
        if self.ticks < speed:
            self._move_to_angles_incrementally(90, 90, 90, 90, 90, 90, 120, 180, self.counter, speed)
        elif self.ticks == speed:
            self.counter = 0
        elif self.ticks < speed * 2:
            self._move_to_angles_incrementally(90, 90, 120, 180, 90, 90, 160, 180, self.counter, speed)
        elif self.ticks == speed * 2:
            self.counter = 0
        
        # move right foot forward
        elif self.ticks < speed * 3:
            self._move_to_angles_incrementally(90, 90, 160, 180, 150, 90, 160, 180, self.counter, speed)
        elif self.ticks == speed * 3:
            self.counter = 0
        elif self.ticks < speed * 4:
            self._move_to_angles_incrementally(150, 90, 160, 180, 150, 90, 90, 90, self.counter, speed)
        elif self.ticks == speed * 4:
            self.counter = 0
        
        # set right foot down
        elif self.ticks < speed * 5:
            self._move_to_angles_incrementally(150, 90, 90, 90, 90, 90, 90, 90, self.counter, speed)
        elif self.ticks == speed * 5:
            self.counter = 0
            self.cycles += 1
            self.ticks = 0
        
        if self.cycles == cycles:
            self.reset()
            self.ticks = 0
            self.cycles = 0
            self.move_count += 1
    
    def _walk_forwards(self, cycles: int):
        '''
        Move the robot forwards
        Move the left foot forward, then the right foot
        First part of the move is the same as the circle move
        Then repeat the circle move but with the left foot
        '''
        speed = self.MEDIUM_MOVE
        
        # balance on left foot
        if self.ticks < speed:
            self._move_to_angles_incrementally(90, 90, 90, 90, 90, 90, 120, 180, self.counter, speed)
        elif self.ticks == speed:
            self.counter = 0
        elif self.ticks < speed * 2:
            self._move_to_angles_incrementally(90, 90, 120, 180, 90, 90, 160, 180, self.counter, speed)
        elif self.ticks == speed * 2:
            self.counter = 0
        
        # move right foot forward
        elif self.ticks < speed * 3:
            self._move_to_angles_incrementally(90, 90, 160, 180, 160, 90, 160, 180, self.counter, speed)
        elif self.ticks == speed * 3:
            self.counter = 0
        elif self.ticks < speed * 4:
            self._move_to_angles_incrementally(160, 90, 160, 180, 160, 90, 90, 90, self.counter, speed)
        elif self.ticks == speed * 4:
            self.counter = 0

        # set right foot down
        elif self.ticks < speed * 5:
            self._move_to_angles_incrementally(160, 90, 90, 90, 90, 90, 90, 90, self.counter, speed)
        elif self.ticks == speed * 5:
            self.counter = 0

        # balance on right foot
        elif self.ticks < speed * 6:
            self._move_to_angles_incrementally(90, 90, 90, 90, 90, 90, 90, 50, self.counter, speed)
        elif self.ticks == speed * 6:
            self.counter = 0
        elif self.ticks < speed * 7:
            self._move_to_angles_incrementally(90, 90, 90, 50, 110, 90, 0, 50, self.counter, speed)
        elif self.ticks == speed * 7:
            self.counter = 0
        elif self.ticks < speed * 8:
            self._move_to_angles_incrementally(110, 90, 0, 50, 90, 90, 0, 0, self.counter, speed)
        elif self.ticks == speed * 8:
            self.counter = 0
        
        # move left foot forward
        elif self.ticks < speed * 9:
            self._move_to_angles_incrementally(90, 90, 0, 0, 90, 10, 0, 0, self.counter, speed)
        elif self.ticks == speed * 9:
            self.counter = 0
        elif self.ticks < speed * 10:
            self._move_to_angles_incrementally(90, 10, 0, 0, 90, 10, 90, 90, self.counter, speed)
        elif self.ticks == speed * 10:
            self.counter = 0
        elif self.ticks < speed * 11:
            self._move_to_angles_incrementally(90, 10, 90, 90, 90, 90, 90, 90, self.counter, speed)
        elif self.ticks == speed * 11:
            self.counter = 0
            self.cycles += 1
            self.ticks = 0
        
        if self.cycles == cycles:
            self.reset()
            self.ticks = 0
            self.cycles = 0
            self.move_count += 1
        
    def _move_to_angles_incrementally(
        self,
        stating_upper_left: int,
        starting_upper_right: int,
        starting_lower_left: int,
        starting_lower_right: int,
        ending_upper_left: int,
        ending_upper_right: int,
        ending_lower_left: int,
        ending_lower_right: int,
        local_counter: int,
        total_ticks: int = None,
    ):
        """Moves from starting angles to ending angles incrementally

        @param local_counter: Counter to keep track of how many ticks have passed for this angle change
                              This is local to the function and should be reset to 0 when the function is called
                              This is not the same as self.ticks
                              And this counter needs to be managed by the caller: start with 0, and with every tick, increment by 1
        @param total_ticks: How many ticks it should take to move from starting to ending angles, default is self.MEDIUM_MOVE
        """
        if total_ticks is None:
            total_ticks = self.MEDIUM_MOVE
        # Calculate the amount to increment each angle by
        increment_upper_left = float(ending_upper_left - stating_upper_left) / total_ticks
        increment_upper_right = float(ending_upper_right - starting_upper_right) / total_ticks
        increment_lower_left = float(ending_lower_left - starting_lower_left) / total_ticks
        increment_lower_right = float(ending_lower_right - starting_lower_right) / total_ticks

        # Calculate the new angles
        new_upper_left = stating_upper_left + (increment_upper_left * local_counter)
        new_upper_right = starting_upper_right + (increment_upper_right * local_counter)
        new_lower_left = starting_lower_left + (increment_lower_left * local_counter)
        new_lower_right = starting_lower_right + (increment_lower_right * local_counter)

        # Set the new angles
        self._set_upper_angles(new_upper_left, new_upper_right)
        self._set_lower_angles(new_lower_left, new_lower_right)

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
    
    ##################################################################
    #                        UNUSED MOVES                            #
    ##################################################################
    
    def _wobble(self, cycles: int):
        speed = self.MEDIUM_MOVE
        if self.ticks < speed:
            # lower angles from 90, 90 to 0, 0
            self._move_to_angles_incrementally(90, 90, 90, 90, 90, 90, 0, 0, self.counter, speed)
        elif self.ticks == speed:
            self.counter = 0
        elif self.ticks < speed * 2:
            # lower angles from 0, 0 to 90, 90
            self._move_to_angles_incrementally(90, 90, 0, 0, 90, 90, 90, 90, self.counter, speed)
        elif self.ticks == speed * 2:
            self.counter = 0
        elif self.ticks < speed * 3:
            # lower angles from 90, 90 to 180, 180
            self._move_to_angles_incrementally(90, 90, 90, 90, 90, 90, 180, 180, self.counter, speed)
        elif self.ticks == speed * 3:
            self.counter = 0
        elif self.ticks < speed * 4:
            # lower angles from 180, 180 to 90, 90
            self._move_to_angles_incrementally(90, 90, 180, 180, 90, 90, 90, 90, self.counter, speed)
        elif self.ticks == speed * 4:
            self.counter = 0
            self.cycles += 1
            self.ticks = 0

        if self.cycles == cycles:
            self.reset()
            self.ticks = 0
            self.cycles = 0
            self.counter = 0
            self.move_count += 1

    def _inward_push(self, cycles: int):
        speed = self.MEDIUM_MOVE
        if self.ticks < speed:
            # lower angles from 90, 90 to 0, 180
            self._move_to_angles_incrementally(90, 90, 90, 90, 90, 90, 0, 180, self.counter, speed)
        elif self.ticks == speed:
            self.counter = 0
        elif self.ticks < speed * 2:
            # lower angles from 0, 180 to 90, 90
            self._move_to_angles_incrementally(90, 90, 0, 180, 90, 90, 90, 90, self.counter, speed)
        elif self.ticks == speed * 2:
            self.counter = 0
            self.cycles += 1
            self.ticks = 0

        if self.cycles == cycles:
            self.reset()
            self.ticks = 0
            self.cycles = 0
            self.counter = 0
            self.move_count += 1