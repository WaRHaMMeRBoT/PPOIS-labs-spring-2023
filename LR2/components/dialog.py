from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDFlatButton
from kivymd.uix.dialog import MDDialog
from kivymd.uix.textfield import MDTextField


def add_dialog(controller):
    return MDDialog(
        title="add person:",
        type="custom",

        content_cls=MDBoxLayout(
            MDTextField(
                id="studentName",
                hint_text="ФИо студента",
                required=True,
                helper_text_mode="on_error",
                helper_text="Enter text"
            ),
            MDTextField(
                id="fatherName",
                hint_text="ФИО отца",
            ),
            MDTextField(
                id="fatherSalary",
                hint_text="заработок отца",
            ),
            MDTextField(
                id="motherName",
                hint_text="ФИО матери",
            ),
            MDTextField(
                id="motherSalary",
                hint_text="заработок матери",
            ),
            MDTextField(
                id="brothersCount",
                hint_text="Число братьев",
            ),
             MDTextField(
                id="sistersCount",
                hint_text="Число сестер",
            ),
            orientation="vertical",
            spacing="10dp",
            size_hint_y=None,
            height="480dp",
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
                id="studentName",
                hint_text="ФИО студента",
            ),
            MDTextField(
                id="fatherName",
                hint_text="ФИО отца",
            ),
            MDTextField(
                id="fatherSalaryBegin",
                hint_text="заработок отца от",
            ),
            MDTextField(
                id="fatherSalaryEnd",
                hint_text="заработок отца до",
            ),
            MDTextField(
                id="motherName",
                hint_text="ФИО матери",
            ),
            MDTextField(
                id="motherSalaryBegin",
                hint_text="заработок матери от",
            ),
            MDTextField(
                id="motherSalaryEnd",
                hint_text="заработок матери до",
            ),
            MDTextField(
                id="brothersCount",
                hint_text="количество братьев",
            ),
            MDTextField(
                id="sistersCount",
                hint_text="количество сестер",
            ),
            orientation="vertical",
            spacing="8dp",
            size_hint_y=None,
            height="600dp",
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

def check_adding_dialog(controller):
    return MDDialog(
        title="Empty text fields",
        text="You didn't enter any fields",
        buttons=[
            MDFlatButton(
                text="OK",
                theme_text_color="Custom",
                on_release=controller.close_dialog,
            )
        ],
    )