from kivy import Config
from kivy.core.window import Window
from kivymd.app import MDApp

from controllers.controller import Controller


class App(MDApp):

    def build(self):
        Window.size = (1200, 750)
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "Cyan"
        self.theme_cls.material_style = "M3"
        self.title = "Students"
        return Controller()


def run():
    App().run()


if __name__ == "__main__":
    run()