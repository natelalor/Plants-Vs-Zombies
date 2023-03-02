import random
import constants as c
import arcade
from grid import Grid


class Game(arcade.Window):
    def __init__(self, level: int):
        super().__init__(c.SCREEN_WIDTH, c.SCREEN_HEIGHT, c.SCREEN_TITLE)
        self.level = level
        self.enemies = []
        # self.enemies = arcade.SpriteList() TODO: Swap these lines once we start creating sprites
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

        for enemy in self.enemies:
            if enemy == 1:
                pass
                # arcade.draw_circle_filled(random.randrange(0, 1200), random.randrange(0, 800), 50, arcade.color.GREEN)

        # self.clear()

        # self.enemies.draw()
        # self.bullet_list.draw()
        # self.player_list.draw()
    def on_update(self, delta_time: float):
        pass

