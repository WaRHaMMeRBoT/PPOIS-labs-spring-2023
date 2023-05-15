from typing import List

from src.BankAccount import BankAccount, Card


class Bank:
    __accounts: List[BankAccount] = list()

    def __init__(self, data: dict):
        self.__name: str = data["name"]
        if type(self.__name) is not str:
            raise ValueError("Invalid bank name")
        for account in data["accounts"]:
            self.__accounts.append(BankAccount(account))

    def getCards(self) -> List[Card]:
        result: list[Card] = list()
        for account in self.__accounts:
            result.extend([*account.getCards()])
        return result

    def getData(self) -> dict:
        data: dict = dict()
        data.update({"name": self.__name})
        data.update({"accounts": [account.getData() for account in self.__accounts]})
        return data
