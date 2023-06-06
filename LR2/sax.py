import xml.sax as sax
import time_1 as time

file='info.xml'

class TableHandler(sax.ContentHandler):
    def __init__(self):
        super(TableHandler,self).__init__()
        self.union = []
        self.num = "1"
        self.train = [self.num]

    def startElement(self, name, attrs):
        self.current = name
        
    def characters(self,  content):
        if self.current == "number_of_train":
            self.number_of_train = content
        elif self.current == "departure":
            self.departure = content
        elif self.current == "arrival":
            self.arrival = content
        elif self.current == "departure_data_time":
            self.departure_data_time = content
        elif self.current == "arrival_data_time":
            self.arrival_data_time = content

    def endElement(self, name):
        if self.current == 'number_of_train':
            self.train.append(self.number_of_train)
        elif self.current == 'departure':
            self.train.append(self.departure)
        elif self.current == 'arrival':
            self.train.append(self.arrival)
        elif self.current == 'departure_data_time':
            self.train.append(self.departure_data_time)
        elif self.current == 'arrival_data_time':
            self.train.append(self.arrival_data_time)
            travel_time = time.time_of_travel(time.to_date(self.departure_data_time), time.to_date(self.arrival_data_time))
            self.train.append(time.from_time_to_string(travel_time))
        self.current = ''
        if len(self.train) == 7:
            self.union.append(self.train)
            self.num = str(int(self.num)+1)
            self.train=[self.num]
           
def work_parser():   
    handler = TableHandler()
    parser = sax.make_parser()
    parser.setContentHandler(handler)
    parser.parse(file)
    return handler.union