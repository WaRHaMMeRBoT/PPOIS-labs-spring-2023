import json as j
import random 

class Users:
    def __init__(self):
        jsonfile = open("information.json","r")
        usersInform = j.load(jsonfile)
        self.__count = usersInform["usersInform"]["count"]
        self.__users = []

        for i in usersInform["usersInform"]["items"]:
            self.__users.append(i)

        jsonfile.close()

    def _getUsersCount(self):
        return self.__count
    
    def _getUsersCardNumber(self,i):
        return self.__users[i]["cardNumber"]

    def _getCardPin(self,i):
        return self.__users[i]["Pin"]

    def _getBalance(self,i):
        return self.__users[i]["cash"]

    def reduceCash(self,i,reduce):
        self.__users[i]["cash"] = str(int(self.__users[i]["cash"])-reduce)
    
    def _getPhoneNumber(self,i):
        return self.__users[i]["phoneNumber"]

    def changeCard(self,i):
        newNumber = [random.randint(1111, 9999), random.randint(1111, 9999), random.randint(1111, 9999), random.randint(1111, 9999)]
        newPin = str(random.randint(1111,9999))

        number = "***" + str(newNumber[3])

        self.__users[i]["cardNumber"] = number
        self.__users[i]["Pin"] = newPin

        print("Новый номер карты: ", end="")
        for i in newNumber:
            print(i, end =" ")

        print("\nНовый PIN", newPin)

    def _getID(self, i):
        return self.__users[i]["ID"]

    def _getUsersInform(self, i, key):
        return self.__users[i][key]

def getUsers(users, i, j):
    return users._getUsersInform(i, j)

def getId(users, i):
    return users._getID(i)

def changeCardNumb(users, i):
    users.changeCard(i)

def getPhoneNum(users, i):
    return users._getPhoneNumber(i)

def reduceMoney(users, i, reduce):
    users.reduceCash(i, reduce)

def getUsersNum(users):
    return users._getUsersCount()

def getUsersCardNum(users, i):
    return users._getUsersCardNumber(i)

def getPIN(users, i):
    return users._getCardPin(i)

def getBalanc(users, i):
    return users._getBalance(i)