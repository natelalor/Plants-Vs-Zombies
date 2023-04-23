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
        self.background = arcade.load_texture("images/menu.jpg")

        self.h_box = arcade.gui.UIBoxLayout()
        button = arcade.gui.UIFlatButton(text="Start Game", width=200)
        self.h_box.add(button.with_space_around(top=250))
        button.on_click = self.on_click_game

        self.manager.add(
            arcade.gui.UIAnchorWidget(
                anchor_x="center_x",
                anchor_y="center_y",
                child=self.h_box)
        )



    def on_draw(self):
        self.clear()
        arcade.draw_lrwh_rectangle_textured(0, 0, c.SCREEN_WIDTH, c.SCREEN_HEIGHT, self.background)
        self.manager.draw()

    def on_click_game(self, event):
        choose_defenders = ChooseDefenders(self.window, 1)
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