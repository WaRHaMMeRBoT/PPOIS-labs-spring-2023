from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDRaisedButton, MDFlatButton
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.textfield import MDTextField
from kivymd.uix.dropdownitem import MDDropDownItem
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.datatables import MDDataTable
from kivy.metrics import dp

from handle_dialog_button import handle_cancel_filter_student, handle_cancel_result_filter_student, handle_filter_student
from toolbar import delete_row_from_table
from table import table

class Filter:
    def __init__(self,controller):
        self.choose_all_hours = ''
        self.choose_ill_hours = ''
        self.set_of_all_hours = all_hours_drop_menu(controller)
        self.set_of_ill_hours = ill_hours_drop_menu(controller)
        self.menu_all = [
            {
                'text' : self.set_of_all_hours[i],
                "viewclass": "OneLineListItem",
                "height": dp(56),
                "on_release": lambda x=self.set_of_all_hours[i]: self.set_all_hours_item(x),
            } for i in range(0,len(self.set_of_all_hours))
        ]
        
        self.menu_ill = [
            {
                'text' : self.set_of_ill_hours[i],
                "viewclass": "OneLineListItem",
                "height": dp(56),
                "on_release": lambda x=self.set_of_ill_hours[i]: self.set_ill_hours_item(x),
            } for i in range(0,len(self.set_of_ill_hours))
        ]
        self.ill_hours = MDDropDownItem()
        self.ill_hours.text = 'Пропуски по болезни'
        self.ill_hours.pos_hint = {'center_x': .5, 'center_y': .5}
        self.all_hours = MDDropDownItem()
        self.all_hours.text = 'Общее число пропусков'
        self.all_hours.pos_hint = {'center_x': .5, 'center_y': .5}
        
        self.all_menu = MDDropdownMenu(
            caller = self.all_hours,
            items=self.menu_all,
            position="auto",
            width_mult=40,
        )
        
        self.ill_menu = MDDropdownMenu(
            caller = self.ill_hours,
            items=self.menu_ill,
            position="auto",
            width_mult=40,
        )
        self.ill_hours.on_release = self.ill_menu.open
        self.all_hours.on_release = self.all_menu.open
        self.dialog = MDDialog(
            title = 'Поиск студентов',
            type = 'custom',
            content_cls = MDBoxLayout(
            MDTextField(
                id = 'name',
                hint_text="ФИО студента",
                font_size='20',
                max_text_length = 100,
                helper_text= "Поле должно содержать миниму 3 слова",
                helper_text_mode= "on_error"
            ),
            MDTextField(
                id = 'group',
                hint_text="Группа",
                font_size='20',
                max_text_length = 6,
                helper_text= "Поле должно содержать как минимум 1 символ, максимум 6",
                helper_text_mode= "on_error"
            ),
            MDTextField(
                id = 'ill_hours',
                hint_text="Число пропусков по болезни",
                font_size='20',
                max_text_length = 6,
                helper_text= "Поле должно содержать 6 цифр",
                helper_text_mode= "on_error"
            ),
            MDTextField(
                id = 'other_reason',
                hint_text="Пропуски по другой причине",
                font_size='20',
                helper_text= "Поле должно содержать миниму 1 цифру",
                helper_text_mode= "on_error"
            ),
            MDTextField(
                id = 'no_reason',
                hint_text="Пропуски без причины",
                font_size='20',
                helper_text= "Поле должно содержать миниму 1 цифру и максимум ",
                helper_text_mode= "on_error"
            ),
            self.ill_hours,
            self.all_hours,
            orientation="vertical",
            spacing="15dp",
            size_hint_y=None,
            height="470dp"
        ), 
            buttons=[
            MDFlatButton(
                text="Отмена",
                font_style = 'Button',
                font_size='17',
                on_release = handle_cancel_filter_student(controller)
            ),
            MDRaisedButton(
                text="Показать",
                font_size='17',
                md_bg_color = 'green',
                font_style = 'Button',
                on_release = handle_filter_student(controller)
            ),
        ],)

    def set_all_hours_item(self, text_item):
        self.all_hours.set_item(text_item)
        self.choose_all_hours = text_item
        self.all_menu.dismiss()
        
    def set_ill_hours_item(self, text_item):
        self.ill_hours.set_item(text_item)
        self.choose_ill_hours = text_item
        self.ill_menu.dismiss()
        
    def build(self):
        self.dialog.open() 
    
    def close(self):
        self.dialog.dismiss()
        self.all_hours.text = 'Общее число пропусков'
        self.ill_hours.text = 'Число пропусков по болезни'
        
    def get_content(self):
        output_data = self.dialog.content_cls.ids
        output_data['all'] = self.choose_all_hours
        output_data['ill'] = self.choose_ill_hours
        self.dialog.dismiss()
        return output_data
        
def all_hours_drop_menu(controller):
    set_of_lang = controller.pick_filter_data(5)
    return set_of_lang

def ill_hours_drop_menu(controller):
    set_of_do_work = controller.pick_filter_data(4)
    return set_of_do_work

def show_result_of_filter(controller, get_filter_result):
    return MDDialog(
        title = 'Результаты поиска',
        type = 'custom',
        size_hint_x = None,
        size_hint_y=None,
        height="800dp",
        width = "1250dp",
        content_cls = MDBoxLayout(
            table(controller, get_filter_result),
            orientation="vertical",
            spacing="15dp",
            size_hint_y=None,
            height="500dp",
        ),
        buttons=[
            MDFlatButton(
                text="Отмена",
                font_style = 'Button',
                font_size='17',
                on_release = handle_cancel_result_filter_student(controller)
            ),
            MDRaisedButton(
                text="Удалить",
                font_size='17',
                md_bg_color = 'red',
                font_style = 'Button',
                on_release = delete_row_from_table(controller)
            ),
        ]
    )
