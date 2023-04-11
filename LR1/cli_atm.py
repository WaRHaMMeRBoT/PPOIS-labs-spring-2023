import json
import click

from src.ATM import ATM
from src.Bank import Bank

databasePath = "database.json"
bank: Bank
atm: ATM


def loadDatabase(path):
    try:
        file = open(path, "r")
    except IOError:
        print("Database doesn't exist")
    else:
        with file as jsonLoad:
            return json.load(jsonLoad)


def saveDatabase(bank: Bank, atm: ATM, path):
    data: dict = {"infoBank": bank.getData(), "infoATM": atm.getData()}
    with open(path, "w") as dataFile:
        json.dump(data, dataFile, indent=4)


@click.group()
def start_atm():
    pass


@start_atm.command('insert_card')
@click.option('-n', '--number', default=-1)
def insertCard(number):
    if atm.isCardInserted():
        print('Card inserted')
        return
    if number == -1:
        currentNum = 1
        for card in atm.getCards():
            print(str(currentNum) + " - " + card.getNumber())
            currentNum += 1
    else:
        try:
            atm.selectCard(number)
            print("Success")
        except ValueError as error:
            print("Error: ", error)
    end_work()


@start_atm.command('get_card')
def getCard():
    if atm.isCardInserted():
        atm.changeInsertedState()
    end_work()


@start_atm.command('enter_pin')
@click.option('-p', '--password', prompt='PIN', hide_input=True)
def enterPin(password):
    try:
        if atm.enterPin(password):
            print('Success')
        else:
            print('Incorrect PIN')
    except ValueError as error:
        print('Error:', error)
    end_work()


@start_atm.command('view_balance')
def viewBalance():
    try:
        print(atm.getCardBalance())
    except ValueError as error:
        print("Error:", error)


@start_atm.command('withdraw_money')
@click.option('-a', '--amount', prompt='Input amount')
def withdrawMoney(amount):
    try:
        cash = atm.withdrawMoney(amount)
    except ValueError as error:
        print("Error:", error)
    else:
        for nominal in cash.keys():
            if cash[nominal] != 0:
                print(str(nominal) + "x" + str(cash[nominal]))
    end_work()


@start_atm.command('phone_payment')
@click.option('-p', '--phone', prompt='Input phone')
@click.option('-a', '--amount', prompt='Input amount')
def phonePayment(phone, amount):
    try:
        atm.makeTelephonePayment(amount, phone)
    except ValueError as error:
        print("Error:", error)
    else:
        print('Success')
    end_work()


def end_work():
    saveDatabase(bank, atm, databasePath)


if __name__ == '__main__':
    data = loadDatabase(databasePath)
    try:
        bank = Bank(data["infoBank"])
        atm = ATM(bank, data["infoATM"])
    except KeyError:
        print("Incorrect database")
    except ValueError as exception:
        print("Incorrect database", exception, sep="\n")
    else:
        start_atm()
