import xml.sax


class SportsmenHandler(xml.sax.handler.ContentHandler):
    def __init__(self):
        super().__init__()
        self.sportsman_list = []
        self.current = ""
        self.name = ""
        self.line_up = ""
        self.position = ""
        self.achievements = ""
        self.sports_discipline = ""
        self.rank = ""
        self.pos_counter = 0

    def startElement(self, name, attrs):
        self.current = name
        if name == "Sportsman":
            self.pos_counter = attrs["number"]
            self.sportsman_list.append([])

    def characters(self, content):
        if self.current == "name":
            self.name = content
        elif self.current == "line_up":
            self.line_up = content
        elif self.current == "position":
            self.position = content
        elif self.current == "achievements":
            self.achievements = content
        elif self.current == "sports_discipline":
            self.sports_discipline = content
        elif self.current == "rank":
            self.rank = content

    def endElement(self, name):
        if self.current == "name":
            self.sportsman_list[int(self.pos_counter)].append(self.name)
        elif self.current == "line_up":
            self.sportsman_list[int(self.pos_counter)].append(self.line_up)
        elif self.current == "position":
            self.sportsman_list[int(self.pos_counter)].append(self.position)
        elif self.current == "achievements":
            self.sportsman_list[int(self.pos_counter)].append(
                self.achievements)
        elif self.current == "sports_discipline":
            self.sportsman_list[int(self.pos_counter)].append(
                self.sports_discipline)
        elif self.current == "rank":
            self.sportsman_list[int(self.pos_counter)].append(self.rank)

    def get_list_of_sportsman(self) -> list:
        temp_list = [iterator[0:-1] for iterator in self.sportsman_list]
        del temp_list[-1][-1]
        return temp_list


def sax_parser_of_save() -> list:
    obj = xml.sax.make_parser()
    content_handler = SportsmenHandler()
    obj.setContentHandler(content_handler)
    obj.parse('D:\Labs University\PPOIS\LAB2_4SEM\save.xml')
    return content_handler.get_list_of_sportsman()
