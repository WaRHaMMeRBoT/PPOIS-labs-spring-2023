from kivymd.app import MDApp

import read_file
import write_file

from kivymd.uix.gridlayout import MDGridLayout
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.datatables import MDDataTable
from kivymd.uix.screen import Screen
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.uix.textinput import TextInput
from kivy.uix.popup import Popup
from kivy.uix.spinner import Spinner
from kivy.uix.label import Label
from kivy.metrics import dp

students = read_file.read_xml('students.xml')


class MyApp(MDApp):
    def build(self):
        screen = Screen()

        main_gl = MDGridLayout(rows=1)
        bl_labels = MDBoxLayout(orientation='vertical', size_hint=[.3, 1], padding=dp(30), spacing=dp(40))

        search_button = Button(text="Окно поиска", on_press=self.btn_press_call_search)
        delete_button = Button(text="Окно удаления", on_press=self.btn_press_call_delete)
        add_button = Button(text="Окно добавления", on_press=self.btn_press_call_add)
        self.path = TextInput(hint_text="Путь к файлу", multiline=False)
        save_button = Button(text="Сохранить", on_press=self.btn_press_save)

        bl_labels.add_widget(search_button)
        bl_labels.add_widget(delete_button)
        bl_labels.add_widget(add_button)
        bl_labels.add_widget(Widget())
        bl_labels.add_widget(self.path)
        bl_labels.add_widget(save_button)

        self.table = MDDataTable(size_hint=[.7, 1], check=False,
                            use_pagination=True,
                            column_data=[("ФИО", dp(60)),
                                         ("Курс", dp(10)),
                                         ("Группа", dp(15)),
                                         ("Общее кол-во работ", dp(35)),
                                         ("Кол-во выполненых работ", dp(45)),
                                         ("Язык программирования", dp(45))],
                            row_data=students
                            )

        bl_delete = MDBoxLayout(orientation='vertical', spacing=dp(20), padding=dp(20))

        self.what_delete = Spinner(
            text='Выберите условие удаления',
            values=('Группа', 'Курс', 'Общее число работ', 'Кол-во невыполненных работ'),
            size_hint=[1, .5]
        )

        self.what_search = Spinner(
            text='Выберите условие поиска',
            values=('Группа', 'Курс', 'Общее число работ', 'Кол-во невыполненных работ'),
            size_hint=[1, .5]
        )

        self.label_delete = Label()
        self.text_input_delete = TextInput(multiline=False)

        bl_delete.add_widget(self.what_delete)
        bl_delete.add_widget(self.label_delete)
        bl_delete.add_widget(self.text_input_delete)
        bl_delete.add_widget(Button(text='Удалить', on_press=self.btn_press_delete))

        self.delete_popup = Popup(content=bl_delete, title='Окно удаления', size_hint=[.35, .5])

        bl_search = MDBoxLayout(orientation='horizontal')

        self.search_popup = Popup(content=bl_search, title='Окно поиска', size_hint=[.8, .6])

        self.table_search = MDDataTable(size_hint=[.7, 1], check=False,
                                 use_pagination=True,
                                 column_data=[("ФИО", dp(60)),
                                              ("Курс", dp(10)),
                                              ("Группа", dp(15)),
                                              ("Общее кол-во работ", dp(35)),
                                              ("Кол-во выполненых работ", dp(45)),
                                              ("Язык программирования", dp(45))]
                                 )
        self.label_search = Label()
        self.text_input_search = TextInput(multiline=False, size_hint=[1, .3])

        bl_search_menu = MDBoxLayout(orientation='vertical', size_hint=[.3, 1], spacing=dp(30), padding=dp(30))

        bl_search_menu.add_widget(self.what_search)
        bl_search_menu.add_widget(self.label_search)
        bl_search_menu.add_widget(self.text_input_search)
        bl_search_menu.add_widget(Button(text='Поиск', on_press=self.btn_press_search, size_hint=[1, .3]))

        bl_search.add_widget(self.table_search)
        bl_search.add_widget(bl_search_menu)

        bl_add = MDBoxLayout(orientation='vertical', spacing=dp(15), padding=dp(15))

        self.text_input_1 = TextInput(hint_text='ФИО', multiline=False)
        bl_add.add_widget(self.text_input_1)
        self.text_input_2 = TextInput(hint_text='Курс', multiline=False)
        bl_add.add_widget(self.text_input_2)
        self.text_input_3 = TextInput(hint_text='Группа', multiline=False)
        bl_add.add_widget(self.text_input_3)
        self.text_input_4 = TextInput(hint_text='Общее кол-во работ', multiline=False)
        bl_add.add_widget(self.text_input_4)
        self.text_input_5 = TextInput(hint_text='Кол-во выполненых работ', multiline=False)
        bl_add.add_widget(self.text_input_5)
        self.text_input_6 = TextInput(hint_text='Язык программирования', multiline=False)
        bl_add.add_widget(self.text_input_6)
        bl_add.add_widget(Button(text='Добавить', on_press=self.btn_press_add))


        self.add_popup = Popup(title='Окно добавления', size_hint=[.8, .6], content=bl_add)

        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "BlueGray"

        main_gl.add_widget(self.table)
        main_gl.add_widget(bl_labels)
        screen.add_widget(main_gl)
        return screen

    def btn_press_save(self, instance):
        write_file.write(students, self.path.text)

    def btn_press_call_delete(self, instance):
        self.delete_popup.open()

    def btn_press_call_search(self, instance):
        self.search_popup.open()

    def btn_press_call_add(self, instance):
        self.add_popup.open()

    def btn_press_delete(self, instance):
        index = -1
        buffer = read_file.read_xml('students.xml')
        counter = 0
        if self.what_delete.text == 'Группа':
            index = 2
        elif self.what_delete.text == 'Курс':
            index = 1
        elif self.what_delete.text == 'Общее число работ':
            index = 3
        elif self.what_delete.text == 'Кол-во невыполненных работ':
            index = 34

        if index == -1:
            self.label_delete.text = 'Вы не указали условие удаления'
            counter = -1
        if index != -1 and index != 34:
            counter = 0
            for student in buffer:
                if int(student[index]) == int(self.text_input_delete.text):
                    students.remove(student)
                    counter += 1
        if index == 34:
            counter = 0
            print(len(buffer))
            for student in buffer:
                print(student)
                amount = int(student[3]) - int(student[4])
                if amount == int(self.text_input_delete.text):
                    students.remove(student)
                    counter += 1
        write_file.write(students, 'students.xml')
        if counter == 0:
            self.label_delete.text = 'По вашему запросу ничего не найдено'
        elif counter != 0 and counter != -1:
            self.label_delete.text = 'Было удалено ' + str(counter) + ' записей'
        self.table.update_row_data(self.table.row_data, students)

    def btn_press_search(self, instance):
        search_output = []
        counter = 0
        index = -1
        if self.what_search.text == 'Группа':
            index = 2
        elif self.what_search.text == 'Курс':
            index = 1
        elif self.what_search.text == 'Общее число работ':
            index = 3
        elif self.what_search.text == 'Кол-во невыполненных работ':
            index = 34

        if index == -1:
            self.label_search.text = 'Вы не указали условие поиска'
            counter = -1
        if index != -1 and index != 34:
            counter = 0
            for student in students:
                if int(student[index]) == int(self.text_input_search.text):
                    search_output.append(student)
                    counter += 1
        if index == 34:
            counter = 0
            for student in students:
                amount = int(student[3]) - int(student[4])
                if amount == int(self.text_input_search.text):
                    search_output.append(student)
                    counter += 1
        if counter == 0:
            self.label_search.text = 'По вашему запросу ничего не найдено'
        elif counter != 0 and counter != -1:
            self.table_search.update_row_data(self.table_search.row_data, search_output)
            self.label_search.text = ''

    def btn_press_add(self, instance):
        student = []
        student.append(self.text_input_1.text)
        student.append(self.text_input_2.text)
        student.append(self.text_input_3.text)
        student.append(self.text_input_4.text)
        student.append(self.text_input_5.text)
        student.append(self.text_input_6.text)
        students.append(student)
        self.table.update_row_data(self.table.row_data, students)
        write_file.write(students, 'students.xml')