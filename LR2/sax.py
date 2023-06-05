import xml.sax as sax

file = 'd.xml'


class TableHandler(sax.ContentHandler):
    def __init__(self):
        super(TableHandler, self).__init__()
        self.union: list = []
        self.num: str = "1"
        self.item: list = [self.num]

    def startElement(self, name, attrs):
        self.current = name

    def characters(self, content):
        if self.current == "fathers_name":
            self.fathers_name = content
        elif self.current == "students_name":
            self.students_name = content
        elif self.current == "fathers_salary":
            self.fathers_salary = content
        elif self.current == "mothers_name":
            self.mothers_name = content
        elif self.current == "mothers_salary":
            self.mothers_salary = content
        elif self.current == "number_of_sisters":
            self.number_of_sisters = content
        elif self.current == "number_of_brothers":
            self.number_of_brothers = content

    def endElement(self, name):
        if self.current == 'fathers_name':
            self.item.append(self.fathers_name)
        elif self.current == 'students_name':
            self.item.append(self.students_name)
        elif self.current == 'fathers_salary':
            self.item.append(self.fathers_salary)
        elif self.current == 'mothers_name':
            self.item.append(self.mothers_name)
        elif self.current == 'mothers_salary':
            self.item.append(self.mothers_salary)
        elif self.current == 'number_of_sisters':
            self.item.append(self.number_of_sisters)
        elif self.current == 'number_of_brothers':
            self.item.append(self.number_of_brothers)
        self.current = ""
        if len(self.item) == 8:
            self.union.append(self.item)
            self.num = str(int(self.num) + 1)
            self.item = [self.num]


def work_parser():
    handler = TableHandler()
    parser = sax.make_parser()
    parser.setContentHandler(handler)
    parser.parse(file)
    return handler.union