import json
import os
from json import load
from typing import List


class Model:
    class Exam:
        def __init__(self, name: str, mark: int):
            self.name = name
            self.mark = mark

    class Person:
        def __init__(self, name: str, group: int, identifier: int):
            self.name = name
            self.group = group
            self.identifier = identifier
            self.exams: List[Model.Exam] = []

    def __init__(self):
        self.json_dir = "/test.json"
        self.people: List[Model.Person] = self.parse_student()

    def save(self):
        students: List = []

        for i in self.people:
            person: dict = {
                "id": i.identifier,
                "name": i.name,
                "group": i.group,
                "courses": []
            }
            for j in i.exams:
                person["courses"].append({"name": j.name, "mark": j.mark})

            students.append(person)

        with open(os.path.realpath(os.path.dirname(__file__)) + self.json_dir, 'w') as fcc_file:
            json.dump({"students": students}, fcc_file, indent=4)

    def parse_student(self) -> List[Person]:
        with open(os.path.realpath(os.path.dirname(__file__)) + self.json_dir, 'r') as fcc_file:
            obj = load(fcc_file)
            raw_list: List[Model.Person] = []
            index = 1
            for i in obj["students"]:
                print(i["name"])
                person: Model.Person = Model.Person(name=i["name"], group=i["group"], identifier=i["id"])
                person.exams = self.parse_marks(person.identifier)
                raw_list.append(person)
                index += 1

        return raw_list

    def parse_marks(self, identifier) -> List[Exam]:
        with open(os.path.realpath(os.path.dirname(__file__)) + "/" + "test" + '.json', 'r') as fcc_file:
            obj = load(fcc_file)
            raw_list: List = []
            index = 1
            for i in obj["students"]:
                if i["id"] == identifier:
                    for j in i["courses"]:
                        course: Model.Exam = Model.Exam(name=j["name"], mark=j["mark"])
                        raw_list.append(course)
                        index += 1

        return raw_list

    def add_person(self, person: Person):
        self.people.append(person)

    def get_id_by_identifier(self, identifier: int) -> int:
        index: int = 0

        for i in self.people:
            if int(i.identifier) == identifier:
                index = self.people.index(i)

        return index

    def delete_person(self, identifier: int):
        del self.people[self.get_id_by_identifier(identifier)]

    def add_person_marks(self, exam: Exam):
        self.Person.exams.append(exam)