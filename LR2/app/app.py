import os
import sys

from kivymd.app import MDApp

sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from app.services.controller import Controller


class App(MDApp):
    model = None
    controller = None

    def build(self):
        self.title = 'PPOIS lab2'
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "DeepOrange"

        self.controller = Controller()
        return self.controller.get_view()
