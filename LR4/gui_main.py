from kivymd.app import MDApp
from src.services.controller import *
from src.simulation import *
from kivy.core.window import Window

SIZE = {"width": 1050, "height": 700}
Window.size = (SIZE.get("width"), SIZE.get("height"))

class MyApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Blue"
        s = Simulation()
        controller = Controller(s)
        return controller.get_root_view()


def main():
    app = MyApp()
    app.run()


if __name__ == "__main__":
    main()
