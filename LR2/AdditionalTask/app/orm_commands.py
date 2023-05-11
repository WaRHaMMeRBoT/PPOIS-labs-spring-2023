from app.db import session_scope
import sqlalchemy as db
from app.db import engine
from sqlalchemy.exc import NoResultFound
from app.models import Student

students = db.Table("students", db.MetaData(), autoload_replace=True, autoload_with=engine)


def get_students():
    query = db.select(students)
    with session_scope() as session:
        result_list = []
        all_students = session.execute(query)
        for student in all_students:
            user = {
                "full_name": student[1],
                "course": student[2],
                "works_number": student[3],
                "completed_works": student[4],
                "programming_language": student[5]
            }
            result_list.append(user)
        return result_list


def get_student_by_id(id: int):
    query = db.select(students).where(students.c.id == id).fetch(count=1)
    try:
        with session_scope() as session:
            info = session.execute(query).one()
            user = {
                "id": info[0],
                "full_name": info[1],
                "course": info[2],
                "works_number": info[3],
                "completed_works": info[4],
                "programming_language": info[5]
            }
            return user
    except NoResultFound:
        return None


def get_student_by_name(full_name: str):
    query = db.select(students).where(students.c.full_name == full_name).fetch(count=1)
    try:
        with session_scope() as session:
            info = session.execute(query).one()
            user = {
                "id": info[0],
                "full_name": info[1],
                "course": info[2],
                "works_number": info[3],
                "completed_works": info[4],
                "programming_language": info[5]
            }
            return user
    except NoResultFound:
        return None


def add_new_student(student):
    new_student = Student(full_name=student["full_name"],
                          course=student["course"],
                          works_number=student["works_number"],
                          completed_works=student["completed_works"],
                          programming_language=student["programming_language"]
                          )
    with session_scope() as session:
        session.add(new_student)


def delete_student_by_id(id: int):
    with session_scope() as session:
        student = session.get(Student, id)
        if not student:
            raise NoResultFound("Student with that id does not exist")
        session.delete(student)
