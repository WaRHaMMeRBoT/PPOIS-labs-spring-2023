import xml.sax as sax

file='d.xml'

class TableHandler(sax.ContentHandler):
    def __init__(self):
        super(TableHandler,self).__init__()
        self.union:list = []
        self.num:str = "1"
        self.item:list=[self.num ]

    def startElement(self, name, attrs):
        self.current = name
        
    def characters(self,  content):
        if self.current == "product":
            self.product = content
        elif self.current == "producer":
            self.producer = content
        elif self.current == "unp":
            self.unp = content
        elif self.current == "number":
            self.number = content
        elif self.current == "address":
            self.address = content

    def endElement(self, name):
        if self.current == 'product':
            self.item.append(self.product)
        elif self.current == 'producer':
            self.item.append(self.producer)
        elif self.current == 'unp':
            self.item.append(self.unp)
        elif self.current == 'address':
            self.item.append(self.address)
        elif self.current == 'number':
            self.item.append(self.number)
        self.current=""
        if len(self.item) == 6:
            self.union.append(self.item)
            self.num = str(int(self.num)+1)
            self.item=[self.num]
           
def work_parser():   
    handler = TableHandler()
    parser = sax.make_parser()
    parser.setContentHandler(handler)
    parser.parse(file)
    return handler.union