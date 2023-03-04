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
            Student.group_number,
            Student.illness_hours,
            Student.other_hours,
            Student.bad_hours,
            Student.all_hours
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
            Student.group_number,
            Student.illness_hours,
            Student.other_hours,
            Student.bad_hours,
            Student.all_hours
        )
        if filter_options.get('last_name'):
            students = students.filter(Student.last_name.contains(filter_options['last_name']))
        if filter_options.get('group_number'):
            students = students.filter(Student.group_number.contains(filter_options['group_number']))
        if filter_options.get('upper_hours_limit') and filter_options.get('hours_type'):
            if filter_options['hours_type'] == 'illness_hours':
                students = students.filter(Student.illness_hours <= filter_options['upper_hours_limit'])
            elif filter_options['hours_type'] == 'other_hours':
                students = students.filter(Student.other_hours <= filter_options['upper_hours_limit'])
            elif filter_options['hours_type'] == 'bad_hours':
                students = students.filter(Student.bad_hours <= filter_options['upper_hours_limit'])
            elif filter_options['hours_type'] == 'all_hours':
                students = students.filter(Student.all_hours <= filter_options['upper_hours_limit'])
        if filter_options.get('lower_hours_limit') and filter_options.get('hours_type'):
            if filter_options['hours_type'] == 'illness_hours':
                students = students.filter(Student.illness_hours >= filter_options['lower_hours_limit'])
            elif filter_options['hours_type'] == 'other_hours':
                students = students.filter(Student.other_hours >= filter_options['lower_hours_limit'])
            elif filter_options['hours_type'] == 'bad_hours':
                students = students.filter(Student.bad_hours >= filter_options['lower_hours_limit'])
            elif filter_options['hours_type'] == 'all_hours':
                students = students.filter(Student.all_hours >= filter_options['lower_hours_limit'])
        students = students.all()
        s.close()
        return students

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
