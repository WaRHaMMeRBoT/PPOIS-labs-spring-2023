from kivy.metrics import dp
from kivy.uix.screenmanager import Screen

from components.buttons import edit_menu_button_layout, main_menu_buttons, marks_button_layout
from components.table import Table


class RemoveScreen(Screen):
    def __init__(self, controller, **kwargs):
        super(RemoveScreen, self).__init__(**kwargs)
        self.controller = controller

        self.books = self.controller.get_book_names()

        self.data_table = Table([
            ("Name", dp(50)),
            ("Author", dp(50)),
            ("Publishing house", dp(50)),
            ("Number of volumes", dp(50)),
            ("Circulation", dp(50)),
            ("Total volumes", dp(50)),
        ], self.books, check=True)

        self.buttons = edit_menu_button_layout(self.controller)
        self.buttons.pos_hint = {'center_x': 0.53, 'center_y': 0.5}

        self.add_widget(self.data_table)
        self.add_widget(self.buttons)


class MenuScreen(Screen):
    def __init__(self, controller, **kwargs):
        super(MenuScreen, self).__init__(**kwargs)
        self.controller = controller
        self.books = self.controller.get_book_names()

        self.data_table = Table(column_data=[
            ("Name", dp(40)),
            ("Author", dp(40)),
            ("Publishing house", dp(40)),
            ("Number of volumes", dp(30)),
            ("Circulation", dp(30)),
            ("Total volumes", dp(30)),
        ], row_data=self.books, check=False)

        self.buttons = main_menu_buttons(self.controller)
        self.buttons.pos_hint = {'center_x': 0.53, 'center_y': 0.5}

        self.add_widget(self.data_table)
        self.add_widget(self.buttons)


class View:
    def __init__(self, controller):
        self.controller = controller
        self.controller.add_widget(MenuScreen(name='menu', controller=self.controller))
        self.controller.add_widget(RemoveScreen(name='remove', controller=self.controller))