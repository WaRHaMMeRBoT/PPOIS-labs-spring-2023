from kivy import Config
from kivy.core.window import Window
from kivymd.app import MDApp

from controller.controller import Controller

Config.set('graphics', 'resizable', False)
Config.write()


class App(MDApp):

    def build(self):
        Window.size = (800, 500)
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Brown"
        self.theme_cls.material_style = "M3"
        self.title = "Student table"
        # self.icon = ""
        sm = Controller()
        return sm


def run():
    App().run()


if __name__ == "__main__":
    run()