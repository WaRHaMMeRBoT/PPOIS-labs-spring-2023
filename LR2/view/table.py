from kivy.metrics import dp
from kivymd.uix.datatables import MDDataTable
from kivymd.uix.boxlayout import MDBoxLayout


class Table:
    def __init__(self, controller) -> None:
        self._controller = controller

    def build_widget(self) -> MDBoxLayout:
        return MDBoxLayout(
            MDDataTable(
                padding=10,
                elevation=0,
                use_pagination=True,
                pagination_menu_height=330,
                check=True,
                column_data=[
                    ("ФИО пациента", dp(50)),
                    ("Адрес прописки", dp(30)),
                    ("Дата рождения", dp(30)),
                    ("Дата приема", dp(30)),
                    ("ФИО врача", dp(30)),
                    ("Заключение", dp(30)),
                ],
                row_data=self._controller.get_patient()
            ),
            id="table",
        )
