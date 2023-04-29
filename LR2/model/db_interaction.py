import sqlalchemy as sql
from db.db import DbConnect
from .declarative_model import Student


class StudentInteractor:

    def __init__(self, db_connect: DbConnect) -> None:
        self.db_connect = db_connect
        self.session = db_connect.session()

    def all(self):
        s = self.session()
        students = s.query(
            Student.student_id,
            Student.last_name,
            Student.first_name,
            Student.middle_name,
            Student.year,
            Student.group_number,
            Student.all_assignments,
            Student.completed_assignments,
            Student.language
        ).all()
        s.close()
        return students

    def get(self, filter_options: dict):
        s = self.session()
        students = s.query(
            Student.student_id,
            Student.last_name,
            Student.first_name,
            Student.middle_name,
            Student.year,
            Student.group_number,
            Student.all_assignments,
            Student.completed_assignments,
            Student.language
        )
        if filter_options.get('last_name'):
            students = students.filter(Student.last_name.contains(filter_options['last_name']))
        if filter_options.get('year'):
            students = students.filter(Student.year.contains(filter_options['year']))
        if filter_options.get('group_number'):
            students = students.filter(Student.group_number.contains(filter_options['group_number']))
        if filter_options.get('all_assignments'):
            students = students.filter(Student.all_assignments.contains(filter_options['all_assignments']))
        if filter_options.get('completed_assignments'):
            students = students.filter(Student.completed_assignments.contains(filter_options['completed_assignments']))
        if filter_options.get('uncompleted_assignments'):
            students = students.filter(Student.completed_assignments.contains(Student.all_assignments - filter_options['uncompleted_assignments']))
        if filter_options.get('language'):
            students = students.filter(Student.language.contains(filter_options['language']))
        students = students.all()
        s.close()
        return students
    
    def get_languages(self):
        s = self.session()
        languages = s.query(Student.language)
        languages = languages.distinct().all()
        s.close()
        return languages

    def add(self, student: Student):
        s = self.session()
        s.add(student)
        s.commit()
        s.close()

    def delete(self, delete_options: dict):
        s = self.session()
        students = self.get(delete_options)
        deleted_notes_count = len(students)
        for student in students:
            delete_sql = sql.delete(Student).where(Student.student_id == student.student_id)
            s.execute(delete_sql)
            s.commit()
        s.close()
        return deleted_notes_count
