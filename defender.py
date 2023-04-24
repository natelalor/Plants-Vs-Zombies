import constants as c
from constants import defenders_data
import arcade
from bullet import Bullet
import os


class Defender(arcade.Sprite):

    def __init__(self, type, lane, bullet_list, time_between_firing, position_placement):
        self.lane = lane
        self.position_placement = position_placement
        self.type = type
        self.dead = False
        self.is_active = False

        self.time_since_last_firing = 0
        self.time_between_firing = time_between_firing

        self.bullet_list = bullet_list

        # depending on which "type" of defender you create, they will have differing preset stats to initialize
        super().__init__(defenders_data[self.type]['image'], 0.075)
        self.name = defenders_data[self.type]['name']
        self.shoot_speed = defenders_data[self.type]['speed']
        self.damage = defenders_data[self.type]['damage']
        self.durability = defenders_data[self.type]['durability']

        # self.position = [0, 0]

        self.num_png = len(os.listdir('animations/'+self.name))-1

        self.set_position(self.position_placement)
        # animations
        self.cur_texture = 0
        # main path is determined by what type of defender it is
        # if self.name == 'peashooter':
        #     main_path = "animations/Pea_Shooter/"
        #     self.num_png = 13
        # if self.name == 'Snow_Pea':
        #     main_path = "animations/Snow_Pea/"
        #     self.num_png = 15
        # if self.name == 'repeater':
        #     main_path = "animations/Repeater/"
        #     #num_legnth = 900
        #     #num_height = 875
        #     self.num_png = 11
        # if self.name == 'WallNut':
        #     main_path = "animations/WallNut/"
        #     self.num_png = 10
        # if self.name == 'Sunflower':
        #     main_path = "animations/Sunflower/"
        #     self.num_png = 9

        # Load textures into a list
        self.cur_texture = 0
        self.idle_textures = []
        self.all_sprites_list = arcade.SpriteList()

        for i in range(self.num_png):
            #texture = arcade.load_texture(f"animations/{main_path}", x = i*num_legnth,y= 0, width=num_legnth, height= num_height, )
            texture = arcade.load_texture("animations/"+self.name+"/"+str(i)+".png")
            self.idle_textures.append(texture)
        self.atlas = arcade.TextureAtlas.create_from_texture_sequence(self.idle_textures)

        # 3/25/23 - TESTING WHETHER THIS CAN BE MOVED OR NOT
        # sprite creation

        self.set_position(self.lane)
        print("inside defender sprite creation. sprite created: ", self.type, self.lane)

    def is_dead(self):
        if self.durability <= 0:
            self.dead = True
        return (self.dead)

    def decrement_health(self, amount):
        self.durability -= amount

    def get_position(self):
        return self.position_placement

    def set_position(self, position_placement):

        vertical = self.position_placement[0]
        horizontal = self.position_placement[1]

        #test this change
        if vertical == 0:
            self.center_y = 50
        elif vertical == 1:
            self.center_y = 155
        elif vertical == 2:
            self.center_y = 260
        elif vertical == 3:
            self.center_y = 365
        elif vertical == 4:
            self.center_y = 470
        else:
            print("########## BUG WITH DEFENDER POSITION VERTICAL")

        if horizontal == 0:
            self.center_x = 50
        elif horizontal == 1:
            self.center_x = 155
        elif horizontal == 2:
            self.center_x = 260
        elif horizontal == 3:
            self.center_x = 365
        elif horizontal == 4:
            self.center_x = 470
        elif horizontal == 5:
            self.center_x = 575
        elif horizontal == 6:
            self.center_x = 680
        elif horizontal == 7:
            self.center_x = 785
        elif horizontal == 8:
            self.center_x = 890
        else:
            print("############### BUG WITH DEFENDER POSITION HORIZONTAL")

    def on_update(self, delta_time: float = 1 / 60) -> None:

        self.time_since_last_firing += delta_time

        if self.is_active:
            if self.time_since_last_firing >= self.time_between_firing:
                self.time_since_last_firing = 0

                #peashooter and snowball
                if self.type == 2 or self.type == 3 or self.type == 6:
                    bullet = Bullet(self.type, self.center_x, self.center_y, c.BULLET_SPEED,self.damage)
                    self.bullet_list.append(bullet)

                #double bullet
                if self.type == 5:
                    bullet = Bullet(self.type, self.center_x, self.center_y, c.BULLET_SPEED,self.damage)
                    #slight offset for bullet 2
                    bullet2 = Bullet(self.type, self.center_x+50, self.center_y, c.BULLET_SPEED,self.damage)
                    self.bullet_list.append(bullet)
                    self.bullet_list.append(bullet2)


        return None

    def update_animation(self, delta_time: float = 1 / 60):

        # sets texture to the correct one in the list
        self.cur_texture += 1
        if self.cur_texture >= self.num_png:
            self.cur_texture = 0
        frame = self.cur_texture

        self.texture = self.idle_textures[frame]
