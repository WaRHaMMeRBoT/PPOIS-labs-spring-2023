from typing import *

from app.manage_services.parser import DomParser, read_from_xml

class Model:
    def __init__(self) -> None:
        self.__student_list: List[List] = read_from_xml()
    
    def add_to_student_list(self, student_data):
        object = StudentModel()
        object.model_initiation(student_data['name'],
                                student_data['group'],
                                student_data['ill_hours'],
                                student_data['other_reason'],
                                student_data['no_reason'],
                                student_data['all_hours'])
        if object.create_data_for_table() not in self.__student_list:
            self.__student_list.append(object.create_data_for_table())
            self.save()
            self.view.update_table()
        else:
            self.view.error_add_student()
        
    @property
    def student_list(self):
        return self.__student_list
    
    def save(self):
        DomParser(self.__student_list).write_in_xml()
    
    def delete(self, delete_template):
        for i in delete_template:
            del self.__student_list[i]
        self.view.update_table()
        DomParser(self.__student_list).write_in_xml()

    def init_view(self, view):
        self.view = view

class StudentModel:
    def __init__(self) -> None:
        self.student_name: str = None
        self.student_course: int = None
        self.student_group: int = None
        self.amount_all_student_work: int = None
        self.amount_do_student_work: int = None
        self.programming_lang: str = None
        
    def model_initiation(self,
                          name: str,
                          course: int,
                          group: int,
                          amount_all_work: int,
                          amout_do_work: int,
                          programming_lang: str
                          ):
        self.student_name = name
        self.student_course = course
        self.student_group = group
        self.amount_all_student_work = amount_all_work
        self.amount_do_student_work = amout_do_work
        self.programming_lang = programming_lang
    
    def create_data_for_table(self):
        return [
            self.student_name,
            self.student_course,
            self.student_group,
            self.amount_all_student_work,
            self.amount_do_student_work,
            self.programming_lang,
        ]