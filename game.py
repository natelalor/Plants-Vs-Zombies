import random
import constants as c
import arcade
from sun import Sun
from defender import Defender
from attacker import Attacker
from grid import Grid
import random


class Game(arcade.Window):
    def __init__(self, level: int):
        super().__init__(c.SCREEN_WIDTH, c.SCREEN_HEIGHT, c.SCREEN_TITLE)
        self.level = level
        self.enemies = []
        self.create_enemies()
        self.currency = 100

        # Tests placing an attacker and defender on the grid
        # first param: 1, 2, are different types: lolli, chocoalte, etc
        # second param: integer for lane, 1-5

        self.attacker1 = Attacker(random.randint(1, 2), random.randint(1, 5))
        self.defender1 = Defender(random.randint(1, 2), random.randint(1, 5))



        # TEMP SUN CREATION
        self.sun1 = Sun()

        self.create_enemies()
        self.grid = Grid(c.SIZE_COLUMNS, c.SIZE_ROWS)

    def create_enemies(self):
        for enemyType in c.levelsDict[self.level]:
            for i in range(enemyType[1]):
                self.enemies.append(enemyType[0])  # TODO: Change to append enemy object



    def run_game(self):
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

        # TEMPORARY SUN DRAWING
        self.sun1.sun_list.draw()

        # currency text (for positioning: 700 is x, 550 is y)
        arcade.draw_text("Currency: " + str(self.currency), 700, 550, arcade.color.ALICE_BLUE, 20, 40, 'left')

        # THIS IS TEMPORARY SPAWNING UNTIL WE IMPLEMENT SPAWNING SYSTEM
        self.attacker1.enemy_list.draw()

        # self.attacker.enemy_list.draw()

        # self.defender.ally_list.draw()
        self.defender1.ally_list.draw()


        #self.bullet_list.draw()
        #self.player_list.draw()

    def on_update(self, delta_time):

        self.attacker1.move()

        self.sun1.move()

        # good if statement to spawn things at different intervals
        # if random.random() < 0.01:







