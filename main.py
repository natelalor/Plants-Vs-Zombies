import tests
from game import Game
import arcade

def main():
    tests.testLevelCreation()
    arcade.open_window(1200, 800, "Plants vs Zombies")
    arcade.set_background_color(arcade.color.GREEN)
    arcade.start_render()
    arcade.finish_render()
    arcade.run()


main()
