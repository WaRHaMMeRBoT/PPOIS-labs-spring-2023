import json
from User import *


def getBalance(wallet, balance):
    balance["dollars"] = round(wallet.balance.dollars, 2)
    balance["euros"] = round(wallet.balance.euros, 2)
    balance["rubles"] = round(wallet.balance.rubles, 2)
    return balance.copy()


def getPhone(_user, phone):
    phone["balance"] = round(_user.phone.balance, 2)
    phone["phoneNumber"] = _user.phone.number
    phone["OwnersName"] = _user.phone.OwnersName
    return phone.copy()


def getCard(_user, creditCard, balance):
    creditCard["cardNumber"] = _user.card.cardNumber
    creditCard["PIN"] = _user.card.PIN
    creditCard["CVV"] = _user.card.CVV
    creditCard["ExpiresDate"] = _user.card.ExpiresDate
    creditCard["balance"] = getBalance(_user.card, balance)
    creditCard["OwnersName"] = _user.card.OwnersName
    return creditCard.copy()


def write(userList, filename):
    Users = {"users": []}
    user = {"name": "", "cash": [], "phone": [], "creditCard": []}
    creditCard = {
        "cardNumber": "",
        "PIN": "",
        "ExpiresDate": "",
        "CVV": "",
        "balance": [],
        "OwnersName": "",
    }
    phone = {"phoneNumber": "", "balance": 0, "OwnersName": ""}
    balance = {"dollars": 0, "euros": 0, "rubles": 0}
    for _user in userList:
        user["name"] = _user.Name
        user["cash"] = getBalance(_user, balance)
        user["phone"] = getPhone(_user, phone)
        user["creditCard"] = getCard(_user, creditCard, balance)
        Users["users"].append(user.copy())
    with open(filename, "w", encoding="utf-8") as file:
        file = json.dump(Users, file, indent=1, sort_keys=False)


# ЗАПИСЬ


def readPhone(_phone, phone):
    _phone.balance = float(phone["balance"])
    _phone.number = phone["phoneNumber"]
    _phone.OwnersName = phone["OwnersName"]


def readCreditCard(_card, card):
    _card.balance.dollars = float(card["balance"]["dollars"])
    _card.balance.euros = float(card["balance"]["euros"])
    _card.balance.rubles = float(card["balance"]["rubles"])
    # Чтение баланса карточки
    _card.cardNumber = card["cardNumber"]
    _card.PIN = card["PIN"]
    _card.CVV = card["CVV"]
    _card.ExpiresDate = card["ExpiresDate"]
    _card.OwnersName = card["OwnersName"]
    # Чтение информации карточки


def readCash(_cash, cash):
    _cash.dollars = float(cash["dollars"])
    _cash.euros = float(cash["euros"])
    _cash.rubles = float(cash["rubles"])


def read(userList, filename):
    with open(filename, "r", encoding="utf-8") as file:
        dataBase = json.load(file)
    for user in dataBase["users"]:
        _user = User()
        _user.Name = user["name"]
        readPhone(_user.phone, user["phone"])
        readCreditCard(_user.card, user["creditCard"])
        readCash(_user.balance, user["cash"])
        userList.append(_user)


# ЧТЕНИЕ
