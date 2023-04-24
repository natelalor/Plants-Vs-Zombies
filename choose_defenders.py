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
        self.gui_buttons = []
        self.v_box = arcade.gui.UIBoxLayout()
        self.background = arcade.load_texture("images/garden.jpg")
        self.num_defenders = 5

        for defender in c.defenders_data.keys():
            self.defenders_list.append(defender)


        while self.defenders_list:
            i = 0
            tmp = arcade.gui.UIBoxLayout(vertical=False)
            for column in range(9):
                if len(self.defenders_list) != 0:
                    defender = c.defenders_data[self.defenders_list[0]]
                    button = arcade.gui.UITextureButton(texture=arcade.load_texture("GUI/"+defender['name']+".png"),
                                                        texture_hovered=arcade.load_texture(
                                                            "GUI/"+defender['name']+"-hover.png"),
                                                        texture_pressed=arcade.load_texture(
                                                            "GUI/"+defender['name']+"-selected.png"),
                                                        width=75, height=75)

                    button.defenderId = self.defenders_list[0]
                    button.cost = defender['cost']
                    # used to determine if its selcted
                    button.selected = False
                    self.gui_buttons.append(button)
                    # holds all teh GUI buttons in a box
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
                anchor_x="left",
                anchor_y="top",
                child=self.v_box)
        )

        texture_hovered = arcade.load_texture("GUI/StartButton_hover.png")
        texture_selected = arcade.load_texture("GUI/StartButton_selected.png")
        texture_unselected = arcade.load_texture("GUI/StartButton.png")
        self.start_button = arcade.gui.UITextureButton(texture=texture_unselected, texture_hovered=texture_hovered, texture_pressed=texture_selected )
        self.start_button.on_click = self.start_game
        self.manager.add(
            arcade.gui.UIAnchorWidget(
                anchor_x="right",
                anchor_y="bottom",
                child=self.start_button)
        )

    def on_draw(self):
        self.clear()
        arcade.draw_lrwh_rectangle_textured(0, 0, c.SCREEN_WIDTH, c.SCREEN_HEIGHT, self.background)
        color = (64, 24, 17)
        width = 165 * len(self.gui_buttons)
        # height only needs to be changed if we have more than 9 defenders
        arcade.draw_rectangle_filled(100, 585, width, 100, color)

        self.manager.draw()


        # GUI SLOTS
        for i, button in enumerate(self.gui_buttons):

            if self.gui_buttons[i].selected:  # selection graphic
                arcade.draw_rectangle_outline(center_x=50 + i * 100 - i, center_y=581, color=(77, 123, 48, 255),
                                                width=76,
                                                height=76, border_width=5)
            arcade.draw_text(button.cost, 23.5 + i * 100, 535, arcade.color.WHITE, 20, 40,
                             'center')  # draw the price
        # text and text background
        arcade.draw_rectangle_filled(center_x=485, center_y = 300, color=(0,0,0,100), width=510, height=60)
        arcade.draw_text('Select ' + str(self.num_defenders) + ' more defenders to start the game!', 230,300.0,
                         arcade.color.WHITE,20,50,'left', font_name="Kenny Mini Square")

        # blocks out start button if not enough defenders
        if len(self.chosen_defenders) != c.NUMBER_OF_DEFENDERS:
            arcade.draw_rectangle_filled(center_x=900, center_y=0, color=(0, 0, 0, 200), width=210, height=75)







    def on_choose(self, event):
        # only 5 plants can be selected at a time
        if event.source.defenderId not in self.chosen_defenders and len(self.chosen_defenders) < c.NUMBER_OF_DEFENDERS:
            self.chosen_defenders.append(event.source.defenderId)
            event.source.selected = True
            self.num_defenders = 5 - len(self.chosen_defenders)
        elif event.source.defenderId in self.chosen_defenders:
            self.chosen_defenders.remove(event.source.defenderId)
            event.source.selected = False
            self.num_defenders = 5 - len(self.chosen_defenders)





        for i in self.chosen_defenders:
            print("CHOOSE DEFENDERS:", i, end=', ')
        print()
        if len(self.chosen_defenders) == c.NUMBER_OF_DEFENDERS:
            # self.start_button.texture.image = ":resources:onscreen_controls/shaded_light/start.png"
            print("ready")



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
