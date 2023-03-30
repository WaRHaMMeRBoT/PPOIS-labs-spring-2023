import dataclasses
from typing import Optional
from .utils import FileUtils


class Students:
    def __init__(self, collection) -> None:
        self.__students = collection

    def to_dict(self):
        data = dict()
        data["students"] = [student.to_dict() for student in self.__students]
        return data

    def add_to_student_list(self, student):
        if student not in self.__students:
            self.__students.append(student)
            self.save()

    def get_students(self):
        students_data = [student.get_student_info() for student in self.__students]
        return students_data

    def load_info(self):
        data = FileUtils.read_from_json("student.json")
        self.__students = State.get_students(data)

    def save(self):
        data = self.to_dict()
        FileUtils.save_in_json(data, "student.json")

    def delete_student(self, opts):
        if opts.student_fio:
            self.delete_by_student_fio(opts.student_fio)
        if opts.father_fio:
            self.delete_by_father_fio(opts.father_fio)
        if opts.father_min_salary or opts.father_max_salary:
            self.delete_by_father_salary(opts.father_min_salary, opts.father_max_salary)
        if opts.mother_fio:
            self.delete_by_mother_fio(opts.mother_fio)
        if opts.mother_min_salary or opts.mother_max_salary:
            self.delete_by_mother_salary(opts.mother_min_salary, opts.mother_max_salary)
        if opts.number_of_brothers:
            self.delete_by_number_of_brothers(opts.number_of_brothers)
        if opts.number_of_sisters:
            self.delete_by_number_of_sisters(opts.number_of_sisters)
        self.save()

    def delete_by_student_fio(self, fio):
        students = []
        for student in self.__students:
            if fio in student.student_fio.split():
                students.append(student)
        for student in students:
            self.__students.remove(student)

    def delete_by_father_fio(self, father_fio):
        students = []
        for student in self.__students:
            if father_fio in student.father_fio.split():
                students.append(student)
        for student in students:
            self.__students.remove(student)

    def delete_by_father_salary(self, father_min_salary=None, father_max_salary=None):
        students = []
        if father_min_salary and father_max_salary:
            for student in self.__students:
                if int(father_max_salary) >= int(student.father_salary) >= int(father_min_salary):
                    students.append(student)
        elif father_min_salary:
            for student in self.__students:
                if int(father_min_salary) <= int(student.father_salary):
                    students.append(student)
        else:
            for student in self.__students:
                if int(father_max_salary) >= int(student.father_salary):
                    students.append(student)
        for student in students:
            self.__students.remove(student)

    def delete_by_mother_fio(self, mother_fio):
        students = []
        for student in self.__students:
            if mother_fio in student.mother_fio.split():
                students.append(student)
        for student in students:
            self.__students.remove(student)

    def delete_by_mother_salary(self, mother_min_salary=None, mother_max_salary=None):
        students = []
        if mother_min_salary and mother_max_salary:
            for student in self.__students:
                if int(mother_max_salary) >= int(student.mother_salary) >= int(mother_min_salary):
                    students.append(student)
        elif mother_min_salary:
            for student in self.__students:
                if int(mother_min_salary) <= int(student.mother_salary):
                    students.append(student)
        else:
            for student in self.__students:
                if int(mother_max_salary) >= int(student.mother_salary):
                    students.append(student)
        for student in students:
            self.__students.remove(student)

    def delete_by_number_of_brothers(self, number_of_brothers):
        students = []
        for student in self.__students:
            if number_of_brothers == student.number_of_brothers:
                students.append(student)
        for student in students:
            self.__students.remove(student)

    def delete_by_number_of_sisters(self, number_of_sisters):
        students = []
        for student in self.__students:
            if number_of_sisters == student.number_of_sisters:
                students.append(student)
        for student in students:
            self.__students.remove(student)

    def filter_student(self, opts):
        self.load_info()
        if opts.student_fio:
            self.filter_by_student_fio(opts.student_fio)
        if opts.father_fio:
            self.filter_by_father_fio(opts.father_fio)
        if opts.father_min_salary or opts.father_max_salary:
            self.filter_by_father_salary(opts.father_min_salary, opts.father_max_salary)
        if opts.mother_fio:
            self.filter_by_mother_fio(opts.mother_fio)
        if opts.mother_min_salary or opts.mother_max_salary:
            self.filter_by_mother_salary(opts.mother_min_salary, opts.mother_max_salary)
        if opts.number_of_brothers:
            self.filter_by_number_of_brothers(opts.number_of_brothers)
        if opts.number_of_sisters:
            self.filter_by_number_of_sisters(opts.number_of_sisters)

    def filter_by_student_fio(self, fio):
        students = []
        for student in self.__students:
            if fio not in student.student_fio.split():
                students.append(student)
        for student in students:
            self.__students.remove(student)

    def filter_by_father_fio(self, father_fio):
        students = []
        for student in self.__students:
            if father_fio not in student.father_fio.split():
                students.append(student)
        for student in students:
            self.__students.remove(student)

    def filter_by_father_salary(self, father_min_salary=None, father_max_salary=None):
        students = []
        if father_min_salary and father_max_salary:
            for student in self.__students:
                if int(father_max_salary) < int(student.father_salary) or int(student.father_salary) < int(father_min_salary):
                    students.append(student)
        elif father_min_salary:
            for student in self.__students:
                if int(father_min_salary) > int(student.father_salary):
                    students.append(student)
        else:
            for student in self.__students:
                if int(father_max_salary) < int(student.father_salary):
                    students.append(student)
        for student in students:
            self.__students.remove(student)

    def filter_by_mother_fio(self, mother_fio):
        students = []
        for student in self.__students:
            if mother_fio not in student.mother_fio.split():
                students.append(student)
        for student in students:
            self.__students.remove(student)

    def filter_by_mother_salary(self, mother_min_salary=None, mother_max_salary=None):
        students = []
        if mother_min_salary and mother_max_salary:
            for student in self.__students:
                if int(mother_max_salary) < int(student.mother_salary) or int(student.mother_salary) < int(mother_min_salary):
                    students.append(student)
        elif mother_min_salary:
            for student in self.__students:
                if int(mother_min_salary) > int(student.mother_salary):
                    students.append(student)
        else:
            for student in self.__students:
                if int(mother_max_salary) < int(student.mother_salary):
                    students.append(student)
        for student in students:
            self.__students.remove(student)

    def filter_by_number_of_brothers(self, number_of_brothers):
        students = []
        for student in self.__students:
            if not number_of_brothers == student.number_of_brothers:
                students.append(student)
        for student in students:
            self.__students.remove(student)

    def filter_by_number_of_sisters(self, number_of_sisters):
        students = []
        for student in self.__students:
            if not number_of_sisters == student.number_of_sisters:
                students.append(student)
        for student in students:
            self.__students.remove(student)


class Student:
    def __init__(self,
                 student_fio=None,
                 father_fio=None,
                 father_salary=None,
                 mother_fio=None,
                 mother_salary=None,
                 number_of_brothers=None,
                 number_of_sisters=None):
        self.student_fio = student_fio
        self.father_fio = father_fio
        self.father_salary = father_salary
        self.mother_fio = mother_fio
        self.mother_salary = mother_salary
        self.number_of_brothers = number_of_brothers
        self.number_of_sisters = number_of_sisters

    def to_dict(self):
        data = dict()
        data['fio'] = self.student_fio
        data['father_fio'] = self.father_fio
        data['father_salary'] = self.father_salary
        data['mother_fio'] = self.mother_fio
        data['mother_salary'] = self.mother_salary
        data['number_of_brothers'] = self.number_of_brothers
        data['number_of_sisters'] = self.number_of_sisters
        return data

    def get_student_info(self):
        student_info = self.to_dict()
        return tuple(student_info.values())


@dataclasses.dataclass
class StudentOptions:
    student_fio: Optional[str]
    father_fio: Optional[str]
    mother_fio: Optional[str]
    father_min_salary: Optional[float]
    father_max_salary: Optional[float]
    mother_min_salary: Optional[float]
    mother_max_salary: Optional[float]
    number_of_brothers: Optional[int]
    number_of_sisters: Optional[int]


class State:
    @staticmethod
    def get_students(data: dict):
        students = []
        for student in data["students"]:
            student_data = Student(*student.values())
            students.append(student_data)
        return students
