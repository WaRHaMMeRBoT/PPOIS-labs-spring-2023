import xml.sax as sax


class XmlReader(sax.ContentHandler):
    def __init__(self) -> None:
        super().__init__()
        self.table_data = []
        self.stock_data = []
        self.parser = sax.make_parser()

    def startElement(self, name, attrs):
        """
        Rewritten function from inherited class which use as start parser element
        :param name: current element name
        :param attrs: attributes (don't used)
        :return: None
        """
        self.current = name
        if name == "stock":
            pass

    def characters(self, content) -> None:
        """
        Also rewritten function that perform getting data characters
        :param content: character
        :return: None
        """
        if self.current == "name":
            self.name = content
        elif self.current == "address":
            self.address = content
        elif self.current == "date_of_birth":
            self.date_of_birth = content
        elif self.current == "date_of_visit":
            self.date_of_visit = content
        elif self.current == "doctor_name":
            self.doctor_name = content
        elif self.current == 'diagnosis':
            self.diagnosis = content

    def endElement(self, name) -> None:
        """
        Rewritten function from inherited class which use as end parser element
        :param name:
        :return: None
        """
        if self.current == "name":
            self.stock_data.append(self.name)
        elif self.current == "address":
            self.stock_data.append(self.address)
        elif self.current == "date_of_birth":
            self.stock_data.append(self.date_of_birth)
        elif self.current == "date_of_visit":
            self.stock_data.append(self.date_of_visit)
        elif self.current == "doctor_name":
            self.stock_data.append(self.doctor_name)
        elif self.current == "diagnosis":
            self.stock_data.append(self.diagnosis)
        if len(self.stock_data) == 6:
            self.table_data.append(tuple(self.stock_data))
            self.stock_data = []

        self.current = ""
