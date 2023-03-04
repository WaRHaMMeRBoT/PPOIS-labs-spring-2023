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
                                   "Первая буква должна быть заглавной.")
            return
        if not Validator.validate_group_number(student_info['group_number']):
            self.validation_dialog("Номер группы не должен содержать более 10 символов")
            return
        if not Validator.validate_hours_amount(student_info['illness_hours']):
            self.validation_dialog("Часы пропуска больше или равны 0, но меньше 32000")
            return
        if not Validator.validate_hours_amount(student_info['other_hours']):
            self.validation_dialog("Часы пропуска больше или равны 0, но меньше 32000")
            return
        if not Validator.validate_hours_amount(student_info['bad_hours']):
            self.validation_dialog("Часы пропуска больше или равны 0, но меньше 32000")
            return
        student_info['all_hours']\
            = student_info['illness_hours'] + student_info['other_hours'] + student_info['bad_hours']
        if not Validator.validate_hours_amount(student_info['all_hours']):
            self.validation_dialog("Сумма часов пропусков больше или равна 0, но меньше 32000")
            return
        self.model.add(student_info)
        self.validation_dialog("Добавлено!")

    def validation_dialog(self, text: str):
        self.dialog = MDDialog(
            title=text,
            buttons=[MDRectangleFlatButton(text="Понятно", on_release=self.close_validation_dialog)]
        )
        self.dialog.open()

    def close_validation_dialog(self, obj):
        self.dialog.dismiss()


