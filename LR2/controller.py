from app.views.view import View
from app.manage_services.model import Model
from app.manage_services.validator import Validator
import time

class Controller:
    def __init__(self, app_object) -> None:
        self.model = Model()
        self.view = View(self, app_object, self.get_student)
        self.model.init_view(self.view)
        self.list_passed_filter_student = []
        self.delete_student_list = []
    
    def get_root_view(self):
        return self.view.base_view
    
    def get_student(self):
        return self.model.student_list
    
    def open_add_window(self):
        self.view.open_add_student_window()
        
    def add_student_in_table(self):
        
        def create_student_data():
            return {
                'name':data_from_add_dialog_window.name.text,
                'group':data_from_add_dialog_window.course.text,
                'ill_hours':data_from_add_dialog_window.group.text,
                'other_reason':data_from_add_dialog_window.all_work.text,
                'no_reason':data_from_add_dialog_window.do_work.text,
                'all_hours':data_from_add_dialog_window.lang.text,
            }
        self.close_add_window()
        
        data_from_add_dialog_window = self.view.add_dialog.content_cls.ids
        validation = Validator(data=create_student_data())
        
        if not validation.validate():
            self.view.error_add_student()
        else:
            self.model.add_to_student_list(student_data=create_student_data())
    
    def close_add_window(self):
        self.view.add_dialog.dismiss()
    
    def close_filter_window(self):
        self.view.close_filter_window()
        
    def close_result_filter_window(self):
        self.list_passed_filter_student = []
        self.view.temp_filter_window.dismiss()
        
    def close_confirm_delete_window(self):
        self.view.confirm_delete_window.dismiss()
    
    def filter_students(self):
        self.view.open_filter_student_window()
        
    def pick_filter_data(self, field):
        set_of_data = set([i[field] for i in self.model.student_list])
        return list(set_of_data)
    
    def get_filter_data(self):            
        data = self.view.filter_student_dialog.get_content()
        return {
                'name': data.name.text,
                'group': data.course.text,
                'ill_hours': data.group.text,
                'other_reason': data.all_work.text,
                'no_reason': data.not_done_work.text,
                'all_hours': data.do_work,
            }
    
    def get_filter_stident_list(self):
        return self.list_passed_filter_student
    
    def pass_filter(self, record, template):
        if template['name']:
            if template['name'] != record[0]:
                return False
        elif template['group']:
            if template['group'] != record[1]:
                return False
        elif template['ill_hours']:
            if template['ill_hours'] != record[2]:
                return False
        elif template['other_reason']:
            if template['other_reason'] != record[3]:
                return False
        elif template['no_reason']:
            if template['no_reason'] != str(int(record[3])-int(record[4])):
                return False
        elif template['all_hours']:
            if template['all_hours'] != record[4]:
                return False
        return True
    
    def filter(self):
        self.view.filter_student_dialog.close()
        template_filter = self.get_filter_data()
                
        for record in self.model.student_list:
            if self.pass_filter(record, template_filter):
                self.list_passed_filter_student.append(record) 
        
        self.view.open_filter_result_window(self.get_filter_stident_list)
    
    def delete_rows(self):
        t1 = time.time()
        self.delete_student_list[:] = [self.model.student_list.index(i) for i in self.delete_student_list]
        self.model.delete(self.delete_student_list)
        self.close_confirm_delete_window()
        self.delete_student_list = []
        if self.view.temp_filter_window:
            self.close_result_filter_window()
        print(time.time()-t1)
     
    def cheked(self, instance, current_row):
        if current_row in self.delete_student_list:
            self.delete_student_list.remove(current_row)
        else:
            self.delete_student_list.append(current_row)
        
    def confirm_delete(self):
        self.view.confirm_delete(len(self.delete_student_list), self)
        
    def close_error_window(self):
        self.view.error_window.dismiss()