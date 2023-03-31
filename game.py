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
import time
import multiprocessing

class Game(arcade.Window):
    def __init__(self, level: int):
        super().__init__(c.SCREEN_WIDTH, c.SCREEN_HEIGHT, c.SCREEN_TITLE)
        self.live_attackers = None
        self.game_time = 0
        self.ally_list = None
        self.level = level
        self.scene = arcade.Scene()
        self.current_time = 0
        self.current_area = 0
        self.release_times = []
        self.attackers_list = None

        # for defender selection/deselection
        self.clicked = 0

        #testing Defenders and Bullets
        self.defender_list = None
        self.bullet_list = None

    def setup(self):
        self.total_attacker_weight = 0
        self.scaled_attackers = []
        self.attackers_list = arcade.SpriteList()
        self.live_attackers = arcade.SpriteList()
        self.create_attackers()
        self.currency = 100
        self.total_area = quad(self.norm, -np.inf, np.inf, args=c.waves)[0]  # integrate to find area under curve
        for attacker in self.attackers_list:  # scale the attacker's individual weight in relation to the area
            self.scaled_attackers.append(attacker.get_type() / self.total_attacker_weight * self.total_area)

        self.determine_release()
        # SCENE FOR ALL SPRITES TO RENDER ON
        self.scene = arcade.Scene()

        # TEMP SUN CREATION
        self.sun1 = Sun()

        #test bullet and defenders
        self.defender_list = arcade.SpriteList()
        self.bullet_list = arcade.SpriteList()
        defender1 = Defender(1,1,self.bullet_list,1.5)
        self.defender_list.append(defender1)
        defender3 = Defender(2,3,self.bullet_list,1.3)
        self.defender_list.append(defender3)
        self.defender_list.append(Defender(1, 2, self.bullet_list, 1.5))
        self.defender_list.append(Defender(1, 4, self.bullet_list, 1.5))
        self.defender_list.append(Defender(1, 5, self.bullet_list, 1.5))



        self.grid = Grid(c.SIZE_COLUMNS, c.SIZE_ROWS)
        # for i in c.SIZE_ROWS:
        #     self.scene.add_sprite("Defenders", Defender(1, i, 1))

    def norm(self, x, waves):
        """
        Create a multimodal Gaussian Curve. See the math here: https://www.desmos.com/calculator/rxrpfq7kim
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
        random.shuffle(list(self.attackers_list))
        min = 100
        max = 0
        first_min = 0
        first_max = 0
        for i, attacker in enumerate(self.attackers_list):
            if attacker.get_type() < min:
                min = attacker.get_type()
                first_min = i
            if attacker.get_type() > max:
                max = attacker.get_type()
                first_max = i
        self.attackers_list.insert(0, self.attackers_list.pop(first_min))  # move it to the front
        self.attackers_list.append(self.attackers_list.pop(first_max))  # move it to the end

    def create_attackers(self):
        for enemyType in c.levelsDict[self.level]:
            self.total_attacker_weight += enemyType[0] * enemyType[1]  # multiply type by weight
            for i in range(enemyType[1]):
                self.attackers_list.append(Attacker(enemyType[0]))
        self.randomize()

    def determine_release(self):
        print(multiprocessing.cpu_count())
        current_total = 0
        t = 0
        current_area = 0
        for attacker in self.attackers_list:  # set the lanes
            attacker.set_position_lane(random.randint(1, 5))
        # figure out when to spawn attackers
        while len(self.release_times) < len(self.attackers_list):
            start = time.perf_counter()
            area = quad(self.norm, -50, t, args=c.waves)[0]  # integrate and find bounded area (-inf, timestep)
            if area > current_area:
                current_area += self.scaled_attackers.pop(0)  # add scaled attacker weight to the current total
                self.release_times.append(t*c.SLOW_RATE)
            t += 1
            elapsed = time.perf_counter()-start
            print(t, round(elapsed, 1), round(area, 2), round(current_area, 2))


    def run_game(self):
        pass

    def draw_gui(self):
        # RYAN U CAN DRAW GUI HERE


        # main gui background
        arcade.draw_rectangle_filled((c.SCREEN_WIDTH/2), (c.SCREEN_HEIGHT - (c.GUI_HEIGHT/2)), c.SCREEN_WIDTH, c.GUI_HEIGHT, arcade.color.AMAZON, 0)

        # currency text (for positioning: 700 is x, 550 is y)
        arcade.draw_text("Currency: " + str(self.currency), 700, 550, arcade.color.ALICE_BLUE, 20, 40, 'left')

    # MOUSE INPUT TESTING HERE
    def on_mouse_press(self, x, y, button, modifiers):
        # clicked = 0
        print("Mouse button is pressed")

        # sun click testing
        if self.sun1.in_sun(x, y):
            # update currency
            if self.sun1.sun_list != None:
                self.currency += c.SUN_ADDITION

            # make sprite disappear
            self.sun1.sun_list = None


        ####################################################
        # \\\\\ ##### GUI MOUSE INTERACTION HERE ##### /////
        ####################################################

        # if x/y is here AND clicked boolean is false, then sunflower is selected
        if ((x >= 10 and y >= 10) and (x < 200 and y < 200)) and (self.clicked % 2 == 0):
            # then call mouse function where its on hover and light up square that its on
            sunflower = True
            self.clicked = self.clicked + 1
            print("Clicked Sunflower Tester IN!")

        # elif x/y is here AND clicked boolean is true, then sunflower is DEselected
        elif ((x >= 10 and y >= 10) and (x < 200 and y < 200)) and not (self.clicked % 2 == 0):
            # sunflower is DEselected
            sunflower = False
            self.clicked = self.clicked + 1
            print("Clicked Sunflower Tester OUT!")

        # TODO: 3/24/23 TESTING!!!! problem: u have to access a square's has_plant(x,y) and im not sure how to get to
        # a specific square... through a grid method maybe? grid.return_square(x, y) ??? (x,y being coordinates clicked?

        # whichever square you place, if there is no plant there, it creates a new defender for you
        # if (x == 0 and y == 0) and (self.grid.has_plant(x, y)):
        #     # new sunflower creation
        #     sunflower1 = Defender(1, 1)


    def on_draw(self):
        """Render the screen. """

        # self.clear()

        arcade.start_render()
        self.grid.grid_draw()
        self.draw_gui()
        self.scene.draw()
        # self.live_attackers.draw()

        # TEMPORARY SUN DRAWING
        if self.sun1.sun_list != None:
            self.sun1.sun_list.draw()
        self.live_attackers.draw()
        
        self.defender_list.draw()
        self.bullet_list.draw()

    def on_update(self, delta_time):
        self.game_time += delta_time
        current_total = 0
        for defender in self.defender_list:
            defender.is_active = False
            for attacker in self.live_attackers:
                if attacker.lane == defender.lane:
                    defender.is_active = True
                    break

        # to spawn attackers
        if self.release_times and self.game_time > self.release_times[0]:
            self.release_times.pop(0)
            self.live_attackers.append(self.attackers_list.pop(0))

        for attacker in self.live_attackers:
            attacker.center_x -= 1
            #testing killing attackers
            if attacker.is_dead():
                self.live_attackers.remove(attacker)

        #testing updtaing bullets and such
        self.defender_list.on_update(delta_time)
        for bullet in self.bullet_list:
            if bullet.center_x > c.SCREEN_WIDTH:
                bullet.remove_from_sprite_lists()
            if arcade.check_for_collision_with_list(bullet,self.live_attackers):
                #get the sprite object hit by the bullet
                attackerHit = arcade.check_for_collision_with_list(bullet, self.live_attackers)[0]
                print("Current health",attackerHit.get_durability())
                attackerHit.decrement_health(15)
                print("Is enemy dead: ",attackerHit.is_dead())
                print("End hitpoint")
                bullet.remove_from_sprite_lists()

        self.bullet_list.update()

        self.sun1.move()
