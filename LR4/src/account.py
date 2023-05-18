class Account:

    id_tf = 0
    def __init__(self, login: str, password: str, balance: float = 0, id_: int = None):

        if id_ is None:
            self.__id = Account.id_tf
            Account.id_tf += 1
        else:
            self.__id = id_

        self.__login = login
        self.__password = password
        self.__balance = balance

    def as_dict(self):
        return {
            'id': self.__id,
            'login': self.__login,
            'password': self.__password,
            'balance': self.__balance
        }

    @property
    def login(self):
        return self.__login

    @property
    def balance(self) -> float:
        return self.__balance

    @property
    def id(self) -> int:
        return self.__id

    def get_access(self, password):
        return self.__password == password

    def increase_balance(self, money: float) -> None:
        self.__balance += money

    def decrease_balance(self, money: float) -> None:
        self.__balance -= money
