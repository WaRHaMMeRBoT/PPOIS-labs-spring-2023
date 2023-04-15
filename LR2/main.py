import  json
import parser_json
from kivy.metrics import dp
from kivymd.app import MDApp
from kivymd.uix.datatables import MDDataTable
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.button import MDRaisedButton
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.textfield import MDTextField
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDIconButton
from kivymd.uix.label import MDLabel

with open("sw_templates.json", "r") as f:
    data = json.load(f)


class Example(MDApp):
    data_tables = None

    def build(self):
        Window.size = (1100, 700)
        Window.top = 100  # установка вертикальной позиции
        Window.left = 200  # установка горизонтальной позиции
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Orange"
        self.dialog = None
        self.dialog_add = None
        self.dialog_delete_wind = None
        self.dialog_search = None

        layout = MDFloatLayout()
        layout.add_widget(
            MDRaisedButton(
                text="Поиск по параметрам",
                pos_hint={"center_x": 0.14},
                on_release=self.show_modal_view,
                y=30,
            )
        )
        layout.add_widget(
            MDRaisedButton(
                text="Удалить",
                pos_hint={"center_x": 0.9},
                on_release=self.delete_datatable_element,
                y=30,
            )
        )
        layout.add_widget(
            MDRaisedButton(
                text="Добавить ",
                pos_hint={"center_x": 0.76},
                on_release=self.show_confirmation_dialog,
                y=30,
            )
        )



        search_layout = BoxLayout(
            size_hint_y=None,
            size_hint_x=0.4,
            pos_hint={"center_y": 0.107, "center_x": 0.48},
        )
        self.search_field = MDTextField(hint_text="Введите запрос", mode="fill", id="search_string")
        search_button = MDIconButton(icon="magnify", on_release=self.search)
        search_layout.add_widget(self.search_field)
        search_layout.add_widget(search_button)
        layout.add_widget(search_layout)

        self.data_tables = MDDataTable(
            pos_hint={"center_y": 0.55, "center_x": 0.5},
            rows_num=100,
            size_hint=(0.95, 0.8),
            check=True,
            use_pagination=False,
            column_data=[
                ("№", dp(20)),
                ("Название книги", dp(30)),
                ("ФИО автора", dp(30)),
                ("Издательство", dp(30)),
                ("Число томов", dp(30)),
                ("Тираж", dp(30)),
                ("Итого томов", dp(30)),
            ],
            row_data=[(i+1, d['book_name'], d['author_name'], d['publishing_house'], d['number_of_tom'],
                       d['number_of_editions'], d['all_editions']) for i, d in enumerate(data)],
        )

        layout.add_widget(self.data_tables)
        self.data_tables.bind(on_check_press=self.on_check_press)
        self.list_for_delete = []



        return layout

    def on_check_press(self, instance_table, current_row):
        if not current_row in self.list_for_delete:
            self.list_for_delete.append(current_row)
        else:
            self.list_for_delete.remove(current_row)

    def show_modal_view(self, *args):
        if not self.dialog_search:

            self.dialog_search = MDDialog(
                title="Поиск по параметрам:",
                type="custom",
                size_hint_x=None,
                width=350,


                content_cls=MDBoxLayout(
                    MDTextField(id="book_title", hint_text="Название книги", size_hint=(0.33, None)),
                    MDTextField(id="author_name", hint_text="ФИО автора", size_hint=(0.33, None)),
                    MDTextField(id="publisher", hint_text="Издательство", size_hint=(0.33, None)),
                    MDLabel(text="Число томов :", font_size="30sp", size_hint=(0.4, 15)),
                    MDBoxLayout(
                        MDTextField(id="min_volumes", hint_text="Мин."),
                        MDLabel(text="_", font_size="70sp", size_hint=(0.2, 1.4)),
                        MDTextField(id="max_volumes", hint_text="Макс."),
                        orientation="horizontal",
                        size_hint=(0.2, 20),
                        spacing="20dp",
                    ),
                    MDLabel(text="Тираж :", halign="left", font_size="20sp", size_hint=(0.4, 15)),
                    MDBoxLayout(
                        MDTextField(id="min_editions", hint_text="Мин."),
                        MDLabel(text="_", font_size="70sp", size_hint=(0.2, 1.4)),
                        MDTextField(id="max_editions", hint_text="Макс."),
                        orientation="horizontal",
                        size_hint=(0.2, 25),
                        spacing="20dp",
                    ),
                    MDLabel(text="Итого томов :", halign="left", font_size="20sp", size_hint=(0.4, 15)),
                    MDBoxLayout(
                        MDTextField(id="min_total_volumes", hint_text="Мин."),
                        MDLabel(text="_", font_size="70sp", size_hint=(0.2, 1.4)),
                        MDTextField(id="max_total_volumes", hint_text="Макс."),
                        orientation="horizontal",
                        size_hint=(0.2, 25),
                        spacing="20dp",
                    ),
                    orientation="vertical",
                    size_hint_y=None,
                    height="470dp",
                    size_hint_x=None,
                    width=900,
                ),
                buttons=[
                    MDFlatButton(
                        text="CANCEL",
                        theme_text_color="Custom",
                        text_color=self.theme_cls.primary_color,
                        on_release=lambda x: self.dialog_search.dismiss()
                    ),
                    MDFlatButton(
                        text="OK",
                        theme_text_color="Custom",
                        text_color=self.theme_cls.primary_color,
                        on_release=self.pro_search
                    ),
                ],
            )
        self.dialog_search.open()

    def show_confirmation_dialog(self, *args):
        if not self.dialog_add:
            self.dialog_add = MDDialog(
                title="Новая книга:",
                type="custom",
                content_cls=MDBoxLayout(
                    MDTextField(
                        id="book_name",
                        hint_text="Название книги",
                    ),
                    MDTextField(
                        id="author_name",
                        hint_text="ФИО автора",
                    ),
                    MDTextField(
                        id="publisher",
                        hint_text="Издательство",
                    ),
                    MDTextField(
                        id="number_of_volumes",
                        hint_text="Число томов",
                    ),
                    MDTextField(
                        id="print_run",
                        hint_text="Тираж",
                    ),
                    orientation="vertical",
                    spacing="16dp",
                    size_hint_y=None,
                    height="370dp",
                ),
                buttons=[
                    MDFlatButton(
                        text="CANCEL",
                        theme_text_color="Custom",
                        text_color=self.theme_cls.primary_color,
                        on_release=lambda x: self.dialog_add.dismiss()
                    ),
                    MDFlatButton(
                        text="OK",
                        theme_text_color="Custom",
                        text_color=self.theme_cls.primary_color,
                        on_release=self.update
                    ),
                ],
            )
        self.dialog_add.open()

    def update(self, *args):
        self.data_tables.row_data = parser_json.update_row_data()
        parser_json.add_book_from_window(self, *args)
        self.data_tables.row_data = parser_json.update_row_data()

    dialog_delete_wind = None

    def delete_datatable_element(self, *args):
        if not self.dialog_delete_wind:
            self.dialog_delete_wind = MDDialog(
                title="Вы действительно хотите удалить ?",

                buttons=[MDFlatButton(
                        text="CANCEL",
                        theme_text_color="Custom",
                        text_color=self.theme_cls.primary_color,
                        on_release=lambda x: self.dialog_delete_wind.dismiss()
                        ),
                        MDFlatButton(
                            text="OK",
                            theme_text_color="Custom",
                            text_color=self.theme_cls.primary_color,
                            on_release=self.delete
                        ),
                ],
                )
        self.dialog_delete_wind.open()

    def delete(self, *args):
        if len(self.list_for_delete) == 0:
            print(self.list_for_delete)
            pass
        else:
            for i in self.list_for_delete:
                i[0] = int(i[0])
                i[4] = int(i[4])
                i[5] = int(i[5])
                i[6] = int(i[6])
                self.data_tables.row_data.remove(tuple(i))

        parser_json.update_file(self.data_tables.row_data)
        self.data_tables.row_data = parser_json.update_row_data()
        self.dialog_delete_wind.dismiss()

    def search(self, *args):
        filtered_data = []
        search_text = str(self.search_field.text)
        if len(search_text) == 0:
            self.data_tables.row_data = parser_json.update_row_data()
        else:
            # Итерируемся по всем строкам таблицы и находим совпадения с введенным текстом
            for row_data in self.data_tables.row_data:
                for cell_data in row_data:
                    if search_text.lower() in str(cell_data).lower():

                        filtered_data.append(row_data)
                        break
                print(row_data)
            # Обновляем данные в таблице
            self.data_tables.row_data = filtered_data

    def pro_search(self, *args):
        book_title = str(self.dialog_search.content_cls.ids.book_title.text.strip())
        author_name = str(self.dialog_search.content_cls.ids.author_name.text.strip())
        publisher = str(self.dialog_search.content_cls.ids.publisher.text.strip())
        min_volumes = int(self.dialog_search.content_cls.children[4].children[2].text) if \
            self.dialog_search.content_cls.children[4].children[2].text.strip() != "" else 0
        max_volumes = int(self.dialog_search.content_cls.children[4].children[0].text) if \
            self.dialog_search.content_cls.children[4].children[0].text.strip() != "" else 100
        min_editions = int(self.dialog_search.content_cls.children[2].children[2].text) if \
            self.dialog_search.content_cls.children[2].children[2].text.strip() != "" else 0
        max_editions = int(self.dialog_search.content_cls.children[2].children[0].text) if \
            self.dialog_search.content_cls.children[2].children[0].text.strip() != "" else 100
        min_total_volumes = int(self.dialog_search.content_cls.children[0].children[2].text) if \
            self.dialog_search.content_cls.children[0].children[2].text.strip() != "" else 0
        max_total_volumes = int(self.dialog_search.content_cls.children[0].children[0].text) if \
            self.dialog_search.content_cls.children[0].children[0].text.strip() != "" else 100

        # Filter the table based on the user's input
        filtered_data = []
        if len(book_title) == 0 and len(author_name) == 0 and len(publisher) == 0:
            self.data_tables.row_data = parser_json.update_row_data()
        else:
            for row_data in self.data_tables.row_data:
                book_title_match = book_title == "" or book_title.lower() in str(row_data[1]).lower()
                author_name_match = author_name == "" or author_name.lower() in str(row_data[2]).lower()
                publisher_match = publisher == "" or publisher.lower() in str(row_data[3]).lower()
                volumes_match = min_volumes <= int(row_data[4]) <= max_volumes
                editions_match = min_editions <= int(row_data[5]) <= max_editions
                total_volumes_match = min_total_volumes <= int(row_data[6]) <= max_total_volumes

                if book_title_match and author_name_match and publisher_match and volumes_match and editions_match \
                        and total_volumes_match:
                    filtered_data.append(row_data)

            # Display the filtered data in the table
            self.data_tables.row_data = filtered_data

            # Close the search dialog
        self.dialog_search.dismiss()


Example().run()