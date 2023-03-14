import random
import constants as c
import arcade
from defender import Defender
from attacker import Attacker
from grid import Grid



class Game(arcade.Window):
    def __init__(self, level: int):
        super().__init__(c.SCREEN_WIDTH, c.SCREEN_HEIGHT, c.SCREEN_TITLE)
        self.level = level
        self.enemies = []
        self.createEnemies()

        # Tests placing an attacker and defender on the grid
                                # first param: 1, 2, are different types: lolli, chocoalte
                                # last param: integer for lane, 1-5
        self.attacker = Attacker(1, 0, 0, 0, "test", 1)
        self.attacker2 = Attacker(2, 0, 0, 0, "test2", 2)
        self.attacker3 = Attacker(1, 0, 0, 0, "test3", 3)
        self.attacker4 = Attacker(2, 0, 0, 0, "test4", 4)
        self.attacker5 = Attacker(1, 0, 0, 0, "test4", 5)
        self.defender = Defender(0, 0, 0, "test", 50, 50)

        self.createEnemies()
        self.grid = Grid(c.SIZE_COLUMNS, c.SIZE_ROWS)






    def createEnemies(self):
        for enemyType in c.levelsDict[self.level]:
            for i in range(enemyType[1]):
                self.enemies.append(enemyType[0])  # TODO: Change to append enemy object

    def runGame(self):
        pass

    def on_draw(self):
        """Render the screen. """

        self.clear()

        #self.enemies.draw()
        self.grid.grid_draw()
        # PLACEHOLDER
        # Prints attacker (red) and defender (blue) as an example
        self.attacker.draw()
        self.defender.draw()
        self.attacker.enemy_list.draw()
        self.attacker2.enemy_list.draw()
        self.attacker3.enemy_list.draw()
        self.attacker4.enemy_list.draw()
        self.attacker5.enemy_list.draw()
        #self.bullet_list.draw()
        #self.player_list.draw()
