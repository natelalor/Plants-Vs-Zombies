import tests
from game import Game
import arcade
import constants as c

def main():
    tests.testLevelCreation()
    arcade.open_window(c.SCREEN_WIDTH, c.SCREEN_HEIGHT, c.SCREEN_TITLE)
    arcade.set_background_color(arcade.color.GREEN)
    arcade.start_render()
    arcade.finish_render()
    arcade.run()


main()
