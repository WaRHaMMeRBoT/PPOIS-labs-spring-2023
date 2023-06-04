from kivy.metrics import dp
from kivy.uix.screenmanager import Screen

from components.buttons import edit_menu_button_layout, main_menu_buttons, marks_button_layout, filtered_menu_buttons
from components.table import Table


class RemoveScreen(Screen):
    def __init__(self, controller, **kwargs):
        super(RemoveScreen, self).__init__(**kwargs)
        self.controller = controller

        self.students = self.controller.get_student_names()

        self.data_table = Table([
            ("No.", dp(50)),
            ("Name", dp(50)),
            ("Group", dp(50)),
        ], self.students, check=True)

        self.buttons = edit_menu_button_layout(self.controller)
        self.buttons.pos_hint = {'center_x': 0.53, 'center_y': 0.5}

        self.add_widget(self.data_table)
        self.add_widget(self.buttons)


class FilterRemoveScreen(Screen):
    def __init__(self, controller, **kwargs):
        super(FilterRemoveScreen, self).__init__(**kwargs)
        self.controller = controller

        self.students = self.controller.get_filter_student_names()

        self.data_table = Table([
            ("No.", dp(50)),
            ("Name", dp(50)),
            ("Group", dp(50)),
        ], self.students, check=True)

        self.buttons = filtered_menu_buttons(self.controller)
        self.buttons.pos_hint = {'center_x': 0.53, 'center_y': 0.5}

        self.add_widget(self.data_table)
        self.add_widget(self.buttons)


class FilteredMenu(Screen):
    def __init__(self, controller, **kwargs):
        super(FilteredMenu, self).__init__(**kwargs)
        self.controller = controller
        self.students = self.controller.filter()

        self.data_table = Table(column_data=[
            ("No.", dp(50)),
            ("Name", dp(50)),
            ("Group", dp(50)),
        ], row_data=self.students, check=False)

        self.buttons = filtered_menu_buttons(self.controller)
        self.buttons.pos_hint = {'center_x': 0.53, 'center_y': 0.5}

        self.data_table.bind(on_row_press=self.controller.transition_to_marks)
    
        self.add_widget(self.data_table)
        self.add_widget(self.buttons)


class MenuScreen(Screen):
    def __init__(self, controller, **kwargs):
        super(MenuScreen, self).__init__(**kwargs)
        self.controller = controller
        self.students = self.controller.get_student_names()

        self.data_table = Table(column_data=[
            ("No.", dp(50)),
            ("Name", dp(50)),
            ("Group", dp(50)),
        ], row_data=self.students, check=False)

        self.buttons = main_menu_buttons(self.controller)
        self.buttons.pos_hint = {'center_x': 0.53, 'center_y': 0.5}

        self.data_table.bind(on_row_press=self.controller.transition_to_marks)

        self.add_widget(self.data_table)
        self.add_widget(self.buttons)


class Marks(Screen):
    def __init__(self, controller, **kwargs):
        super(Marks, self).__init__(**kwargs)
        self.controller = controller
        self.data_table = Table(column_data=[
            ("No.", dp(50)),
            ("Name", dp(50)),
            ("Mark", dp(50)),
        ],
            row_data=[("NULL", "NULL", "NULL")], check=True)
        self.data_table.bind(on_check_press=self.on_check_press)

        self.buttons = marks_button_layout(self.controller)
        self.buttons.pos_hint = {'center_x': 0.53, 'center_y': 0.5}

        self.add_widget(self.data_table)
        self.add_widget(self.buttons)

    def on_check_press(self, instance_table, instance_row):
        print(self.data_table.get_row_checks())


class View:
    def __init__(self, controller):
        self.controller = controller
        self.controller.add_widget(MenuScreen(name='menu', controller=self.controller))
        self.controller.add_widget(Marks(name='marks', controller=self.controller))
        self.controller.add_widget(RemoveScreen(name='remove', controller=self.controller))
        self.controller.add_widget(FilterRemoveScreen(name='filter_remove', controller=self.controller))
        self.controller.add_widget(FilteredMenu(name='filtered', controller=self.controller))
