
import constants as c
import arcade
import random

class Sun(arcade.Sprite):

    def __init__(self, sunflower_sun):
        super().__init__("images/sun.png", 0.05)
        self.speed = 2
        self.location = []
        self.end_location = []
        self.lifespan = 10


        # call to function to set up random spawnpoint
        if not sunflower_sun:
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
    def set_position(self, x, y):
        super().set_position(x,y)
        self.target_y = y

    def random_spawning(self):
        self.center_x = random.randint(200, 900)
        self.center_y = 1000
        self.target_y = random.randint(300, 600)


    def move(self):
        if self.center_y < self.target_y:
            self.center_y -= self.speed

    def is_dead(self):
        return False

    def on_update(self, delta_time: float = 1 / 60):
        self.lifespan -= delta_time

