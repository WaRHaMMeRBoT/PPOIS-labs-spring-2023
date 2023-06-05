import xml.sax
from person import *


class FootballHandler(xml.sax.ContentHandler):

    def __init__(self):
        self.current_data = ""
        self.birth_date = ""
        self.club = ""
        self.home_city = ""
        self.compound = ""
        self.position = ""
        self.information = []
        self.temp_person = []

    def startElement(self, tag, attributes):
        self.current_data = tag
        if tag == "player":
            full_name = attributes["full_name"]
            self.temp_person.append(full_name)

    def endElement(self, tag):
        if self.current_data == "birth_date":
            self.temp_person.append(self.birth_date)
        elif self.current_data == "club":
            self.temp_person.append(self.club)
        elif self.current_data == "home_city":
            self.temp_person.append(self.home_city)
        elif self.current_data == "compound":
            self.temp_person.append(self.compound)
        elif self.current_data == "position":
            self.temp_person.append(self.position)
        elif len(self.temp_person) > 0:
            tuple_player = (*self.temp_person,)
            self.information.append(tuple_player)
            self.temp_person = []
        self.current_data = ""

    def characters(self, content):
        if self.current_data == "birth_date":
            self.birth_date = content
        elif self.current_data == "club":
            self.club = content
        elif self.current_data == "home_city":
            self.home_city = content
        elif self.current_data == "compound":
            self.compound = content
        elif self.current_data == "position":
            self.position = content
