from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDFlatButton
from kivymd.uix.dialog import MDDialog
from kivymd.uix.textfield import MDTextField
from kivymd.uix.list import OneLineListItem

def add_dialog(controller):
    return MDDialog(
        title="add person:",
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
            MDTextField(
                id="exam_name",
                hint_text="Exams names",
            ),
            MDTextField(
                id="exam_mark",
                hint_text="Exams marks",
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
                on_release=controller.add_person
            )
        ],
    )


def find_dialog(controller):
    return MDDialog(
        title="filter:",
        type="custom",
        content_cls=MDBoxLayout(
            MDTextField(
                id="avg_mark_subject",
                hint_text="Avarage mark upper bound, lower bound, subject",
            ),
            MDTextField(
                id="group",
                hint_text="Group",
            ),
            MDTextField(
                id="mark_subject",
                hint_text="Mark upper bound, lower bound, subject",
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
