from kivymd.app import MDApp
from kivymd.uix.dialog import MDDialog
from kivy.lang.builder import Builder
from kivymd.uix.button import MDRectangleFlatButton
from controller.controller import Controller
from model.model import StudentModel
from kivymd.uix.screen import MDScreen
from kivymd.uix.screenmanager import MDScreenManager
from kivy.metrics import dp
from kivymd.uix.datatables.datatables import MDDataTable
from kivymd.uix.menu.menu import MDDropdownMenu
from kivy.clock import Clock
import re
from typing import Optional


class StudentsAppMainScreen(MDScreen):
    pass


class AddStudentScreen(MDScreen):
    def __init__(self, **kwargs):
        super(AddStudentScreen, self).__init__(**kwargs)
        self.controller = Controller()
        self.dialog = None

    def send_add_data(self):
        student_info = dict()
        student_info['last_name'] = self.ids.last_name.text
        if student_info['last_name'] in ('', None):
            self.validation_dialog("Фамилия - обязательный параметр")
            return
        student_info['first_name'] = self.ids.first_name.text
        if student_info['first_name'] in ('', None):
            self.validation_dialog("Фамилия - обязательный параметр")
            return
        student_info['middle_name'] = self.ids.middle_name.text
        student_info['year'] = self.ids.year.text
        student_info['group_number'] = self.ids.group_number.text
        student_info['all_assignments'] = self.ids.all_assignments.text
        student_info['all_assignments'] \
            = 0 if student_info['all_assignments'] in ('', None) else abs(int(student_info['all_assignments']))
        student_info['completed_assignments'] = self.ids.completed_assignments.text
        student_info['completed_assignments'] \
            = 0 if student_info['completed_assignments'] in ('', None) else abs(int(student_info['completed_assignments']))
        student_info['language'] = self.ids.language.text
        self.controller.add(student_info)
        self.flush_text_input()

    def validation_dialog(self, text: str):
        self.dialog = MDDialog(
            title=text,
            buttons=[MDRectangleFlatButton(
                text="Принять",
                on_release=self.close_dialog
            )
            ]
        )
        self.dialog.open()

    def close_dialog(self, obj):
        self.dialog.dismiss()

    def flush_text_input(self):
        for i in (self.ids.last_name, self.ids.first_name, self.ids.middle_name,
                  self.ids.year, self.ids.group_number, self.ids.all_assignments,
                  self.ids.completed_assignments, self.ids.language):
            i.text = ''


class AllStudentScreen(MDScreen):
    def __init__(self, **kwargs):
        super(AllStudentScreen, self).__init__(**kwargs)
        self.model = StudentModel()
        self.data = self.model.all()
        self.column_data = [
            ("ID", dp(40)),
            ("Фамилия", dp(40)),
            ("Имя", dp(40)),
            ("Отчество", dp(40)),
            ("Курс", dp(40)),
            ("Номер группы", dp(40)),
            ("Общее число работ", dp(40)),
            ("Число выполненных работ", dp(40)),
            ("Язык программирования", dp(40))
        ]
        self.table = MDDataTable(
            pos_hint={'center_x': .5, 'center_y': .5},
            size_hint=(.9, .6),
            use_pagination=True,
            column_data=self.column_data,
            row_data=self.data,
            rows_num=5
        )
        self.add_widget(self.table)

    def label_text(self):
        record_amount = len(self.data)
        return f"Найдено {record_amount} записей"

    def on_pre_enter(self, *args):
        Clock.schedule_once(self.get_data, -1)

    def get_data(self, dt):
        self.table.row_data = self.model.all()


class FindStudentScreen(MDScreen):

    def __init__(self, **kwargs):
        super(FindStudentScreen, self).__init__(**kwargs)
        self.model = StudentModel()
        self.column_data = [
            ("ID", dp(35)),
            ("Фамилия", dp(35)),
            ("Имя", dp(35)),
            ("Отчество", dp(35)),
            ("Курс", dp(35)),
            ("Номер группы", dp(35)),
            ("Общее число работ", dp(35)),
            ("Число выполненных работ", dp(35)),
            ("Язык программирования", dp(35))
        ]
        self.table = MDDataTable(
            pos_hint={'center_x': .5, 'center_y': .5},
            size_hint=(.9, .6),
            use_pagination=True,
            column_data=self.column_data,
            row_data=self.model.all(),
            rows_num=5
        )
        self.add_widget(self.table)
        self.filter_options = dict()


    def set_language_filter(self, value):
        self.filter_options['language'] = '' if value is None else value
        self.ids.language_choose.text = 'Ничего' if value is None else str(value)
        self.filter()

    def construct_dropdown_entry(self, value):
        return {
            'viewclass': 'OneLineListItem',
            'text': 'Ничего' if value is None else str(value),
            'on_release': lambda x=value: self.set_language_filter(x)
        }

    def languages_dropdown(self):
        languages_menu = list()
        languages_menu.append(self.construct_dropdown_entry(None))
        for language in self.model.get_languages():
            languages_menu.append(self.construct_dropdown_entry(re.search("'(.*)'", str(language)).group(1)))
        
        menu_dropdown = MDDropdownMenu(
            caller=self.ids.language_choose,
            items=languages_menu,
            width_mult=5
        )
        menu_dropdown.open()

    def filter(self):
        self.filter_options['last_name'] = self.ids.last_name.text
        self.filter_options['group_number'] = self.ids.group_number.text
        self.filter_options['year'] = 0 if self.ids.year.text == '' \
            else int(self.ids.year.text)
        self.filter_options['all_assignments'] = 0 if self.ids.all_assignments.text == '' \
            else int(self.ids.all_assignments.text)
        self.filter_options['completed_assignments'] = 0 if self.ids.completed_assignments.text == '' \
            else int(self.ids.completed_assignments.text)
        self.filter_options['uncompleted_assignments'] = 0 if self.ids.uncompleted_assignments.text == '' \
            else int(self.ids.uncompleted_assignments.text)
        self.table.row_data = self.model.get(self.filter_options)
        #self.ids.records_amount_label.text = f'Найдено {len(self.table.row_data)} запись(и/ей)'


class DeleteStudentScreen(FindStudentScreen):
    def __init__(self, **kwargs):
        super(DeleteStudentScreen, self).__init__(**kwargs)
        self.dialog = None

    def delete(self):
        self.dialog = MDDialog(
            title=f'Вы действительно хотите удалить {len(self.table.row_data)} запись(и/ей)',
            buttons=[
                MDRectangleFlatButton(
                    text='Нет',
                    on_release=self.close_dialog
                ),
                MDRectangleFlatButton(
                    text='Да',
                    on_release=self.final_delete
                )
            ]
        )
        self.dialog.open()

    def close_dialog(self, obj):
        self.dialog.dismiss()

    def final_delete(self, obj):
        self.dialog.dismiss()
        deleted_records_amount = self.model.delete(self.filter_options)
        self.dialog = MDDialog(
            title=f'Успешно удалена(ы) {deleted_records_amount} запись(и/ей)',
            buttons=[
                MDRectangleFlatButton(
                    text='Хорошо',
                    on_release=self.close_dialog
                ),
            ]
        )
        self.dialog.open()


class StudentsScreenManager(MDScreenManager):
    pass


class StudentsApp(MDApp):

    def build(self):
        self.theme_cls.primary_palette = "Indigo"
        Builder.load_file("view/kv/students.kv")
        Builder.load_file("view/kv/add_student_screen.kv")
        Builder.load_file("view/kv/all_student_screen.kv")
        Builder.load_file("view/kv/find_student_screen.kv")
        Builder.load_file("view/kv/delete_student_screen.kv")
        screen_manager = StudentsScreenManager()
        screen_manager.add_widget(StudentsAppMainScreen(name='main'))
        screen_manager.add_widget(AddStudentScreen(name='add_student'))
        screen_manager.add_widget(AllStudentScreen(name='all_student'))
        screen_manager.add_widget(FindStudentScreen(name='find_student'))
        screen_manager.add_widget(DeleteStudentScreen(name='delete_student'))
        return screen_manager
