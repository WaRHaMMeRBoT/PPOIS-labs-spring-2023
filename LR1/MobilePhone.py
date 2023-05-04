from Balance import *


class Mobile:
    def __init__(self):
        self.__balance: float = 0
        self.__number = str(0)
        self.__OwnersName = ""

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, balance):
        self.__balance = balance

    @property
    def number(self):
        return self.__number

    @number.setter
    def number(self, number):
        self.__number = number

    @property
    def OwnersName(self):
        return self.__OwnersName

    @OwnersName.setter
    def OwnersName(self, OwnersName):
        self.__OwnersName = OwnersName

    def print(self):
        print(f"Phone info:\nNumber: {self.__number}\tBalance: {self.__balance}₽")
