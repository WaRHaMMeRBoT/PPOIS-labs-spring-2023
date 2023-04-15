import json
import os
from json import load
from typing import List


class Model:

    class Person:
        def __init__(self, identifier: int, studentName: str, fatherName: str, fatherSalary: int, motherName: str, motherSalary: int, brothersCount: int, sistersCount: int):
            self.identifier = identifier
            self.studentName = studentName
            self.fatherName = fatherName
            self.fatherSalary = fatherSalary
            self.motherName = motherName
            self.motherSalary = motherSalary
            self.brothersCount = brothersCount
            self.sistersCount = sistersCount

    def __init__(self):
        self.json_dir = "/test.json"
        self.persons: List[Model.Person] = self.parse_student()

    def save(self):
        students: List = []

        for person in self.persons:
            student: dict = {
                "identifier": person.identifier,
                "studentName": person.studentName,
                "fatherName": person.fatherName,
                "fatherSalary": person.fatherSalary,
                "motherName": person.motherName,
                "motherSalary": person.motherSalary,
                "brothersCount": person.brothersCount,
                "sistersCount": person.sistersCount,
            }
            students.append(student)

        with open(os.path.realpath(os.path.dirname(__file__)) + self.json_dir, 'w') as fcc_file:
            json.dump({"students": students}, fcc_file, indent=4)

    def parse_student(self) -> List[Person]:
        with open(os.path.realpath(os.path.dirname(__file__)) + self.json_dir, 'r') as fcc_file:
            obj = load(fcc_file)
            raw_list: List[Model.Person] = []
            index = 1
            for student in obj["students"]:
                print(student["studentName"])
                person: Model.Person = Model.Person(
                    identifier = student["identifier"],
                    studentName = student["studentName"],
                    fatherName = student["fatherName"],
                    fatherSalary = student["fatherSalary"],
                    motherName = student["motherName"],
                    motherSalary = student["motherSalary"],
                    brothersCount = student["brothersCount"],
                    sistersCount = student["sistersCount"]
                )
                raw_list.append(person)
                index += 1

        return raw_list


    def add_person(self, person: Person):
        self.persons.append(person)

    def get_id_by_identifier(self, identifier: int) -> int:
        index: int = 0
        for i in self.persons:
            if int(i.identifier) == identifier:
                index = self.persons.index(i)
        return index

    def delete_person(self, identifier: int):
        del self.persons[self.get_id_by_identifier(identifier)]
