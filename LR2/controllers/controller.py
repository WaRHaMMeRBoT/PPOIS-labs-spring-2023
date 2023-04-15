from typing import List, Set

from kivymd.uix.dialog import MDDialog
from kivymd.uix.screenmanager import MDScreenManager
from kivymd.uix.transition import MDSlideTransition
from kivymd.uix.button import MDFlatButton

from components.dialog import add_dialog, find_dialog, check_adding_dialog
from view import View
from model import Model


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
        data_table.row_data = self.get_student_names()
        self.current_screen.add_widget(data_table)
        self.current_screen.add_widget(self.current_screen.buttons)

    def get_student_names(self) -> List[tuple]:
        student_names: List[tuple] = []
        for person in self.model.persons:
            student: tuple = (
                person.identifier,
                person.studentName,
                person.fatherName,
                person.fatherSalary,
                person.motherName,
                person.motherSalary,
                person.brothersCount,
                person.sistersCount
            )
            student_names.append(student)
        return student_names

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

    def check_adding_dialog(self):
        self.close_dialog(self.dialog)
        self.dialog = check_adding_dialog(self)
        self.dialog.open()

    def find(self, obj):
        self.current_screen.data_table.row_data = self.filtration
        self.close_dialog(self.dialog)

    @property
    def filtration(self) -> List[tuple]:
        filtraded_students: List[tuple] = []

        for person in self.model.persons:
            fields: dict = {
                "studentName": person.studentName,
                "fatherName": person.fatherName,
                "motherName": person.motherName,
                "brothersCount": person.brothersCount,
                "sistersCount": person.sistersCount,
            }
            check = True
            for key in fields:
                if  self.dialog.content_cls.ids[key].text != '' and self.dialog.content_cls.ids[key].text != str(fields[key]):
                    check = False
                    break

                if self.dialog.content_cls.ids.motherSalaryBegin.text != '' and int(person.motherSalary) < int(self.dialog.content_cls.ids.motherSalaryBegin.text):
                    check = False
                    break
                if self.dialog.content_cls.ids.motherSalaryEnd.text != '' and int(person.motherSalary) > int(self.dialog.content_cls.ids.motherSalaryEnd.text):
                    check = False
                    break
                if self.dialog.content_cls.ids.fatherSalaryBegin.text != '' and int(person.fatherSalary) < int(self.dialog.content_cls.ids.fatherSalaryBegin.text):
                    check = False
                    break
                if self.dialog.content_cls.ids.fatherSalaryEnd.text != '' and int(person.fatherSalary) > int(self.dialog.content_cls.ids.fatherSalaryEnd.text):
                    check = False
                    break

            if check:
                filtraded_students.append((
                    person.identifier,
                    person.studentName,
                    person.fatherName,
                    person.fatherSalary,
                    person.motherName,
                    person.motherSalary,
                    person.brothersCount,
                    person.sistersCount
                ))

        return list(set(filtraded_students))

    def close_dialog(self, obj):
        self.dialog.dismiss()

    def transition_to_deleting(self, obj):
        self.current = 'remove'
        self.update()

    def delete_selected_rows(self, obj):
        checked_rows = self.current_screen.data_table.get_row_checks()
        print(checked_rows)
        for row in checked_rows:
            self.model.delete_person(int(row[0]))
        self.update()

    def add_person(self, obj):
        if(
            self.dialog.content_cls.ids.studentName.text == '' and
            self.dialog.content_cls.ids.fatherName.text == '' and
            self.dialog.content_cls.ids.fatherSalary.text == '' and
            self.dialog.content_cls.ids.motherName.text == '' and
            self.dialog.content_cls.ids.motherSalary.text == '' and
            self.dialog.content_cls.ids.brothersCount.text == '' and
            self.dialog.content_cls.ids.sistersCount.text == ''
        ): 
            self.check_adding_dialog()
            return

        person = Model.Person(
            identifier = len(self.model.persons),
            studentName = self.dialog.content_cls.ids.studentName.text,
            fatherName = self.dialog.content_cls.ids.fatherName.text,
            fatherSalary = self.dialog.content_cls.ids.fatherSalary.text,
            motherName = self.dialog.content_cls.ids.motherName.text,
            motherSalary = self.dialog.content_cls.ids.motherSalary.text,
            brothersCount = self.dialog.content_cls.ids.brothersCount.text,
            sistersCount = self.dialog.content_cls.ids.sistersCount.text,
        )
        self.model.add_person(person)
        self.close_dialog(self.dialog)
        self.update()