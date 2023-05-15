from random import randint
from parsers.dom_writer import XmlWriter
from numpy.random import choice
import numpy as np
import names


class XMLGenerator:
    def __init__(self):
        pass

    @staticmethod
    def generate_xml_files(files_count: int, sportsman_count: int) -> None:
        """
        Generate N files with each of which has one number of players
        :param files_count: amount of files
        :param sportsman_count: amount of student in each file
        :return: None
        """
        for i in range(files_count):
            path = f"../xml/{str(i)}.xml"
            data_dict = {}
            line_up_values = np.array(['main', 'reserve', 'n/a'])
            sick_values = np.array(['goalkeeper', 'forward', 'defender', 'midfielder'])
            rank_values = np.array(['1st', '2nd', '3d', 'CMS', 'master'])
            sport_type_values = np.array(['football'])
            with open(path, 'w') as file:
                dom_writer = XmlWriter(path)
                for _ in range(sportsman_count):
                    # dictionary filling
                    data_dict["name"] = names.get_full_name()
                    data_dict["line_up"] = choice(line_up_values)
                    data_dict["position"] = choice(sick_values)
                    data_dict["titles"] = str(randint(0, 150))
                    data_dict["sport_type"] = choice(sport_type_values)
                    data_dict["rank"] = choice(rank_values)
                    # adding record for each sportsman
                    dom_writer.create_sportsman(data_dict)
            # creating xml file using dom parser
            dom_writer.create_xml_file()


def main():
    # creating 10 files with 50 sportsmans in each other
    XMLGenerator.generate_xml_files(files_count=10, sportsman_count=50)


if __name__ == "__main__":
    main()
