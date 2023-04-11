import xml.dom.minidom as minidom


class XmlWriter:
    def __init__(self, file_name: str) -> None:
        """
        DOM parser for writing XML files
        :param file_name: name of the file
        """
        self.file_name = file_name
        self.document = minidom.Document()
        self.rows = []

    def create_sportsman(self, data: dict) -> None:
        """
        Creating sportsman element based on input data
        :param data: dictionary with ['name', 'line_up',
                                      'position', 'titles',
                                      'sport_type', 'rank'] keys
        :return: None
        """
        sportsman = self.document.createElement("sportsman")

        for key in data:
            temp_child = self.document.createElement(key)
            sportsman.appendChild(temp_child)
            node_text = self.document.createTextNode(data[key].strip())
            temp_child.appendChild(node_text)
        self.rows.append(sportsman)

    def create_xml_file(self) -> None:
        table = self.document.createElement("table")

        for student in self.rows:
            table.appendChild(student)

        self.document.appendChild(table)

        self.document.writexml(open(self.file_name, 'w'),
                               indent="  ",
                               addindent="  ",
                               newl='\n'
                               )
        self.document.unlink()
