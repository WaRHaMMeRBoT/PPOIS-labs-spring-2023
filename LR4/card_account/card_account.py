import exceptions.exceptions as exc


class CardAccount:
    def __init__(self, acc_id: str, balance: float) -> None:
        self.__acc_id: str = acc_id
        self.__balance: float = balance

    @property
    def balance(self) -> float:
        return self.__balance

    def bal_add(self, value: float):
        self.__balance += value
        self.__balance = round(self.__balance, 2)

    def bal_sub(self, value: float):
        if self.__balance < value:
            raise exc.NotEnoughMoney
        self.__balance -= value
        self.__balance = round(self.__balance, 2)

    @property
    def acc_id(self) -> str:
        return self.__acc_id

    def __str__(self):
        return f"Account ID: {self.__acc_id}\n" \
               f"Account Balance: {self.__balance}"
