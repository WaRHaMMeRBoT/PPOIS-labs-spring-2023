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
        if name == 'teacher': self.result.append({})

    def endElement(self, name):
        if not name == 'teacher': self.result[-1][name] = self.getCharacterData()


def read_xml(path):
    info = MyHandler().parse(path)
    teachers = []
    for i in range(0, len(info)):
        teacher = []
        teacher.append(info[i]['faculty'])
        teacher.append(info[i]['department'])
        teacher.append(info[i]['fio'])
        teacher.append(info[i]['academic_title'])
        teacher.append(info[i]['academic_degree'])
        teacher.append(info[i]['work'])
        teachers.append(teacher)
    return teachers
