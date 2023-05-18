class Repository:

    def __init__(self, money: float = 0):
        self.__money = money

    @property
    def money(self) -> float:
        return self.__money

    def get_money(self, money: float) -> None:
        self.__money -= money

    def put_money(self, money: float) -> None:
        self.__money += money
