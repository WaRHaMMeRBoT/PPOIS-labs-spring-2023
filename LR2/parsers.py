from xml.dom import minidom
import xml.sax

class DomParser:
    def __init__(self, list_of_student) -> None:
        self.list_of_student = list_of_student
    
    def write_in_xml(self):
        root = minidom.Document()
        xml = root.createElement('students')
        root.appendChild(xml)
        
        for i in range(0, len(self.list_of_student), 1):
            number_of_student = root.createElement('student')
            number_of_student.setAttribute('id', str(i))
            student_name = root.createElement('name')
            student_name.appendChild(root.createTextNode(self.list_of_student[i][0]))
            student_group = root.createElement('group')
            student_group.appendChild(root.createTextNode(self.list_of_student[i][1]))
            student_ill_hours = root.createElement('ill_hours')
            student_ill_hours.appendChild(root.createTextNode(self.list_of_student[i][2]))
            student_other_reason = root.createElement('other_reason')
            student_other_reason.appendChild(root.createTextNode(self.list_of_student[i][3]))
            student_no_reason = root.createElement('no_reason')
            student_no_reason.appendChild(root.createTextNode(self.list_of_student[i][4]))
            student_all_hours = root.createElement('all_hours')
            student_all_hours.appendChild(root.createTextNode(self.list_of_student[i][5]))
        
            xml.appendChild(number_of_student)
            number_of_student.appendChild(student_name)
            number_of_student.appendChild(student_group)  
            number_of_student.appendChild(student_ill_hours)  
            number_of_student.appendChild(student_other_reason)  
            number_of_student.appendChild(student_no_reason) 
            number_of_student.appendChild(student_all_hours)

        with open('students.xml', 'w') as file:
            file.write(root.toprettyxml())

class SaxParser(xml.sax.ContentHandler):
    def __init__(self) -> None:
        super().__init__()
        self.student_list = []
    
    def startElement(self, name, attrs):
        self.current = name
        if name == 'student':
            self.id = attrs['id']
            self.student_list.append([])
        
    def characters(self, content):
        if self.current == 'name':
            self.name = content
        elif self.current == 'group':
            self.group = content
        elif self.current == 'ill_hours':
            self.ill_hours = content
        elif self.current == 'other_reason':
            self.other_reason = content
        elif self.current == 'no_reason':
            self.no_reason = content
        elif self.current == 'all_hours':
            self.all_hours = content
    
    def endElement(self, name):
        if self.current == 'name':
            self.student_list[int(self.id)].append(self.name)
        elif self.current == 'group':
            self.student_list[int(self.id)].append(self.group)
        elif self.current == 'ill_hours':
            self.student_list[int(self.id)].append(self.ill_hours)
        elif self.current == 'other_reason':
            self.student_list[int(self.id)].append(self.other_reason)
        elif self.current == 'no_reason':
            self.student_list[int(self.id)].append(self.no_reason)
        elif self.current == 'all_hours':
            self.student_list[int(self.id)].append(self.all_hours)
            
    def get_student_list(self):
        return [i[0:-1] for i in self.student_list]

def read_from_xml():
    handler = SaxParser()
    parser = xml.sax.make_parser()
    parser.setContentHandler(handler)
    parser.parse('students.xml')
    return handler.get_student_list()