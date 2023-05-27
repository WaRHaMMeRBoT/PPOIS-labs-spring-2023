from kivy.config import Config
Config.set('graphics', 'width', 1300)
Config.set('graphics', 'height', 700)

from kivymd.app import MDApp
from kivymd.theming import ThemeManager
from controller import Controller

class App(MDApp):
    theme_cls = ThemeManager()
    title = 'Часы пропусков'
    
    def build(self):
        self.theme_cls.theme_style_switch_animation = True
        self.theme_cls.theme_style_switch_animation_duration = 0.1
        controller = Controller(self)
        return controller.get_root_view()
    