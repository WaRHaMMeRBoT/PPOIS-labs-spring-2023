from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDFlatButton
from kivymd.uix.dialog import MDDialog
from kivymd.uix.textfield import MDTextField


def add_dialog(controller):
    return MDDialog(
        title="Add Book:",
        type="custom",

        content_cls=MDBoxLayout(
            MDTextField(
                id="book_name",
                hint_text="Book name",
                required=True,
                helper_text_mode="on_error",
                # helper_text="Enter text"
            ),
            MDTextField(
                id="author",
                hint_text="Author",
            ),
            MDTextField(
                id="publishing_house",
                hint_text="Publishing house",
            ),
            MDTextField(
                id="volumes",
                hint_text="Volumes",
            ),
            MDTextField(
                id="circulation",
                hint_text="Circulation",
            ),
            orientation="vertical",
            spacing="12dp",
            size_hint_y=None,
            height="380dp",
        ),

        buttons=[
            MDFlatButton(
                text="CANCEL",
                theme_text_color="Custom",
                on_release=controller.close_dialog,
            ),
            MDFlatButton(
                text="OK",
                theme_text_color="Custom",
                on_release=controller.add_book
            )
        ],
    )


def find_dialog(controller):
    return MDDialog(
        title="Filter:",
        type="custom",
        content_cls=MDBoxLayout(
            MDTextField(
                id="book_name",
                hint_text="Book name",
            ),
            MDTextField(
                id="author",
                hint_text="Author",
            ),
            MDTextField(
                id="publishing_house",
                hint_text="Publishing house",
            ),
            MDTextField(
                id="circulation",
                hint_text="Circulation",
            ),
            MDTextField(
                id="total_volumes",
                hint_text="Total volumes",
            ),
            orientation="vertical",
            spacing="15dp",
            size_hint_y=None,
            height="380dp",
        ),
        buttons=[
            MDFlatButton(
                text="CANCEL",
                theme_text_color="Custom",
                on_release=controller.close_dialog,
            ),
            MDFlatButton(
                text="OK",
                theme_text_color="Custom",
                on_release=controller.find
            ),
        ],
    )
