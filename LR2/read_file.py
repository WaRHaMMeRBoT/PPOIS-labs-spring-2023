import xml.sax


class MyHandler(xml.sax.handler.ContentHandler):
    def __init__(self):
        self.charBuffer = []
        self.result = []

    def getCharacterData(self):
        data = ''.join(self.charBuffer).strip()
        self.charBuffer = []
        return data.strip()

    def parse(self, f):
        xml.sax.parse(f, self)
        return self.result

    def characters(self, content):
        self.charBuffer.append(content)

    def startElement(self, name, attrs):
        if name == 'student': self.result.append({})

    def endElement(self, name):
        if not name == 'student': self.result[-1][name] = self.getCharacterData()


def read_xml(path):
    info = MyHandler().parse(path)
    students = []
    for i in range(0, len(info)):
        student = []
        student.append(info[i]['name'])
        student.append(info[i]['course'])
        student.append(info[i]['group'])
        student.append(info[i]['amount_of_works'])
        student.append(info[i]['amount_success_works'])
        student.append(info[i]['language'])
        students.append(student)
    return students
