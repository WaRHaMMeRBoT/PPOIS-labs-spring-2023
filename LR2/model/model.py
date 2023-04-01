from db.db import DbConnect
from .db_interaction import StudentInteractor
from .declarative_model import Student


class StudentModel:
    def __init__(self):
        self.interactor = StudentInteractor(DbConnect())
        self.students = list()

    def all(self):
        return self.interactor.all()

    def get(self, filtered_options: dict):
        return self.interactor.get(filtered_options)
    
    def get_languages(self):
        return self.interactor.get_languages()

    def add(self, student_info: dict):
        new_student = Student(
            first_name=student_info['first_name'],
            last_name=student_info['last_name'],
            middle_name=student_info['middle_name'],
            year=student_info['year'],
            group_number=student_info['group_number'],
            all_assignments=student_info['all_assignments'],
            completed_assignments=student_info['completed_assignments'],
            language=student_info['language']
        )
        self.interactor.add(new_student)

    def delete(self, delete_options: dict):
        deleted_notes_count = self.interactor.delete(delete_options)
        return deleted_notes_count
