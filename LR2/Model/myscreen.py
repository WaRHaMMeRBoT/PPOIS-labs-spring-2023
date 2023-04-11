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
                self.add_new_sportsman(data)
        except Exception as e:
            print(e)
            exit()
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
                data_dict["line_up"] = row[1]
                data_dict["position"] = row[2]
                data_dict["titles"] = row[3]
                data_dict["sport_type"] = row[4]
                data_dict["rank"] = row[5]

                dom.create_sportsman(data_dict)
            dom.create_xml_file()

    def add_new_sportsman(self, row):
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

    def refresh_sportsman_in_table(self):
        try:
             self.table.row_data += self._not_filtered
             self._not_filtered = []
        except Exception as e:
             pass

    def select_sportsman_by_filters(self, filters: list):
        not_filtered_sportsman = []
        for row in self.table.row_data:
            # first case
            if filters[0] and filters[4]:  # fio
                surname = row[0]
                filter_surname = filters[0]
                print(filter_surname, filters[4], surname, row[4])
                if not (surname == filter_surname and row[4] == filters[4]):
                    not_filtered_sportsman.append(tuple(row))
                    print(len(not_filtered_sportsman))
                    continue
            # second case
            elif filters[1] and not row[1] == filters[1]:  # group
                not_filtered_sportsman.append(tuple(row))
                continue
            # third case
            elif filters[3]:
                if re.match(r'^\d+-\d+$', filters[3]):
                    start, end = filters[3].split('-')
                    if int(row[3]) not in range(int(start), int(end) + 1):
                        not_filtered_sportsman.append(tuple(row))
                        continue
        return not_filtered_sportsman

    def filter_sportsman_in_table(self, filters: list):
        self._not_filtered = self.select_sportsman_by_filters(filters=filters)
        for row in self._not_filtered:
            self.table.row_data.remove(row)

    @staticmethod
    def empty_filters(filters):
        for filter in filters:
            if filter != '':
                return False
        return True

    def delete_sportsman_from_table(self, filters):
        ''' delete a sportsmans that are in _not_filtered list '''
        count_to_delete = 0
        if self.empty_filters(filters):
            return count_to_delete
        unselected_sportsmans = self.select_sportsman_by_filters(filters=filters)
        for row in self.table.row_data[:]:
            if row not in unselected_sportsmans:
                try:
                    self.table.row_data.remove(row)
                    count_to_delete += 1
                except Exception as e:
                    Snackbar(text="No such sportsmans").open()
                    pass
        return count_to_delete
