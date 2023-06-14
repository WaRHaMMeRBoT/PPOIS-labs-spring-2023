from kivy import Config
from kivymd.app import MDApp
from kivy.core.window import Window
from controller import Controller

Config.set('graphics', 'resizable', False)
Config.write()


class MainApp(MDApp):
    def build(self):
        Window.size = (970, 600)
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "BlueGray"
        self.theme_cls.material_style = "M3"
        return Controller()


if __name__ == "__main__":
    MainApp().run()
