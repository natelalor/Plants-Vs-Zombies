import constants as c
import arcade
class Defender:
    
    def __init__(self,shootSpeed,damage,durability,name,x,y):
        self.shootSpeed = shootSpeed
        self.damage = damage
        self.durability = durability
        self.name = name
        self.x = x
        self.y = y
        
    
    def is_dead(self):
        if self.durability <= 0:
            self.dead = True
        return (self.dead)
    
    def decrement_health(self,amount):
        self.durability -= amount

    def draw(self):
        #placeholder
        arcade.draw_rectangle_filled(self.x,self.y,50,50,arcade.color.BLUE,0)    
