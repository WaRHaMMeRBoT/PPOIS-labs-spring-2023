from typing import List

from kivymd.uix.datatables import MDDataTable


def Table(column_data: List[tuple], row_data: List[tuple], check):
    return MDDataTable(
        pos_hint={'center_x': 0.5, 'center_y': 0.5},
        size_hint=(1, 1),
        check=check,
        use_pagination=True,
        rows_num=7,
        elevation=0,
        column_data=column_data,
        row_data=row_data
    )