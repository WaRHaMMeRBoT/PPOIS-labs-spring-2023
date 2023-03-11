from kivymd.uix.button import MDFlatButton
from kivymd.uix.dialog import MDDialog

from app.views.dialog.handle_dialog_button import handle_error_add_student

def error(controller):
    return MDDialog(
        text = 'Проверьте корректность данных!',
        buttons = [
            MDFlatButton(
                text="ОК",
                font_style = 'Button',
                font_size='17',
                on_release = handle_error_add_student(controller)
            )
        ]
    )