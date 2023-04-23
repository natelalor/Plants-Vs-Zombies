import time

import arcade
import constants as c
from game import Game


class ChooseDefenders(arcade.View):
    def __init__(self, window, level):
        super().__init__(window=window)
        self.level = level
        self.manager = arcade.gui.UIManager()
        self.manager.enable()
        self.chosen_defenders = []
        self.defenders_list = []
        self.v_box = arcade.gui.UIBoxLayout()

        for defender in c.defenders_data.keys():
            self.defenders_list.append(defender)

        while self.defenders_list:
            i = 0
            tmp = arcade.gui.UIBoxLayout(vertical=False)
            for column in range(4):
                if len(self.defenders_list) != 0:
                    defender = c.defenders_data[self.defenders_list[0]]
                    button = arcade.gui.UITextureButton(texture=arcade.load_texture("GUI/"+defender['name']+".png"),
                                                        texture_hovered=arcade.load_texture(
                                                            "GUI/"+defender['name']+"-hover.png"),
                                                        texture_pressed=arcade.load_texture(
                                                            "GUI/"+defender['name']+"-selected.png"),
                                                        width=75, height=75)
                    button.defenderId = self.defenders_list[0]

                    tmp.add(
                        arcade.gui.UIBorder(button.with_border(color=(117, 35, 19, 255)), border_width=10,
                                            border_color=(117, 35, 19, 255)))
                    button.on_click = self.on_choose
                    self.defenders_list.pop(0)

                else:
                    break
            self.v_box.add(tmp)

        self.manager.add(
            arcade.gui.UIAnchorWidget(
                anchor_x="center_x",
                anchor_y="center_y",
                child=self.v_box)
        )

        texture_hovered = arcade.load_texture("GUI/StartButton_hover.png")
        texture_selected = arcade.load_texture("GUI/StartButton_selected.png")
        texture_unselected = arcade.load_texture("GUI/StartButton.png")
        self.start_button = arcade.gui.UITextureButton(texture=texture_unselected, texture_hovered=texture_hovered, texture_selected=texture_selected)
        self.start_button.on_click = self.start_game



    def on_draw(self):
        self.clear()
        self.manager.draw()

    def on_choose(self, event):

        # loading_screen = LoadingScreen(self.window)
        # self.window.show_view(loading_screen)
        if event.source.defenderId not in self.chosen_defenders:
            self.chosen_defenders.append(event.source.defenderId)
        else:
            self.chosen_defenders.remove(event.source.defenderId)
        for i in self.chosen_defenders:
            print("CHOOSE DEFENDERS:", i, end=', ')
        print()
        if len(self.chosen_defenders) == c.NUMBER_OF_DEFENDERS:
            # self.start_button.texture.image = ":resources:onscreen_controls/shaded_light/start.png"
            print("ready")
            self.manager.add(
                arcade.gui.UIAnchorWidget(
                    anchor_x="right",
                    anchor_y="bottom",
                    child=self.start_button)
            )

    def start_game(self, event):
        if len(self.chosen_defenders) == c.NUMBER_OF_DEFENDERS:
            # game = Game(1, self.window, [1,2,3,4,5])
            self.manager.disable()
            print("CHOOSE_DEFENDER MANAGER DISABLED")
            game = Game(self.level, self.window, self.chosen_defenders)
            game.setup()
            self.window.show_view(game)

    def on_show_view(self):
        print("#####IN ONSHOWVIEW CHOOSE_DEFENDERS")
