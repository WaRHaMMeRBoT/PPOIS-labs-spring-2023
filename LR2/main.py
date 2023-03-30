from kivymd.app import MDApp
from services.controller import *
from kivy.core.window import Window

SIZE = {"width": 1050, "height": 700}
Window.size = (SIZE.get("width"), SIZE.get("height"))

class MyApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Blue"
        data = FileUtils.read_from_json("patient.json")
        patients = Patients(State.get_patients(data))
        controller = Controller(patients)
        return controller.get_root_view()


def main():
    app = MyApp()
    app.run()


if __name__ == "__main__":
    main()
