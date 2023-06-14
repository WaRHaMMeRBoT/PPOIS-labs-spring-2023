import json


class Bank:
    def __init__(self):
        self.__pin_list = dict()
        with open("./JSON_files/pins.json", "r") as pins_file:
            pins_data = json.load(pins_file)
            for card in pins_data:
                self.__pin_list.update(card)

    def TryPin(self, card_id: str, pin: str) -> bool:
        return self.__pin_list[card_id] == pin
