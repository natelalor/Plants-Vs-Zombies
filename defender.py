import constants as c
import arcade
class Defender:
    
    def __init__(self, type, lane):
        self.position = []
        self.lane = lane
        self.type = type
        self.dead = False

        # depending on which "type" of defender you create, they will have differing preset stats to initialize
        if self.type == 1:
            self.shoot_speed = 1
            self.damage = 1
            self.durability = 1
            self.name = "toothbrush"
        elif self.type == 2:
            self.shoot_speed = 1
            self.damage = 1
            self.durability = 1
            self.name = "toothpaste"
        elif self.type == 3:
            self.shoot_speed = 1
            self.damage = 1
            self.durability = 1
            self.name = "floss"
        else:
            self.shoot_speed = 1
            self.damage = 1
            self.durability = 1
            self.name = "tbd"

        # TODO: figure out why these dont render and appear. (set_position_lane works so its gotta be here?)
        self.ally_list = arcade.SpriteList()
        if self.type == 1:
            self.ally_sprite = arcade.Sprite("images/toothbrush_ally.png", 0.05)
        elif self.type == 2:
            self.ally_sprite = arcade.Sprite("images/toothpaste_ally.png", 0.08)
        else:
            self.ally_sprite = arcade.Sprite("images/toothbrush_ally.png", 0.08)

        self.set_position_lane(self.lane)
        self.ally_list.append(self.ally_sprite)
    
    def is_dead(self):
        if self.durability <= 0:
            self.dead = True
        return (self.dead)
    
    def decrement_health(self, amount):
        self.durability -= amount

    def draw(self):
        # placeholder
        arcade.draw_rectangle_filled(self.position[0], self.position[1], 50, 50, arcade.color.BLUE, 0)

        # this is here so draw() has atleast something lol.. a placeholder
        if self.type == 99999:
            return

    # a setter for defender's position.
    # set_position_xy uses 2 parameters (x & y coordinates) to set the position of the defender.
    def set_position_xy(self, position_x, position_y):
        self.position = [position_x, position_y]

    def set_position_lane(self, lane):
        # a 'lane' is just a value from the constructor. Depending on lane this enemy spawns in,
        # this will set up that enemy to start moving.

        if lane == 1:
            self.ally_sprite.center_x = 50
            self.ally_sprite.center_y = 470

            self.position = [50, 470]

        elif lane == 2:
            self.ally_sprite.center_x = 50
            self.ally_sprite.center_y = 365

            self.position = [50, 365]

        elif lane == 3:
            self.ally_sprite.center_x = 50
            self.ally_sprite.center_y = 260

            self.position = [50, 260]

        elif lane == 4:
            self.ally_sprite.center_x = 50
            self.ally_sprite.center_y = 155

            self.position = [50, 155]

        elif lane == 5:
            self.ally_sprite.center_x = 50
            self.ally_sprite.center_y = 50

            self.position = [50, 50]
        else:
            self.ally_sprite.center_x = 100
            self.ally_sprite.center_y = 100

            self.position = [100, 100]