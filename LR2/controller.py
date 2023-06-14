from kivy.config import Config
Config.set("graphics", "width", 800)
Config.set("graphics", "height", 600)
from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.screen import Screen
from kivymd.uix.datatables import MDDataTable
from kivy.metrics import dp
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton
from kivymd.uix.textfield import MDTextField
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDFlatButton, MDRaisedButton
from kivymd.uix.anchorlayout import MDAnchorLayout

import json 
import os.path
from buttonfunc import *


KV = '''
Screen:

    MDNavigationLayout:

        ScreenManager:

            Screen:

                MDBoxLayout:
                    orientation: 'horizontal'

                    MDTopAppBar:
                        title: "Таблица поездов"
                        elevation: 4
                        pos_hint: {"top": 1}
                        md_bg_color: "#ADD8E6"
                        specific_text_color: "#000000"
                        left_action_items:
                            [['menu', lambda x: nav_drawer.set_state("open")]]


        MDNavigationDrawer:
            id: nav_drawer
            radius: (0, 16, 16, 0)
 
            ContentNavigationDrawer:
                ScrollView:
                    MDList:
                        OneLineListItem:
                            text:"Добавление строки"
                            on_release:app.show_string_adding_dialog()
                            

                        OneLineListItem:
                            text:"Удаление строки"
                            on_release:app.show_string_removing_dialog()
            
                        OneLineListItem:
                            text:"Поиск строки"
                            on_release:app.show_string_filtering_dialog()

                        OneLineListItem:
                            text:"Считывание/Сохранение из/в файл(а)"
                            on_release:app.show_reading_writing_file_dialog()
'''

class ContentNavigationDrawer(BoxLayout):
    pass




class app(MDApp):
    dialog_for_adding = None
    dialog_for_filtering = None
    dialog_for_removing = None
    dialog_for_writing_reading_file = None
    info,info1,error_dialog = None,None,None

    def on_button_press(self, instance_button: MDRaisedButton):
        try:
            {
                #"Чтение": self.read_file,
                "Чтение": self.read_file,
                "Запись": self.write_file,
                "Отмена": self.close_string_adding_dialog,
                "Отмена.": self.close_string_removing_dialog,
                ".Отмена": self.close_string_filtering_dialog,
                ".Отмена.": self.close_reading_writing_file_dialog,
                "Добавить": self.add_row,
                "Попробовать заново": self.close_error_dialog,
                "Поиск": self.search_and_output_rows,
                "Удалить.": self.remove_row,
                "Удалить": self.search_and_delete_rows,
                "Закрыть": self.close_info_dialog,
            }[instance_button.text]()
        except KeyError:
            pass

    def read_file(self):
        return read_file_realise(self)

    def write_file(self):
        return write_file_realise(self)

    def close_string_adding_dialog(self):
        return close_string_adding_dialog_realise(self)

    def close_string_removing_dialog(self):
        return close_string_removing_dialog_realise(self)

    def close_string_filtering_dialog(self):
        return close_string_filtering_dialog_realise(self)
    
    def close_reading_writing_file_dialog(self):
        return close_reading_writing_file_dialog_realise(self)

    def add_row(self):
        return add_row_realise(self)

    def close_error_dialog(self):
        return close_error_dialog_realise(self)

    def search_and_output_rows(self):
        return search_and_output_rows_realise(self)

    def remove_row(self):
        return remove_row_realise(self)

    def search_and_delete_rows(self):
        return search_and_delete_rows_realise(self)

    def close_info_dialog(self):
        return close_info_dialog_realise(self)

    def build(self):
        screen = Screen()
        
        self.theme_cls.theme_style = "Light"
        self.table = MDDataTable(
                size_hint=(1, 0.9),
                use_pagination=True,
                check = True,
                rows_num = 10,
                pagination_menu_height = 300,
                column_data=[
                    ("Номер поезда", dp(90)),
                    ("Станция отправления", dp(45)),
                    ("Станция прибытия", dp(60)),
                    ("Дата и время отправления", dp(60)),
                    ("Дата и время прибытия",dp(60)),
                    ("Время в пути", dp(60)),
                ],
                
            
            )
        screen.add_widget(self.table)
        screen.add_widget(Builder.load_string(KV))


        return screen

    def show_string_adding_dialog(self):

        if not self.dialog_for_adding:
            self.dialog_for_adding = MDDialog(
                 title = 'Новая запись',
        type = 'custom',
        content_cls = MDBoxLayout(
            MDTextField(
                id = 'number',
                hint_text="Номер поезда",
                font_size='20',
                max_text_length = 10,
            ),
            MDTextField(
                id = 'departure_station',
                hint_text="Станция отправления",
                font_size='20',
                max_text_length = 50,
            ),
            MDTextField(
                id = 'arrival_station',
                hint_text="Станция прибытия",
                font_size='20',
                max_text_length = 50,
            ),
            MDTextField(
                id = 'date_and_time_of_departure',
                hint_text="Дата и время отправления",
                font_size='20',
                max_text_length = 50,
            ),
            MDTextField(
                id = 'date_and_time_of_arrival',
                hint_text="Дата и время прибытия",
                font_size='20',
                max_text_length = 50,
            ),
            MDTextField(
                id = 'time_in_travel',
                hint_text="Время в пути",
                font_size='20',
                max_text_length = 50,
                helper_text= "Поле должно содержать минимум одну строку",
                helper_text_mode= "on_error"
            ),
            orientation="vertical",
            spacing="15dp",
            size_hint_y=None,
            height="470dp"
        ),
        buttons=[
            MDFlatButton(
                text="Отмена",
                font_style = 'Button',
                font_size='17',
                on_release = self.on_button_press,
            ),
            MDRaisedButton(
                text="Добавить",
                font_size='17',
                md_bg_color = 'gray',
                font_style = 'Button',
                on_release = self.on_button_press,
            ),
        ],
            )
        self.dialog_for_adding.open()

    def show_string_removing_dialog(self):
        if not self.dialog_for_removing:
            self.dialog_for_removing = MDDialog(
                title = f'Удалить последнюю запись?',
                buttons=[
                MDFlatButton(
                    text="Отмена.",
                    font_style = 'Button',
                    font_size='17',
                    on_release = self.on_button_press
                ),
                MDRaisedButton(
                    text="Удалить.",
                    font_size='17',
                    md_bg_color = 'gray',
                    font_style = 'Button',
                    on_release = self.on_button_press,
                ),
            ],
        )
        self.dialog_for_removing.open()

    def show_string_filtering_dialog(self):
        self.dialog_for_filtering = MDDialog(
            title="Заполните одно из полей:",
            type="custom",
            content_cls=MDBoxLayout(
                MDTextField(
                id = 'number',
                hint_text="Номер поезда",
                font_size='20',
                max_text_length = 10,
                helper_text= "Поле должно содержать минимум одну цифру",
                helper_text_mode= "on_error"
            ),
            MDTextField(
                id = 'departure_station',
                hint_text="Станция отправления",
                font_size='20',
                max_text_length = 50,
                helper_text= "Поле должно содержать хотя бы одну строку",
                helper_text_mode= "on_error"
            ),
            MDTextField(
                id = 'arrival_station',
                hint_text="Станция прибытия",
                font_size='20',
                max_text_length = 50,
                helper_text= "Поле должно содержать хотя бы одну строку",
                helper_text_mode= "on_error"
            ),
            MDTextField(
                id = 'date_and_time_of_departure',
                hint_text="Дата и время отправления",
                font_size='20',
                max_text_length = 50,
                helper_text= "Поле должно содержать минимум одну дату",
                helper_text_mode= "on_error"
            ),
            MDTextField(
                id = 'date_and_time_of_arrival',
                hint_text="Дата и время прибытия",
                font_size='20',
                max_text_length = 50,
                helper_text= "Поле должно содержать минимум одну дату",
                helper_text_mode= "on_error"
            ),
            MDTextField(
                id = 'time_in_travel',
                hint_text="Время в пути",
                font_size='20',
                max_text_length = 50,
                helper_text= "Поле должно содержать минимум одну строку",
                helper_text_mode= "on_error"
            ),
            orientation="vertical",
            spacing="15dp",
            size_hint_y=None,
            height="470dp"
        ),
            buttons=[
                MDFlatButton(
                    text=".Отмена",
                    theme_text_color="Custom",
                    text_color=self.theme_cls.primary_color,
                    on_release=self.on_button_press,
                ),
                MDFlatButton(
                    text="Поиск",
                    theme_text_color="Custom",
                    text_color=self.theme_cls.primary_color,
                    on_release=self.on_button_press,
                ),
                MDFlatButton(
                    text="Удалить",
                    theme_text_color="Custom",
                    text_color=self.theme_cls.primary_color,
                    on_release=self.on_button_press,
                ),
            ],
        )
        self.dialog_for_filtering.open()

    def show_reading_writing_file_dialog(self):
        self.dialog_for_writing_reading_file = MDDialog(
            title="Enter File Name:",
            type="custom",
            content_cls=MDBoxLayout(
                MDTextField(
                    id="File Name",
                    hint_text="File Name",
                ),
                orientation="vertical",
                spacing="8dp",
                size_hint_y=None,
                height="60dp",
            ),
            buttons=[
                MDFlatButton(
                    text=".Отмена.",
                    theme_text_color="Custom",
                    text_color=self.theme_cls.primary_color,
                    on_release=self.on_button_press,
                ),
                MDFlatButton(
                    text="Чтение",
                    theme_text_color="Custom",
                    text_color=self.theme_cls.primary_color,
                    on_release=self.on_button_press,
                ),
                MDFlatButton(
                    text="Запись",
                    theme_text_color="Custom",
                    text_color=self.theme_cls.primary_color,
                    on_release=self.on_button_press,
                )
            ],
        )
        self.dialog_for_writing_reading_file.open()


