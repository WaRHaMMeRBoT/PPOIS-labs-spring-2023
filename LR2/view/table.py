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
                    ("ФИО студента", dp(50)),
                    ("ФИО отца", dp(50)),
                    ("Заработок отца", dp(30)),
                    ("ФИО матери", dp(50)),
                    ("Заработок матери", dp(20)),
                    ("Число братьев", dp(20)),
                    ("Число сестёр", dp(20))
                ],
                row_data=self._controller.get_student()
            ),
            id="table",
        )
