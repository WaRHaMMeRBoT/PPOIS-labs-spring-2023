from typing import List


class BankAccount:
    __numberSize = 10

    def __init__(self, data: dict) -> None:
        self.__ownerFirstName: str = data["firstName"]
        if type(self.__ownerFirstName) is not str:
            raise ValueError("Incorrect first name")

        self.__ownerLastName: str = data["lastName"]
        if type(self.__ownerLastName) is not str:
            raise ValueError("Incorrect last name")

        self.__number: str = data["number"]
        if len(self.__number) != self.__numberSize or not self.__number.isdigit():
            raise ValueError("Incorrect account number")

        self.__balance: float = data["balance"]
        if type(self.__balance) is not float and type(self.__balance) is not int:
            raise ValueError("Incorrect account balance")

        self.__cards: List[Card] = list()
        for card in data["cards"]:
            self.__cards.append(Card(card, self))

    def getBalance(self) -> float:
        return self.__balance

    def decreaseBalance(self, delta: float) -> None:
        self.__balance -= delta

    def increaseBalance(self, delta: float) -> None:
        self.__balance += delta

    def getCards(self):
        return self.__cards

    def getOwnerFirstName(self) -> str:
        return self.__ownerFirstName

    def getOwnerLastName(self) -> str:
        return self.__ownerLastName

    def getData(self) -> dict:
        data: dict = dict()
        data.update({"firstName": self.__ownerFirstName, "lastName": self.__ownerLastName, "number": self.__number,
                     "balance": self.__balance})
        data.update({"cards": [card.getData() for card in self.__cards]})
        return data


class Card:
    __numberSize = 16
    __pinSize = 4

    def __init__(self, data: dict, account: BankAccount) -> None:
        self.__account = account
        self.__number = data["cardNum"]
        self.__attempt = data["attempt"]
        if len(self.__number) != self.__numberSize or not self.__number.isdigit():
            raise ValueError("Incorrect card number")

        self.__pin = data["cardPIN"]
        if len(self.__pin) != self.__pinSize or not self.__pin.isdigit():
            raise ValueError("Incorrect card PIN")

        if data["status"] == "unlock":
            self.__locked: bool = False
        elif data["status"] == "lock":
            self.__locked: bool = True
        else:
            raise ValueError("Invalid card status")
        if self.__attempt >= 3:
            self.__locked = True

    def checkPIN(self, pin: str) -> bool:
        if len(pin) is not self.__pinSize or not pin.isdigit():
            raise ValueError("Invalid input")
        if pin == self.__pin:
            return True
        else:
            return False

    def getBankAccount(self) -> BankAccount:
        return self.__account

    def getNumber(self) -> str:
        return self.__number

    def isLocked(self) -> bool:
        return self.__locked

    def setLockedStatus(self, status: bool) -> None:
        self.__locked = status

    def getAttempts(self):
        return self.__attempt

    def increaseAttempts(self):
        self.__attempt += 1
        if self.__attempt >= 3:
            self.__locked = True

    def getData(self) -> dict:
        data: dict = dict()
        data.update({"cardNum": self.__number, "cardPIN": self.__pin, "attempt":self.__attempt})
        if not self.__locked:
            data.update({"status": "unlock"})
        else:
            data.update({"status": "lock"})
        return data
