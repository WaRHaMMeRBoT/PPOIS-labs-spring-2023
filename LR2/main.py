from kivymd.app import MDApp
from services.controller import *


class MyApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Orange"
        data = FileUtils.read_from_json("student.json")
        students = Students(State.get_students(data))
        controller = Controller(students)
        return controller.get_root_view()


def main():
    app = MyApp()
    app.run()


if __name__ == "__main__":
    main()
