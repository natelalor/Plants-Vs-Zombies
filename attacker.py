import constants as c
import arcade


class Attacker:

    def __init__(self, type, lane):
        self.position = []
        self.lane = lane
        self.type = type
        self.dead = False


        # set up the attacker's starting position using their lane
        # self.set_position_lane(self.lane)

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
            self.name = "tbd"

        # // IMPORTANT NOTE  (lastest work 3/14/23) //
        # for some reason this code segment has to be ALL TOGETHER or else it will not function at all.
        # this means for now draw function has NOTHING which we can change lol but idk how to fix for now.
        self.enemy_list = arcade.SpriteList()
        if self.type == 1:
            self.enemy_sprite = arcade.Sprite("images/lolli_enemy.png", 0.05)
        elif self.type == 2:
            self.enemy_sprite = arcade.Sprite("images/chocolate_enemy.png", 0.08)
        else:
            self.enemy_sprite = arcade.Sprite("images/lolli_enemy.png", 0.08)

        self.set_position_lane(self.lane)
        self.enemy_list.append(self.enemy_sprite)

    def is_dead(self):
        if self.durability <= 0:
            self.dead = True
        return (self.dead)

    def decrement_health(self, amount):
        self.durability -= amount

    def alter_speed(self, rate):
        self.speed *= rate

    def draw(self):
        # placeholder
        # arcade.draw_rectangle_filled(self.position[0],self.position[1],50,50,arcade.color.RED,0)
        # TODO: figure out why tf this doesn't work when its here
        # type is which "kind" of enemy is spawned, i.e. which sprite we should load
        # if self.type == 1:
        #     self.enemy_sprite = arcade.Sprite("images/lolli_enemy.png", 0.05)
        # elif self.type == 2:
        #     self.enemy_sprite = arcade.Sprite("images/chocolate_enemy.png", 0.08)
        # else:
        #     self.enemy_sprite = arcade.Sprite("images/lolli_enemy.png", 0.08)
        #
        # self.set_position_lane(self.lane)
        # self.enemy_list.append(self.enemy_sprite)
        if self.type == 99999:
            return

    def move(self):
        # move leftward
        self.position[0] -= self.speed
        # stop if zombie reaches house
        if self.position[0] < 10:
            self.speed = 0

    # a setter for position (which is a list of x & y values).
    # this setter takes in one parameter, the lane, and sets the position of the sprite
    # to that corresponding spot. Used in the beginning of the game to initialize enemy's starting spot
    def set_position_lane(self, lane):
        # 'lane' is just a value from the constructor. Depending on lane this enemy spawns in,
        # this will set up that enemy to start moving.


        if lane == 1:
            self.enemy_sprite.center_x = 900
            self.enemy_sprite.center_y = 470

            self.position = [900, 470]

        elif lane == 2:
            self.enemy_sprite.center_x = 900
            self.enemy_sprite.center_y = 365

            self.position = [900, 365]

        elif lane == 3:
            self.enemy_sprite.center_x = 900
            self.enemy_sprite.center_y = 260

            self.position = [900, 260]

        elif lane == 4:
            self.enemy_sprite.center_x = 900
            self.enemy_sprite.center_y = 155

            self.position = [900, 155]

        elif lane == 5:
            self.enemy_sprite.center_x = 900
            self.enemy_sprite.center_y = 50

            self.position = [900, 50]
        else:
            self.enemy_sprite.center_x = 100
            self.enemy_sprite.center_y = 100

            self.position = [100, 100]


    # similar setter for position but with different parameters, actual x & y for heightened flexibility when needed.
    def set_position_xy(self, position_x, position_y):
        self.position = [position_x, position_y]

    # a getter to return the current attacker's position (which is a list of x & y coordinates)
    # // now that i think about it i dont think we will need this lol... maybe later on //
    def get_position(self):
        return self.position
