from kivymd.uix.button import MDFlatButton, MDRaisedButton
from kivymd.uix.dialog import MDDialog
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.textfield import MDTextField


class AddStudentDialog:
    def __init__(self, controller):
        self._controller = controller

    def build_dialog(self):
        return MDDialog(
            title='Новая запись',
            type='custom',
            content_cls=MDBoxLayout(
                MDTextField(
                    id='fio',
                    hint_text="ФИО студента",
                    font_size='10',
                    max_text_length=100,
                    helper_text="Поле должно содержать 3 слова",
                    helper_text_mode="on_error"
                ),
                MDTextField(
                    id='father_fio',
                    hint_text="ФИО отца",
                    font_size='10',
                    max_text_length=100,
                    helper_text="Поле должно содержать 3 слова",
                    helper_text_mode="on_error"
                ),
                MDTextField(
                    id='father_salary',
                    hint_text="Заработок отца",
                    font_size='10',
                    max_text_length=6,
                    helper_text="Поле должно содержать число",
                    helper_text_mode="on_error"
                ),
                MDTextField(
                    id='mother_fio',
                    hint_text="ФИО матери",
                    font_size='10',
                    max_text_length=100,
                    helper_text="Поле должно содержать 3 слова",
                    helper_text_mode="on_error"
                ),
                MDTextField(
                    id='mother_salary',
                    hint_text="Заработок матери",
                    font_size='10',
                    max_text_length=6,
                    helper_text="Поле должно содержать число",
                    helper_text_mode="on_error"
                ),
                MDTextField(
                    id='number_of_brothers',
                    hint_text="Число братьев",
                    font_size='10',
                    max_text_length=2,
                    helper_text="Поле должно содержать число",
                    helper_text_mode="on_error"
                ),
                MDTextField(
                    id='number_of_sisters',
                    hint_text="Число сестёр",
                    font_size='10',
                    max_text_length=2,
                    helper_text="Поле должно содержать число",
                    helper_text_mode="on_error"
                ),
                orientation="vertical",
                spacing="15dp",
                size_hint_y=None,
                height="470dp"
            ),
            buttons=[
                MDFlatButton(
                    text="Отмена",
                    font_style='Button',
                    font_size='17',
                    on_release=lambda event: self.close_dialog()
                ),
                MDRaisedButton(
                    text="Добавить",
                    font_size='17',
                    md_bg_color='gray',
                    font_style='Button',
                    on_release=lambda event: self.add_student()
                ),
            ],
        )

    def close_dialog(self):
        self._controller.close_dialog()

    def add_student(self):
        self._controller.add_student()
