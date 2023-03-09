from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDRaisedButton, MDFlatButton
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.textfield import MDTextField
from kivymd.uix.dropdownitem import MDDropDownItem
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.datatables import MDDataTable
from kivy.metrics import dp

from app.views.dialog.handle_dialog_button import handle_cancel_filter_student, handle_cancel_result_filter_student, handle_filter_student
from app.views.toolbar import delete_row_from_table
from app.views.table import table

class Filter:
    def __init__(self,controller):
        self.choose_lang = ''
        self.choose_do_work = ''
        self.set_of_lang = lang_drop_menu(controller)
        self.set_of_do_work = do_work_drop_menu(controller)
        self.menu_lang_item = [
            {
                'text' : self.set_of_lang[i],
                "viewclass": "OneLineListItem",
                "height": dp(56),
                "on_release": lambda x=self.set_of_lang[i]: self.set_lang_item(x),
            } for i in range(0,len(self.set_of_lang))
        ]
        
        self.menu_do_work = [
            {
                'text' : self.set_of_do_work[i],
                "viewclass": "OneLineListItem",
                "height": dp(56),
                "on_release": lambda x=self.set_of_do_work[i]: self.set_do_work_item(x),
            } for i in range(0,len(self.set_of_do_work))
        ]
        self.do_work = MDDropDownItem()
        self.do_work.text = 'Кол-во выполненных работ'
        self.do_work.pos_hint = {'center_x': .5, 'center_y': .5}
        self.lang_item = MDDropDownItem()
        self.lang_item.text = 'Язык программирования'
        self.lang_item.pos_hint = {'center_x': .5, 'center_y': .5}
        
        self.lang_menu = MDDropdownMenu(
            caller = self.lang_item,
            items=self.menu_lang_item,
            position="auto",
            width_mult=40,
        )
        
        self.do_work_menu = MDDropdownMenu(
            caller = self.do_work,
            items=self.menu_do_work,
            position="auto",
            width_mult=40,
        )
        self.do_work.on_release = self.do_work_menu.open
        self.lang_item.on_release = self.lang_menu.open
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
                id = 'course',
                hint_text="Курс",
                font_size='20',
                max_text_length = 1,
                helper_text= "Поле должно содержать 1 символ",
                helper_text_mode= "on_error"
            ),
            MDTextField(
                id = 'group',
                hint_text="Номер группы",
                font_size='20',
                max_text_length = 6,
                helper_text= "Поле должно содержать 6 цифр",
                helper_text_mode= "on_error"
            ),
            MDTextField(
                id = 'all_work',
                hint_text="Общее число работ",
                font_size='20',
                helper_text= "Поле должно содержать миниму 1 цифру",
                helper_text_mode= "on_error"
            ),
            MDTextField(
                id = 'not_done_work',
                hint_text="Кол-во невыполненных работ",
                font_size='20',
                helper_text= "Поле должно содержать миниму 1 цифру",
                helper_text_mode= "on_error"
            ),
            self.do_work,
            self.lang_item,
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
                md_bg_color = 'gray',
                font_style = 'Button',
                on_release = handle_filter_student(controller)
            ),
        ],)

    def set_lang_item(self, text_item):
        self.lang_item.set_item(text_item)
        self.choose_lang = text_item
        self.lang_menu.dismiss()
        
    def set_do_work_item(self, text_item):
        self.do_work.set_item(text_item)
        self.choose_do_work = text_item
        self.do_work_menu.dismiss()
        
    def build(self):
        self.dialog.open() 
    
    def close(self):
        self.dialog.dismiss()
        self.lang_item.text = 'Язык_программирования'
        self.do_work.text = 'Кол-во_выполненных_работ'
        
    def get_content(self):
        output_data = self.dialog.content_cls.ids
        output_data['lang'] = self.choose_lang
        output_data['do_work'] = self.choose_do_work
        self.dialog.dismiss()
        return output_data

        
def lang_drop_menu(controller):
    set_of_lang = controller.pick_filter_data(5)
    return set_of_lang

def do_work_drop_menu(controller):
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
                md_bg_color = 'gray',
                font_style = 'Button',
                on_release = delete_row_from_table(controller)
            ),
        ]
    )