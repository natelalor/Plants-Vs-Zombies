
import constants as c
import arcade
import random

class Sun(arcade.Sprite):

    def __init__(self):
        super().__init__("images/sun.png", 0.05)
        self.speed = 2
        self.location = []
        self.end_location = []

        # call to function to set up random spawnpoint
        self.random_spawning()

    # a function that returns a boolean.
    # given parameters x, y, it will see if those x and y are within the sprite's borders
    def in_sun(self, x, y):
        print("x: ", x, "y: ", y)
        if (x <= (self.position[0] + 50) and y <= (self.position[1] + 50)) \
                and (x > (self.position[0] - 50) and y > (self.position[1] - 50)):
            print("You have clicked the sun!")
            return True
        else:
            return False

    def random_spawning(self):
        position = random.randint(1, 4)
        if position == 1:
            self.center_x = 250
            self.center_y = 1000
        elif position == 2:
            self.center_x = 500
            self.center_y = 1000
        elif position == 3:
            self.center_x = 750
            self.center_y = 1000
        else:
            self.center_x = 900
            self.center_y = 1000

    def move(self):
        self.center_y -= self.speed

    def is_dead(self):


        return False

