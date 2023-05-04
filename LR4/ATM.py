from Bank import *


class Atm:
    def __init__(self):
        bank = Bank()
        self.__UsersList = []
        self.__balance = Balance()
        read(self.__UsersList, "dataBase.json")

    def inputCard(self):
        while True:

            cardNumber = input("Input yout cardNumber and PIN: ")
            PIN = input()
            for user in self.__UsersList:
                if (user.card.PIN == PIN) and (user.card.cardNumber == cardNumber):
                    print(f"Access granted\nHello {user.Name}")
                    return user
            print("cardNotFound or wrong PIN")

    @property
    def UsersList(self):
        return self.__UsersList

    @UsersList.setter
    def UsersList(self, UsersList):
        self.__UsersList = UsersList

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, balance):
        self.__balance = balance
