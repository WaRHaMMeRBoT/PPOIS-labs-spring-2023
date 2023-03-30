from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDRaisedButton


class Bar:
    def __init__(self, controller) -> None:
        self._controller = controller

    def build_widget(self) -> MDBoxLayout:
        return MDBoxLayout(
            MDRaisedButton(
                text="Добавить",
                size_hint=(1, 1),
                elevation=0,
                on_press=lambda event: self.add_patient()
            ),
            MDRaisedButton(
                text="Удалить",
                size_hint=(1, 1),
                elevation=0,
                on_press=lambda event: self.delete_patient()
            ),
            MDRaisedButton(
                text="Фильтр",
                size_hint=(1, 1),
                elevation=0,
                on_press=lambda event: self.filter_patient()
            ),

            id="bar",
            size=(200, 100),
            size_hint=(1, None),
            spacing=10,
            padding=10
        )

    def add_patient(self) -> None:
        self._controller.open_add_dialog()

    def delete_patient(self) -> None:
        self._controller.open_delete_dialog()

    def filter_patient(self) -> None:
        self._controller.open_filter_dialog()
