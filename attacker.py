import constants as c
import arcade


class Attacker:
    
    def __init__(self,speed,damage,durability,name,x,y):
        self.speed = speed
        self.damage = damage
        self.durability = durability
        self.dead = False
        self.name = name
        self.x = x
        self.y = y
        

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




