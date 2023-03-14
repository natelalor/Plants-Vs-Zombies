import constants as c
import arcade


class Attacker:
    
    def __init__(self, type, speed, damage, durability, name, x, y): # TODO: instead of x,y we should just specify lane. Then, each lane possibility would have different predetermined coords
        self.type = type
        self.speed = speed
        self.damage = damage
        self.durability = durability
        self.dead = False
        self.name = name
        self.x = x
        self.y = y
        self.enemy_list = arcade.SpriteList()
        # type is which "kind" of enemy is spawned, i.e. which sprite we should load
        if type == 1:
            self.enemy_sprite = arcade.Sprite("images/lolli_enemy.png", 0.25)
        elif type == 2:
            self.enemy_sprite = arcade.Sprite("images/chocolate_enemy.png", 0.25)
        else:
            self.enemy_sprite = arcade.Sprite("images/lolli_enemy.png", 0.25)

        # move these later, its enemy sprite placements... these are just tester values
        self.enemy_sprite.center_x = 64
        self.enemy_sprite.center_y = 120
        self.enemy_list.append(self.enemy_sprite)
        

    def is_dead(self):
        if self.durability <= 0:
            self.dead = True
        return (self.dead)
    
    def decrement_health(self,amount):
        self.durability -= amount

    def alter_speed(self,rate):
        self.speed *= rate

    def draw(self):
        #placeholder
        arcade.draw_rectangle_filled(self.x,self.y,50,50,arcade.color.RED,0)
    
    def move(self):
        #move leftward
        self.x -= self.speed   
        #stop if zombie reaches house
        if self.x < 10 :
            self.speed = 0




