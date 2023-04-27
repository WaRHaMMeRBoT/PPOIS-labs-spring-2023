from kivy.metrics import dp
from kivymd.uix.datatables import MDDataTable
from kivymd.uix.boxlayout import MDBoxLayout

class Table:
    def __init__(self, controller):
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
                    ("Name", dp(50)),
                    ("State", dp(50)),
                    ("Health", dp(50)),
                ],
                row_data=self._controller.get_items()
            ),
            id="table",
        )