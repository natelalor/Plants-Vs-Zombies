
import constants as c
import arcade

class Sun:

    def __init__(self, x, y):
        self.center = [x, y]

        self.sun_list = arcade.SpriteList()
        self.sun_sprite = arcade.Sprite("images/sun.png", 0.05)
        self.sun_list.append(self.sun_sprite)

        self.sun_sprite.center_x = 250
        self.sun_sprite.center_y = 250

    # a function that returns a boolean.
    # given parameters x, y, it will see if those x and y are within the sprite's borders
    def in_sun(self, x, y):
        if (x <= (self.center[0] + 50) and y <= (self.center[1] + 50)) and (x > (self.center[0] - 50) and y > (self.center[1] - 50)):
            print("You have clicked the sun!")
            return True
        else:
            return False

