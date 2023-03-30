
import constants as c
import arcade
import random

class Sun:

    def __init__(self):
        self.speed = 2
        self.sun_list = arcade.SpriteList()
        self.sun_sprite = arcade.Sprite("images/sun.png", 0.05)
        self.sun_list.append(self.sun_sprite)

        # call to function to set up random spawnpoint
        self.random_spawning()

    # a function that returns a boolean.
    # given parameters x, y, it will see if those x and y are within the sprite's borders
    def in_sun(self, x, y):
        if (x <= (self.sun_sprite.center_x + 50) and y <= (self.sun_sprite.center_y + 50)) \
                and (x > (self.sun_sprite.center_x - 50) and y > (self.sun_sprite.center_y - 50)):
            print("You have clicked the sun!")
            return True
        else:
            return False

    def random_spawning(self):
        for sun in self.sun_list:
            position = random.randint(1, 4)
            if position == 1:
                self.sun_sprite.center_x = 250
                self.sun_sprite.center_y = 1000

            elif position == 2:
                self.sun_sprite.center_x = 500
                self.sun_sprite.center_y = 1000
            elif position == 3:
                self.sun_sprite.center_x = 750
                self.sun_sprite.center_y = 1000
            else:
                self.sun_sprite.center_x = 900
                self.sun_sprite.center_y = 1000

    def move(self):
        if self.sun_list != None:
            for sun in self.sun_list:
                sun.center_y -= self.speed

