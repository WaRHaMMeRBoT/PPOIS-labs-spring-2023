import utils.Exceptions as excep

class BankAccount:
    def __init__(self, account_id:str, balance:float) ->None:
        self.__account_id:str = account_id
        self.__balance: float = balance

    @property
    def balance(self) ->float:
        return self.__balance

    def add_balance(self, value:float):
        self.__balance += value

    def subtract_money(self, value:float):
        if self.__balance<value:
            raise excep.NotEnoughMoney
        self.__balance -=value

    @property
    def account_id(self) -> str:
        return self.__account_id

    def __str__(self):
        return f"Account ID: {self.__account_id}\nAccount Balance: {self.__balance}"
