import xml
from xml.sax.handler import ContentHandler
import xml.etree.ElementTree as ET
from tkinter import filedialog

from models.models import Sportsmen


class XMLWriter:
    __file: str = ''

    @staticmethod
    def __writing_parser():
        all_sportsmens = Sportsmen.get_all_sportsmens_in_list()

        root = ET.Element("sportsmens")

        for sportsmen in all_sportsmens:
            element_sportsmen = ET.SubElement(root, 'sportsmen')

            element_id = ET.SubElement(element_sportsmen, 'id')
            element_id.text = sportsmen['id']

            element_name = ET.SubElement(element_sportsmen, 'sportsmen_name')
            element_name.text = sportsmen['sportsmen_name']

            element_group = ET.SubElement(element_sportsmen, 'compound')
            element_group.text = sportsmen['compound']

            element_group = ET.SubElement(element_sportsmen, 'position')
            element_group.text = sportsmen['position']

            element_group = ET.SubElement(element_sportsmen, 'tituls')
            element_group.text = sportsmen['tituls']

            element_group = ET.SubElement(element_sportsmen, 'type_of_sport')
            element_group.text = sportsmen['type_of_sport']

            element_group = ET.SubElement(element_sportsmen, 'rank')
            element_group.text = sportsmen['rank']

        tree = ET.ElementTree(root)
        return tree

    @classmethod
    def writer_as(cls):
        filename = filedialog.asksaveasfilename(defaultextension='.xml')
        if not filename:
            return  # пользователь не выбрал файл, просто выходим

        cls.__file = filename

        tree = XMLWriter.__writing_parser()

        tree.write(filename, encoding="utf-8", xml_declaration=True)

    @classmethod
    def writer(cls):
        if cls.__file:
            tree = XMLWriter.__writing_parser()
            tree.write(cls.__file, encoding="utf-8", xml_declaration=True)
        else:
            cls.writer_as()
