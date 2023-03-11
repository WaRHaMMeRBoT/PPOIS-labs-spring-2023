from kivy.config import Config
Config.set("graphics", "width", 1200)
Config.set("graphics", "height", 800)

from kivymd.app import MDApp
from kivymd.theming import ThemeManager

from app.manage_services.controller import Controller

class App(MDApp):
    theme_cls = ThemeManager()
    title = 'Таблица'
    
    def build(self):
        self.theme_cls.theme_style_switch_animation = True
        self.theme_cls.theme_style_switch_animation_duration = 0.1
        controller = Controller(self)
        return controller.get_root_view()
    
    def switch_theme_style(self, *args):
        self.theme_cls.theme_style = (
            "Dark" if self.theme_cls.theme_style == "Light" else "Light"
        )