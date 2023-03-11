import constants as c

class Attacker:
    
    def __init__(self,speed,damage,durability,name):
        self.speed = speed
        self.damage = damage
        self.durability = durability
        self.dead = False
        self.name = name
        

    def is_dead(self):
        if self.durability <= 0:
            self.dead = True
        return (self.dead)
    
    def decrement_health(self,amount):
        self.durability -= amount

    def alter_speed(self,rate):
        self.speed *= rate