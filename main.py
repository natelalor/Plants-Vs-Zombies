import tests
from game import Game
import arcade
import constants as c

def main():
    myGame = Game(1)
    print(myGame.enemies)
    # tests.testLevelCreation()
    # arcade.open_window(c.SCREEN_WIDTH, c.SCREEN_HEIGHT, c.SCREEN_TITLE)
    arcade.set_background_color(arcade.color.ARMY_GREEN)
    arcade.start_render()
    arcade.finish_render()
    arcade.run()


main()
