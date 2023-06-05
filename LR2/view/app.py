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
        student_info['group_number'] = self.ids.group_number.text
        student_info['illness_hours'] = self.ids.illness_hours.text
        student_info['illness_hours'] \
            = 0 if student_info['illness_hours'] in ('', None) else abs(int(student_info['illness_hours']))
        student_info['other_hours'] = self.ids.other_hours.text
        student_info['other_hours'] \
            = 0 if student_info['other_hours'] in ('', None) else abs(int(student_info['other_hours']))
        student_info['bad_hours'] = self.ids.bad_hours.text
        student_info['bad_hours'] \
            = 0 if student_info['bad_hours'] in ('', None) else abs(int(student_info['bad_hours']))
        self.controller.add(student_info)
        self.flush_text_input()

    def validation_dialog(self, text: str):
        self.dialog = MDDialog(
            title=text,
            buttons=[MDRectangleFlatButton(
                text="Понятно",
                on_release=self.close_dialog
            )
            ]
        )
        self.dialog.open()

    def close_dialog(self, obj):
        self.dialog.dismiss()

    def flush_text_input(self):
        for i in (self.ids.last_name, self.ids.first_name, self.ids.middle_name,
                  self.ids.group_number, self.ids.illness_hours, self.ids.other_hours,
                  self.ids.bad_hours):
            i.text = ''


class AllStudentScreen(MDScreen):
    def __init__(self, **kwargs):
        super(AllStudentScreen, self).__init__(**kwargs)
        self.model = StudentModel()
        self.data = self.model.all()
        self.column_data = [
            ("ID", dp(30)),
            ("Фамилия", dp(30)),
            ("Имя", dp(30)),
            ("Отчество", dp(30)),
            ("Номер группы", dp(30)),
            ("Пропуски по болезни", dp(30)),
            ("Пропуски по другим причинам", dp(30)),
            ("Пропуски по н/у", dp(30)),
            ("Общее число пропусков", dp(30))
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
            ("ID", dp(30)),
            ("Фамилия", dp(30)),
            ("Имя", dp(30)),
            ("Отчество", dp(30)),
            ("Номер группы", dp(30)),
            ("Пропуски по болезни", dp(30)),
            ("Пропуски по другим причинам", dp(30)),
            ("Пропуски по н/у", dp(30)),
            ("Общее число пропусков", dp(30))
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

    def hours_dropdown(self):
        hours_menu = [
            {
                'viewclass': 'OneLineListItem',
                'text': 'Ничего',
                'on_release': lambda x='Ничего': self.hours_type_choose(None)
            },
            {
                'viewclass': 'OneLineListItem',
                'text': 'Часы по болезни',
                'on_release': lambda x='Часы по болезни': self.hours_type_choose('illness_hours')
            },
            {
                'viewclass': 'OneLineListItem',
                'text': 'Часы у/в',
                'on_release': lambda x='Часы у/в': self.hours_type_choose('other_hours')
            },
            {
                'viewclass': 'OneLineListItem',
                'text': 'Часы н/у',
                'on_release': lambda x='Часы н/у': self.hours_type_choose('bad_hours')
            },
            {
                'viewclass': 'OneLineListItem',
                'text': 'Все часы',
                'on_release': lambda x="Все часы": self.hours_type_choose('all_hours')
            }
        ]
        menu_dropdown = MDDropdownMenu(
            caller=self.ids.hours_choose,
            items=hours_menu,
            width_mult=5
        )
        menu_dropdown.open()

    def hours_type_choose(self, hours_type: Optional[str]):
        hours_button_text = {None: 'Выберите тип пропуска',
                             'illness_hours': 'Часы по болезни',
                             'other_hours': 'Часы у/в',
                             'bad_hours': 'Часы н/у',
                             'all_hours': 'Все часы'}
        self.ids.hours_choose.text = hours_button_text[hours_type]
        self.filter_options['hours_type'] = hours_type
        self.filter()

    def filter(self):
        self.filter_options['last_name'] = self.ids.last_name.text
        self.filter_options['group_number'] = self.ids.group_number.text
        self.filter_options['lower_hours_limit'] = 0 if self.ids.lower_hours_limit.text == '' \
            else abs(int(self.ids.lower_hours_limit.text))
        self.filter_options['upper_hours_limit'] = 0 if self.ids.upper_hours_limit.text == '' \
            else abs(int(self.ids.upper_hours_limit.text))
        self.table.row_data = self.model.get(self.filter_options)
        self.ids.records_amount_label.text = f'Найдено {len(self.table.row_data)} запись(и/ей)'


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