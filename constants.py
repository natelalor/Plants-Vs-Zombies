SCREEN_TITLE = "Plants vs. Zombies"

# grid dimensions
SIZE_COLUMNS = 9
SIZE_ROWS = 5

# This sets the margin between each cell
# and on the edges of the screen.
MARGIN = 5

# gui height
GUI_HEIGHT = 100

# for sun clicking, the currency it gives you
SUN_ADDITION = 25

# Do the math to figure out our screen dimensions
SCREEN_WIDTH = (100 + MARGIN) * SIZE_COLUMNS + MARGIN
SCREEN_HEIGHT = ((100 + MARGIN) * SIZE_ROWS + MARGIN) + GUI_HEIGHT

# individual square object size
SQUARE_SIZE = 1

#  slows down spawning, default 10
SLOW_RATE = 20

LEVEL_TIME = 120

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
attackers_data = {
    1: {
        'name': 'lollipop',
        'speed': 1,
        'damage': 1,
        'durability': 100,
        'image': "images/lolli_enemy.png",
    },
    2: {
        'name': 'chocolate',
        'speed': 1,
        'damage': 1,
        'durability': 100,
        'image': "images/chocolate_enemy.png",
    },
    3: {
        'name': 'creampuff',
        'speed': 1,
        'damage': 1,
        'durability': 100,
        'image': "images/lolli_enemy.png",
    },

}
defenders_data = {
    1: {
        'name': 'toothbrush',
        'speed': 1,
        'damage': 1,
        'durability': 1,
        'image': "images/toothbrush_ally.png",
    },
    2: {
        'name': 'toothpaste',
        'speed': 1,
        'damage': 1,
        'durability': 1,
        'image': "images/toothbrush_ally.png",
    },
    3: {
        'name': 'floss',
        'speed': 1,
        'damage': 1,
        'durability': 1,
        'image': "images/toothbrush_ally.png",
    }
}

waves = {
    1: {
        "intensity": 4,
        "x": -2,
        "weight": .9
    },
    2: {
        "intensity": 1,
        "x": 3,
        "weight": .4
        },
    3: {
        "intensity": .5,
        "x": 9,
        "weight": .1
        }
}

BULLET_SPEED = 4