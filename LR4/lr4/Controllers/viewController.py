from kivymd.uix.dialog import MDDialog
from kivymd.uix.screenmanager import MDScreenManager
from kivymd.uix.transition import MDSlideTransition

from lr4.Controllers.baseController import BaseController
from lr4.view.components.buttons import plants_buttons
from lr4.view.components.dialogs import add_seed_dialog, get_info_about_plant, warp_dialog, weather_dialog
from lr4.view.components.text import weather_info
from lr4.view.view import View


class ViewController(MDScreenManager):
    def __init__(self, **kwargs):
        super(ViewController, self).__init__(**kwargs)
        self.index_and_row: tuple = (0, 0)
        self.transition = MDSlideTransition()
        self.dialog: MDDialog = NotImplemented
        self.baseController = BaseController()
        self.view = View(self)

    def get_index_and_row_by_index(self, index: int) -> tuple:
        row: int = index % len(self.baseController.get_plants()[0])

        index = index // len(self.baseController.get_plants()[0])
        index_and_row: tuple = (index, row)

        return index_and_row

    def weather_dialog(self, obj):
        self.dialog = weather_dialog(self)
        self.dialog.open()

    def change_weather(self, obj):
        checked_items = []
        for item in self.dialog.items:
            if item.checkbox.active:
                checked_items.append(item.text)

        self.baseController.weather(type=checked_items[0], time=100)

        print(self.baseController.garden.model.weather.weather)
        self.update_screen()
        self.dialog.dismiss()

    def remove_plant(self, obj):
        self.baseController.remove(x=self.index_and_row[0], y=self.index_and_row[1])
        self.update_screen()
        self.dialog.dismiss()

    def update_screen(self):
        self.current_screen.remove_widget(self.current_screen.plants_buttons)
        self.current_screen.remove_widget(self.current_screen.weather)
        self.current_screen.weather = weather_info(self)
        self.current_screen.plants_buttons = plants_buttons(self)
        self.current_screen.add_widget(self.current_screen.weather)
        self.current_screen.add_widget(self.current_screen.plants_buttons)

    def warp_dialog(self, obj):
        self.dialog = warp_dialog(self)
        self.dialog.open()

    def warp(self, obj):
        self.baseController.warp(int(self.dialog.content_cls.value))
        self.update_screen()
        self.dialog.dismiss()

    def add_seed(self, obj):
        self.baseController.add_seed(self.dialog.content_cls.ids.name.text, self.index_and_row[0],
                                     self.index_and_row[1])
        self.update_screen()
        self.dialog.dismiss()

    def get_info_of_plant(self, obj):
        self.index_and_row = self.get_index_and_row_by_index(int(obj.id))
        if self.baseController.get_plants()[self.index_and_row[0]][self.index_and_row[1]] is None:
            self.dialog = add_seed_dialog(self)
        else:
            self.dialog = get_info_about_plant(self)
        self.dialog.open()

    def close_dialog(self, obj):
        self.dialog.dismiss()
