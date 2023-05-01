import xml.etree.ElementTree as ET


def write(lst: list, path):
    data = ET.Element('data')
    for elem in lst:
        student = ET.SubElement(data, 'student')
        name = ET.SubElement(student, 'name')
        name.text = elem[0]
        course = ET.SubElement(student, 'course')
        course.text = str(elem[1])
        group = ET.SubElement(student, 'group')
        group.text = str(elem[2])
        amount_of_works = ET.SubElement(student, 'amount_of_works')
        amount_of_works.text = str(elem[3])
        amount_success_works = ET.SubElement(student, 'amount_success_works')
        amount_success_works.text = str(elem[4])
        language = ET.SubElement(student, 'language')
        language.text = elem[5]
    ET.ElementTree(data).write(path)
