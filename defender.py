import constants as c
import arcade
from bullet import Bullet
class Defender(arcade.Sprite):
    
    def __init__(self, type, lane,bullet_list,time_between_firing):
        
        self.lane = lane
        self.type = type
        self.dead = False

        self.time_since_last_firing = 0
        self.time_between_firing = time_between_firing

        self.bullet_list = bullet_list

        # depending on which "type" of defender you create, they will have differing preset stats to initialize


        if self.type == 1:
            super().__init__("images/toothbrush_ally.png", 0.05)
            self.shoot_speed = 1
            self.damage = 1
            self.durability = 1
            self.name = "toothbrush"
        elif self.type == 2:
            super().__init__("images/toothbrush_ally.png", 0.05)
            self.shoot_speed = 1
            self.damage = 1
            self.durability = 1
            self.name = "toothpaste"
        elif self.type == 3:
            super().__init__("images/toothbrush_ally.png", 0.05)
            self.shoot_speed = 1
            self.damage = 1
            self.durability = 1
            self.name = "floss"
        else:
            super().__init__("images/toothbrush_ally.png", 0.05)
            self.shoot_speed = 1
            self.damage = 1
            self.durability = 1
            self.name = "bug catcher"

        self.position = [0,0]

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

    def draw(self):
        # placeholder
        arcade.draw_rectangle_filled(self.position[0], self.position[1], 50, 50, arcade.color.BLUE, 0)

        # this is here so draw() has at least something lol.. a placeholder
        if self.type == 99999:
            return

    # a setter for defender's position.
    # set_position_xy uses 2 parameters (x & y coordinates) to set the position of the defender.
    def set_position_xy(self, position_x, position_y):
        self.position = [position_x, position_y]

    def set_position(self, lane):
        # TODO: do we need this function? this is just c + v from attacker's set_position_lane function.
        #  but we may just be able to use square to spawn defenders in specific locations instead of this

        # a 'lane' is just a value from the constructor. Depending on lane this enemy spawns in,
        # this will set up that enemy to start moving.

        if lane == 1:
            self.center_x = 50
            self.center_y = 470

            self.position = [50, 470]

        elif lane == 2:
            self.center_x = 50
            self.center_y = 365

            self.position = [50, 365]

        elif lane == 3:
            self.center_x = 50
            self.center_y = 260

            self.position = [50, 260]

        elif lane == 4:
            self.center_x = 50
            self.center_y = 155

            self.position = [50, 155]

        elif lane == 5:
            self.center_x = 50
            self.center_y = 50

            self.position = [50, 50]
        else:
            self.center_x = 100
            self.center_y = 100

            self.position = [100, 100]


    def on_update(self, delta_time: float = 1 / 60):
        
        self.time_since_last_firing += delta_time
        
        if self.time_since_last_firing >= self.time_between_firing:
            
            self.time_since_last_firing = 0

            #create the bullet
            bullet = Bullet(1,self.center_x,self.center_y,c.BULLET_SPEED)
            
            self.bullet_list.append(bullet)