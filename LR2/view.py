from kivy.metrics import dp
from kivy.uix.screenmanager import Screen

from components.buttons import edit_menu_button_layout, main_menu_buttons
from components.table import Table


class RemoveScreen(Screen):
    def __init__(self, controller, **kwargs):
        super(RemoveScreen, self).__init__(**kwargs)
        self.controller = controller

        self.students = self.controller.get_student_names()

        self.data_table = Table([
            ("номер", dp(20)),
            ("ФИо студента.", dp(40)),
            ("ФИО отца", dp(40)),
            ("заработок отца", dp(40)),
            ("ФИО матери", dp(40)),
            ("заработок матери", dp(40)),
            ("Число братьев", dp(40)),
            ("Число сестер", dp(40)),
        ], self.students, check=True)

        self.buttons = edit_menu_button_layout(self.controller)
        self.buttons.pos_hint = {'center_x': 0.53, 'center_y': 0.5}

        self.add_widget(self.data_table)
        self.add_widget(self.buttons)


class MenuScreen(Screen):
    def __init__(self, controller, **kwargs):
        super(MenuScreen, self).__init__(**kwargs)
        self.controller = controller
        self.students = self.controller.get_student_names()

        self.data_table = Table(column_data=[
            ("номер", dp(20)),
            ("ФИО студента", dp(40)),
            ("ФИО отца", dp(40)),
            ("заработок отца", dp(40)),
            ("ФИО матери", dp(40)),
            ("заработок матери", dp(40)),
            ("Число братьев", dp(40)),
            ("Число сестер", dp(40)),
        ], row_data=self.students, check=False)

        self.buttons = main_menu_buttons(self.controller)
        self.buttons.pos_hint = {'center_x': 0.53, 'center_y': 0.5}

        self.add_widget(self.data_table)
        self.add_widget(self.buttons)


class View:
    def __init__(self, controller):
        self.controller = controller
        self.controller.add_widget(MenuScreen(name='menu', controller=self.controller))
        self.controller.add_widget(RemoveScreen(name='remove', controller=self.controller))