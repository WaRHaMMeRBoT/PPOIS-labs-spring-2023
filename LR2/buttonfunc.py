import controller
from kivy.config import Config
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


def get_rows(self):
        data_temp = self.table.row_data
        data = {}
        data["items"] = []
        for item in data_temp:
            data["items"].append({
                "number": 0 if item[0] == "" else int(item[0]),
                "departure_station": item[1],
                "arrival_station": item[2],
                "date_and_time_of_departure":item[3],
                "date_and_time_of_arrival": item[4],
                "time_in_travel":item[5]
            })
        return data
    
def clear_data_base(self):
        while len(self.table.row_data) > 0:
            self.table.remove_row(self.table.row_data[-1])

def read_file_realise(self):
        clear_data_base(self) 
        file_name = get_for_writing_reading_file_dialog_data(self)
        if os.path.isfile(file_name["File Name"].text):
            json_file = open(file_name["File Name"].text, "r")
            data_base = json.load(json_file)
            for item in data_base["items"]:
                self.table.add_row((item["number"], item["departure_station"],
                                          item["arrival_station"], item["date_and_time_of_departure"],
                                          item["date_and_time_of_arrival"],item["time_in_travel"]))
            json_file.close()
            self.dialog_for_writing_reading_file.dismiss()
        else:
            error_file_dialog(self)


def error_file_dialog(self):
        self.error_dialog = MDDialog(
            text="The File Does Not Exist!",
            buttons=[
                MDFlatButton(
                    text="Попробовать заново",
                    theme_text_color="Custom",
                    text_color=self.theme_cls.primary_color,
                    on_release=self.on_button_press,
                ),
            ],
        )
        self.error_dialog.open()

def write_file_realise(self):
        file_name = get_for_writing_reading_file_dialog_data(self)
        with open(file_name["File Name"].text, "w+") as outfile:
            json.dump(get_rows(self), outfile)
        self.dialog_for_writing_reading_file.dismiss()

    

def search_and_output_rows_realise(self):
        data = get_rows(self)
        filled_fields = get_filtering_dialog_data(self)
        section_for_search = field_for_search = None
        counter = 0
        self.new_data = []
        for field in filled_fields:
            if filled_fields[field].text:
                section_for_search = field
                if section_for_search == "number":
                    field_for_search = int(filled_fields[field].text)
                else:
                    field_for_search = filled_fields[field].text
                break
        for item in data["items"]:
            for section in item:
                if section == section_for_search:
                    if item[section] == field_for_search:
                        self.new_data.append(item)
                        counter += 1
                    else:
                        continue
        self.new_data = [list(i.values()) for i in self.new_data]
        self.counter = counter
        self.close_string_filtering_dialog()
        info_about_searched_rows(self)


def returned_table(self,new_data):
        return MDAnchorLayout(
            MDDataTable(
                size_hint=(1, 1),
                use_pagination=True,
                rows_num=5,
                width="700dp",
                height="500dp",
                column_data=[
                    ("Номер поезда", dp(90)),
                    ("Станция отправления", dp(45)),
                    ("Станция прибытия", dp(60)),
                    ("Дата и время отправления", dp(60)),
                    ("Дата и время прибытия", dp(60)),
                    ("Время в пути",dp(60)),
                ],
                row_data = new_data
            )
        )
    
def info_about_searched_rows(self):
        self.info1 = MDDialog(
            title="Result: " + str(self.counter) + " rows found",
            type="custom",
            size_hint_x=None,
            size_hint_y=None,
            height="700dp",
            width="500dp",
            content_cls=MDBoxLayout(
                returned_table(self, self.new_data),
                orientation="vertical",
                spacing="15dp",
                size_hint_y=None,
                height="500dp",
                width="1000dp"
            ),
        )
        self.info1.open()

    

def search_and_delete_rows_realise(self):
        data = get_rows(self)
        filled_fields = get_filtering_dialog_data(self)
        section_for_search = field_for_search = None
        counter = 0
        new_data = {}
        new_data["items"] = []
        for field in filled_fields:
            if filled_fields[field].text:
                section_for_search = field
                if section_for_search == "number":
                    field_for_search = int(filled_fields[field].text)
                else:
                    field_for_search = filled_fields[field].text
                break
        for item in data["items"]:
            for section in item:
                if section == section_for_search:
                    if item[section] == field_for_search:
                        counter += 1
                        continue
                    else:
                        new_data["items"].append(item)
        clear_data_base(self)
        for item in new_data["items"]:
            self.table.add_row((item["number"], item["departure_station"],
                                      item["arrival_station"], item["date_and_time_of_departure"], item["date_and_time_of_arrival"],item["time_in_travel"]))
        self.close_string_filtering_dialog()
        info_about_deleted_rows(self,counter)

def info_about_deleted_rows(self, counter):
        self.info = MDDialog(
            text="Count Of Deleted Rows: " + str(counter),
            buttons=[
                MDFlatButton(
                    text="Закрыть",
                    theme_text_color="Custom",
                    text_color=self.theme_cls.primary_color,
                    on_release=self.on_button_press,
                ),
            ],
        )
        self.info.open()


def close_error_dialog_realise(self):
        self.error_dialog.dismiss()

def close_info_dialog_realise(self):
        self.info.dismiss()

def close_string_adding_dialog_realise(self):
        self.dialog_for_adding.dismiss()

def close_string_removing_dialog_realise(self):
        self.dialog_for_removing.dismiss()

def close_string_filtering_dialog_realise(self):
        self.dialog_for_filtering.dismiss()
    
def close_reading_writing_file_dialog_realise(self):
        self.dialog_for_writing_reading_file.dismiss()

    
def add_row_realise(self):
        item = get_adding_dialog_data(self)
        self.table.add_row((item["number"].text, item["departure_station"].text,
                                  item["arrival_station"].text, item["date_and_time_of_departure"].text,
                                  item["date_and_time_of_arrival"].text,item["time_in_travel"].text))
        self.dialog_for_adding.dismiss()

def get_adding_dialog_data(self):
        return self.dialog_for_adding.content_cls.ids
    
def get_filtering_dialog_data(self):
        return self.dialog_for_filtering.content_cls.ids

def get_for_writing_reading_file_dialog_data(self):
        return self.dialog_for_writing_reading_file.content_cls.ids
    
def remove_row_realise(self):
        if len(self.table.row_data) > 0:
            self.table.remove_row(self.table.row_data[-1])

    
