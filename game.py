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
        self.attacker = Attacker(0, 0, 0, "test", 900, 50)
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
        #self.bullet_list.draw()
        #self.player_list.draw()
