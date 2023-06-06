from kivy.metrics import dp
from kivymd.app import MDApp
from kivymd.uix.datatables import MDDataTable
from kivy.uix.anchorlayout import AnchorLayout
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.anchorlayout import MDAnchorLayout
from kivymd.uix.button import MDFlatButton
from kivymd.uix.dialog import MDDialog
from kivymd.uix.textfield import MDTextField

import json as j
import os.path


class Patients(MDApp):
    dialog = dialog_error = data_tables = info = info_table = new_data = counter = None

    def on_button_press(self, instance_button: MDRaisedButton):
        try:
            {
                "+": self.form_to_add_new_row,
                "-": self.remove_row,
                "Read / Write": self.wr_form,
                "Read": self.read,
                "Write": self.write,
                "Cancel": self.close_dialog,
                "Add": self.add_row,
                "Try again": self.close_error_dialog,
                "Find / Delete": self.form_for_search_delete,
                "Find": self.search_and_output_rows,
                "Delete": self.search_and_delete_rows,
                "Close": self.close_info_dialog,
            }[instance_button.text]()
        except KeyError:
            pass

    def search_and_output_rows(self):
        data = self.get_rows()
        filled_fields = self.get_dialog_data()
        section_for_search = field_for_search = None
        counter = 0
        self.new_data = []
        for field in filled_fields:
            if filled_fields[field].text:
                section_for_search = field
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
        self.close_dialog()
        self.info_about_searched_rows()

    def info_about_searched_rows(self):
        self.close_dialog()
        self.info = MDDialog(
            title="Result: " + str(self.counter) + " row(s) found",
            type="custom",
            size_hint_x=None,
            size_hint_y=None,
            height="500dp",
            width="800dp",
            content_cls=MDBoxLayout(
                returned_table(self.new_data),
                orientation="vertical",
                spacing="15dp",
                size_hint_y=None,
                height="500dp",
                width="800dp"
            ),
        )
        self.info.open()

    def search_and_delete_rows(self):
        data = self.get_rows()
        filled_fields = self.get_dialog_data()
        section_for_search = field_for_search = None
        counter = 0
        new_data = {}
        new_data["items"] = []
        for field in filled_fields:
            if filled_fields[field].text:
                section_for_search = field
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
        self.clear_data_base()
        for item in new_data["items"]:
            self.data_tables.add_row((item["Patient's name"], item["Address"],
                                      item["Birth date"], item["Appointment date"],
                                      item["Doctor's name"], item["Conclusion"]))
        self.close_dialog()
        self.info_about_deleted_rows(counter)

    def close_info_dialog(self):
        self.info.dismiss()

    def form_for_search_delete(self):
        self.dialog = MDDialog(
            title="Fill in the data:",
            type="custom",
            content_cls=MDBoxLayout(
                MDTextField(
                    id="Patient's name",
                    hint_text="Patient's name",
                ),
                MDTextField(
                    id="Address",
                    hint_text="Address",
                ),
                MDTextField(
                    id="Birth date",
                    hint_text="Birth date",
                ),
                MDTextField(
                    id="Appointment date",
                    hint_text="Appointment date",
                    max_text_length=10,
                ),
                MDTextField(
                    id="Doctor's name",
                    hint_text="Doctor's name",
                ),
                MDTextField(
                    id="Conclusion",
                    hint_text="Conclusion",
                ),
                orientation="vertical",
                spacing="8dp",
                size_hint_y=None,
                height="400dp",
            ),
            buttons=[
                MDFlatButton(
                    text="Cancel",
                    theme_text_color="Custom",
                    text_color=self.theme_cls.primary_color,
                    on_release=self.on_button_press,
                ),
                MDFlatButton(
                    text="Find",
                    theme_text_color="Custom",
                    text_color=self.theme_cls.primary_color,
                    on_release=self.on_button_press,
                ),
                MDFlatButton(
                    text="Delete",
                    theme_text_color="Custom",
                    text_color=self.theme_cls.primary_color,
                    on_release=self.on_button_press,
                ),
            ],
        )
        self.dialog.open()

    def info_about_deleted_rows(self, counter):
        self.info = MDDialog(
            text="Deleted Rows: " + str(counter),
            buttons=[
                MDFlatButton(
                    text="Close",
                    theme_text_color="Custom",
                    text_color=self.theme_cls.primary_color,
                    on_release=self.on_button_press,
                ),
            ],
        )
        self.info.open()

    def get_rows(self):
        data_temp = self.data_tables.row_data
        data = {}
        data["items"] = []
        for item in data_temp:
            data["items"].append({
                "Patient's name": item[0],
                "Address": item[1],
                "Birth date": item[2],
                "Appointment date": item[3],
                "Doctor's name": item[4],
                "Conclusion": item[5],
            })
        return data

    def read(self):
        self.clear_data_base()
        file_name = self.get_dialog_data()
        if os.path.isfile(file_name["File Name"].text):
            json_file = open(file_name["File Name"].text, "r")
            data_base = j.load(json_file)
            for item in data_base["items"]:
                self.data_tables.add_row((item["Patient's name"], item["Address"],
                                          item["Birth date"], item["Appointment date"],
                                          item["Doctor's name"], item["Conclusion"]))
            json_file.close()
            self.dialog.dismiss()
        else:
            self.error_file_dialog()

    def write(self):
        file_name = self.get_dialog_data()
        with open(file_name["File Name"].text, "w") as outfile:
            j.dump(self.get_rows(), outfile, sort_keys=True, indent=4)
        self.dialog.dismiss()

    def clear_data_base(self):
        while len(self.data_tables.row_data) > 0:
            self.data_tables.remove_row(self.data_tables.row_data[-1])

    def error_file_dialog(self):
        self.dialog_error = MDDialog(
            text="No such file",
            buttons=[
                MDFlatButton(
                    text="Try again",
                    theme_text_color="Custom",
                    text_color=self.theme_cls.primary_color,
                    on_release=self.on_button_press,
                ),
            ],
        )
        self.dialog_error.open()

    def close_dialog(self):
        self.dialog.dismiss()

    def close_error_dialog(self):
        self.dialog_error.dismiss()

    def add_row(self):
        item = self.get_dialog_data()
        self.data_tables.add_row((item["Patient's name"].text, item["Address"].text,
                                  item["Birth date"].text, item["Appointment date"].text,
                                  item["Doctor's name"].text, item["Conclusion"].text))
        self.dialog.dismiss()

    def remove_row(self):
        if len(self.data_tables.row_data) > 0:
            self.data_tables.remove_row(self.data_tables.row_data[-1])

    def get_dialog_data(self):
        return self.dialog.content_cls.ids

    def form_to_add_new_row(self):
        self.dialog = MDDialog(
            title="Enter data:",
            type="custom",
            content_cls=MDBoxLayout(
                MDTextField(
                    id="Patient's name",
                    hint_text="Patient's name",
                ),
                MDTextField(
                    id="Address",
                    hint_text="Address",
                ),
                MDTextField(
                    id="Birth date",
                    hint_text="Birth date",
                    max_text_length=10,
                ),
                MDTextField(
                    id="Appointment date",
                    hint_text="Appointment date",
                ),
                MDTextField(
                    id="Doctor's name",
                    hint_text="Doctor's name",
                ),
                MDTextField(
                    id="Conclusion",
                    hint_text="Conclusion",
                ),
                orientation="vertical",
                spacing="8dp",
                size_hint_y=None,
                height="400dp",
            ),
            buttons=[
                MDFlatButton(
                    text="Cancel",
                    theme_text_color="Custom",
                    text_color=self.theme_cls.primary_color,
                    on_release=self.on_button_press,
                ),
                MDFlatButton(
                    text="Add",
                    theme_text_color="Custom",
                    text_color=self.theme_cls.primary_color,
                    on_release=self.on_button_press,
                ),
            ],
        )
        self.dialog.open()

    def wr_form(self):
        self.dialog = MDDialog(
            title="Enter the file name:",
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
                    text="Cancel",
                    theme_text_color="Custom",
                    text_color=self.theme_cls.primary_color,
                    on_release=self.on_button_press,
                ),
                MDFlatButton(
                    text="Read",
                    theme_text_color="Custom",
                    text_color=self.theme_cls.primary_color,
                    on_release=self.on_button_press,
                ),
                MDFlatButton(
                    text="Write",
                    theme_text_color="Custom",
                    text_color=self.theme_cls.primary_color,
                    on_release=self.on_button_press,
                )
            ],
        )
        self.dialog.open()

    def build(self):
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "Blue"

        button_box = MDBoxLayout(
            padding="10dp",
            spacing="5dp",
        )

        for button_text in ["+", "-", "Read / Write", "Find / Delete"]:
            button_box.add_widget(
                MDRaisedButton(
                    text=button_text, on_release=self.on_button_press
                )
            )

        layout = AnchorLayout()
        self.data_tables = MDDataTable(
            size_hint=(1, 1),
            use_pagination=True,
            rows_num=6,
            column_data=[
                ("Patient's name", dp(25)),
                ("Address", dp(25)),
                ("Birth date", dp(25)),
                ("Appointment date", dp(25)),
                ("Doctor's name", dp(25)),
                ("Conclusion", dp(25))
            ]
        )

        layout.add_widget(self.data_tables)
        layout.add_widget(button_box)
        return layout


def returned_table(new_data):
    return MDAnchorLayout(
        MDDataTable(
            size_hint=(1, 1),
            use_pagination=True,
            rows_num=6,
            width="500dp",
            height="500dp",
            column_data=[
                ("Patient's name", dp(25)),
                ("Address", dp(25)),
                ("Birth date", dp(25)),
                ("Appointment date", dp(25)),
                ("Doctor's name", dp(25)),
                ("Conclusion", dp(25))
            ],
            row_data=new_data
        )
    )


Patients().run()
