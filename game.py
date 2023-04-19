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
from sunflower import Sunflower


class Game(arcade.View):
    def __init__(self, level: int, window):
        super().__init__(window)
        # arcade.set_viewport(0, c.SCREEN_WIDTH,0,c.SCREEN_HEIGHT)
        # arcade.set_background_color(arcade.color.ANDROID_GREEN)

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
                # SCENE FOR ALL SPRITES TO RENDER ON
        self.scene = arcade.Scene()

        # TEMP SUN CREATION
        # self.sun1 = Sun()
        self.sun_list = arcade.SpriteList()

        for x in range(0, 10):
            sun = Sun(sunflower_sun=False)
            self.sun_list.append(sun)

        #test bullet and defenders
        self.defender_list = arcade.SpriteList()
        self.bullet_list = arcade.SpriteList()
        # defender1 = Defender(1,1,self.bullet_list,1.5)
        # self.defender_list.append(defender1)
        defender3 = Defender(2,1,self.bullet_list,1.3, [0,0])
        self.defender_list.append(defender3)
        self.defender_list.append(Defender(2, 2, self.bullet_list, 1.5, [1,0]))
        self.defender_list.append(Defender(2, 3, self.bullet_list, 1.5, [2,0]))
        self.defender_list.append(Defender(2, 4, self.bullet_list, 1.5, [3,0]))
        self.defender_list.append(Defender(5, 5, self.bullet_list, 1.5, [4,0]))
        self.defender_list.append(Sunflower(1, 2, [3,2]))
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

        #testing getting the square 
         
        for row in self.grid.grid_list:
            for square in row:
                if square.in_square(x,y):
                    print(f'SQUARE FOUND Pressed [{x} {y}]{square.get_position()} {square.get_abs_coords()}')
                    
                    lane = square.get_position()[0] + 1
                    print(lane)

                    if (self.plant1_selected) and (not square.has_plant):
                        if self.currency >= 50:
                            defender = Defender(1, lane, self.bullet_list, 1.5, square.get_position())
                            self.defender_list.append(Sunflower(1, lane,square.get_position()))
                            self.currency -= 50
                            square.add_plant()
                    elif (self.plant2_selected) and (not square.has_plant):
                        if self.currency >= 100:
                            defender = Defender(2, lane, self.bullet_list, 1.5, square.get_position())
                            self.defender_list.append(defender)
                            self.currency -= 100
                            square.add_plant()
                    elif (self.plant3_selected) and (not square.has_plant):
                        if self.currency >= 150:
                            defender = Defender(3, lane, self.bullet_list, 1.5, square.get_position())
                            self.defender_list.append(defender)
                            self.currency -= 150
                            square.add_plant()
                    elif (self.plant4_selected) and (not square.has_plant):
                        if self.currency >= 200:
                            defender = Defender(4, lane, self.bullet_list, 1.5, square.get_position())
                            self.defender_list.append(defender)
                            self.currency -= 200
                            square.add_plant()
                    elif (self.plant5_selected) and (not square.has_plant):
                        if self.currency >= 300:
                            defender = Defender(5, lane, self.bullet_list, 1.5, square.get_position())
                            self.defender_list.append(defender)
                            self.currency -= 300
                            square.add_plant()
                    elif (self.shovel_selected):
                        if square.has_plant:
                            for plant in self.defender_list:
                                if plant.get_position() == square.get_position():
                                    self.defender_list.remove(plant)
                                    square.remove_plant()


        self.bullet_list.update()
        self.defender_list.update()

        for defender in self.defender_list:
            if isinstance(defender, Sunflower) and defender.has_sun and defender.sun.in_sun(x, y):
                self.currency += c.SUN_ADDITION
                self.sun_list.remove(defender.collect_sun())



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

        self.sun_list.draw()

        # TEMPORARY SUN DRAWING
        # if self.sun1.sun_list != None:
        #     self.sun1.sun_list.draw()
    def on_update(self, delta_time):
        self.game_time += delta_time
        if self.game_time%10==0:
            self.sun_list.append(Sun(False))
        current_total = 0
        sun = None
        for defender in self.defender_list:
            sun = defender.on_update(delta_time)
            if sun:
                sun.set_position(defender.center_x, defender.center_y)
                self.sun_list.append(sun)
            defender.is_active = False
            for attacker in self.live_attackers:
                if attacker.lane == defender.lane:
                    defender.is_active = True
                   
        # Wave 0 is just random spawning
        # to spawn attackers
        if self.current_wave == 0:
            if self.wave_0_spawn_times and self.game_time > self.wave_0_spawn_times[0] + 10:  # +10 for now because game time atarts at ~10
                self.wait_to_start_wave = False
                self.wave_0_spawn_times.pop(0)
                self.live_attackers.append(self.waves[0].pop(0))
            if not self.live_attackers and not self.wait_to_start_wave:
                self.current_wave += 1
                self.pause_between_waves = self.game_time + 10
                self.wait_to_start_wave = True

        # Waves 1 and 2 are released all at once (ish)
        elif self.current_wave == 1 or self.current_wave == 2: # for the actual waves of attackers
            if self.game_time > self.pause_between_waves:  # wait 10 secs between waves
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

            #attack defender
            if arcade.check_for_collision_with_list(attacker,self.defender_list):
                defenderHit = arcade.check_for_collision_with_list(attacker, self.defender_list)[0]
                #set speed to 0
                attacker.speed = 0
                #if time is greater than attack duration attack
                if attacker.ready_to_attack(delta_time):
                
                
                    defenderHit.decrement_health(attacker.damage)
                    print(f'Damaged defender: {defenderHit.durability}')
                #if defender is dead reset speed
                if defenderHit.is_dead():
                    self.defender_list.remove(defenderHit)
                    
            #reset speed for multiple attackers after defender dies
            if not arcade.check_for_collision_with_list(attacker,self.defender_list) and attacker.speed == 0:
                attacker.reset_speed()

        self.defender_list.update()

        #testing updtaing bullets and such
        # self.defender_list.on_update(delta_time)
        for bullet in self.bullet_list:
            if bullet.center_x > c.SCREEN_WIDTH:
                bullet.remove_from_sprite_lists()
            if arcade.check_for_collision_with_list(bullet,self.live_attackers):
                #get the sprite object hit by the bullet
                attackerHit = arcade.check_for_collision_with_list(bullet, self.live_attackers)[0]
                #different effects for each bullet type
                
                
                attackerHit.alter_speed(bullet.speed_change) #only changes for snowball
                attackerHit.decrement_health(bullet.damage)   
                bullet.remove_from_sprite_lists()

        self.bullet_list.update()

        #SUN MOVEMENT
        for sun in self.sun_list:
            if sun.lifespan < 0:
                self.sun_list.remove(sun)
            else:
                sun.move()
                # print("moving: ", x)





