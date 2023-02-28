from game import Game
from game import levelsDict
from game import enemiesDict


def testLevelCreation():
    for level in levelsDict:
        print("\nLevel", level)
        numEnemies = {1: 0,
                      2: 0,
                      3: 0,
                      4: 0}
        game = Game(level)
        for i in game.enemies:
            numEnemies[i] += 1
        for i in numEnemies.keys():
            if numEnemies[i] > 0:
                print(enemiesDict[i], "-", numEnemies[i])


