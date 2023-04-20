import constants as c
import arcade

class Bullet(arcade.Sprite):

    def __init__(self,type,x,y,speed,damage):

        self.type = type
        self.speed_change = 1
        self.damage = damage
        
        self.x = x + 10
        self.y = y + 10

        if self.type == 2:
            super().__init__("images/baseball.png", 0.08)
        elif self.type == 3:
            super().__init__("images/snowball.png", 0.13)
            self.speed_change = .95
            
        else:
            super().__init__("images/baseball.png", 0.08)

        
        #important to set the center coords here
        self.center_x = self.x
        self.center_y = self.y
        self.position = [self.center_x,self.center_y]
        self.change_x = speed
        

    

    def reset(self):
        self.center_x = self.x   
        self.center_y = self.y

    def move(self):
        
            
        for bullet in self.bullet_list:
            bullet.center_x += c.BULLET_SPEED    
            if bullet.center_x > c.SCREEN_WIDTH:
                #reset to defender starting point
                self.reset()
                #self.bullet_list.remove(bullet)
        
                    
