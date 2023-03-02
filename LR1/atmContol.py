import json as j


class ATM:
    def __init__(self, number):
        jsonFile = open("atmDataBase.json", "r")
        atmData = j.load(jsonFile)
        self.__banknote_5rub = atmData["atmData"]["5RUB"]
        self.__banknote_10rub = atmData["atmData"]["10RUB"]
        self.__banknote_20rub = atmData["atmData"]["20RUB"]
        self.__banknote_50rub = atmData["atmData"]["50RUB"]
        self.__banknote_100rub = atmData["atmData"]["100RUB"]
        jsonFile.close()

    def _getBanknoteNumberInit(self, i):
        if i == 1:
            return self.__banknote_5rub[0]
        elif i == 2:
            return self.__banknote_10rub[0]
        elif i == 3:
            return self.__banknote_20rub[0]
        elif i == 4:
            return self.__banknote_50rub[0]
        elif i == 5:
            return self.__banknote_100rub[0]

    def _getBanknoteValueInit(self, i):
        if i == 1:
            return self.__banknote_5rub[1]
        elif i == 2:
            return self.__banknote_10rub[1]
        elif i == 3:
            return self.__banknote_20rub[1]
        elif i == 4:
            return self.__banknote_50rub[1]
        elif i == 5:
            return self.__banknote_100rub[1]

    def _banknotReduceInit(self, i, number):
        if i == 1:
            self.__banknote_5rub[0] = str(int(self.__banknote_5rub[0]) - number)
        elif i == 2:
            self.__banknote_10rub[0] = str(int(self.__banknote_10rub[0]) - number)
        elif i == 3:
            self.__banknote_20rub[0] = str(int(self.__banknote_20rub[0]) - number)
        elif i == 4:
            self.__banknote_50rub[0] = str(int(self.__banknote_50rub[0]) - number)
        elif i == 5:
            self.__banknote_100rub[0] = str(int(self.__banknote_100rub[0]) - number)

    def _banknoteShow(self):
        print(" [5   RUB]:", self.__banknote_5rub[0], "шт.\n",
              "[10  RUB]:", self.__banknote_10rub[0], "шт.\n",
              "[20  RUB]:", self.__banknote_20rub[0], "шт.\n",
              "[50  RUB]:", self.__banknote_50rub[0], "шт.\n",
              "[100 RUB]:", self.__banknote_100rub[0], "шт.")


def banknoteReduce(atm, i, number):
    atm._banknotReduceInit(i, number)


def getBanknoteNumber(atm, i):
    return int(atm._getBanknoteNumberInit(i))


def getBanknoteValue(atm, i):
    return atm._getBanknoteValueInit(i)

def banknoteShow(atm):
    atm._banknoteShow()