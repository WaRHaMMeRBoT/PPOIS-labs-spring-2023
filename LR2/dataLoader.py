import json
from tkinter import ttk


def read(_filename):
    filename = _filename
    with open(filename, "r", encoding="utf-8") as file:
        dataBase = json.load(file)
    students = []
    for user in dataBase["users"]:
        info = []
        info.append(user["FullName"])
        info.append(user["groupNumber"])
        for i in range(1, 11):
            info.append(user["Hours"][str(i)])
        info.append(user["Hours"]["general"])
        students.append(tuple(info))
    return students


def write(StudentBase, _filename):
    filename = _filename
    students = {"users": []}
    student = {"FullName": "", "groupNumber": "", "Hours": []}
    hours = {
        "1": "",
        "2": "",
        "3": "",
        "4": "",
        "5": "",
        "6": "",
        "7": "",
        "8": "",
        "9": "",
        "10": "",
        "general": "",
    }
    for person in StudentBase.get_children():
        student["FullName"] = StudentBase.set(person, 0)
        student["groupNumber"] = StudentBase.set(person, 1)
        for i in range(1, 11):
            hours[str(i)] = StudentBase.set(person, i + 1)
        hours["general"] = StudentBase.set(person, 12)
        student["Hours"] = hours.copy()
        temp = student.copy()
        students["users"].append(temp)
    with open(filename, "w", encoding="utf-8") as file:
        file = json.dump(students, file, indent=1, sort_keys=False)
