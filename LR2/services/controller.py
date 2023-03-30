from view.view import *
from .students import *


class Controller:
    def __init__(self, repository: Students):
        self.repository = repository
        self.view = View(self)

    def get_root_view(self):
        return self.view.root

    def close_dialog(self):
        self.view.close_dialog()

    def add_student(self):
        data = self.view.dialog.content_cls.ids

        student = Student(data.fio.text,
                          data.father_fio.text,
                          data.father_salary.text,
                          data.mother_fio.text,
                          data.mother_salary.text,
                          data.number_of_brothers.text,
                          data.number_of_sisters.text)

        self.repository.add_to_student_list(student)

        self.view.close_dialog()
        self.view.update_table()

    def delete_student(self):
        data = self.view.dialog.content_cls.ids
        opts = StudentOptions(student_fio=data.fio.text,
                              father_fio=data.father_fio.text,
                              mother_fio=data.mother_fio.text,
                              father_min_salary=data.father_min_salary.text,
                              father_max_salary=data.father_max_salary.text,
                              mother_min_salary=data.mother_min_salary.text,
                              mother_max_salary=data.mother_max_salary.text,
                              number_of_brothers=data.number_of_brothers.text,
                              number_of_sisters=data.number_of_sisters.text
                              )

        self.repository.delete_student(opts)

        self.view.close_dialog()
        self.view.update_table()

    def filter_student(self):
        data = self.view.dialog.content_cls.ids
        opts = StudentOptions(student_fio=data.fio.text,
                              father_fio=data.father_fio.text,
                              mother_fio=data.mother_fio.text,
                              father_min_salary=data.father_min_salary.text,
                              father_max_salary=data.father_max_salary.text,
                              mother_min_salary=data.mother_min_salary.text,
                              mother_max_salary=data.mother_max_salary.text,
                              number_of_brothers=data.number_of_brothers.text,
                              number_of_sisters=data.number_of_sisters.text
                              )
        self.repository.filter_student(opts)

        self.view.close_dialog()
        self.view.update_table()
        self.repository.load_info()

    def get_student(self):
        return self.repository.get_students()

    def open_add_dialog(self):
        self.view.open_add_student_dialog()

    def open_delete_dialog(self):
        self.view.open_delete_student_dialog()

    def open_filter_dialog(self):
        self.view.open_filter_student_dialog()
