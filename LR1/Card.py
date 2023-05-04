from Balance import *


class CreditCard:
    def __init__(self):
        self.__balance = Balance()
        self.__cardNumber = ""
        self.__CVV = ""
        self.__ExpiresDate = ""
        self.__OwnersName = ""
        self.__PIN = ""

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, balance):
        self.__balance = balance

    @property
    def cardNumber(self):
        return self.__cardNumber

    @cardNumber.setter
    def cardNumber(self, cardNumber):
        self.__cardNumber = cardNumber

    @property
    def CVV(self):
        return self.__CVV

    @CVV.setter
    def CVV(self, CVV):
        self.__CVV = CVV

    @property
    def ExpiresDate(self):
        return self.__ExpiresDate

    @ExpiresDate.setter
    def ExpiresDate(self, ExpiresDate):
        self.__ExpiresDate = ExpiresDate

    @property
    def OwnersName(self):
        return self.__OwnersName

    @OwnersName.setter
    def OwnersName(self, OwnersName):
        self.__OwnersName = OwnersName

    @property
    def PIN(self):
        return self.__PIN

    @PIN.setter
    def PIN(self, PIN):
        self.__PIN = PIN

    def print(self):
        print(
            f"CreditCard info:\nCardNumber: {self.__cardNumber}\tCVV: {self.__CVV}\tPIN: {self.__PIN}\nExpiresDate: {self.__ExpiresDate}\nBalance: {self.__balance}"
        )
