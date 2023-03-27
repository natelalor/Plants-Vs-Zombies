import random
import constants as c
import arcade
from sun import Sun
from defender import Defender
from attacker import Attacker
from grid import Grid
import random
import time
import math
import sympy as sp
import numpy as np
from scipy.integrate import quad


class Game(arcade.Window):
    def __init__(self, level: int):
        super().__init__(c.SCREEN_WIDTH, c.SCREEN_HEIGHT, c.SCREEN_TITLE)
        self.game_time = 0
        self.level = level
        self.attackers = []
        self.live_attackers = arcade.SpriteList()
        self.total_attacker_weight = 0
        self.scaled_attackers = []
        self.create_attackers()
        self.currency = 100
        self.total_area = quad(self.norm, -np.inf, np.inf, args=c.waves)[0]  # integrate to find area under curve
        for attacker in self.attackers:  # scale the attacker's individual weight in relation to the area
            self.scaled_attackers.append(attacker / self.total_attacker_weight * self.total_area)

    def setup(self):

        # SCENE FOR ALL SPRITES TO RENDER ON
        self.scene = arcade.Scene()

        # TEMP SUN CREATION
        self.sun1 = Sun()

        self.grid = Grid(c.SIZE_COLUMNS, c.SIZE_ROWS)

    def norm(self, x, waves):
        """
        Create a multimodal Gaussian Curve
            :param var x: variable for integration
            :param dict waves: a dictionary of dictionaries storing the variables for each of the waves
        """
        equation = 0.0
        for i in waves.keys():  # for each wave
            coefficient = 1 / (waves[i]['intensity'] * math.sqrt(2 * math.pi))  # #math
            exponent = -waves[i]['weight'] * ((x - waves[i]['x']) / waves[i]['intensity']) ** 2  # #moremath
            equation += coefficient * sp.E ** exponent  # combine the wave
        return equation

    def randomize(self):
        """
        Organize a list semi-randomly
            :param List attacker: the list to be randomized
        """
        random.shuffle(self.attackers)
        first_min = self.attackers.index(min(self.attackers))  # find the index of the first instance of minimum
        self.attackers.insert(0, self.attackers.pop(first_min))  # move it to the front
        first_max = self.attackers.index(max(self.attackers))  # find the index of the first instance of the max
        self.attackers.append(self.attackers.pop(first_max))  # move it to the end

    def create_attackers(self):
        for enemyType in c.levelsDict[self.level]:
            self.total_attacker_weight += enemyType[0] * enemyType[1]  # multiply type by weight
            for i in range(enemyType[1]):
                self.attackers.append(enemyType[0])
        self.randomize()

    def run_game(self):
        pass

    # MOUSE INPUT TESTING HERE
    def on_mouse_press(self, x, y, button, modifiers):
        clicked = False
        print("Mouse button is pressed")

        # sun click testing
        if self.sun1.in_sun(x, y):
            # disappear sprite  # TODO: delete objects (how to make sprites disappear?)
            # del self.sun1    #this breaks because then it has no sun1 to draw later on. how do we safely remove objects?
            # update currency
            self.currency += c.SUN_ADDITION

        ####################################################
        # \\\\\ ##### GUI MOUSE INTERACTION HERE ##### /////
        ####################################################

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
            # Deselect frozen pea
            frozen_pea = False
            clicked = False


    def on_draw(self):
        """Render the screen. """

        self.clear()

        self.grid.grid_draw()
        self.live_attackers.draw()

        # TEMPORARY SUN DRAWING
        self.sun1.sun_list.draw()

        # currency text (for positioning: 700 is x, 550 is y)
        arcade.draw_text("Currency: " + str(self.currency), 700, 550, arcade.color.ALICE_BLUE, 20, 40, 'left')
        for attacker in self.live_attackers:
            attacker.draw()

    def on_update(self, delta_time):
        self.game_time +=delta_time
        current_total = 0
        # to spawn attackers
        if len(self.attackers) != 0:
            area = quad(self.norm, -np.inf, self.game_time / 5, args=c.waves)[0]  # integrate and find bounded area (-inf, timestep)
            if area > current_total:
                current_total += self.scaled_attackers.pop(0)  # add scaled attacker weight to the current total
                self.live_attackers.append(Attacker(self.attackers.pop(0), random.randint(1, 5)))
                print("SPAWN", self.live_attackers)

        for attacker in self.live_attackers:
            attacker.draw()
            # attacker.move()

        self.sun1.move()


