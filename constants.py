SCREEN_TITLE = "Plants vs. Zombies"
TEST_WIDTH = 1200
TEST_HEIGHT = 800
# grid dimensions
SIZE_COLUMNS = 9
SIZE_ROWS = 5

# This sets the margin between each cell
# and on the edges of the screen.
MARGIN = 5

# gui height
GUI_HEIGHT = 100

# for sun clicking, the currency it gives you
SUN_ADDITION = 50

# Do the math to figure out our screen dimensions
SCREEN_WIDTH = (100 + MARGIN) * SIZE_COLUMNS + MARGIN
SCREEN_HEIGHT = ((100 + MARGIN) * SIZE_ROWS + MARGIN) + GUI_HEIGHT

# individual square object size
SQUARE_SIZE = 1

#  slows down spawning, default 10
SLOW_RATE = 15

LEVEL_TIME = 120

levelsDict = {
    # level: [[enemyType, number of that type]]
    1: [[1, 15], [2, 6]],
    2: [[1, 8], [2, 8], [3, 5], [4, 2]],
    3: [[1, 6], [2, 10], [3, 4], [4, 3]],
    4: [[1, 4], [2, 10], [3, 10], [4,5]]
}

# TODO: eventually add characteristics to this dict as a list in value
enemiesDict = {1: "easy",
               2: "normal",
               3: "cone",
               4: "bucket"}
attackers_data = {
    1: {
        'name': 'Zombie',
        'speed': 1,
        'damage': 100,
        'durability': 175,
        'attack_speed': 1.5,
        'image':"animations/zombie_walk/0.png",
    },
    2: {
        'name': 'Conehead_Zombie',
        'speed': 1,
        'damage': 100,
        'durability': 550,
        'attack_speed': 3,
        'image': "animations/zombie_walk/0.png",
    },
    3: {
        'name': 'Buckethead_Zombie',
        'speed': .7,
        'damage': 100,
        'durability': 1250,
        'attack_speed': 2,
        'image': "animations/zombie_walk/0.png",
    },
    4: {
        'name': 'Tank_Zombie',
        'speed': .5,
        'damage': 200,
        'durability': 2500,
        'attack_speed': 2,
        'image': "animations/zombie_walk/0.png",
    }

}
defenders_data = {
    1: {
        'name': 'Sunflower',
        'speed': 1,
        'damage': 0,
        'durability': 300,
        'image': "GUI/Sunflower.png",
        'cost':50
    },
    2: {
        'name': 'Pea_Shooter',
        'speed': 1,
        'damage': 20,
        'durability': 300,
        'image': "GUI/Pea_Shooter.png",
        'cost': 100
    },
    3: {
        'name': 'Snow_Pea',
        'speed': 1,
        'damage': 20,
        'durability': 300,
        'image': "GUI/Snow_Pea.png",
        'cost': 150
    },
    4: {
        'name': 'WallNut',
        'speed': 1,
        'damage': 0,
        'durability': 4000,
        'image': "GUI/WallNut.png",
        'cost': 50
    },
    5: {
        'name': 'Repeater',
        'speed': 1,
        'damage': 20,
        'durability': 300,
        'image': "GUI/Repeater.png",
        'cost' : 200
    },
    6: {
        'name': 'Shiny_Pea',
        'speed': 1,
        'damage': 40,
        'durability': 1,
        'image': "GUI/Shiny_Pea.png",
        'cost' : 450
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

GAME_LENGTH = 120
FIRST_ROUND_PERCENT = .4

SUNFLOWER_WAIT_TIME = 25

NUMBER_OF_DEFENDERS = 5

STARTING_SUNS = 125

SLOW_ATTACKERS = 3

SUN_INTERVAL = 15

WIN_MESSAGES = {
    1: "Congratulations! You defended your house from the zombies...""It's not over yet though...",
    2: ["We're glad you passed that easy level...now for a real challenge..."],
    3: ["Now for the hardest level..."],
    4: ["CONGRATS! YOU WON"]
}