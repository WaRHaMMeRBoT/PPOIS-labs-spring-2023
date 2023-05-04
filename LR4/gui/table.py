from kivymd.uix.datatables import MDDataTable
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.metrics import dp

def table(controller: object):
    window = MDBoxLayout()
    table = MDDataTable(
            size_hint=(0.9, 0.93),
            use_pagination=True,
            rows_num = 10,
            pagination_menu_height = 300,
            column_data=[
                ('Грядка', dp(60)),
                ('HP', dp(30)),
                ('Вода', dp(30)),
                ('Вредители', dp(60)),
                ('Сорняки', dp(40)),
                ('Засыхает', dp(40)),
                ('Болезни', dp(40)),
                ('Урожай', dp(40))
            ],
            row_data=controller.get_garden(),
        
        )
    window.add_widget(table)
    return window

    
