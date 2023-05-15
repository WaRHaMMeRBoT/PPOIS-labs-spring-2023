import json
from xml.dom import minidom
from bs4 import BeautifulSoup

class Record:
    def __init__(self,_fullName,_rank,_sport,_position,_squad,_titles:list):
        self.fullName=_fullName
        self.rank=_rank
        self.sport=_sport
        self.position =_position
        self.squad = _squad
        self.titles = _titles
    def to_list(self) -> list:
        return self.fullName,self.rank , self.sport, self.position, self.squad, ", ".join(self.titles)
    
class XmlRecordRepository():
    def __init__(self, path):
        self.storage = []
        self.path = path

        with open(self.path) as file:
            data = file.read()

        bs = BeautifulSoup(data, "xml")
        records = bs.find_all("record")

        for record in records:
            self.storage.append(Record(
                record["name"],
                record["rank"],
                record["sport"],
                record["position"],
                record["squad"],
                json.loads(record["titles"].replace("'", '"'))
            ))

    def save_records(self):
        doc = minidom.Document()
        xml = doc.createElement("records")
        doc.appendChild(xml)
        for record in self.storage:
            entry = doc.createElement("record")
            entry.setAttribute("name", record.fullName)
            entry.setAttribute("rank", record.rank)
            entry.setAttribute("sport", record.sport)
            entry.setAttribute("position", record.position)
            entry.setAttribute("squad", record.squad)
            entry.setAttribute("titles", str(record.titles))
            xml.appendChild(entry)

        with open(self.path, 'w') as f:
            f.write(doc.toprettyxml(indent="    "))

    def get_all(self):
            return self.storage

    def add_record(self, record: Record):
        self.storage.append(record)

    def remove_record(self, fullName: str):
        self.storage = list(filter(lambda x: x.fullName != fullName, self.storage))
