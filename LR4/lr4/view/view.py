from kivy.uix.screenmanager import Screen
from kivymd.uix.gridlayout import MDGridLayout

from lr4.view.components.buttons import menu_buttons, plants_buttons


class MenuScreen(Screen):
    def __init__(self, controller, **kwargs):
        super(MenuScreen, self).__init__(**kwargs)
        self.controller = controller

        self.menu_buttons = menu_buttons()

        self.menu_buttons.pos = (1300, 880)
        self.plants_buttons = plants_buttons(self.controller)

        self.plants_buttons.pos = (150, -150)

        self.add_widget(self.plants_buttons)

        self.add_widget(self.menu_buttons)


class View:
    def __init__(self, controller):
        self.controller = controller
        self.controller.add_widget(MenuScreen(name='menu', controller=self.controller))
