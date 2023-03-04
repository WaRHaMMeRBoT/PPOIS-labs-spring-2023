from random import randint
from parsers.dom_writer import XmlWriter
from numpy.random import choice
import numpy as np
import names


class XMLGenerator:
    def __init__(self):
        pass

    @staticmethod
    def generate_xml_files(files_count: int, stock_count: int) -> None:
       
        for i in range(files_count):
            path = f"../xml/{str(i)}.xml"
            data_dict = {}
            group = np.array(['121701', '121702', '121703'])
            language = np.array(['Python', 'C#', 'C++', 'Java'])
            with open(path, 'w') as file:
                dom_writer = XmlWriter(path)
                for _ in range(stock_count):
                    # dictionary filling
                    data_dict["name"] = names.get_full_name()
                    data_dict["course"] = str(randint(1, 4))
                    data_dict['group'] = choice(group)
                    data_dict["all_works"] = str(randint(5, 10))
                    data_dict["completed_works"] = str(randint(0, 5))
                    data_dict["language"] = choice(language)
                    dom_writer.create_stock(data_dict)
            # creating xml file using dom parser
            dom_writer.create_xml_file()


def main():
    XMLGenerator.generate_xml_files(files_count=10, stock_count=50)


if __name__ == "__main__":
    main()
