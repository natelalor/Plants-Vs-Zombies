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
import arcade.gui

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

        # Create a horizontal BoxGroup to align buttons
        self.h_box = arcade.gui.UIBoxLayout(vertical=False, )

        # Creating the buttons, each button has a loaded texture for hover, and clicked

        plant1_button = arcade.gui.UITextureButton(texture=arcade.load_texture('images/sunflower.png'),texture_hovered= arcade.load_texture('images/sunflowerHover.png'),texture_pressed=arcade.load_texture('images/sunflowerSelected.png'), width=75, height= 75)
        self.h_box.add(arcade.gui.UIBorder(plant1_button.with_border(color=(117, 35, 19, 255)), border_width=10,border_color=(117, 35, 19, 255)))

        plant2_button =arcade.gui.UITextureButton(texture=arcade.load_texture('images/peaShooter.png'),texture_hovered= arcade.load_texture('images/peaShooterHover.png'),texture_pressed=arcade.load_texture('images/peaShooterSelected.png'), width=75, height= 75)
        self.h_box.add(arcade.gui.UIBorder(plant2_button.with_border(color=(117, 35, 19, 255)), border_width=10,border_color=(117, 35, 19, 255)))

        plant3_button = arcade.gui.UITextureButton(texture=arcade.load_texture('images/peaShooter.png'),texture_hovered= arcade.load_texture('images/peaShooterHover.png'),texture_pressed=arcade.load_texture('images/peaShooterSelected.png'), width=75, height= 75)
        self.h_box.add(arcade.gui.UIBorder(plant3_button.with_border(color=(117, 35, 19, 255)), border_width=10,border_color=(117, 35, 19, 255)))

        plant4_button =arcade.gui.UITextureButton(texture=arcade.load_texture('images/peaShooter.png'),texture_hovered= arcade.load_texture('images/peaShooterHover.png'),texture_pressed=arcade.load_texture('images/peaShooterSelected.png'), width=75, height= 75)
        self.h_box.add(arcade.gui.UIBorder(plant4_button.with_border(color=(117, 35, 19, 255)), border_width=10,border_color=(117, 35, 19, 255)))

        plant5_button  =arcade.gui.UITextureButton(texture=arcade.load_texture('images/peaShooter.png'),texture_hovered= arcade.load_texture('images/peaShooterHover.png'),texture_pressed=arcade.load_texture('images/peaShooterSelected.png'), width=75, height= 75)
        self.h_box.add(arcade.gui.UIBorder(plant5_button.with_border(color=(117, 35, 19, 255)), border_width=10,border_color=(117, 35, 19, 255)))

        shovel_button = arcade.gui.UITextureButton(texture=arcade.load_texture('images/shovel.png'),texture_hovered= arcade.load_texture('images/shovel.png'),texture_pressed=arcade.load_texture('images/shovel.png'), width=75, height= 75)
        self.h_box.add(arcade.gui.UIBorder(shovel_button.with_border(color=(117, 35, 19, 255)), border_width=10,border_color=(117, 35, 19, 255)))

        sun = arcade.gui.UITextureButton(texture=arcade.load_texture('images/sun.png'), width=75, height= 75)
        self.h_box.add(arcade.gui.UIBorder(sun.with_border(color=(117, 35, 19, 255)), border_width=10,border_color=(117, 35, 19, 255)))

        # THIS MIGHT BE TEMPORARY its just to display the round
        round = arcade.gui.UITextureButton(texture=arcade.load_texture('images/round.png'), width=100, height= 100)
        self.h_box.add(round.with_space_around(left=155))

        # Initially all plant selections are set to false, these are only true if a plant is clicked on
        self.plant1_selected = False
        self.plant2_selected = False
        self.plant3_selected = False
        self.plant4_selected = False
        self.plant5_selected = False
        self.shovel_selected = False

        # each of these controls an individual button
        # when clicked it sets the buttons selected variable to true and all the other buttons to false
        @plant1_button.event("on_click")
        def on_click_settings(event):
            if (self.plant1_selected):
                self.plant1_selected = False
            else:
                self.plant1_selected = True
                # set others to false
                self.shovel_selected = False
                self.plant2_selected = False
                self.plant3_selected = False
                self.plant5_selected = False
                self.plant4_selected = False



        @shovel_button.event("on_click")
        def on_click_settings(event):
            if (self.shovel_selected):
                self.shovel_selected = False
            else:
                # set clicked to true
                self.shovel_selected = True
                # set others to false
                self.plant1_selected = False
                self.plant2_selected = False
                self.plant3_selected = False
                self.plant5_selected = False
                self.plant4_selected = False

        @plant2_button.event("on_click")
        def on_click_settings(event):
            if (self.plant2_selected):
                self.plant2_selected = False
            else:
                # set clicked to true
                self.plant2_selected = True
                # set others to false
                self.plant1_selected = False
                self.plant4_selected = False
                self.plant3_selected = False
                self.plant5_selected = False
                self.shovel_selected = False
        @plant3_button.event("on_click")
        def on_click_settings(event):
            if (self.plant3_selected):
                self.plant3_selected = False
            else:
                # set clicked to true
                self.plant3_selected = True
                # set others to false
                self.plant1_selected = False
                self.plant2_selected = False
                self.plant4_selected = False
                self.plant5_selected = False
                self.shovel_selected = False


        @plant4_button.event("on_click")
        def on_click_settings(event):
            if (self.plant4_selected):
                self.plant4_selected = False
            else:
                # set clicked to true
                self.plant4_selected = True
                # set others to false
                self.plant1_selected = False
                self.plant2_selected = False
                self.plant3_selected = False
                self.plant5_selected = False
                self.shovel_selected = False
            #check plant object to see if you have enough currency to buy
            #if not enough set clicked to false


        @plant5_button.event("on_click")
        def on_click_settings(event):
            if (self.plant5_selected):
                self.plant5_selected = False
            else:
                self.plant5_selected = True
                # set others to false
                self.plant1_selected = False
                self.plant2_selected = False
                self.plant3_selected = False
                self.plant4_selected = False
                self.shovel_selected = False

        # Create a widget to hold the h_box(horizontal box) widget, that will center the buttons along the top
        self.manager.add(
            arcade.gui.UIAnchorWidget(
                anchor_x="left",
                anchor_y="top",
                child=self.h_box)
        )


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

        #GUI
        self.manager.draw()


        # currency text (for positioning: 700 is x, 550 is y)
        arcade.draw_text(str(self.currency), 623.5, 535, arcade.color.ALICE_BLUE, 20, 40, 'center')

        # GUI SLOTS
        # FIFTH GUI SLOT
        if (self.currency >= 300):
            # currency text
            arcade.draw_text(str(300), 423.5, 535, arcade.color.ALICE_BLUE, 20, 40, 'center')
            if (self.plant5_selected):
                arcade.draw_rectangle_filled(center_x=445, center_y=581, color=(255, 255, 255, 75), width=75, height=75)
                arcade.draw_rectangle_outline(center_x=445, center_y=581, color=(154, 205, 50, 255), width=76, height=76, border_width= 5)
                arcade.draw_text(str(300), 423.5, 535, arcade.color.ALICE_BLUE, 20, 40, 'center')
        else:
            arcade.draw_rectangle_filled(center_x=445, center_y=581,color=(50, 50, 50, 200), width=75, height=75 )
            arcade.draw_text(str(300), 423.5, 535, arcade.color.RED, 20, 40, 'center')
            self.plant5_selected = False

        # FOURTH GUI SLOT
        if (self.currency >= 200):
            arcade.draw_text(str(200), 323.5, 535, arcade.color.ALICE_BLUE, 20, 40, 'center')
            if (self.plant4_selected):
                arcade.draw_rectangle_filled(center_x=346, center_y=581, color=(255, 255, 255, 75), width=75, height=75)
                arcade.draw_rectangle_outline(center_x=346, center_y=581, color=(154, 205, 50, 255), width=76, height=76, border_width=5)
                arcade.draw_text(str(200), 323.5, 535, arcade.color.ALICE_BLUE, 20, 40, 'center')
        else:
            arcade.draw_rectangle_filled(center_x=346, center_y=581, color=(50, 50, 50, 200), width=75, height=75)
            arcade.draw_text(str(200), 323.5, 535, arcade.color.RED, 20, 40, 'center')
            self.plant4_selected = False

        # THIRD GUI SLOT
        if (self.currency >= 150):
            arcade.draw_text(str(150), 223.5, 535, arcade.color.ALICE_BLUE, 20, 40, 'center')
            if (self.plant3_selected):
                arcade.draw_rectangle_filled(center_x=247, center_y=581, color=(255, 255, 255, 75), width=75, height=75)
                arcade.draw_rectangle_outline(center_x=247, center_y=581, color=(154, 205, 50, 255), width=76, height=76, border_width=5)
                arcade.draw_text(str(150), 223.5, 535, arcade.color.ALICE_BLUE, 20, 40, 'center')

        else:
            arcade.draw_rectangle_filled(center_x=247, center_y=581, color=(50, 50, 50, 200), width=75, height=75)
            arcade.draw_text(str(150), 223.5, 535, arcade.color.RED, 20, 40, 'center')
            self.plant3_selected = False

        # SECOND GUI SLOT
        if (self.currency >= 100):
            arcade.draw_text(str(100), 123.5, 535, arcade.color.ALICE_BLUE, 20, 40, 'center')
            if (self.plant2_selected):
                arcade.draw_rectangle_filled(center_x=150, center_y=581, color=(255, 255, 255, 75), width=75, height=75)
                arcade.draw_rectangle_outline(center_x=150, center_y=581, color=(154, 205, 50, 255), width=76, height=76, border_width=5)
                arcade.draw_text(str(100), 123.5, 535, arcade.color.ALICE_BLUE, 20, 40, 'center')
        else:
            arcade.draw_rectangle_filled(center_x=150, center_y=581, color=(50, 50, 50, 200), width=75, height=75)
            arcade.draw_text(str(100), 123.5, 535, arcade.color.RED, 20, 40, 'center')
            self.plant2_selected = False

        # FIRST GUI SLOT
        if (self.currency >= 50):
            arcade.draw_text(str(50), 23.5, 535, arcade.color.ALICE_BLUE, 20, 40, 'center')
            if (self.plant1_selected):
                arcade.draw_rectangle_filled(center_x=50, center_y=581, color=(255, 255, 255, 75), width=75, height=75)
                arcade.draw_rectangle_outline(center_x=50, center_y=581, color=(245, 245, 0), width=76, height=76, border_width=5)
                arcade.draw_text(str(50), 23.5, 535, arcade.color.ALICE_BLUE, 20, 40, 'center')
        else:
            arcade.draw_rectangle_filled(center_x=50, center_y=581, color=(50, 50, 50, 200), width=75, height=75)
            arcade.draw_text(str(50), 23.5, 535, arcade.color.RED, 20, 40, 'center')
            self.plant1_selected = False


        if (self.shovel_selected):
            arcade.draw_rectangle_filled(center_x=545, center_y=581, color=(255, 255, 255, 75), width=75, height=75)
            arcade.draw_rectangle_outline(center_x=545, center_y=581, color=(200, 0, 0), width=76, height=76, border_width=5)

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
            #change speed (for snowballs)
            attacker.center_x -= attacker.speed
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
                #different effects for each bullet type
                if bullet.type == 1:
                    
                    attackerHit.decrement_health(15)
                else:
                    attackerHit.alter_speed(.9) 
                    attackerHit.decrement_health(8)   
                bullet.remove_from_sprite_lists()

        self.bullet_list.update()

        self.sun1.move()
