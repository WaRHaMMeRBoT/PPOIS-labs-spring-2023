from random import randint
from parsers.dom_writer import XmlWriter
from random import randint
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
            name = np.array(['Tom', "Jerry", "Cooper", "Milo", "Teddy", "Rocky", 'Molly', 'Alex', 'Sanya',
                             'Kenny', 'Marry', 'Alonso', 'Barsik', 'Max', 'Bobby'])
            date_of_birth = np.array(['12.01.2020', '15.03.2017', '21.10.2022', '20.12.2019', '19.03.2023',
                                      '10.11.2020', '15.10.2021'])
            date_of_last_visit = np.array(['22.01.2022', '15.03.2023', '21.01.2023', '20.02.2023', '19.03.2023',
                                           '10.11.2023', '01.08.2023'])
            diagnosis = np.array(['Lymphoma', 'Kidney Disease', 'Arthritis', 'Heart Disease'])
            with open(path, 'w') as file:
                dom_writer = XmlWriter(path)
                for _ in range(stock_count):
                    # dictionary filling
                    data_dict["name"] = choice(name)
                    data_dict["date_of_birth"] = str(randint(1, 30)) + '.' + str(randint(1, 12)) + '.' +\
                                                 str(randint(2015, 2022))
                    data_dict['date_of_last_visit'] = str(randint(1, 30)) + '.' + str(randint(1, 12)) + '.2023'
                    data_dict["veterinary_name"] = names.get_full_name()
                    data_dict["diagnosis"] = choice(diagnosis)
                    dom_writer.create_stock(data_dict)
            # creating xml file using dom parser
            dom_writer.create_xml_file()


def main():
    XMLGenerator.generate_xml_files(files_count=1, stock_count=50)


if __name__ == "__main__":
    main()
