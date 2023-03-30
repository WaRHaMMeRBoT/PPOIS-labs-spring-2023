from kivymd.uix.button import MDFlatButton
from kivymd.uix.dialog import MDDialog
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.textfield import MDTextField


class FilterStudentDialog:
    def __init__(self, controller) -> None:
        self._controller = controller

    def build_dialog(self) -> MDDialog:
        return MDDialog(
            title="Информация",
            type="custom",
            content_cls=MDBoxLayout(
                MDTextField(
                    id='fio',
                    hint_text="ФИО студента",
                    font_size='10',
                    max_text_length=100,
                    helper_text_mode="on_error"
                ),
                MDTextField(
                    id='father_fio',
                    hint_text="ФИО отца",
                    font_size='10',
                    max_text_length=100,
                    helper_text_mode="on_error"
                ),
                MDTextField(
                    id='father_max_salary',
                    hint_text="Заработок отца(верхняя граница)",
                    font_size='10',
                    max_text_length=6,
                    helper_text_mode="on_error"
                ),
                MDTextField(
                    id='father_min_salary',
                    hint_text="Заработок отца(нижняя граница)",
                    font_size='10',
                    max_text_length=6,
                    helper_text_mode="on_error"
                ),
                MDTextField(
                    id='mother_fio',
                    hint_text="ФИО матери",
                    font_size='10',
                    max_text_length=100,
                    helper_text_mode="on_error"
                ),
                MDTextField(
                    id='mother_max_salary',
                    hint_text="Заработок матери(верхняя граница)",
                    font_size='10',
                    max_text_length=6,
                    helper_text_mode="on_error"
                ),
                MDTextField(
                    id='mother_min_salary',
                    hint_text="Заработок матери(нижняя граница)",
                    font_size='10',
                    max_text_length=6,
                    helper_text_mode="on_error"
                ),
                MDTextField(
                    id='number_of_brothers',
                    hint_text="Число братьев",
                    font_size='10',
                    max_text_length=2,
                    helper_text_mode="on_error"
                ),
                MDTextField(
                    id='number_of_sisters',
                    hint_text="Число сестёр",
                    font_size='10',
                    max_text_length=2,
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
                    on_release=lambda event: self._filter_student(),
                ),
            ],
        )

    def _close_dialog(self) -> None:
        self._controller.close_dialog()

    def _filter_student(self) -> None:
        self._controller.filter_student()
