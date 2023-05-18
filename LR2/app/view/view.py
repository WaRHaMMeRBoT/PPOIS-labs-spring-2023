import sys
import os

from kivymd.uix.boxlayout import MDBoxLayout

sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from app.view.components.bar import bar
from app.view.components.table import table

from app.view.components.dialog.add import adding_dialog
from app.view.components.dialog.filter import filter_dialog
from app.view.components.dialog.file_chooser import choose_file_dialog


class View(MDBoxLayout):
    def __init__(self, controller, **kw):
        super().__init__(**kw)
        self.controller = controller

        props = {
            "controller": self.controller
        }

        self.dialog = None

        self.bar = bar(props)
        self.table = table(props)
        self.root = MDBoxLayout(
            self.bar,
            self.table,
            id='root_box',
            orientation='vertical',
        )

    def update(self):

        self.root.remove_widget(self.table)
        self.table = table({
            "controller": self.controller
        })
        self.root.add_widget(self.table)

        print('ALL WIDGETS UPDATED')

    def close_dialog(self):
        self.dialog.dismiss(force=True)

    def open_choose_file_dialog(self):
        self.dialog = choose_file_dialog({
            "controller": self.controller
        })
        self.dialog.show(os.path.expanduser("~/git/labs4sem/PPOIS/lab2/app/data"))

    def close_choose_file_dialog(self):
        self.dialog.close()

    def open_adding_dialog(self):
        self.dialog = adding_dialog({
            "controller": self.controller
        })
        self.dialog.open()

    def open_filter_dialog(self):
        self.dialog = filter_dialog({
            "controller": self.controller
        })
        self.dialog.open()
        