import constants as c

class Defender:
    
    def __init__(self,shootSpeed,damage,durability,name):
        self.shootSpeed = shootSpeed
        self.damage = damage
        self.durability = durability
        self.name = name
        
    
    def is_dead(self):
        if self.durability <= 0:
            self.dead = True
        return (self.dead)
    
    def decrement_health(self,amount):
        self.durability -= amount

        
