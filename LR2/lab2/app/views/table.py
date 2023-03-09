from kivymd.uix.datatables import MDDataTable
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.metrics import dp

def table(controller: object, function_get_student):
    window = MDBoxLayout()
    table = MDDataTable(
            size_hint=(0.9, 0.93),
            use_pagination=True,
            check = True,
            rows_num = 10,
            pagination_menu_height = 300,
            column_data=[
                ("ФИО студента", dp(90)),
                ("Курс", dp(45)),
                ("Группа", dp(60)),
                ("Общее число работ", dp(60)),
                ("Кол-во выполненных работ", dp(60)),
                ("Язык программирования", dp(60)),
            ],
            row_data=function_get_student(),
        
        )
    table.bind(on_check_press = controller.cheked)
    window.add_widget(table)
    return window
    
    
    
    
