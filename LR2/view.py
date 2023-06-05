from kivymd.app import MDApp
from kivy.core.window import Window
from kivymd.uix.screen import Screen
from kivymd.uix.datatables import MDDataTable
from kivy.metrics import dp
from kivy.uix.screenmanager import Screen

from components.buttons import edit_menu_button_layout, main_menu_buttons, marks_button_layout


class View:
    def __init__(self, controller):
        self.controller = controller
        self.controller.add_widget(MainScreen(name='main', controller=self.controller))
        self.controller.add_widget(RemoveScreen(name='remove', controller=self.controller))


class MainScreen(Screen):
    def __init__(self, controller, **kwargs):
        super(MainScreen, self).__init__(**kwargs)
        self.controller = controller
        self.table = MDDataTable(
            column_data=[
                ("Book name", dp(40)),
                ("Author", dp(40)),
                ("Publishing house", dp(30)),
                ("Volumes", dp(20)),
                ("Circulation", dp(25)),
                ("Total volumes", dp(30))
            ],

            row_data=self.controller.model.table_rows,
            rows_num=7,
            size_hint=(1, 1),
            use_pagination=True,
            elevation=0

        )

        self.buttons = main_menu_buttons(self.controller)
        self.buttons.pos_hint = {'center_x': 0.52, 'center_y': 0.5}

        self.add_widget(self.table)
        self.add_widget(self.buttons)


class RemoveScreen(Screen):
    def __init__(self, controller, **kwargs):
        super(RemoveScreen, self).__init__(**kwargs)
        self.controller = controller
        self.table = MDDataTable(
            check=True,
            column_data=[

                ("Book name", dp(40)),
                ("Author", dp(40)),
                ("Publishing house", dp(30)),
                ("Volumes", dp(20)),
                ("Circulation", dp(25)),
                ("Total volumes", dp(30))
            ],

            row_data=self.controller.model.table_rows,
            rows_num=7,
            size_hint=(1, 1),
            use_pagination=True,
            elevation=0
        )

        self.buttons = edit_menu_button_layout(self.controller)
        self.buttons.pos_hint = {'center_x': 0.53, 'center_y': 0.5}

        self.add_widget(self.table)
        self.add_widget(self.buttons)
