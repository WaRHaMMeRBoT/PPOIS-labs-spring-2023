from kivymd.uix.dialog.dialog import MDDialog
from kivymd.uix.button.button import MDRectangleFlatButton
from typing import Optional


class Validator:
    @staticmethod
    def validate_name(name: Optional[str]) -> bool:
        if name in ('', None):
            return True
        if not 0 < len(name) <= 100:
            return False
        if not name[0].isalpha():
            return False
        for i in name:
            if not (i.isalpha() or i == "-"):
                return False
        if not name == name.capitalize():
            return False
        return True

    @staticmethod
    def validate_group_number(group_number: Optional[str]) -> bool:
        if group_number in ('', None):
            return True
        if not 0 < len(group_number) <= 10:
            return False
        for i in group_number:
            if not i.isdigit():
                return False
        return True

    @staticmethod
    def validate_hours_amount(hours: int) -> bool:
        if hours is None:
            return True
        if hours < 0:
            return False
        if hours > 32000:
            return False
        return True

class Controller:
    def __init__(self):
        # self.model = StudentModel()
        self.dialog = None

    def add(self, student_info: dict):
        if not Validator.validate_name(student_info['product_name']):
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
        # self.model.add(student_info)
        self.validation_dialog("Добавлено!")

    def validation_dialog(self, text: str):
        self.dialog = MDDialog(
            title=text,
            buttons=[MDRectangleFlatButton(text="Понятно", on_release=self.close_validation_dialog)]
        )
        self.dialog.open()

    def close_validation_dialog(self, obj):
        self.dialog.dismiss()