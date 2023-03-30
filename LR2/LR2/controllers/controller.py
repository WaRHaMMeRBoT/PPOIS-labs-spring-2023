from typing import List, Set

from kivymd.uix.dialog import MDDialog
from kivymd.uix.screenmanager import MDScreenManager
from kivymd.uix.transition import MDSlideTransition

from components.dialog import add_dialog, find_dialog
from view import View
from model import Model


class Controller(MDScreenManager):

    def __init__(self, **kwargs):
        super(Controller, self).__init__(**kwargs)
        self.transition = MDSlideTransition()
        self.dialog: MDDialog = NotImplemented
        self.model = Model()
        self.view = View(controller=self)

    def update(self, data_table=None):
        if not data_table:
            data_table = self.current_screen.data_table
        self.current_screen.remove_widget(data_table)
        self.current_screen.remove_widget(self.current_screen.buttons)
        print(self.current)
        print(self.current_screen)
        if self.current != "marks":
            print('MARKS')
            data_table.row_data = self.get_student_names()
        else:
            data_table.row_data = self.get_student_marks()
        self.current_screen.add_widget(data_table)
        self.current_screen.add_widget(self.current_screen.buttons)

    def transition_to_marks(self, instance_table, instance_row):
        identifier = self.get_screen(self.current).data_table.row_data[instance_row.index // 3][0]
        self.get_screen("marks").data_table.row_data = self.get_student_marks(identifier)
        self.current = 'marks'

    def get_student_names(self) -> List[tuple]:
        student_names: List[tuple] = []
        for i in self.model.persons:
            student: tuple = (i.identifier, i.name, i.group)
            student_names.append(student)
        return student_names

    def get_student_marks(self, identifier) -> List[tuple]:
        student_marks: List[tuple] = []
        index = 1
        for i in self.model.persons:
            if i.identifier == identifier:
                for j in i.exams:
                    exam: tuple = (index, j.name, j.mark)
                    student_marks.append(exam)
                    index += 1
        return student_marks

    def save(self, obj):
        self.model.save()

    def transition_to_menu(self, *args):
        self.current = 'menu'
        self.update()
        
    def transition_to_filtered(self, *args):
        self.current = 'filtered'
        self.filter()
    def add_dialog(self, obj):
        self.dialog = add_dialog(self)
        self.dialog.open()

    def find_dialog(self, obj):
        self.dialog = find_dialog(self)
        self.dialog.open()
        
    def filter(self):
        print('filterereferfe')
        self.dialog = find_dialog(self)
        self.dialog.open()
        return self.filtration

    def transition_to_filtered_deleting(self, *args):
        print('d')
        self.current = 'remove'
        self.current_screen.remove_widget(self.current_screen.data_table)
        self.current_screen.remove_widget(self.current_screen.buttons)

        self.current_screen.data_table.row_data = self.get_filter_student_names()
        self.current_screen.add_widget(self.current_screen.data_table)
        self.current_screen.add_widget(self.get_screen("remove").buttons)

        
        
    def get_filter_student_names(self):
        self.dialog = find_dialog(self)
        self.dialog.open()
        return self.filtration
    
    def find(self, obj):
        print('HERE')
        print(self.current)
        self.current_screen.data_table.row_data = self.filtration
        self.close_dialog(self.dialog)

    @property
    def filtration(self) -> List[tuple]:
        filtraded_students: List[tuple] = []
        try:
            if self.dialog.content_cls.ids.avg_mark_subject.text != "":
                upper_bound, lower_bound, subject_name = self.dialog.content_cls.ids.avg_mark_subject.text.split(',')
                
                for person in self.model.persons:
                    marks = [exam.mark for exam in person.exams]
                    try:
                        person_avg_mark = sum(marks) // len(marks)
                    except ZeroDivisionError:
                        continue
                    subject: bool = len([exam.name for exam in person.exams if subject_name.strip() in exam.name]) != 0
                    if  int(lower_bound.strip()) <= person_avg_mark <= int(upper_bound.strip()) and subject:
                        filtraded_students.append((person.identifier, person.name, person.group))


            if self.dialog.content_cls.ids.group.text != "":
                print(self.dialog.content_cls.ids.group.text)
                for person in self.model.persons:
                    if person.group == int(self.dialog.content_cls.ids.group.text):
                        filtraded_students.append((person.identifier, person.name, person.group))
                    else:
                        if filtraded_students.count((person.identifier, person.name, person.group)) > 0:
                            filtraded_students.remove((person.identifier, person.name, person.group))

            if self.dialog.content_cls.ids.mark_subject.text != "":
                upper_bound, lower_bound, subject_name = self.dialog.content_cls.ids.mark_subject.text.split(',')
                
                for person in self.model.persons:
                    try:
                        exam: Model.Exam = [exam for exam in person.exams if subject_name.strip() in exam.name][0]
                    except IndexError:
                        print('except')
                        continue
                    person_subject_mark = exam.mark
                    if  int(lower_bound.strip()) <= person_subject_mark <= int(upper_bound.strip()):
                        filtraded_students.append((person.identifier, person.name, person.group))
        except ValueError:
            print('global exc')
            return list(set(filtraded_students))
        return list(set(filtraded_students))

    def close_dialog(self, obj):
        self.dialog.dismiss()

    def transition_to_deleting(self, obj):
        self.current = 'remove'
        self.update()

    def delete_selected_rows(self, obj):
        checked_rows = self.current_screen.data_table.get_row_checks()
        print(checked_rows)
        for i in checked_rows:
            self.model.delete_person(int(i[0]))
        self.update()

    def add_person(self, obj):
        name = self.dialog.content_cls.ids.name.text
        id = int(self.dialog.content_cls.ids.id.text)
        group = int(self.dialog.content_cls.ids.group.text)
        exam_name = self.dialog.content_cls.ids.exam_name.text.split()
        exam_mark = list(map(int, self.dialog.content_cls.ids.exam_mark.text.split()))
        print(exam_mark)
        person = Model.Person(name=name, group=group, identifier=id)
        exams = [Model.Exam(name=exam_name, mark=exam_mark) for exam_name, exam_mark in zip(exam_name, exam_mark)]
        person.exams = exams
        self.model.add_person(person)
        self.close_dialog(self.dialog)
        self.update()
