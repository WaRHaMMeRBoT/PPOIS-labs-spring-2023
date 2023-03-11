from xml.dom import minidom
import xml.sax

class DomParser:
    def __init__(self, list_of_student) -> None:
        self.list_of_student = list_of_student
    
    def write_in_xml(self):
        root = minidom.Document()
        xml = root.createElement('students')
        root.appendChild(xml)
        
        for i in range(len(self.list_of_student)):
            number_of_student = root.createElement('student')
            number_of_student.setAttribute('id', str(i))
            student_name = root.createElement('name')
            student_name.appendChild(root.createTextNode(self.list_of_student[i][0]))
            student_course = root.createElement('group')
            student_course.appendChild(root.createTextNode(self.list_of_student[i][1]))
            student_group = root.createElement('ill_hours')
            student_group.appendChild(root.createTextNode(self.list_of_student[i][2]))
            student_all_work = root.createElement('other_reason')
            student_all_work.appendChild(root.createTextNode(self.list_of_student[i][3]))
            student_do_work = root.createElement('no_reason')
            student_do_work.appendChild(root.createTextNode(self.list_of_student[i][4]))
            student_lang = root.createElement('all_hours')
            student_lang.appendChild(root.createTextNode(self.list_of_student[i][5]))
        
            xml.appendChild(number_of_student)
            number_of_student.appendChild(student_name)
            number_of_student.appendChild(student_course)  
            number_of_student.appendChild(student_group)  
            number_of_student.appendChild(student_all_work)  
            number_of_student.appendChild(student_do_work) 
            number_of_student.appendChild(student_lang)
        
        xml_str = root.toprettyxml(indent='\t') 
        self.save(xml_str)
    
    def save(self, xml):
        with open('Test.xml', 'w') as file:
            file.write(xml)

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
            self.course = content
        elif self.current == 'ill_hours':
            self.group = content
        elif self.current == 'other_reason':
            self.all_work = content
        elif self.current == 'no_reason':
            self.do_work = content
        elif self.current == 'all_hours':
            self.lang = content
    
    def endElement(self, name):
        if self.current == 'name':
            self.student_list[int(self.id)].append(self.name)
        elif self.current == 'group':
            self.student_list[int(self.id)].append(self.course)
        elif self.current == 'ill_hours':
            self.student_list[int(self.id)].append(self.group)
        elif self.current == 'other_reason':
            self.student_list[int(self.id)].append(self.all_work)
        elif self.current == 'no_reason':
            self.student_list[int(self.id)].append(self.do_work)
        elif self.current == 'all_hours':
            self.student_list[int(self.id)].append(self.lang)
            
    def get_student_list(self):
        temp_list_screening = [i[0:-1] for i in self.student_list]
        del temp_list_screening[-1][-1]
        return temp_list_screening

def read_from_xml():
    handler = SaxParser()
    parser = xml.sax.make_parser()
    parser.setContentHandler(handler)
    parser.parse('Test.xml')
    return handler.get_student_list()