import random
import constants as c




class Game:
    def __init__(self, level: int):
        self.level = level
        self.enemies = []
        self.createEnemies()

    def createEnemies(self):
        for enemyType in c.levelsDict[self.level]:
            for i in range(enemyType[1]):
                self.enemies.append(enemyType[0]) # TODO: Change to append enemy object

