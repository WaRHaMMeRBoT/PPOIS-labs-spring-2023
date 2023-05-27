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
                ("ФИО студента", dp(80)),
                ("Группа", dp(20)),
                ("Пропуски по болезни", dp(40)),
                ("Пропуски по другой причине", dp(40)),
                ("Пропуски без причины", dp(40)),
                ("Общее число пропущенных", dp(40)),
            ],
            row_data=function_get_student(),
        
        )
    table.bind(on_check_press = controller.cheked)
    window.add_widget(table)
    return window
    
    
    
    
