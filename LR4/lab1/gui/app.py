from kivy.config import Config
Config.set("graphics", "width", 1250)
Config.set("graphics", "height", 1000)

from kivymd.app import MDApp
from kivymd.theming import ThemeManager
import sys
import os

sys.path.insert(1, os.path.join(sys.path[0], '..'))

from gui.controller import Controller
import manage

class App(MDApp):
    theme_cls = ThemeManager()
    title = 'Сад'
    
    def build(self):
        self.theme_cls.theme_style_switch_animation = True
        self.theme_cls.theme_style_switch_animation_duration = 0.1
        garden_manage: manage.ManageGarden = manage.ManageGarden()
        controller = Controller(self, garden_manage)
        return controller.get_root_view()