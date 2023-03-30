from kivymd.uix.button import MDFlatButton
from kivymd.uix.dialog import MDDialog
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.textfield import MDTextField


class FilterPatientDialog:
    def __init__(self, controller) -> None:
        self._controller = controller

    def build_dialog(self) -> MDDialog:
        return MDDialog(
            title="Информация",
            type="custom",
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
                    max_text_length=10,
                    helper_text_mode="on_error"
                ),
                id="form",
                orientation="vertical",
                spacing="4dp",
                size_hint_y=None,
                height="500dp",
            ),
            buttons=[
                MDFlatButton(
                    text="Отмена",
                    theme_text_color="Custom",
                    on_release=lambda event: self._close_dialog(),
                ),
                MDFlatButton(
                    text="Отфильтровать",
                    theme_text_color="Custom",
                    on_release=lambda event: self._filter_patient(),
                ),
            ],
        )

    def _close_dialog(self) -> None:
        self._controller.close_dialog()

    def _filter_patient(self) -> None:
        self._controller.filter_patient()
