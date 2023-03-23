import json


class DataPlayers:
    __data: list

    def __init__(self):
        with open("data.json") as file:
            self.__data = json.load(file)
            file.close()

    def get_data(self):
        return self.__data

    def push_data(self):
        with open('data.json', 'w') as file:
            data_json = json.dumps(self.__data, indent=3)
            file.write(data_json)
            file.close()

    def refresh_data(self, new_data):
        self.__data = new_data
