import os

from src.Bank import Bank
from src.BankAccount import Card
from src.BanknoteVault import BanknoteVault

clear = lambda: os.system("cls")


class ATM:

    def __init__(self, bank: Bank, data: dict) -> None:
        self.__bank: Bank = bank
        self.__vault = BanknoteVault(data["cash"])
        self.__insertedCard = None
        self.__isPinEntered = True if data["isPinEntered"] == "True" else False
        if data['insertedCard'] != 'None':
            cardList = self.__bank.getCards()
            for card in cardList:
                if data['insertedCard'] == card.getNumber():
                    self.__insertedCard = card
                    break

    def isCardInserted(self):
        return self.__insertedCard is not None

    def changeInsertedState(self):
        self.__insertedCard = None
        self.__isPinEntered = False

    def getCards(self):
        return self.__bank.getCards()

    def selectCard(self, number):
        if number <= 0 or number > len(self.__bank.getCards()):
            raise ValueError('number out of range')
        self.__insertedCard = self.__bank.getCards()[number - 1]

    def enterPin(self, pin):
        if not self.__insertedCard:
            raise ValueError('card is not inserted')
        if self.__insertedCard.getAttempts() >= 3 or self.__insertedCard.isLocked():
            raise ValueError('card is locked')
        if self.__isPinEntered:
            raise ValueError('pin entered')
        if self.__insertedCard.checkPIN(pin):
            self.__isPinEntered = True
            return True
        else:
            self.__insertedCard.increaseAttempts()
            return False

    def withdrawMoney(self, moneyCount):
        if not self.__insertedCard:
            raise ValueError('card is not inserted')
        if not self.__isPinEntered:
            raise ValueError('pin not entered')
        if int(moneyCount) > self.__insertedCard.getBankAccount().getBalance():
            raise ValueError("not enough money in the account")
        cash = self.__vault.giveMoney(int(moneyCount))
        if cash is None:
            raise ValueError("ATM cannot dispense this amount")
        self.__insertedCard.getBankAccount().decreaseBalance(int(moneyCount))
        return cash

    def makeTelephonePayment(self, amount, number):
        if not self.__insertedCard:
            raise ValueError('card is not inserted')
        if not self.__isPinEntered:
            raise ValueError('pin not entered')
        if int(amount) > self.__insertedCard.getBankAccount().getBalance():
            raise ValueError("not enough money in the account")

        if not len(number) == 9 or not number.isdigit():
            raise ValueError("incorrect phone number, expected 9 digits")

        self.__insertedCard.getBankAccount().decreaseBalance(int(amount))

    def getCardBalance(self):
        if not self.__insertedCard:
            raise ValueError('card is not inserted')
        if not self.__isPinEntered:
            raise ValueError('pin not entered')
        return self.__insertedCard.getBankAccount().getBalance()

    def getData(self) -> dict:
        return {"insertedCard": "None" if self.__insertedCard is None else self.__insertedCard.getNumber(),
                "cash": self.__vault.getData(),
                "isPinEntered": "True" if self.__isPinEntered else "False"}
