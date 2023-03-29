import constants as c
import arcade


class Attacker(arcade.Sprite):
    def __init__(self, type):
        self.type = type
        if self.type == 1:
            super().__init__("images/lolli_enemy.png", 0.05)
        elif self.type == 2:
            super().__init__("images/chocolate_enemy.png", 0.08)
        else:
            super().__init__("images/lolli_enemy.png", 0.08)

        self.position = [0, 0]
        self.dead = False

        # depending on which "type" of attacker you create, they will have differing preset stats to initialize
        if self.type == 1:
            self.speed = 1
            self.damage = 1
            self.durability = 1
            self.name = "lollipop"
        elif self.type == 2:
            self.speed = 1
            self.damage = 1
            self.durability = 1
            self.name = "chocolate"
        elif self.type == 3:
            self.speed = 1
            self.damage = 1
            self.durability = 1
            self.name = "creampuff"
        else:
            self.speed = 1
            self.damage = 1
            self.durability = 1
            self.name = "bug catcher"

    def is_dead(self):
        if self.durability <= 0:
            self.dead = True
        return self.dead

    def decrement_health(self, amount):
        self.durability -= amount

    def alter_speed(self, rate):
        self.speed *= rate

    def move(self):
        # move leftward
        for enemy in self.enemy_list:
            enemy.center_x -= self.speed

            # stop if zombie reaches house TODO: fix this
            if enemy.center_x < 10:
                enemy.speed = 0
                # LOSE GAME HERE

    # a setter for position (which is a list of x & y values).
    # this setter takes in one parameter, the lane, and sets the position of the sprite
    # to that corresponding spot. Used in the beginning of the game to initialize enemy's starting spot
    def set_position_lane(self, lane):
        # a 'lane' is just a value from the constructor. Depending on lane this enemy spawns in,
        # this will set up that enemy to start moving.

        if lane == 1:
            self.center_x = 900
            self.center_y = 470

            self.position = [900, 470]

        elif lane == 2:
            self.center_x = 900
            self.center_y = 365

            self.position = [900, 365]

        elif lane == 3:
            self.center_x = 900
            self.center_y = 260

            self.position = [900, 260]

        elif lane == 4:
            self.center_x = 900
            self.center_y = 155

            self.position = [900, 155]

        elif lane == 5:
            self.center_x = 900
            self.center_y = 50

            self.position = [900, 50]
        else:
            self.center_x = 100
            self.center_y = 100

            self.position = [100, 100]

    # similar setter for position but with different parameters, actual x & y for heightened flexibility when needed.
    def set_position_xy(self, position_x, position_y):
        self.position = [position_x, position_y]

    # a getter to return the current attacker's position (which is a list of x & y coordinates)
    # // now that i think about it i don't think we will need this lol... maybe later on //
    def get_position(self):
        return self.position
    def get_type(self):
        return self.type
