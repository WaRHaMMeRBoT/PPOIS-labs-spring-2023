from kivymd.uix.button import MDFlatButton, MDRaisedButton
from kivymd.uix.dialog import MDDialog
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.textfield import MDTextField


class AddEntityDialog:
    def __init__(self, controller):
        self._controller = controller

    def build_dialog(self):
        return MDDialog(
            title='New record',
            type='custom',
            content_cls=MDBoxLayout(
                MDTextField(
                    id='entity',
                    hint_text="Item Name: Rabbit, Wolf, Plant",
                    font_size='10',
                    max_text_length=10,
                    helper_text="on_error",
                    helper_text_mode="on_error"
                ),
                MDTextField(
                    id='pos_x',
                    hint_text="X",
                    font_size='10',
                    max_text_length=2,
                    helper_text="Value should be integer",
                    helper_text_mode="on_error"
                ),
                MDTextField(
                    id='pos_y',
                    hint_text="Y",
                    font_size='10',
                    max_text_length=2,
                    helper_text="Value should be integer",
                    helper_text_mode="on_error"
                ),
                orientation="vertical",
                spacing="15dp",
                size_hint_y=None,
                height="200dp"
            ),
            buttons=[
                MDFlatButton(
                    text="Cancel",
                    font_style='Button',
                    font_size='17',
                    on_release=lambda event: self.close_dialog()
                ),
                MDRaisedButton(
                    text="Add",
                    font_size='17',
                    md_bg_color='gray',
                    font_style='Button',
                    on_release=lambda event: self.add_entity()
                ),
            ],
        )

    def close_dialog(self):
        self._controller.close_dialog()

    def add_entity(self):
        self._controller.add_entity()
