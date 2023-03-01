from game import Game
import constants as c


def testLevelCreation():
    for level in c.levelsDict:
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
                print(c.enemiesDict[i], "-", numEnemies[i])


