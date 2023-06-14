import xml
from tkinter import filedialog
from xml.sax.handler import ContentHandler
import xml.etree.ElementTree as ET

from models.models import Sportsmen


class XMLReader(ContentHandler):

    @staticmethod
    def __reading_parser(filename):
        tree = ET.parse(filename)  # замените file.xml на имя вашего файла
        root = tree.getroot()

        sportsmens = []

        for sportsmen in root.findall('sportsmen'):
            sportsmen_data = {}
            for field in sportsmen:
                sportsmen_data[field.tag] = field.text
            sportsmens.append(sportsmen_data)
        return sportsmens

    @staticmethod
    def reader():
        file_path = filedialog.askopenfilename()
        students = XMLReader.__reading_parser(file_path)
        Sportsmen.set_sportsmens_from_file(students)
