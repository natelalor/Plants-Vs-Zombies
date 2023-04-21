import time
from game import Game
import constants as c
import arcade


def test_game():
    window = arcade.Window(c.SCREEN_WIDTH, c.SCREEN_HEIGHT, c.SCREEN_TITLE)
    game = Game(1, window, [1, 2, 3, 4, 5])
    game.setup()
    window.show_view(game)
    arcade.run()

# test_game()

