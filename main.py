import tests
from game import Game
import arcade
import constants as c

def main():
    # commented this out for now as it was making extra windows
    # tests.testLevelCreation()
    # arcade.set_background_color(arcade.color.OLIVE)
    # arcade.start_render()
    # arcade.finish_render()
    game = Game(1)
    game.on_draw()
    arcade.run()

main()

