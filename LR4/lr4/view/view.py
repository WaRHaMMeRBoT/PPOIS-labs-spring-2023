import os

from kivy.graphics import Rectangle
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.screen import MDScreen

from lr4.view.components.buttons import menu_buttons, plants_buttons
from lr4.view.components.text import weather_info


class MenuScreen(MDScreen):
    def __init__(self, controller, **kwargs):
        super(MenuScreen, self).__init__(**kwargs)
        self.layer = MDBoxLayout()
        self.controller = controller

        self.menu_buttons = menu_buttons(self.controller)

        self.weather = weather_info(self.controller)

        with self.canvas.before:
            Rectangle(pos=(0, 0), size=(1600, 1200),
                      source=os.path.realpath(os.path.dirname(__file__)) + "/assets/backgroud.png")

        self.plants_buttons = plants_buttons(self.controller)

        self.add_widget(self.plants_buttons)

        self.add_widget(self.menu_buttons)

        self.add_widget(self.weather)


class View:
    def __init__(self, controller):
        self.controller = controller
        self.controller.add_widget(MenuScreen(name='menu', controller=self.controller))
