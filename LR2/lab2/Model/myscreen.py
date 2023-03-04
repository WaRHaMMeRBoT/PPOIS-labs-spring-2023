import re

# parsers
from Utility.parsers.dom_writer import XmlWriter
from Utility.parsers.sax_reader import XmlReader
from kivymd.uix.snackbar import Snackbar


class MyScreenModel:

    _not_filtered = []

    def __init__(self, table):
        self.table = table
        self.dialog = None
        self._observers = []

    def add_observer(self, observer):
        self._observers.append(observer)

    def remove_observer(self, observer):
        self._observers.remove(observer)

    def notify_observers(self, data):
        for x in self._observers:
            x.model_is_changed(data)

    def read_from_file(self, file_name: str) -> None:
        """
        Read data from XML file
        :param file_name: XML file name
        :return: None
        """
        try:
            reader = XmlReader()
            reader.parser.setContentHandler(reader)
            reader.parser.parse("xml/" + file_name)
            for data in reader.table_data:
                self.add_new_stock(data)
        except Exception as e:
            print(e)
            pass

    @staticmethod
    def create_empty_file(path):
        try:
            with open(path, 'w'):
                pass
            return True
        except Exception as e:
            return False

    def write_to_file(self, path: str):
        path = "xml/" + path
        if self.create_empty_file(path):
            dom = XmlWriter(path)
            data_dict = {}
            for row in self.table.row_data:
                data_dict["name"] = row[0]
                data_dict["course"] = row[1]
                data_dict["group"] = row[2]
                data_dict["all_works"] = row[3]
                data_dict["completed_works"] = row[4]
                data_dict["language"] = row[5]
                dom.create_stock(data_dict)
            dom.create_xml_file()

    def add_new_stock(self, row):
        try:
            self.table.row_data.insert(
                len(self.table.row_data),
                (
                    row[0],
                    row[1],
                    row[2],
                    row[3],
                    row[4],
                    row[5]
                )
            )
        except ValueError as v:
            Snackbar(text="Data inserting error").open()

    def refresh_stock_in_table(self):
        try:
             self.table.row_data += self._not_filtered
             self._not_filtered = []
        except Exception as e:
             pass

    def select_stock_by_filters(self, filters: list):
        not_filtered_stock = []
        for row in self.table.row_data:
            # first case
            if filters[0]:  # product
                if not (row[0] == filters[0]):
                    not_filtered_stock.append(tuple(row))
                    print(len(not_filtered_stock))
                    continue
            elif filters[1]:  # product
                if not (row[1] == filters[1]):
                    not_filtered_stock.append(tuple(row))
                    print(len(not_filtered_stock))
                    continue
            elif filters[2]:  # product
                if not (row[2] == filters[2]):
                    not_filtered_stock.append(tuple(row))
                    print(len(not_filtered_stock))
                    continue
            elif filters[3]:  # product
                if not (row[3] == filters[3]):
                    not_filtered_stock.append(tuple(row))
                    print(len(not_filtered_stock))
                    continue
            elif filters[4]:  # product
                if not (row[4] == filters[4]):
                    not_filtered_stock.append(tuple(row))
                    print(len(not_filtered_stock))
                    continue

            # second case
            elif filters[5]:  # product
                if not (row[5] == filters[5]):
                    not_filtered_stock.append(tuple(row))
                    print(len(not_filtered_stock))
                    continue
        return not_filtered_stock

    def filter_stock_in_table(self, filters: list):
        self._not_filtered = self.select_stock_by_filters(filters=filters)
        for row in self._not_filtered:
            self.table.row_data.remove(row)

    @staticmethod
    def empty_filters(filters):
        for filter in filters:
            if filter != '':
                return False
        return True

    def delete_stock_from_table(self, filters):
        count_to_delete = 0
        if self.empty_filters(filters):
            return count_to_delete
        unselected_stock = self.select_stock_by_filters(filters=filters)
        for row in self.table.row_data[:]:
            if row not in unselected_stock:
                try:
                    self.table.row_data.remove(row)
                    count_to_delete += 1
                except Exception as e:
                    Snackbar(text="No such stock").open()
                    pass
        return count_to_delete
