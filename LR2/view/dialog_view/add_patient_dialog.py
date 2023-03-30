from kivymd.uix.button import MDFlatButton, MDRaisedButton
from kivymd.uix.dialog import MDDialog
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.textfield import MDTextField


class AddPatientDialog:
    def __init__(self, controller):
        self._controller = controller

    def build_dialog(self):
        return MDDialog(
            title='Новая запись',
            type='custom',
            content_cls=MDBoxLayout(
                MDTextField(
                    id='patient_fio',
                    hint_text="ФИО пациента",
                    font_size='20',
                    max_text_length=100,
                    helper_text_mode="on_error"
                ),
                MDTextField(
                    id='residence_place',
                    hint_text="Адрес прописки",
                    font_size='20',
                    max_text_length=100,
                    helper_text_mode="on_error"
                ),
                MDTextField(
                    id='birthday',
                    hint_text="Дата рождения",
                    font_size='20',
                    max_text_length=10,
                    helper_text_mode="on_error"
                ),
                MDTextField(
                    id='date_receipt',
                    hint_text="Дата приема",
                    font_size='20',
                    max_text_length=10,
                    helper_text_mode="on_error"
                ),
                MDTextField(
                    id='doctor_fio',
                    hint_text="ФИО врача",
                    font_size='20',
                    max_text_length=100,
                    helper_text_mode="on_error"
                ),
                MDTextField(
                    id='conclusion',
                    hint_text="Заключение",
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
                    text="Отмена",
                    font_size='17',
                    font_style='Button',
                    on_release=lambda event: self.close_dialog()
                ),
                MDRaisedButton(
                    text="Добавить",
                    font_size='17',
                    md_bg_color='gray',
                    font_style='Button',
                    on_release=lambda event: self.add_patient()
                ),
            ],
        )

    def close_dialog(self):
        self._controller.close_dialog()

    def add_patient(self):
        self._controller.add_patient()
