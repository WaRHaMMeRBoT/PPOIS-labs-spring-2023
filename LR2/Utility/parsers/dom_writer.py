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

    def create_stock(self, data: dict) -> None:
        
        stock = self.document.createElement("stock")

        for key in data:
            temp_child = self.document.createElement(key)
            stock.appendChild(temp_child)
            node_text = self.document.createTextNode(data[key].strip())
            temp_child.appendChild(node_text)
        self.rows.append(stock)

    def create_xml_file(self) -> None:
        table = self.document.createElement("table")

        for element in self.rows:
            table.appendChild(element)

        self.document.appendChild(table)

        self.document.writexml(open(self.file_name, 'w'),
                               indent="  ",
                               addindent="  ",
                               newl='\n'
                               )
        self.document.unlink()
