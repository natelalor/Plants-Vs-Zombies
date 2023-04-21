import tests
from game import Game
import arcade
import constants as c
import entrance

from start_screen import StartScreen


def main():
    # commented this out for now as it was making extra windows
    # tests.testLevelCreation()
    # arcade.set_background_color(arcade.color.OLIVE)
    # arcade.start_render()
    # arcade.finish_render()
    # game = Game(1)
    window = arcade.Window(c.SCREEN_WIDTH, c.SCREEN_HEIGHT, c.SCREEN_TITLE)
    start_view = StartScreen(window)
    window.show_view(start_view)
    # game.setup()
    arcade.run()
    # entrance()


if __name__ == '__main__':
    main()
