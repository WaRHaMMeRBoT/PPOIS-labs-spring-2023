from kivymd.uix.button import MDFlatButton, MDRaisedButton
from kivymd.uix.dialog import MDDialog
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.textfield import MDTextField

from app.views.dialog.handle_dialog_button import handle_add_new_student, hadle_cancel_add_new_student

def add_new_student(controller):
    return MDDialog(
        title = 'Новая запись',
        type = 'custom',
        content_cls = MDBoxLayout(
            MDTextField(
                id = 'name',
                hint_text="ФИО студента",
                font_size='20',
                max_text_length = 100,
                helper_text= "Поле должно содержать миниму 3 слова",
                helper_text_mode= "on_error"
            ),
            MDTextField(
                id = 'course',
                hint_text="Курс",
                font_size='20',
                max_text_length = 1,
                helper_text= "Поле должно содержать 1 цифру",
                helper_text_mode= "on_error"
            ),
            MDTextField(
                id = 'group',
                hint_text="Номер группы",
                font_size='20',
                max_text_length = 6,
                helper_text= "Поле должно содержать 6 цифр",
                helper_text_mode= "on_error"
            ),
            MDTextField(
                id = 'all_work',
                hint_text="Общее число работ",
                font_size='20',
                helper_text= "Поле должно содержать миниму 1 цифру",
                helper_text_mode= "on_error"
            ),
            MDTextField(
                id = 'do_work',
                hint_text="Кол-во выполненных работ",
                font_size='20',
                max_text_length = 100,
                helper_text= "Поле должно содержать миниму 1 цифру",
                helper_text_mode= "on_error"
            ),
            MDTextField(
                id = 'lang',
                hint_text="Язык программирования",
                font_size='20',
                max_text_length = 100,
                helper_text= "Поле должно содержать миниму 1 символ",
                helper_text_mode= "on_error"
            ),
            orientation="vertical",
            spacing="15dp",
            size_hint_y=None,
            height="470dp"
        ),
        buttons=[
            MDFlatButton(
                text="Отмена",
                font_style = 'Button',
                font_size='17',
                on_release = hadle_cancel_add_new_student(controller)
            ),
            MDRaisedButton(
                text="Добавить",
                font_size='17',
                md_bg_color = 'gray',
                font_style = 'Button',
                on_release = handle_add_new_student(controller)
            ),
        ],
    )