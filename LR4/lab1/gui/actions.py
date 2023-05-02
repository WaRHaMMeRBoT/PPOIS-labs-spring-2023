from kivymd.uix.button import MDFlatButton, MDRaisedButton
from kivymd.uix.dialog import MDDialog
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.textfield import MDTextField

from gui.handle_dialog_button import handle_action_window, hadle_cancel_action_window

def action_dialog(controller):
    return MDDialog(
        title = 'Новая запись',
        type = 'custom',
        content_cls = MDBoxLayout(
            MDTextField(
                id = 'actions',
                hint_text="Действие",
                font_size='20',
                max_text_length = 100,
                helper_text= "Поле должно содержать миниму 1 слова",
                helper_text_mode= "on_error"
            ),
            MDTextField(
                id = 'gardenbed',
                hint_text="Номер грядки",
                font_size='20',
                max_text_length = 2,
                helper_text= "Поле должно содержать 1 число",
                helper_text_mode= "on_error"
            ),
            orientation="vertical",
            spacing="15dp",
            size_hint_y=None,
            height="150dp"
        ),
        buttons=[
            MDFlatButton(
                text="Отмена",
                font_style = 'Button',
                font_size='17',
                on_release = hadle_cancel_action_window(controller)
            ),
            MDRaisedButton(
                text="Действие",
                font_size='17',
                md_bg_color = 'gray',
                font_style = 'Button',
                on_release = handle_action_window(controller)
            ),
        ],
    )