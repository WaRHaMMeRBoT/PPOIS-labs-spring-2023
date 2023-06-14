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
        students_name = self.students_name.text
        fathers_name = self.fathers_name.text
        fathers_salary = self.fathers_salary.text
        mothers_name = self.mothers_name.text
        mothers_salary = self.mothers_salary.text
        brothers = self.brothers.text
        sisters = self.sisters.text
        if brothers.isdigit() and sisters.isdigit():
            d.add(file, 'item',
                  {'students_name': students_name, "fathers_name": fathers_name, 'fathers_salary': fathers_salary,
                   'mothers_name': mothers_name,  'mothers_salary': mothers_salary, 'brothers': brothers, "sisters": sisters})


class DataScreen(Screen):
    pass


class MenuScreen(Screen):
    pass


search_list = []


class SearchScreen(Screen):
    def on_press_button_search(self):
        global search_list
        answer = []
        students_name = self.students_name.text
        fathers_name = self.fathers_name.text
        mothers_name = self.mothers_name.text
        fathers_salary = self.fathers_salary.text
        mothers_salary = self.mothers_salary.text
        brothers = self.brothers.text
        sisters = self.sisters.text

        key = ["students_name", "fathers_name", "fathers_salary",  "mothers_name", "mothers_salary", "brothers", "sisters"]
        el = [students_name, fathers_name, fathers_salary, mothers_name, mothers_salary, brothers, sisters]

        for i in range(7):
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
        students_name = self.students_name.text
        fathers_name = self.fathers_name.text
        fathers_salary = self.fathers_salary.text
        mothers_name = self.mothers_name.text
        mothers_salary = self.mothers_salary.text
        brothers = self.brothers.text
        sisters = self.sisters.text

        key = ["students_name", "fathers_name", "fathers_salary", "mothers_name", "mothers_salary", "brothers", "sisters"]
        el = [students_name, fathers_name, fathers_salary, mothers_name, mothers_salary, brothers, sisters]

        for i in range(7):
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
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Red"
        self.theme_cls.primary_hue = "200"
        self.data_tables = MDDataTable(
            use_pagination=True,
            check=True,
            rows_num=7,
            elevation=7,
            column_data=[
                ("[color=#9932CC]No.[/color]", dp(20), None, "Custom tooltip"),
                ("[color=#9932CC]Имя студента[/color]", dp(25)),
                ("[color=#FAC0C0]Имя отца[/color]", dp(25)),
                ("[color=#CD00CD]Зарплата отца[/color]", dp(25)),
                ("[color=#9932CC]Имя матери[/color]", dp(25)),
                ("[color=#CD00CD]Зарплата матери[/color]", dp(25)),
                ("[color=#CD00CD]Братья[/color]", dp(25)),
                ("[color=#CD00CD]Сёстры[/color]", dp(25))],
            row_data=sax.work_parser(), )
        self.root.ids.data_scr.ids.data_layout.add_widget(self.data_tables)

    def load_table_search(self):
        global search_list

        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "Red"
        self.theme_cls.primary_hue = "500"

        self.data_tables = MDDataTable(
            use_pagination=True,
            check=True,
            rows_num=3,
            elevation=1,
            column_data=[
                ("[color=#0932FC]Имя студента[/color]", dp(25)),
                ("[color=#0AA0C0]Имя отца[/color]", dp(25)),
                ("[color=#0B00CD]Зарплата отца[/color]", dp(25)),
                ("[color=#0932FC]Имя матери[/color]", dp(25)),
                ("[color=#0B00CD]Зарплата матери[/color]", dp(25)),
                ("[color=#0B00CD]Братья[/color]", dp(25)),
                ("[color=#0B00CD]Сёстры[/color]", dp(25))],
            row_data=search_list, )
        self.root.ids.search_scr.ids.data_search.add_widget(self.data_tables)

    def load_table_delete(self):
        global del_list

        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "Red"
        self.theme_cls.primary_hue = "500"

        self.data_tables = MDDataTable(
            use_pagination=True,
            check=True,
            rows_num=3,
            elevation=1,
            column_data=[
                ("[color=#9932CC]Имя студента[/color]", dp(25)),
                ("[color=#FAC0C0]Имя отца[/color]", dp(25)),
                ("[color=#CD00CD]Зарплата отца[/color]", dp(25)),
                ("[color=#9932CC]Имя матери[/color]", dp(25)),
                ("[color=#CD00CD]Зарплата матери[/color]", dp(25)),
                ("[color=#CD00CD]Братья[/color]", dp(25)),
                ("[color=#CD00CD]Сёстры[/color]", dp(25))],
            row_data=del_list, )
        self.root.ids.delete_scr.ids.data_delete.add_widget(self.data_tables)


if __name__ == '__main__':
    MainApp().run()
