import xml.sax
ONE = "1"
SIX = 6
file='inform.xml'

class TableHandler(xml.sax.ContentHandler):
    def __init__(self):
        super(TableHandler,self).__init__()
        self.union:list = []
        self.number:str = ONE
        self.persone:list=[self.number]

    def startElement(self, name, attrs):
        self.current = name
        
    def characters(self,  content):
        if self.current == "fio":
            self.fio = content
        elif self.current == "accountNumber":
            self.accountNumber = content
        elif self.current == "address":
            self.address = content
        elif self.current == "mobileTelefon":
            self.mobileTelefon = content
        elif self.current == "homeTelefon":
            self.homeTelefon = content

    def endElement(self, name):
        if self.current == 'fio':
            self.persone.append(self.fio)
        elif self.current == 'accountNumber':
            self.persone.append(self.accountNumber)
        elif self.current == 'address':
            self.persone.append(self.address)
        elif self.current == 'mobileTelefon':
            self.persone.append(self.mobileTelefon)
        elif self.current == 'homeTelefon':
            self.persone.append(self.homeTelefon)
        self.current=""
        if len(self.persone) == SIX:
            self.union.append(self.persone)
            self.number = str(int(self.number)+1)
            self.persone=[self.number]
           
def Parser():   
    handler = TableHandler()
    parser = xml.sax.make_parser()
    parser.setContentHandler(handler)
    parser.parse(file)

    return handler.union