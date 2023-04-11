class BanknoteVault:
    def __init__(self, cash: list):
        self.__cash: dict = dict()
        for banknote in cash:
            self.__cash.update({banknote["nominal"]: banknote["count"]})

    def giveMoney(self, cash: int) -> dict | None:
        result: dict = dict()
        nominals = [*self.__cash.keys()]
        nominals.sort()

        while cash != 0:
            if len(nominals) == 0 or cash < nominals[0]:
                return None
            result.update({nominals[-1]: min(self.__cash[nominals[-1]], cash // nominals[-1])})
            cash = cash - nominals[-1] * result[nominals[-1]]
            nominals = nominals[:-1]

        for nominal in result.keys():
            self.__cash[nominal] -= result[nominal]
        return result

    def print(self) -> None:
        for nominal in self.__cash.keys():
            print(str(nominal) + "x" + str(self.__cash[nominal]))

    def allMoney(self) -> int:
        result: int = 0
        for nominal in self.__cash.keys():
            result += nominal * self.__cash[nominal]
        return result

    def getData(self) -> list:
        return [{"nominal": nominal, "count": self.__cash[nominal]} for nominal in self.__cash.keys()]
