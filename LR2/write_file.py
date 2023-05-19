import xml.etree.ElementTree as ET


def write(lst: list, path):
    data = ET.Element('data')
    for elem in lst:
        teacher = ET.SubElement(data, 'teacher')
        faculty = ET.SubElement(teacher, 'faculty')
        faculty.text = elem[0]
        department = ET.SubElement(teacher, 'department')
        department.text = str(elem[1])
        fio = ET.SubElement(teacher, 'fio')
        fio.text = str(elem[2])
        academic_title = ET.SubElement(teacher, 'academic_title')
        academic_title.text = str(elem[3])
        academic_degree = ET.SubElement(teacher, 'academic_degree')
        academic_degree.text = str(elem[4])
        work = ET.SubElement(teacher, 'work')
        work.text = elem[5]
    ET.ElementTree(data).write(path)
