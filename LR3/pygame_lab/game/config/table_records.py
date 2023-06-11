import json

from pygame_lab.game.config.settings import PATH_FOR_TABLE


class Table:
    def __init__(self) -> None:
        self.list_of_player = dict()

    @staticmethod
    def load_table():
        with open("records_table.json", 'r') as file:
            list_of_player = json.loads(file.read())
        return list_of_player

    @staticmethod
    def upload_table(info: dict):
        table:dict = Table.load_table()
        table.update(**info)
        with open("records_table.json", 'w') as file:
            json.dump(table, file, ensure_ascii=False, indent=4)

    def create_table_line(self, player_name, score):
        if not player_name:
            player_name = 'Anonymous'
        self.list_of_player[player_name] = score
