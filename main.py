import tests
from game import Game
import arcade
import constants as c
import entrance

from start_screen import StartScreen


def main():
    window = arcade.Window(c.SCREEN_WIDTH, c.SCREEN_HEIGHT, c.SCREEN_TITLE)
    start_view = StartScreen(window)
    window.show_view(start_view)
    arcade.run()


if __name__ == '__main__':
    main()
