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


class StoreDataBase(MDApp):
    dialog = dialog_error = data_tables = info = info_table = new_data = counter = None

    def on_button_press(self, instance_button: MDRaisedButton):
        try:
            {
                "+": self.form_to_add_new_row,
                "-": self.remove_row,
                "Read / Write": self.form_for_read_write_file,
                "READ": self.read_file,
                "WRITE": self.write_file,
                "CANCEL": self.close_dialog,
                "ADD": self.add_row,
                "TRY AGAIN": self.close_error_dialog,
                "Search / Delete": self.form_for_search_delete,
                "SEARCH": self.search_and_output_rows,
                "DELETE": self.search_and_delete_rows,
                "CLOSE": self.close_info_dialog,
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
                if section_for_search == "Quantity In Stock":
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
        self.close_dialog()
        self.info_about_searched_rows()

    def info_about_searched_rows(self):
        self.close_dialog()
        self.info = MDDialog(
            title="Result: " + str(self.counter) + " rows found",
            type="custom",
            size_hint_x=None,
            size_hint_y=None,
            height="800dp",
            width="1500dp",
            content_cls=MDBoxLayout(
                returned_table(self.new_data),
                orientation="vertical",
                spacing="15dp",
                size_hint_y=None,
                height="500dp",
                width="1000dp"
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
                if section_for_search == "Quantity In Stock":
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
        self.clear_data_base()
        for item in new_data["items"]:
            self.data_tables.add_row((item["Product Name"], item["Manufacturer Name"],
                                      item["Manufacturer's UCR"], item["Quantity In Stock"], item["Warehouse Address"]))
        self.close_dialog()
        self.info_about_deleted_rows(counter)

    def close_info_dialog(self):
        self.info.dismiss()

    def form_for_search_delete(self):
        self.dialog = MDDialog(
            title="Fill Out One of The Fields:",
            type="custom",
            content_cls=MDBoxLayout(
                MDTextField(
                    id="Product Name",
                    hint_text="Product Name",
                ),
                MDTextField(
                    id="Quantity In Stock",
                    hint_text="Quantity In Stock",
                ),
                MDTextField(
                    id="Manufacturer Name",
                    hint_text="Manufacturer Name",
                ),
                MDTextField(
                    id="Manufacturer's UCR",
                    hint_text="Manufacturer's UCR",
                    max_text_length=9,
                ),
                MDTextField(
                    id="Warehouse Address",
                    hint_text="Warehouse Address",
                ),
                orientation="vertical",
                spacing="8dp",
                size_hint_y=None,
                height="340dp",
            ),
            buttons=[
                MDFlatButton(
                    text="CANCEL",
                    theme_text_color="Custom",
                    text_color=self.theme_cls.primary_color,
                    on_release=self.on_button_press,
                ),
                MDFlatButton(
                    text="SEARCH",
                    theme_text_color="Custom",
                    text_color=self.theme_cls.primary_color,
                    on_release=self.on_button_press,
                ),
                MDFlatButton(
                    text="DELETE",
                    theme_text_color="Custom",
                    text_color=self.theme_cls.primary_color,
                    on_release=self.on_button_press,
                ),
            ],
        )
        self.dialog.open()

    def info_about_deleted_rows(self, counter):
        self.info = MDDialog(
            text="Count Of Deleted Rows: " + str(counter),
            buttons=[
                MDFlatButton(
                    text="CLOSE",
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
                "Product Name": item[0],
                "Manufacturer Name": item[1],
                "Manufacturer's UCR": item[2],
                "Quantity In Stock": 0 if item[3] == "" else int(item[3]),
                "Warehouse Address": item[4]
            })
        return data

    def write_file(self):
        file_name = self.get_dialog_data()
        with open(file_name["File Name"].text, "w+") as outfile:
            j.dump(self.get_rows(), outfile)
        self.dialog.dismiss()

    def clear_data_base(self):
        while len(self.data_tables.row_data) > 0:
            self.data_tables.remove_row(self.data_tables.row_data[-1])

    def read_file(self):
        self.clear_data_base()
        file_name = self.get_dialog_data()
        if os.path.isfile(file_name["File Name"].text):
            json_file = open(file_name["File Name"].text, "r")
            data_base = j.load(json_file)
            for item in data_base["items"]:
                self.data_tables.add_row((item["Product Name"], item["Manufacturer Name"],
                                          item["Manufacturer's UCR"], item["Quantity In Stock"],
                                          item["Warehouse Address"]))
            json_file.close()
            self.dialog.dismiss()
        else:
            self.error_file_dialog()

    def error_file_dialog(self):
        self.dialog_error = MDDialog(
            text="The File Does Not Exist!",
            buttons=[
                MDFlatButton(
                    text="TRY AGAIN",
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
        self.data_tables.add_row((item["Product Name"].text, item["Manufacturer Name"].text,
                                  item["Manufacturer's UCR"].text, item["Quantity In Stock"].text,
                                  item["Warehouse Address"].text))
        self.dialog.dismiss()

    def remove_row(self):
        if len(self.data_tables.row_data) > 0:
            self.data_tables.remove_row(self.data_tables.row_data[-1])

    def get_dialog_data(self):
        return self.dialog.content_cls.ids

    def form_to_add_new_row(self):
        self.dialog = MDDialog(
            title="Enter Data:",
            type="custom",
            content_cls=MDBoxLayout(
                MDTextField(
                    id="Product Name",
                    hint_text="Product Name",
                ),
                MDTextField(
                    id="Manufacturer Name",
                    hint_text="Manufacturer Name",
                ),
                MDTextField(
                    id="Manufacturer's UCR",
                    hint_text="Manufacturer's UCR",
                    max_text_length=9,
                ),
                MDTextField(
                    id="Quantity In Stock",
                    hint_text="Quantity In Stock",
                ),
                MDTextField(
                    id="Warehouse Address",
                    hint_text="Warehouse Address",
                ),
                orientation="vertical",
                spacing="8dp",
                size_hint_y=None,
                height="340dp",
            ),
            buttons=[
                MDFlatButton(
                    text="CANCEL",
                    theme_text_color="Custom",
                    text_color=self.theme_cls.primary_color,
                    on_release=self.on_button_press,
                ),
                MDFlatButton(
                    text="ADD",
                    theme_text_color="Custom",
                    text_color=self.theme_cls.primary_color,
                    on_release=self.on_button_press,
                ),
            ],
        )
        self.dialog.open()

    def form_for_read_write_file(self):
        self.dialog = MDDialog(
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
                    text="CANCEL",
                    theme_text_color="Custom",
                    text_color=self.theme_cls.primary_color,
                    on_release=self.on_button_press,
                ),
                MDFlatButton(
                    text="READ",
                    theme_text_color="Custom",
                    text_color=self.theme_cls.primary_color,
                    on_release=self.on_button_press,
                ),
                MDFlatButton(
                    text="WRITE",
                    theme_text_color="Custom",
                    text_color=self.theme_cls.primary_color,
                    on_release=self.on_button_press,
                )
            ],
        )
        self.dialog.open()

    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Yellow"

        button_box = MDBoxLayout(
            padding="10dp",
            spacing="5dp",
        )

        for button_text in ["+", "-", "Read / Write", "Search / Delete"]:
            button_box.add_widget(
                MDRaisedButton(
                    text=button_text, on_release=self.on_button_press
                )
            )

        layout = AnchorLayout()
        self.data_tables = MDDataTable(
            size_hint=(1, 1),
            use_pagination=True,
            rows_num=5,
            column_data=[
                ("Product Name", dp(60)),
                ("Manufacturer Name", dp(60)),
                ("Manufacturer's UCR", dp(60)),
                ("Quantity In Stock", dp(60)),
                ("Warehouse Address", dp(60)),
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
            rows_num=5,
            width="1000dp",
            height="1000dp",
            column_data=[
                ("Product Name", dp(55)),
                ("Manufacturer Name", dp(55)),
                ("Manufacturer's UCR", dp(55)),
                ("Quantity In Stock", dp(55)),
                ("Warehouse Address", dp(62)),
            ],
            row_data=new_data
        )
    )


StoreDataBase().run()
