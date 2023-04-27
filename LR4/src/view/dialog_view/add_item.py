from kivymd.uix.button import MDFlatButton, MDRaisedButton
from kivymd.uix.dialog import MDDialog
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.textfield import MDTextField

class AddItemDialog:
    def __init__(self, controller):
        self._controller = controller

    def build_dialog(self):
        return MDDialog(
            title='Новая запись',
            type='custom',
            content_cls=MDBoxLayout(
                MDTextField(
                    id='name',
                    hint_text="Name",
                    font_size='20',
                    max_text_length=100,
                    helper_text_mode="on_error"
                ),
                MDTextField(
                    id='state',
                    hint_text="State",
                    font_size='20',
                    max_text_length=100,
                    helper_text_mode="on_error"
                ),
                MDTextField(
                    id='health',
                    hint_text="Health",
                    font_size='20',
                    max_text_length=100,
                    helper_text_mode="on_error"
                ),

                orientation="vertical",
                spacing="15dp",
                size_hint_y=None,
                height="470dp"
            ),
            buttons=[
                MDFlatButton(
                    text="Exit",
                    font_size='17',
                    font_style='Button',
                    on_release=lambda event: self.close_dialog()
                ),
                MDRaisedButton(
                    text="Add",
                    font_size='17',
                    md_bg_color='gray',
                    font_style='Button',
                    on_release=lambda event: self.add_item()
                ),
            ],
        )

    def close_dialog(self):
        self._controller.close_dialog()

    def add_item(self):
        self._controller.add_item()