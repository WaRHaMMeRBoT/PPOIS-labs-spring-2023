import json as j

class ATM:
    def __init__(self, number):
        jsonfile = open("ATM.json", "r")
        ATMinfm = j.load(jsonfile)
        self.__banknote_5Rub = ATMinfm["ATMinfm"]["5Rub"]
        self.__banknote_10Rub = ATMinfm["ATMinfm"]["10Rub"]
        self.__banknote_20Rub = ATMinfm["ATMinfm"]["20Rub"]
        self.__banknote_50Rub = ATMinfm["ATMinfm"]["50Rub"]
        self.__banknote_100Rub = ATMinfm["ATMinfm"]["100Rub"]
        self.__banknote_200Rub = ATMinfm["ATMinfm"]["200Rub"]
        self.__banknote_500Rub = ATMinfm["ATMinfm"]["500Rub"]
        jsonfile.close()

    def _getBanknoteNumber(self,i):
        if i == 1:
            return self.__banknote_5Rub[0]
        elif i == 2:
            return self.__banknote_10Rub[0]
        elif i == 3:
            return self.__banknote_20Rub[0]
        elif i == 4:
            return self.__banknote_50Rub[0]
        elif i == 5:
            return self.__banknote_100Rub[0]
        elif i == 6:
            return self.__banknote_200Rub[0]
        elif i == 7:
            return self.__banknote_500Rub[0]
    
    def _getBanknoteValue(self, i):
        if i == 1:
            return self.__banknote_5Rub[1]
        elif i == 2:
            return self.__banknote_10Rub[1]
        elif i == 3:
            return self.__banknote_20Rub[1]
        elif i == 4:
            return self.__banknote_50Rub[1]
        elif i == 5:
            return self.__banknote_100Rub[1]
        elif i == 6:
            return self.__banknote_200Rub[1]
        elif i == 7:
            return self.__banknote_500Rub[1]
    
    def _banknoteReduce(self, i, number):
        if i == 1:
            self.__banknote_5Rub[0] = str(int(self.__banknote_5Rub[0]) - number)
        elif i == 2:
            self.__banknote_10Rub[0] = str(int(self.__banknote_10Rub[0]) - number)
        elif i == 3:
            self.__banknote_20Rub[0] = str(int(self.__banknote_20Rub[0]) - number)
        elif i == 4:
            self.__banknote_50Rub[0] = str(int(self.__banknote_50Rub[0]) - number)
        elif i == 5:
            self.__banknote_100Rub[0] = str(int(self.__banknote_100Rub[0]) - number)
        elif i == 6:
            self.__banknote_200Rub[0] = str(int(self.__banknote_200Rub[0]) - number)
        elif i == 7:
            self.__banknote_500Rub[0] = str(int(self.__banknote_500Rub[0]) - number)

    def _banknoteShow(self):
        print("[5   Rub]:", self.__banknote_5Rub[0], "шт.\n",
              "[10  Rub]:", self.__banknote_10Rub[0], "шт.\n",
              "[20  Rub]:", self.__banknote_20Rub[0], "шт.\n",
              "[50  Rub]:", self.__banknote_50Rub[0], "шт.\n",
              "[100  Rub]:", self.__banknote_100Rub[0], "шт.\n",
              "[200  Rub]:", self.__banknote_200Rub[0], "шт.\n",
              "[500 Rub]:", self.__banknote_500Rub[0], "шт.")

def banknoteReduc(atm, i, number):
    atm._banknoteReduce(i, number)

def getBanknoteNumb(atm, i):
    return int(atm._getBanknoteNumber(i))


def getBanknoteVal(atm, i):
    return atm._getBanknoteValue(i)

def banknotShow(atm):
    atm._banknoteShow()



