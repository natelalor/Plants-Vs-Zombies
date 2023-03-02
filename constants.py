SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800
SCREEN_TITLE = "Plants vs. Zombies"

# grid dimensions
SIZE_COLUMNS = 9
SIZE_ROWS = 5

# individual square object size
SQUARE_SIZE = 1

levelsDict = {
    # level: [[enemyType, number of that type]]
    1: [[2, 10], [3, 2]],
    2: [[2, 8], [3, 2], [4, 2]],
    3: [[2, 8], [3, 4], [4, 3]],
    4: [[2, 4], [3, 0]]
}

# TODO: eventually add characteristics to this dict as a list in value
enemiesDict = {1: "easy",
               2: "normal",
               3: "cone",
               4: "bucket"}