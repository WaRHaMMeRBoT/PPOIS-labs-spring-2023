from kivymd.uix.anchorlayout import MDAnchorLayout
from toolbar import tool_bar
from table import table
from views.add_student_window import add_new_student
from views.filter_student_window import Filter, show_result_of_filter
from views.confirm_delete_window import confirm_delete_window
from views.error_view import error

class View:
    def __init__(self, controller, app_object, get_all_student_function) -> None:
        self.controller = controller
        self.get_all_student_function = get_all_student_function
        self.temp_filter_window = None
        self.add_dialog = add_new_student(controller)
        self.filter_student_dialog = Filter(controller)
        self.table = table(controller, get_all_student_function)
        self.tool_bar = tool_bar(controller, app_object)
        self.base_view = MDAnchorLayout(self.tool_bar, self.table)
        self.confirm_delete_window = None
        self.error_window = None
    
    def open_add_student_window(self):
        self.add_dialog = add_new_student(self.controller)
        self.add_dialog.open()
        
    def update_table(self):
        self.base_view.remove_widget(self.table)
        self.table = table(self.controller,self.get_all_student_function)
        self.base_view.add_widget(self.table)
        
    def open_filter_student_window(self):
        self.filter_student_dialog = Filter(self.controller)
        self.filter_student_dialog.build()
    
    def close_filter_window(self):
        self.filter_student_dialog.close()
        
    def open_filter_result_window(self, get_filter_result):
        self.temp_filter_window = show_result_of_filter(self.controller, get_filter_result)
        self.temp_filter_window.open()
        
    def confirm_delete(self, amount_of_rows, controller):
        self.confirm_delete_window = confirm_delete_window(amount_of_rows, controller)
        self.confirm_delete_window.open()
        
    def error_add_student(self):
        self.error_window = error(self.controller)
        self.error_window.open()
        