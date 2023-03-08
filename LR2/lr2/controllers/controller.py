from typing import List

from kivymd.uix.dialog import MDDialog
from kivymd.uix.screenmanager import MDScreenManager
from kivymd.uix.transition import MDSlideTransition

from lr2.components.dialog import add_dialog, find_dialog
from lr2.view import View
from lr2.model import Model


class Controller(MDScreenManager):

    def __init__(self, **kwargs):
        super(Controller, self).__init__(**kwargs)
        self.transition = MDSlideTransition()
        self.dialog: MDDialog = NotImplemented
        self.model = Model()
        self.view = View(controller=self)

    def update(self):
        data_table = self.current_screen.data_table
        self.current_screen.remove_widget(data_table)
        self.current_screen.remove_widget(self.current_screen.buttons)
        if self.current_screen != "marks":
            data_table.row_data = self.get_student_names()
        else:
            data_table.row_data = self.get_student_marks()
        self.current_screen.add_widget(data_table)
        self.current_screen.add_widget(self.current_screen.buttons)

    def transition_to_marks(self, instance_table, instance_row):
        identifier = self.get_screen("menu").data_table.row_data[instance_row.index // 3][0]
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

    def add_dialog(self, obj):
        self.dialog = add_dialog(self)
        self.dialog.open()

    def find_dialog(self, obj):
        self.dialog = find_dialog(self)
        self.dialog.open()

    def find(self, obj):
        self.current_screen.data_table.row_data = self.filtration()
        self.close_dialog(self.dialog)

    def filtration(self) -> List[tuple]:
        filtraded_students: List[tuple] = []
        if self.dialog.content_cls.ids.name.text != "":
            for i in self.model.persons:
                if i.name.__contains__(self.dialog.content_cls.ids.name.text):
                    filtraded_students.append((i.identifier, i.name, i.group))
        else:
            if self.dialog.content_cls.ids.group.text != "":
                for i in self.model.persons:
                    if i.group == int(self.dialog.content_cls.ids.group.text):
                        filtraded_students.append((i.identifier, i.name, i.group))

        return filtraded_students

    def close_dialog(self, obj):
        print(self.dialog.content_cls.ids.name.text)
        print(self.dialog.content_cls.ids.group.text)
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
        id = self.dialog.content_cls.ids.id.text
        group = self.dialog.content_cls.ids.group.text
        person = Model.Person(name=name, group=group, identifier=id)
        self.model.add_person(person)
        self.close_dialog(self.dialog)
        self.update()
