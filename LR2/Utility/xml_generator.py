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
            address = np.array(['Minsk', 'Gomel', "Grodno", "Brest", "Vitebsk"])
            date_of_birth = np.array(['12.01.2000', '15.03.2007', '21.10.2002', '20.12.2009', '19.03.2001'])
            date_of_last_visit = np.array(['22.01.2022', '15.03.2023', '21.01.2023', '20.02.2023', '19.03.23'])
            diagnosis = np.array(['Lymphoma', 'Kidney Disease', 'Arthritis', 'Heart Disease'])
            with open(path, 'w') as file:
                dom_writer = XmlWriter(path)
                for _ in range(stock_count):
                    # dictionary filling

                    data_dict["name"] = names.get_full_name()
                    data_dict["address"] = choice(address)
                    data_dict['date_of_birth'] = choice(date_of_birth)
                    data_dict["date_of_visit"] = choice(date_of_last_visit)
                    data_dict["doctor_name"] = names.get_full_name()
                    data_dict['diagnosis'] = choice(diagnosis)
                    dom_writer.create_stock(data_dict)
            # creating xml file using dom parser
            dom_writer.create_xml_file()


def main():
    XMLGenerator.generate_xml_files(files_count=10, stock_count=50)


if __name__ == "__main__":
    main()
