import tests
from game import Game
import arcade
import constants as c
import multiprocessing
import arcade.gui


# class Entrance():
#
#     manager = arcade.gui.UIManager()
#     manager.enable()
#
#     start_button = arcade.gui.UIFlatButton(text="Start Game", width=200)
#
#     @start_button.event("on_click")
#         def on_click_settings(event):
#             arcade.run()
#
#
# def on_draw(self):
#     self.clear()
#     self.manager.draw()