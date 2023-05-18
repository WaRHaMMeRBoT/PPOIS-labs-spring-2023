from src.account import Account
import datetime
from random import randint


class Card:

    id_tf = 0

    @staticmethod
    def get_number() -> str:
        num = str(Card.id_tf)

        Card.id_tf += 1
        return num if len(num) == 8 else (num[::-1] + '0' * (8 - len(num)))[::-1]

    def __init__(self, pin: str, account: Account, number: str = None, cvv: str = None, date: str = None):

        if number is None:
            self.__number = Card.get_number()
        else:
            self.__number = number

        if cvv is None:
            self.__cvv = ''.join(str(randint(0, 9)) for i in range(3))
        else:
            self.__cvv = cvv

        if date is None:
            self.__date = f'{datetime.datetime.now().month}/{datetime.datetime.now().year + 5}'
        else:
            self.__date = date

        self.__pin = pin
        self.__account = account

    def as_dict(self):
        return {
            'number': self.__number,
            'cvv': self.cvv,
            'date': self.date,
            'pin': self.__pin,
            'account_id': self.account.id
        }

    @property
    def number(self) -> str:
        return self.__number

    @property
    def cvv(self) -> str:
        return self.__cvv

    @property
    def date(self) -> str:
        return self.__date

    @property
    def account(self) -> Account:
        return self.__account

    def get_access(self, pin: str):
        return self.__pin == pin
