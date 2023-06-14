from kivy import Config
from kivy.core.window import Window
from kivymd.app import MDApp

from controllers.controller import Controller

Config.set('graphics', 'resizable', False)
Config.write()


class App(MDApp):

    def build(self):
        Window.size = (1100, 650)
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "Gray"
        self.theme_cls.material_style = "M3"
        self.title = "Laba 2"
        self.icon = "/Users/ardonplay/Developer/Python/PPOIS-labs-spring-2023/LR2/lr2/assets/capybara.png"
        sm = Controller()
        return sm


def run():
    App().run()


if __name__ == "__main__":
    run()