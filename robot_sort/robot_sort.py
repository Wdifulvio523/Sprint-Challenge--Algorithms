class SortingRobot:
    def __init__(self, l):
        """
        SortingRobot takes a list and sorts it.
        """
        self._list = l   # The list the robot is tasked with sorting
        self._item = None   # The item the robot is holding
        self._position = 0    # The list position the robot is at
        self._light = "OFF"    # The state of the robot's light
        self._time = 0   # A time counter (stretch)

    def can_move_right(self):
        """
        Returns True if the robot can move right or False if it's
        at the end of the list.
        """
        return self._position < len(self._list) - 1

    def can_move_left(self):
        """
        Returns True if the robot can move left or False if it's
        at the start of the list.
        """
        return self._position > 0

    def move_right(self):
        """
        If the robot can move to the right, it moves to the right and
        returns True. Otherwise, it stays in place and returns False.

        This will increment the time counter by 1.
        """
        self._time += 1
        if self._position < len(self._list) - 1:
            self._position += 1
            return True
        else:
            return False

    def move_left(self):
        """
        If the robot can move to the left, it moves to the left and
        returns True. Otherwise, it stays in place and returns False.

        This will increment the time counter by 1.
        """
        self._time += 1
        if self._position > 0:
            self._position -= 1
            return True
        else:
            return False

    def swap_item(self):
        """
        The robot swaps its currently held item with the list item in front
        of it.

        This will increment the time counter by 1.
        """
        self._time += 1
        # Swap the held item with the list item at the robot's position
        self._item, self._list[self._position] = self._list[self._position], self._item

    def compare_item(self):
        """
        Compare the held item with the item in front of the robot:

        If the held item's value is greater, return 1.
        If the held item's value is less, return -1.
        If the held item's value is equal, return 0.
        If either item is None, return None.
        """
        if self._item is None or self._list[self._position] is None:
            return None
        elif self._item > self._list[self._position]:
            return 1
        elif self._item < self._list[self._position]:
            return -1
        else:
            return 0

    def set_light_on(self):
        """
        Turn on the robot's light
        """
        self._light = "ON"

    def set_light_off(self):
        """
        Turn off the robot's light
        """
        self._light = "OFF"

    def light_is_on(self):
        """
        Returns True if the robot's light is on and False otherwise.
        """
        return self._light == "ON"

    def sort(self):
        #turn light on
        self.set_light_on() 
        
        # start a loop using light is on method. and the loop continues while the light is off.
        while self.light_is_on(): 
            
            # turn light off at beginning of loop
            self.set_light_off() 

            # while the robot is able to move right:
            while self.can_move_right(): 
                #swap the held item with floor item, and move right
                self.swap_item() 
                self.move_right()  
                # if held item is greater than floor item:
                if self.compare_item() == 1:  
                    # swap the two items
                    self.swap_item()  
                    # move left
                    self.move_left()
                    #swap these items
                    self.swap_item()  
                    # move back right 
                    self.move_right()  
                    #turn the light on
                    self.set_light_on() 
                # in any other case besides the held item being greater than the floor item:
                else:  
                    # move robot left
                    self.move_left()  # move left
                      # swap the two items
                    self.swap_item()  
                       # move robot right
                    self.move_right()  
             # while the light is off:
            if self.light_is_on():
                # while the robot it able to move left 
                while self.can_move_left():
                    #move left
                    self.move_left()
    
   


if __name__ == "__main__":
    # Test our your implementation from the command line
    # with `python robot_sort.py`

    l = [15, 41, 58, 49, 26, 4, 28, 8, 61, 60, 65, 21, 78, 14, 35, 90, 54, 5, 0, 87, 82, 96, 43, 92, 62, 97, 69, 94, 99, 93, 76, 47, 2, 88, 51, 40, 95, 6, 23, 81, 30, 19, 25, 91, 18, 68, 71, 9, 66, 1,
         45, 33, 3, 72, 16, 85, 27, 59, 64, 39, 32, 24, 38, 84, 44, 80, 11, 73, 42, 20, 10, 29, 22, 98, 17, 48, 52, 67, 53, 74, 77, 37, 63, 31, 7, 75, 36, 89, 70, 34, 79, 83, 13, 57, 86, 12, 56, 50, 55, 46]

    robot = SortingRobot(l)

    robot.sort()
    print(robot._list)


    #   # initialize our boolean to true (turn light on)
    #     self.set_light_on()

    #     #run loop while light is on
    #     while self._light == "ON":

    #         #default it to off inside the loop so that the loop will be able to exit
    #         self.set_light_off()

    #         #loop through a range from 0 up to the length of the list
    #         for i in range(0, len(self._list)):

    #             # if i equals 0, set the position of robot to i and continue loop
    #             if i == 0:
    #                 self._position = i
    #                 continue
    #             # set the item equal to the item at _position in the _list
    #             self._item = self._list[self._position]
    #             # Move robot right
    #             self.move_right()

    #             # compare item in hand to item on floor
    #             # if less than 0, do nothing because floor item is greater than held item, so do nothing
    #             if self.compare_item() < 0:
    #                 continue
    #             # if more than 0, this means that the held item is greater than the floor item:
    #             elif self.compare_item() > 0:

    #                 #swap the two items so now floor item is greater than held item
    #                 self.swap_item()
    #                 #move back left
    #                 self.move_left()
    #                 # Swap this floor item with held item
    #                 self.swap_item()
    #                 # move back right
    #                 self.move_right()
    #                 # turn light on to continue loop and comparisons
    #                 self.set_light_on()
