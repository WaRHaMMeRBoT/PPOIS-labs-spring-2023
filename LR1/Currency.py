class currency_value:
    def __init__(self):
        self.__EURUSD = 1.11  # Валютная пара евро к доллару
        self.__EURRUB = 81.34  # Валютная пара евро к рублю
        self.__USDRUB = round(
            self.__EURRUB / self.__EURUSD, 2
        )  # Валютная пара доллар к рублю
        self.__comission = 0.007  # Комиссия

    @property
    def EURUSD(self):
        return self.__EURUSD

    @EURUSD.setter
    def EURUSD(self):
        return self.__EURUSD

    @property
    def EURRUB(self):
        return self.__EURRUB

    @EURRUB.setter
    def EURRUB(self):
        return self.__EURRUB

    @property
    def USDRUB(self):
        return self.__USDRUB

    @USDRUB.setter
    def USDRUB(self):
        return self.__USDRUB

    @property
    def comission(self):
        return self.__comission

    @comission.setter
    def comission(self):
        return self.__comission

    def get_cost_pair(self, currency, buy):
        cost = 0.0
        if currency == "eurusd":
            cost = self.__EURUSD
        elif currency == "eurrub":
            cost = self.__EURRUB
        elif currency == "usdrub":
            cost = self.__USDRUB
        if buy:
            return cost / (1 + self.__comission)
        else:
            return cost * (1 + self.__comission)


def currency(targetCurrency):
    currency = ["$", "€", "₽"]
    currencyDictionary = {"dollars": "$", "euros": "€", "rubles": "₽"}
    targetCurrency = targetCurrency.lower()
    if targetCurrency in currencyDictionary.keys():
        return currencyDictionary.get(targetCurrency)
    if targetCurrency in currency:
        return targetCurrency
    return None


def get_wallet(wallet, currency):
    if currency == "$":
        return wallet.balance.dollars
    elif currency == "€":
        return wallet.balance.euros
    elif currency == "₽":
        return wallet.balance.rubles


def get_currencies_sighns(currency, way_to_exchange):
    first_currency = ""
    second_currency = ""
    if currency == "eurusd":
        if way_to_exchange:
            first_currency = "€"
            second_currency = "$"
        else:
            first_currency = "$"
            second_currency = "€"
    if currency == "eurrub":
        if way_to_exchange:
            first_currency = "€"
            second_currency = "₽"
        else:
            first_currency = "₽"
            second_currency = "€"
    if currency == "usdrub":
        if way_to_exchange:
            first_currency = "$"
            second_currency = "₽"
        else:
            first_currency = "₽"
            second_currency = "$"
    return first_currency, second_currency
