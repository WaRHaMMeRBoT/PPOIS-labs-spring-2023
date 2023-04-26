from .bar import *
from .add_entity_dialog import *
from .warp_dialog import *

from kivy.metrics import dp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.gridlayout import MDGridLayout


class View:
    def __init__(self, controller):
        self.dialog = None
        self.controller = controller

        self.bar = Bar(self.controller).build_widget()
        self.plants_buttons = plants_buttons(self.controller)
        self.root = MDBoxLayout(self.bar, self.plants_buttons, orientation='vertical')

    def open_add_dialog(self):
        self.dialog = AddEntityDialog(self.controller).build_dialog()
        self.dialog.open()

    def open_warp_dialog(self):
        self.dialog = WarpDialog(self.controller).build_dialog()
        self.dialog.open()

    def close_dialog(self):
        if self.dialog is not None:
            self.dialog.dismiss()

    def update_table(self):
        self.root.remove_widget(self.plants_buttons)
        self.plants_buttons = plants_buttons(self.controller)
        self.root.add_widget(self.plants_buttons)


def plants_buttons(controller):
    entity = controller.base_controller.get_game_board()
    buttons = MDGridLayout(padding=[100], rows=len(entity), cols=len(entity), spacing=20)

    index = 0
    for i in range(len(entity)):
        for j in range(len(entity[0])):
            if not entity[i][j].get_entity():
                button = MDRaisedButton(
                    id=str(index),
                    text="",
                    theme_icon_color="Custom",
                    elevation=0,
                    md_bg_color="#fefbff",
                    icon_color="#6851a5",
                )
                buttons.add_widget(button)
                index += 1
            else:
                text = ''
                for name in entity[i][j].get_entity():
                    text += str(name)
                button = MDRaisedButton(
                    id=str(index),
                    text=text,
                    theme_icon_color="Custom",
                    elevation=0,
                    md_bg_color="#fefbff",
                    icon_color="#6851a5",
                )
                buttons.add_widget(button)
                index += 1
    buttons.pos = (dp(30), dp(-100))
    return buttons
