import os

from kivy.core.window import Window
from kivymd.app import MDApp

from lr4.Controllers.viewController import ViewController


class App(MDApp):

    def build(self):
        Window.size = (800, 500)
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "Cyan"
        self.theme_cls.material_style = "M3"
        self.title = "Garden"
        self.icon = os.path.realpath(os.path.dirname(__file__)) + "/view/assets/garden.png"
        sm = ViewController()
        return sm


def app():
    App().run()


if __name__ == '__main__':
    app()
