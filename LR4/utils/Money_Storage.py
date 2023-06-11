import utils.Exceptions as excep

class MoneyStorage:
    def __init__(self, moneyStorage: dict[int, int])->None:
        self.__moneyStorage: dict[int,int] = moneyStorage

    @property
    def moneyStorage(self) -> dict:
        return self.__moneyStorage

    def get_money(self, money_value: int) -> None:
        self.__moneyStorage = dict(sorted(self.__moneyStorage.items(), reverse=True))
        possible_opt = dict()
        available_best_sum, rest_sum = 0, money_value
        for banknote, amount in self.__moneyStorage.items():
            best_amount_available = min(rest_sum // banknote, amount)
            possible_opt[banknote] = best_amount_available
            available_best_sum += banknote * best_amount_available
            rest_sum -= banknote * best_amount_available
        if available_best_sum != money_value:
            raise excep.NoAvailableMoneyConfig
        else:
            for banknote in self.__moneyStorage.keys():
                self.__moneyStorage[banknote] -= possible_opt[banknote]

    def __str__(self):
        return_str = "Available banknotes:\n"
        for banknote, amount in self.__moneyStorage.items():
            return_str += f"{banknote} BYN - {amount}\n"
        return return_str