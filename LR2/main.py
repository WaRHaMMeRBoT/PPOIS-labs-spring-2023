from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.app import MDApp
import data as d
import sax
from kivymd.uix.datatables import MDDataTable
from kivy.metrics import dp

file = 'd.xml'


class MainWidget(FloatLayout):
    def on_press_button_add(self):
        product = self.product.text
        producer = self.producer.text
        unp = self.unp.text
        number = self.number.text
        address = self.address.text
        if unp.isdigit() and number.isdigit():
            d.add(file, 'item',
                  {"producer": producer, 'product': product, 'unp': unp, 'number': number, 'address': address})


class DataScreen(Screen):
    pass


class MenuScreen(Screen):
    pass


search_list = []


class SearchScreen(Screen):
    def on_press_button_search(self):
        global search_list
        answer = []
        product = self.product.text
        producer = self.producer.text
        unp = self.unp.text
        number = self.number.text
        address = self.address.text

        key = ["producer", "product", "unp", "number", "address"]
        el = [producer, product, unp, number, address]

        for i in range(5):
            value = d.find(file, el[i], key[i])
            if not value == None:
                answer = answer + value

        search_list = answer


class MyButton(Button):
    pass


del_list = []


class DeleteScreen(Screen):
    def on_press_button_delete(self):
        global del_list
        answer = []
        producer = self.producer.text
        product = self.product.text
        unp = self.unp.text
        number = self.number.text
        address = self.address.text

        key = ["producer", "product", "unp", "number", "address"]
        el = [producer, product, unp, number, address]

        for i in range(5):
            value = d.delete(file, el[i], key[i])
            if not value == None:
                answer = answer + value

        del_list = answer


class MyLabel(Label):
    pass


class MyTextInput(TextInput):
    pass


class WindowManager(ScreenManager):
    pass


class MainApp(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.data_tables = None

    def build(self):
        super(MainApp, self).__init__()
        self.title = "MyApp"
        self.load_kv("conf.kv")
        m = WindowManager()
        return m

    def change_screen(self, screen: str):
        self.root.current = screen

    def load_table(self):
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "Purple"
        self.theme_cls.primary_hue = "500"
        self.data_tables = MDDataTable(
            use_pagination=True,
            check=True,
            rows_num=5,
            elevation=7,
            column_data=[
                ("[color=#9932CC]No.[/color]", dp(20), None, "Custom tooltip"),
                ("[color=#CD00CD]Producer[/color]", dp(25)),
                ("[color=#9932CC]Product[/color]", dp(25)),
                ("[color=#CD00CD]UNP[/color]", dp(25)),
                ("[color=#9932CC]Number[/color]", dp(25)),
                ("[color=#CD00CD]Address[/color]", dp(25))],
            row_data=sax.work_parser(), )
        self.root.ids.data_scr.ids.data_layout.add_widget(self.data_tables)

    def load_table_search(self):
        global search_list

        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "Purple"
        self.theme_cls.primary_hue = "500"

        self.data_tables = MDDataTable(
            use_pagination=True,
            check=True,
            rows_num=5,
            elevation=7,
            column_data=[
                ("[color=#CD00CD]Producer[/color]", dp(25)),
                ("[color=#9932CC]Product[/color]", dp(25)),
                ("[color=#CD00CD]UNP[/color]", dp(25)),
                ("[color=#9932CC]Number[/color]", dp(25)),
                ("[color=#CD00CD]Address[/color]", dp(25))],
            row_data=search_list, )
        self.root.ids.search_scr.ids.data_search.add_widget(self.data_tables)

    def load_table_delete(self):
        global del_list

        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "Purple"
        self.theme_cls.primary_hue = "500"

        self.data_tables = MDDataTable(
            use_pagination=True,
            check=True,
            rows_num=5,
            elevation=7,
            column_data=[
                ("[color=#CD00CD]Producer[/color]", dp(25)),
                ("[color=#9932CC]Product[/color]", dp(25)),
                ("[color=#CD00CD]UNP[/color]", dp(25)),
                ("[color=#9932CC]Number[/color]", dp(25)),
                ("[color=#CD00CD]Address[/color]", dp(25))],
            row_data=del_list, )
        self.root.ids.delete_scr.ids.data_delete.add_widget(self.data_tables)


if __name__ == '__main__':
    MainApp().run()
