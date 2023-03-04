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
        elif self.current == "course":
            self.course = content
        elif self.current == "group":
            self.group = content
        elif self.current == "all_works":
            self.all_works = content
        elif self.current == "completed_works":
            self.completed_works = content
        elif self.current == 'language':
            self.language = content

    def endElement(self, name) -> None:
        """
        Rewritten function from inherited class which use as end parser element
        :param name:
        :return: None
        """
        if self.current == "name":
            self.stock_data.append(self.name)
        elif self.current == "course":
            self.stock_data.append(self.course)
        elif self.current == "group":
            self.stock_data.append(self.group)
        elif self.current == "all_works":
            self.stock_data.append(self.all_works)
        elif self.current == "completed_works":
            self.stock_data.append(self.completed_works)
        elif self.current == "language":
            self.stock_data.append(self.language)
        if len(self.stock_data) == 6:
            self.table_data.append(tuple(self.stock_data))
            self.stock_data = []

        self.current = ""
