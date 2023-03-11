from kivymd.uix.button import MDFlatButton, MDRaisedButton
from kivymd.uix.dialog import MDDialog

from app.views.dialog.handle_dialog_button import handle_cancel_confirm_delete_student, handle_confirm_delete

def confirm_delete_window(amount_of_rows, controller):
    return MDDialog(
        title = f'Удалить {amount_of_rows} записей?',
        buttons=[
            MDFlatButton(
                text="Отмена",
                font_style = 'Button',
                font_size='17',
                on_release = handle_cancel_confirm_delete_student(controller)
            ),
            MDRaisedButton(
                text="Удалить",
                font_size='17',
                md_bg_color = 'gray',
                font_style = 'Button',
                on_release = handle_confirm_delete(controller)
            ),
        ],
    ) 