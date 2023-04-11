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
        self.manager = arcade.gui.UIManager()
        self.manager.enable()
        self.live_attackers = None
        self.game_time = 0
        self.level = level
        self.scene = arcade.Scene()
        self.attackers_list = None
        self.waves = []
        self.current_wave = 0
        self.wave_0_spawn_times = []
        self.num_dead_attackers = 0
        self.num_attackers_to_kill = 0
        self.pause_between_waves = 0
        self.wait_to_start_wave = True
        self.lanes = [1, 2, 3, 4, 5]

        # for defender selection/deselection
        self.clicked = 0

        # aniamtion
        self.update_animation = True
        self.frame_count = 0

        #testing Defenders and Bullets
        self.defender_list = None
        self.bullet_list = None

        # Create a horizontal BoxGroup to align buttons
        self.h_box = arcade.gui.UIBoxLayout(vertical=False, )

        # Creating the buttons, each button has a loaded texture for hover, and clicked

        plant1_button = arcade.gui.UITextureButton(texture=arcade.load_texture('GUI/sunflower.png'),texture_hovered= arcade.load_texture('GUI/sunflowerHover.png'),texture_pressed=arcade.load_texture('GUI/sunflowerSelected.png'), width=75, height= 75)
        self.h_box.add(arcade.gui.UIBorder(plant1_button.with_border(color=(117, 35, 19, 255)), border_width=10,border_color=(117, 35, 19, 255)))

        plant2_button =arcade.gui.UITextureButton(texture=arcade.load_texture('GUI/pea_shooter.png'),texture_hovered= arcade.load_texture('GUI/pea_shooter_hover.png'),texture_pressed=arcade.load_texture('GUI/pea_shooter_selected.png'), width=75, height= 75)
        self.h_box.add(arcade.gui.UIBorder(plant2_button.with_border(color=(117, 35, 19, 255)), border_width=10,border_color=(117, 35, 19, 255)))

        plant3_button = arcade.gui.UITextureButton(texture=arcade.load_texture('GUI/peaShooter.png'),texture_hovered= arcade.load_texture('GUI/peaShooterHover.png'),texture_pressed=arcade.load_texture('GUI/peaShooterSelected.png'), width=75, height= 75)
        self.h_box.add(arcade.gui.UIBorder(plant3_button.with_border(color=(117, 35, 19, 255)), border_width=10,border_color=(117, 35, 19, 255)))

        plant4_button =arcade.gui.UITextureButton(texture=arcade.load_texture('GUI/peaShooter.png'),texture_hovered= arcade.load_texture('GUI/peaShooterHover.png'),texture_pressed=arcade.load_texture('GUI/peaShooterSelected.png'), width=75, height= 75)
        self.h_box.add(arcade.gui.UIBorder(plant4_button.with_border(color=(117, 35, 19, 255)), border_width=10,border_color=(117, 35, 19, 255)))

        plant5_button  =arcade.gui.UITextureButton(texture=arcade.load_texture('GUI/peaShooter.png'),texture_hovered= arcade.load_texture('GUI/peaShooterHover.png'),texture_pressed=arcade.load_texture('GUI/peaShooterSelected.png'), width=75, height= 75)
        self.h_box.add(arcade.gui.UIBorder(plant5_button.with_border(color=(117, 35, 19, 255)), border_width=10,border_color=(117, 35, 19, 255)))

        shovel_button = arcade.gui.UITextureButton(texture=arcade.load_texture('GUI/shovel.png'),texture_hovered= arcade.load_texture('GUI/Shovel_hover.png'),texture_pressed=arcade.load_texture('GUI/Shovel_selected.png'), width=75, height= 75)
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
                # SCENE FOR ALL SPRITES TO RENDER ON
        self.scene = arcade.Scene()

        # TEMP SUN CREATION
        # self.sun1 = Sun()
        self.sun_list = arcade.SpriteList()
        for x in range(0, 10):
            sun = Sun()
            self.sun_list.append(sun)


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
        self.num_attackers_to_kill = len(self.waves[0])



        self.grid = Grid(c.SIZE_COLUMNS, c.SIZE_ROWS)
        self.game_time = 0
        # for i in c.SIZE_ROWS:
        #     self.scene.add_sprite("Defenders", Defender(1, i, 1))


    def randomize(self):
        def random_lane() -> int:
            if not self.lanes:
                self.lanes = [1, 2, 3, 4, 5]
            loc = random.randint(0, len(self.lanes)-1)
            if random.randint(0, 10) > 2: # 80% of the time fill the unused lanes
                return self.lanes.pop(loc)
            return random.randint(1,5)  # the rest of the time choose a random lane

        """
        Organize a list semi-randomly
            :param List attacker: the list to be randomized
        """
        for i in range(len(self.attackers_list)*10):
            rand = random.randint(0, len(self.attackers_list)-1)
            self.attackers_list.append(self.attackers_list.pop(rand))
        min = 100
        max = 0
        first_min = 0
        first_max = 0
        for i, attacker in enumerate(self.attackers_list): # find the indicies of the min and max attackers
            if attacker.get_type() < min:
                min = attacker.get_type()
                first_min = i
            elif attacker.get_type() > max:
                max = attacker.get_type()
                first_max = i
        self.attackers_list.insert(0, self.attackers_list.pop(first_min))  # move it to the front
        self.attackers_list.append(self.attackers_list.pop(first_max))  # move it to the end
        for attacker in self.attackers_list:  # set the lanes
            attacker.set_position_lane(random_lane())
        print("FIXED ATTACKERS_LIST")
        for i in self.attackers_list:
            print(i.get_type(), end=", ")


    def create_attackers(self):
        for enemyType in c.levelsDict[self.level]:
            for i in range(enemyType[1]):
                self.attackers_list.append(Attacker(enemyType[0]))
        self.randomize()
        wave_1_end = round(len(self.attackers_list) * .25)
        self.waves.append(self.attackers_list[0:wave_1_end])  # first wave includes 25% of attackers
        wave_2_end = round(len(self.attackers_list) * .3 + wave_1_end)
        self.waves.append(self.attackers_list[wave_1_end:wave_2_end])  # second wave is 30% of attackers
        self.waves.append(self.attackers_list[wave_2_end:])  # final wave is 45% of the attackers
        for attacker in self.waves[0]:
            self.wave_0_spawn_times.append(random.randint(0, c.GAME_LENGTH*c.FIRST_ROUND_PERCENT))
        self.wave_0_spawn_times.sort()


    def run_game(self):
        pass

    # MOUSE INPUT TESTING HERE
    def on_mouse_press(self, x, y, button, modifiers):
        # clicked = 0
        print("Mouse button is pressed")

        # sun click testing
        for z in self.sun_list:
            if z.in_sun(x, y):
                if self.sun_list != None:
                    self.currency += c.SUN_ADDITION

                # make sprite disappear
                self.sun_list.remove(z)


    def on_draw(self):
        """Render the screen. """

        # self.clear()

        arcade.start_render()
        self.grid.grid_draw()
        self.scene.draw()
        # self.live_attackers.draw()


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
        # TEMPORARY SUN DRAWING
        # if self.sun1.sun_list != None:
        #     self.sun1.sun_list.draw()

        # SUN
        self.sun_list.draw()
    def on_update(self, delta_time):
        self.game_time += delta_time
        current_total = 0
        for defender in self.defender_list:
            defender.is_active = False
            for attacker in self.live_attackers:
                if attacker.lane == defender.lane:
                    defender.is_active = True
                    break
        # Wave 0 is just random spawning
        # to spawn attackers
        if self.current_wave == 0:
            if self.wave_0_spawn_times and self.game_time > self.wave_0_spawn_times[0] + 10:  # +10 for now because game time atarts at ~10
                self.wait_to_start_wave = False
                print(self.game_time, self.wave_0_spawn_times[0])
                self.wave_0_spawn_times.pop(0)
                print(self.wave_0_spawn_times)
                self.live_attackers.append(self.waves[0].pop(0))
            if not self.live_attackers and not self.wait_to_start_wave:
                self.current_wave += 1
                self.pause_between_waves = self.game_time + 10
                self.wait_to_start_wave = True

        # Waves 1 and 2 are released all at once (ish)
        elif self.current_wave == 1 or self.current_wave == 2: # for the actual waves of attackers
            if self.game_time > self.pause_between_waves:  # wait 10 secs between waves
                print("WAVE", self.current_wave)
                if self.waves[self.current_wave] and random.randint(0, 100) > 98:  # prevent all from spawning at once
                    self.live_attackers.append(self.waves[self.current_wave].pop(0))
                    self.wait_to_start_wave = False
            if not self.wait_to_start_wave and not self.live_attackers:
                self.current_wave += 1
                self.pause_between_waves = self.game_time + 10
                self.wait_to_start_wave = True
        elif self.current_wave >= 3:
            print("GAME OVER")
            exit()



        for attacker in self.live_attackers:
            #change speed (for snowballs)
            attacker.center_x -= attacker.speed
            if attacker.center_x <= 0:
                attacker.kill()
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

        #SUN MOVEMENT
        for x in range(len(self.sun_list)):
            if (not self.sun_list[x].is_dead()):
                self.sun_list[x].move()
                print("moving: ", x)

        if self.update_animation:
            self.live_attackers.update_animation()
            self.defender_list.update_animation()

            self.update_animation = False
        else:
            if self.frame_count > 2:
                self.frame_count = 0
                self.update_animation = True
            else:
                self.frame_count += 1





