import random

enemiesDict = {1: "easy",
               2: "normal",
               3: "cone",
               4: "bucket"}

levelsDict = {
    1: [[2, 10], [3, 2]],
    2: [[2, 8], [3, 2], [4, 2]],
    3: [[2, 8], [3, 4], [4, 3]]
}

class Game:
    def __init__(self, level: int):
        self.level = level
        self.enemies = []
        self.createEnemies()

    def createEnemies(self):
        for enemyType in levelsDict[self.level]:
            for i in range(enemyType[1]):
                self.enemies.append(enemyType[0]) # TODO: Change to append enemy object

