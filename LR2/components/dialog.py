from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDFlatButton
from kivymd.uix.dialog import MDDialog
from kivymd.uix.textfield import MDTextField
from kivy.uix.scrollview import ScrollView


def add_dialog(controller):
    return MDDialog(
        title="add:",
        type="custom",
        content_cls=MDBoxLayout(
            MDTextField(
                id="name",
                hint_text="Name",
                required=True,
                helper_text_mode="on_error",
                helper_text="Enter text"
            ),
            MDTextField(
                id="author",
                hint_text="Author",
            ),
            MDTextField(
                id="publishing_house",
                hint_text="Publishing_house",
            ),
            MDTextField(
                id="number_of_volumes",
                hint_text="Number_of_volumes",
            ),
            MDTextField(
                id="circulation",
                hint_text="Circulation",
            ),
            orientation="vertical",
            spacing="12dp",
            size_hint_y=None,
            height="400dp",
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
        title="Find",
        type="custom",
        content_cls=MDBoxLayout(
            ScrollView(do_scroll_x=False),
            MDTextField(
                id="name",
                hint_text="Name",
                required=True,
                helper_text_mode="on_error",
                helper_text="Enter text"
            ),
            MDTextField(
                id="author",
                hint_text="Author",
            ),
            MDTextField(
                id="publishing_house",
                hint_text="Publishing_house",
            ),
            MDTextField(
                id="max_number_of_volumes",
                hint_text="Max_number_of_volumes",
            ),
            MDTextField(
                id="min_number_of_volumes",
                hint_text="Min_number_of_volumes",
            ),
            MDTextField(
                id="max_total_volumes",
                hint_text="Max_total_volumes",
            ),
            MDTextField(
                id="min_total_volumes",
                hint_text="Min_total_volumes",
            ),
            MDTextField(
                id="max_circulation",
                hint_text="Max_circulation",
            ),
            MDTextField(
                id="min_circulation",
                hint_text="Min_circulation",
            ),
            orientation="vertical",
            spacing="0dp",
            size_hint_y=None,
            height="530dp",
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