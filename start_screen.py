import arcade
import constants as c
from game import Game
from choose_defenders import ChooseDefenders



class StartScreen(arcade.View):
    """ Class that manages the 'start' game view. """
    def __init__(self, window):
        super().__init__(window=window)
        self.manager = arcade.gui.UIManager()
        self.manager.enable()
        arcade.set_background_color(arcade.color.ARMY_GREEN)

        self.h_box = arcade.gui.UIBoxLayout()

        for level_name in c.levelsDict.keys():
            button = arcade.gui.UIFlatButton(text="Level " + str(level_name), width=200)
            button.level = level_name
            self.h_box.add(button.with_space_around(bottom=20))
            button.on_click = self.on_click_game
        self.manager.add(
            arcade.gui.UIAnchorWidget(
                anchor_x="center_x",
                anchor_y="center_y",
                child=self.h_box)
        )



    def on_draw(self):
        self.clear()
        self.manager.draw()

    def on_click_game(self, event):
        print(event.source.level)
        choose_defenders = ChooseDefenders(self.window, event.source.level)
        self.window.show_view(choose_defenders)
        # game = Game(1, self.window, [1, 2, 3, 4, 5])
        # game.setup()
        # self.window.show_view(game)



    # def on_mouse_press(self, x, y, button, modifiers):
    #     """If a button is pressed, start the game with the corresponding level. """
    #     for i, button in enumerate(self.button_list):
    #          if button.collides_with_point((x, y)):
    #              game_view = Game(i + 1)
    #              game_view.setup()
    #     #         self.window.show_view(game_view)