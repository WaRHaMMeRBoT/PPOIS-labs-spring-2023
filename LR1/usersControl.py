import json as j
import random


class User:
    def __init__(self):
        jsonFile = open("dataBase.json", "r")
        userData = j.load(jsonFile)
        self.__count = userData["userData"]["count"]
        self.__user = []

        for i in userData["userData"]["items"]:
            self.__user.append(i)

        jsonFile.close()

    def _getUserCountInit(self):
        return self.__count

    def _getUserCardNumberInit(self, i):
        return self.__user[i]["cardNumber"]

    def _getCvvInit(self, i):
        return self.__user[i]["cvv"]

    def _getBanalceInit(self, i):
        return self.__user[i]["money"]

    def _reduceMoneyInit(self, i, reduce):
        self.__user[i]["money"] = str(int(self.__user[i]["money"]) - reduce)

    def _getPhoneNumberInit(self, i):
        return self.__user[i]["phoneNumber"]

    def _changeCardInit(self, i):
        newNumberSections = [random.randint(1000, 9999), random.randint(1000, 9999),
                             random.randint(1000, 9999), random.randint(1000, 9999)]
        newCvv = str(random.randint(100, 999))
        number = "**" + str(newNumberSections[3])

        self.__user[i]["cardNumber"] = number
        self.__user[i]["cvv"] = newCvv

        print("Новый номер карты: ", end="")

        for i in newNumberSections:
            print(i, end=" ")

        print("\nНовый CVV код:", newCvv)

    def _getIdInit(self, i):
        return self.__user[i]["ID"]

    def _getUserDataInit(self, i, key):
        return self.__user[i][key]


def getUserData(user, i, j):
    return user._getUserDataInit(i, j)


def getId(user, i):
    return user._getIdInit(i)


def changeCardNumber(user, i):
    user._changeCardInit(i)


def getPhoneNumber(user, i):
    return user._getPhoneNumberInit(i)


def reduceMoney(user, i, reduce):
    user._reduceMoneyInit(i, reduce)


def getUserCount(user):
    return user._getUserCountInit()


def getUserCardNumber(user, i):
    return user._getUserCardNumberInit(i)


def getCvv(user, i):
    return user._getCvvInit(i)


def getBalance(user, i):
    return user._getBanalceInit(i)
