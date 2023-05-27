from typing import *
from parsers import DomParser
from parsers import read_from_xml

class Model:
    def __init__(self) -> None:
        self._student_list: List[List] = read_from_xml()
    
    def add_to_student_list(self, student_data):
        object = StudentModel()
        object.model_initiation(student_data['name'], student_data['group'], student_data['ill_hours'],
                                student_data['other_reason'], student_data['no_reason'], student_data['all_hours'])
        if object.create_data_for_table() not in self._student_list:
            self._student_list.append(object.create_data_for_table())
            self.save()
            self.view.update_table()
        else:
            self.view.error_add_student()
        
    @property
    def student_list(self):
        return self._student_list
    
    def save(self):
        DomParser(self._student_list).write_in_xml()
    
    def delete(self, delete_template):
        for i in delete_template:
            del self._student_list[i]
        self.view.update_table()
        DomParser(self._student_list).write_in_xml()

    def init_view(self, view):
        self.view = view

class StudentModel:
    def __init__(self) -> None:
        self.student_name: str = None
        self.student_group: int = None
        self.student_ill_hours: int = None
        self.student_other_reason: int = None
        self.student_no_reason: int = None
        self.student_all_hours: str = None
        
    def model_initiation(self, name, group, ill_hours, other_reason, no_reason, all_hours):
        self.student_name = name
        self.student_group = group
        self.student_ill_hours = ill_hours
        self.student_other_reason = other_reason
        self.student_no_reason = no_reason
        self.student_all_hours = all_hours
    
    def create_data_for_table(self):
        return [self.student_name, self.student_group, self.student_ill_hours,
            self.student_other_reason, self.student_no_reason, self.student_all_hours]