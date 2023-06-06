import xml.sax as sax

file='info.xml'

class TableHandler(sax.ContentHandler):
    def __init__(self):
        super(TableHandler,self).__init__()
        self.union = []
        self.num = "1"
        self.tournament = [self.num]

    def startElement(self, name, attrs):
        self.current = name
        
    def characters(self,  content):
        if self.current == "tournaname":
            self.tournaname = content
        elif self.current == "date":
            self.date = content
        elif self.current == "sport":
            self.sport = content
        elif self.current == "winner":
            self.winner = content
        elif self.current == "prize":
            self.prize = content

    def endElement(self, name):
        if self.current == 'tournaname':
            self.tournament.append(self.tournaname)
        elif self.current == 'date':
            self.tournament.append(self.date)
        elif self.current == 'sport':
            self.tournament.append(self.sport)
        elif self.current == 'winner':
            self.tournament.append(self.winner)
        elif self.current == 'prize':
            self.tournament.append(self.prize)
            self.tournament.append(str(round(float(self.prize)*0.6)))
        self.current = ''
        if len(self.tournament) == 7:
            self.union.append(self.tournament)
            self.num = str(int(self.num)+1)
            self.tournament=[self.num]
           
def work_parser():   
    handler = TableHandler()
    parser = sax.make_parser()
    parser.setContentHandler(handler)
    parser.parse(file)
    return handler.union