from Card import *
from MobilePhone import Mobile


class User:
    def __init__(self):
        self.__balance = Balance()
        self.__Name = ""
        self.__phone = Mobile()
        self.__card = CreditCard()

    def print(self):
        print(f"UserName: {self.__Name}\nCash: {self.__balance}")
        self.__phone.print()
        self.__card.print()

    @property
    def card(self):
        return self.__card

    @card.setter
    def card(self, card):
        self.__card = card

    @property
    def phone(self):
        return self.__phone

    @phone.setter
    def phone(self, phone):
        self.__phone = phone

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, balance):
        self.__balance = balance

    @property
    def Name(self):
        return self.__Name

    @Name.setter
    def Name(self, Name):
        self.__Name = Name
