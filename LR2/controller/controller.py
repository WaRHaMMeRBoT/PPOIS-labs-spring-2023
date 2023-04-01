from model.model import StudentModel
from .validators import Validator
from kivymd.uix.dialog.dialog import MDDialog
from kivymd.uix.button.button import MDRectangleFlatButton


class Controller:
    def __init__(self):
        self.model = StudentModel()
        self.dialog = None

    def add(self, student_info: dict):
        if not Validator.validate_name(student_info['first_name']):
            self.validation_dialog("Имя должно содержать только буквы и быть длиной не более 100 символов.\n"
                                   "Первая буква должна быть заглавной.")
            return
        if not Validator.validate_name(student_info['last_name']):
            self.validation_dialog("Фамилия должна содержать только буквы и быть длиной не более 100 символов\n"
                                   "Первая буква должна быть заглавной.")
            return
        if not Validator.validate_name(student_info['middle_name']):
            self.validation_dialog("Отчество должно содержать только буквы и быть длиной не более 100 символов\n"
                                   "Первая буква должна быть заглавной.\n")
            return
        if not Validator.validate_year(int(student_info['year'])):
            self.validation_dialog("Номер курса не может быть отрицательным числом или первышать 4")
            return
        if not Validator.validate_group_number(student_info['group_number']):
            self.validation_dialog("Номер группы не должен содержать более 10 символов")
            return
        if not Validator.validate_pos_small_int(int(student_info['all_assignments'])):
            self.validation_dialog("Общее кол-во работ не может быть отрицательным числом или первышать 32767")
            return
        if not Validator.validate_pos_small_int(int(student_info['completed_assignments'])):
            self.validation_dialog("Кол-во выполненных работ не может быть отрицательным числом или первышать 32767")
            return
        if int(student_info['completed_assignments']) > int(student_info['all_assignments']):
            self.validation_dialog("Кол-во выполненных работ не может превышать общее кол-во работ")
            return
        self.model.add(student_info)
        self.validation_dialog("Добавлено!")

    def validation_dialog(self, text: str):
        self.dialog = MDDialog(
            title=text,
            buttons=[MDRectangleFlatButton(text="Принять", on_release=self.close_validation_dialog)]
        )
        self.dialog.open()

    def close_validation_dialog(self, obj):
        self.dialog.dismiss()


