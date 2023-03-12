SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800
SCREEN_TITLE = "Plants vs. Zombies"

# grid dimensions
SIZE_COLUMNS = 9
SIZE_ROWS = 5

# This sets the margin between each cell
# and on the edges of the screen.
MARGIN = 5

# Do the math to figure out our screen dimensions
SCREEN_WIDTH = (100 + MARGIN) * SIZE_COLUMNS + MARGIN
SCREEN_HEIGHT = (100 + MARGIN) * SIZE_ROWS + MARGIN

# individual square object size
SQUARE_SIZE = 1

levelsDict = {
    1: [[2, 10], [3, 2]],
    2: [[2, 8], [3, 2], [4, 2]],
    3: [[2, 8], [3, 4], [4, 3]],
    4: [[2, 4], [3, ]]
}

enemiesDict = {1: "easy",
               2: "normal",
               3: "cone",
               4: "bucket"}
