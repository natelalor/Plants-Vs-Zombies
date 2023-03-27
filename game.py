import math
import random
import constants as c
import arcade
from sun import Sun
from defender import Defender
from attacker import Attacker
from grid import Grid
import random
import sympy as sp
import numpy as np
from scipy.integrate import quad



class Game(arcade.Window):
    def __init__(self, level: int):
        super().__init__(c.SCREEN_WIDTH, c.SCREEN_HEIGHT, c.SCREEN_TITLE)
        self.live_attackers = []
        self.attackers = [Attacker]
        self.game_time = 0
        self.ally_list = None
        self.level = level
        self.live_attackers = [Attacker]




    def setup(self):
        self.total_attacker_weight = 0
        self.scaled_attackers = []
        self.createAttackers()
        self.currency = 100
        self.total_area = quad(self.norm, -np.inf, np.inf, args=c.waves)[0]  # integrate to find area under curve
        for attacker in self.attackers:  # scale the attacker's individual weight in relation to the area
            self.scaled_attackers.append(attacker / self.total_attacker_weight * self.total_area)

        # on_update movement testing:
        self.change_x = 100
        self.change_y = 100

        # Tests placing an attacker and defender on the grid
        # first param: 1, 2, are different types: lolli, chocoalte, etc
        # second param: integer for lane, 1-5

        # self.attacker1 = Attacker(1, 1)
        # self.attacker2 = Attacker(2, 2)
        # self.attacker3 = Attacker(1, 3)
        # self.attacker4 = Attacker(2, 4)
        # self.attacker5 = Attacker(1, 5)
        self.ally_list = [Defender(2, 1),Defender(1, 2), Defender(2, 3)]


        # TEMP SUN CREATION
        self.sun1 = Sun(250, 250)

        self.grid = Grid(c.SIZE_COLUMNS, c.SIZE_ROWS)

    """
        Create a multimodal Gaussian Curve
        :param var x: variable for integration
        :param dict waves: a dictionary of dictionaries storing the variables for each of the waves
    """
    def norm(self, x, waves):
        equation = 0.0
        for i in waves.keys():  # for each wave
            coefficient = 1 / (waves[i]['intensity'] * math.sqrt(2 * math.pi))  # #math
            exponent = -waves[i]['weight'] * ((x - waves[i]['x']) / waves[i]['intensity']) ** 2  # #moremath
            equation += coefficient * sp.E ** exponent  # combine the wave
        return equation


    """
        Organize a list semi-randomly
        :param List attacker: the list to be randomized 
    """

    def randomize(self):
        random.shuffle(self.attackers)
        first_min = self.attackers.index(min(self.attackers))  # find the index of the first instance of minimum
        self.attackers.insert(0, self.attackers.pop(first_min))  # move it to the front
        first_max = self.attackers.index(max(self.attackers))  # find the index of the first instance of the max
        self.attackers.append(self.attackers.pop(first_max))  # move it to the end

    def createAttackers(self):
        for enemyType in c.levelsDict[self.level]:
            self.total_attacker_weight += enemyType[0] * enemyType[1]  # multiply type by weight
            for i in range(enemyType[1]):
                self.attackers.append(Attacker(enemyType[0]))
        self.randomize()

    def runGame(self):
        pass

    # MOUSE INPUT TESTING HERE
    def on_mouse_press(self, x, y, button, modifiers):
        clicked = False
        print("Mouse button is pressed")

        # if x/y is here AND clicked boolean is false, then sunflower is selected
        if (x == 0 and y == 0) and (clicked == False):

            # then call mouse function where its on hover and light up square that its on
            sunflower = True
            clicked = True

        # TODO: 3/24/23 TESTING!!!! problem: u have to access a square's has_plant(x,y) and im not sure how to get to
        # a specific square... through a grid method maybe? grid.return_square(x, y) ??? (x,y being coordinates clicked?

        # whichever square you place, if there is no plant there, it creates a new defender for you
        # if (x == 0 and y == 0) and (self.grid.has_plant(x, y)):
        #     # new sunflower creation
        #     sunflower1 = Defender(1, 1)

        # elif x/y is here AND clicked boolean is true, then sunflower is DEselected
        elif (x == 0 and y == 0) and (clicked == True):
            # sunflower is DEselected
            sunflower = False
            clicked = False

        # if x/y is here, then pea shooter is selected AND clicked boolean is false
        if (x == 0 and y == 0) and (clicked == False):

            # then call mouse function where its on hover and light up square that its on
            pea_shooter = True
            clicked = True

        # elif x/y is here AND clicked boolean is true, then sunflower is DEselected
        if (x == 0 and y == 0) and (clicked == True):
            # pea shooter DEselected
            pea_shooter = False
            clicked = False


        # if x/y is here, then frozen pea shooter is selected AND clicked boolean is false
        if (x == 0 and y == 0) and (clicked == False):

            # then call mouse function where its on hover and light up square that its on
            frozen_pea = True
            clicked = True

        # if x/y is here, then frozen pea shooter is selected AND clicked boolean is TRUE,
        if (x == 0 and y == 0) and (clicked == True):
            #DEselect frozen pea
            frozen_pea = False
            clicked = False

        # SUN CLICK TESTING!!!!
        if self.sun1.in_sun(x, y):
            # disappear sprite  # TODO: delete objects (how to make sprites disappear?)
            # del self.sun1    #this breaks because then it has no sun1 to draw later on. how do we safely remove objects?
            # update currency
            self.currency += c.SUN_ADDITION


    def on_draw(self):
        """Render the screen. """

        self.clear()

        self.grid.grid_draw()
        self.live_attackers.draw()
        # TEMPORARY SUN DRAWING
        self.sun1.sun_list.draw()

        # currency text (for positioning: 700 is x, 550 is y)
        arcade.draw_text("Currency: " + str(self.currency), 700, 550, arcade.color.ALICE_BLUE, 20, 40, 'left')

        # THIS IS TEMPORARY SPAWNING UNTIL WE IMPLEMENT SPAWNING SYSTEM
        # self.attacker1.enemy_list.draw()
        # self.attacker2.enemy_list.draw()
        # self.attacker3.enemy_list.draw()
        # self.attacker4.enemy_list.draw()
        # self.attacker5.enemy_list.draw()
        # self.attacker.enemy_list.draw()

        # self.defender.ally_list.draw()
        self.ally_list.draw()



        #self.bullet_list.draw()
        #self.player_list.draw()

    def on_update(self, delta_time):
        self.game_time +=delta_time
        current_total = 0
        # to spawn attackers
        if len(self.attackers) != 0:
            area = quad(self.norm, -np.inf, self.game_time / 5, args=c.waves)[0]  # integrate and find bounded area (-inf, timestep)
            if area > current_total:
                current_total += self.scaled_attackers.pop(0)  # add scaled attacker weight to the current total
                self.attackers[0].set_position_lane(random.randint(1,5))
                self.live_attackers.append(self.attackers.pop(0))
                print("SPAWN", self.live_attackers)

        for attacker in self.live_attackers:
            # attacker.draw()
            attacker.move()


        # if random.random() < 0.01:
        #     # TODO: change to waves of attakcers rather than random semi-constant
        #     # generate random int for "type" of enemy spawned
        #     random_type = random.randint(0, 100)
        #     print("RANDOMTYPE: ", random_type)
        #     if 0 <= random_type <= 85:
        #         type = 1
        #     elif 81 <= random_type <= 95:
        #         type = 2
        #     else:
        #         type = 3
        #
        #     # generate random lane it will go on
        #     random_lane = random.randint(0, 100)
        #     print("RANDOMLANE: ", random_lane)
        #     if 0 <= random_lane <= 20:
        #         lane = 1
        #     elif 21 <= random_lane <= 40:
        #         lane = 2
        #     elif 41 <= random_lane <= 60:
        #         lane = 3
        #     elif 61 <= random_lane <= 80:
        #         lane = 4
        #     else:
        #         lane = 5

            # TODO: fix this! attackers do not show up! type/lane works,
            #          but why doesnt it render the new attacker animations??
            # print("create attacker now: ", type, " ", lane)
            # attacker = Attacker(type, lane)
            # to move all the new attackers
            # for enemy in self.attacker.enemy_list:
            #     enemy.move()

