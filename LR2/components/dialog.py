from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDFlatButton
from kivymd.uix.dialog import MDDialog
from kivymd.uix.textfield import MDTextField


def add_dialog(controller):
    return MDDialog(
        title="Add a student",
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
                id="group",
                hint_text="Group",
            ),
            MDTextField(
                id="id",
                hint_text="Id",
            ),
            orientation="vertical",
            spacing="12dp",
            size_hint_y=None,
            height="200dp",
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
                on_release=controller.add_person
            )
        ],
    )


def find_dialog(controller):
    return MDDialog(
        title="Filter",
        type="custom",
        content_cls=MDBoxLayout(
            MDTextField(
                id="name",
                hint_text="Name",
            ),
            MDTextField(
                id="group",
                hint_text="Group",
            ),
            MDTextField(
                id="id",
                hint_text="Id",
            ),
            orientation="vertical",
            spacing="12dp",
            size_hint_y=None,
            height="200dp",
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


def add_mark_dialog(controller):
    return MDDialog(
        title="Add mark",
        type="custom",
        content_cls=MDBoxLayout(
            MDTextField(
                id="name",
                hint_text="Name",
            ),
            MDTextField(
                id="mark",
                hint_text="Mark",
            ),
            orientation="vertical",
            spacing="12dp",
            size_hint_y=None,
            height="120dp",
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
                on_release=controller.add_mark
            ),
        ],
    )

def show_gpa_dialog(controller, gpa: float):
    return MDDialog(
        title="Calculate average gpa",
        text="Average gpa = " + str(gpa),
        buttons=[
            MDFlatButton(
                text="OK",
                theme_text_color="Custom",
                on_release=controller.close_dialog,
            )
        ],
    )