import arcade
import constants as c
from game import Game



class StartScreen(arcade.View):
    """ Class that manages the 'start' game view. """
    def __init__(self, window):
        super().__init__(window=window)
        self.manager = arcade.gui.UIManager()
        self.manager.enable()
        arcade.set_background_color(arcade.color.DARK_BLUE_GRAY)

        self.h_box = arcade.gui.UIBoxLayout()
        level_names = [1,2,3]
        for i, level_name in enumerate(level_names):
            button = arcade.gui.UIFlatButton(text="Level " + str(level_name), width=200)
            self.h_box.add(button.with_space_around(bottom=20))
            button.on_click = self.on_click_game
        self.manager.add(
            arcade.gui.UIAnchorWidget(
                anchor_x="center_x",
                anchor_y="center_y",
                child=self.h_box)
        )
        # Adding button in our uimanager
        # self.uimanager.add(
        #     arcade.gui.UIAnchorWidget(
        #         anchor_x="center_x",
        #         anchor_y="center_y",
        #         child=start_button))
    def on_show(self):
        pass
        # Create buttons for each level
        # self.button_list = arcade.SpriteList()
        # button_center_x = c.SCREEN_WIDTH // 2
        # button_center_y = c.SCREEN_HEIGHT // 2
        # button_width = 200
        # button_height = 50
        # level_names = ["Level 1", "Level 2", "Level 3"]
        # for i, level_name in enumerate(level_names):
        #     button = arcade.SpriteSolidColor(button_width, button_height, arcade.color.BLUE)
        #     button.position = (button_center_x, button_center_y - i * (button_height + 10))
        #     button.textures = [
        #         arcade.create_text_image(level_name, arcade.color.WHITE, button_width, button_height, align="center")]
        #     self.button_list.append(button)

    def on_draw(self):
        self.clear()
        self.manager.draw()

    def on_click_game(self, event):
        print("Pressed")
        # loading_screen = LoadingScreen(self.window)
        # self.window.show_view(loading_screen)
        game = Game(1, self.window)
        game.setup()
        self.window.show_view(game)



    # def on_mouse_press(self, x, y, button, modifiers):
    #     """If a button is pressed, start the game with the corresponding level. """
    #     for i, button in enumerate(self.button_list):
    #          if button.collides_with_point((x, y)):
    #              game_view = Game(i + 1)
    #              game_view.setup()
    #     #         self.window.show_view(game_view)