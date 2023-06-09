import constants as c
import arcade
from constants import attackers_data


class Attacker(arcade.Sprite):
    def __init__(self, type):
        self.lane = None
        self.type = type

        self.time_since_last_attack = 0

        #change image size for tank
        if self.type == 4:
            super().__init__(attackers_data[self.type]['image'], 2)
        else:
            super().__init__(attackers_data[self.type]['image'], 1.2)
        self.name = attackers_data[self.type]['name']
        self.speed = attackers_data[self.type]['speed']
        self.damage = attackers_data[self.type]['damage']
        self.durability = attackers_data[self.type]['durability']
        self.time_between_attacking = attackers_data[self.type]['attack_speed']
        self.position = [0, 0]
        self.dead = False
        self.done = False

        # Load textures
        self.cur_texture = 0
        self.dead_texture = 0
        self.walk_textures = []
        self.death_textures = []

        #
        # # Load texture based off of attacker type
        # if self.name == 'Zombie':
        #     main_path = "animations/zombie_walk/"
        #     self.num_pngs = 22
        #     self.num_row = 4
        # elif self.name == 'Conehead_Zombie':
        #     main_path = "animations/conehead_walk/"
        #     self.num_pngs = 21
        #     self.num_row = 4
        # elif self.name == 'Buckethead_Zombie':
        #     main_path = "animations/buckethead_walk/"
        #     self.num_pngs = 14
        #     self.num_row = 3
        #
        # # Load all the pngs from the correct path into a list
        # h = 0
        # q = 0
        #
        # d = 0




        # Load texture based off of attacker type
        if self.name == 'Zombie' or self.name == 'Tank_Zombie':
            main_path = "animations/zombie_walk/"
            self.num_pngs = 11
        elif self.name == 'Conehead_Zombie':
            main_path = "animations/conehead_walk/"
            self.num_pngs = 11
        elif self.name == 'Buckethead_Zombie':
            main_path = "animations/buckethead_walk/"
            self.num_pngs = 14

        # Load all the pngs from the correct path into a list
        x = 0
        for i in range(self.num_pngs):
            texture = arcade.load_texture(f"{main_path}{x}.png")
            self.walk_textures.append(texture)
            x += 1
        x = 0
        self.atlas = arcade.TextureAtlas.create_from_texture_sequence(self.walk_textures)
        for i in range(12):
            texture = arcade.load_texture(f"animations/zombie_death/{x}.png")
            self.death_textures.append(texture)
            x += 1
        self.atlas2 = arcade.TextureAtlas.create_from_texture_sequence( self.death_textures)



    def is_dead(self):
        if self.durability <= 0:
            self.dead = True
        return self.dead
    def is_done(self):
        return self.done

    def kill(self):
        self.dead = True

    def decrement_health(self, amount):
        self.durability -= amount

    def alter_speed(self, rate):
        self.speed *= rate

    # def draw(self):
    #     # placeholder
    #     # arcade.draw_rectangle_filled(self.position[0],self.position[1],50,50,arcade.color.RED,0)
    #     # TODO: figure out why tf this doesn't work when its here
    #     # type is which "kind" of enemy is spawned, i.e. which sprite we should load
    #     # if self.type == 1:
    #     #     self.enemy_sprite = arcade.Sprite("images/lolli_enemy.png", 0.05)
    #     # elif self.type == 2:
    #     #     self.enemy_sprite = arcade.Sprite("images/chocolate_enemy.png", 0.08)
    #     # else:
    #     #     self.enemy_sprite = arcade.Sprite("images/lolli_enemy.png", 0.08)
    #     #
    #     # self.set_position_lane(self.lane)
    #     # self.enemy_list.append(self.enemy_sprite)
    #
    #     # this is here so draw() has atleast something lol.. a placeholder
    #     if self.type == 99999:
    #         return

    # a setter for position (which is a list of x & y values).
    # this setter takes in one parameter, the lane, and sets the position of the sprite
    # to that corresponding spot. Used in the beginning of the game to initialize enemy's starting spot
    def set_position_lane(self, lane):
        # a 'lane' is just a value from the constructor. Depending on lane this enemy spawns in,
        # this will set up that enemy to start moving.
        self.lane = lane

        # offset for tank zombie
        offset = 10
        if self.type == 4:
            offset = 50
        if lane == 5:
            self.center_x = 1000
            self.center_y = 470 + offset

            self.position = [1000, self.center_y]

        elif lane == 4:
            self.center_x = 1000
            self.center_y = 365 + offset

            self.position = [1000, self.center_y]

        elif lane == 3:
            self.center_x = 1000
            self.center_y = 260 + offset

            self.position = [1000, self.center_y]

        elif lane == 2:
            self.center_x = 1000
            self.center_y = 155 + offset

            self.position = [1000, self.center_y]

        elif lane == 1:
            self.center_x = 1000
            self.center_y = 50 + offset

            self.position = [1000, self.center_y]
        else:
            self.center_x = 100
            self.center_y = 100 + offset

            self.position = [100, self.center_y]

    # similar setter for position but with different parameters, actual x & y for heightened flexibility when needed.
    def set_position_xy(self, position_x, position_y):
        self.position = [position_x, position_y]

    # a getter to return the current attacker's position (which is a list of x & y coordinates)
    # // now that i think about it i don't think we will need this lol... maybe later on //
    def get_position(self):
        return self.position

    def get_type(self):
        return self.type

    def get_durability(self):
        return self.durability

    def ready_to_attack(self, delta_time: float = 1 / 60):

        self.time_since_last_attack += delta_time

        attack = False

        if self.time_since_last_attack >= self.time_between_attacking:
            self.time_since_last_attack = 0
            attack = True
            # create the bullet

        return attack

    def reset_speed(self):
        self.speed = attackers_data[self.type]['speed']


    def update_animation(self, delta_time: float = 1 / 60):

        # sets texture to the correct one in the list

        if self.dead:
            self.texture = self.death_textures[self.dead_texture]
            self.dead_texture += 1
            if self.dead_texture >= 11:
                #self.dead_texture = 0
                self.done = True



        else:
            self.cur_texture += 1
            if self.cur_texture >= self.num_pngs:
                self.cur_texture = 0
            frame = self.cur_texture

            self.texture = self.walk_textures[frame]





