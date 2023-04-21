from kivymd.app import MDApp
from services.view_controller import *


class MyApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Orange"
        controller = Controller()
        return controller.get_root_view()


def main():
    app = MyApp()
    app.run()


if __name__ == "__main__":
    main()
