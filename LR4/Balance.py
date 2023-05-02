class Balance:
    def __init__(self):
        self.__dollars: float = 0
        self.__euros: float = 0
        self.__rubles: float = 0

    @property
    def dollars(self) -> float:
        return self.__dollars

    @dollars.setter
    def dollars(self, dollars):
        self.__dollars = dollars

    @property
    def euros(self) -> float:
        return self.__euros

    @euros.setter
    def euros(self, euros):
        self.__euros = euros

    @property
    def rubles(self) -> float:
        return self.__rubles

    @rubles.setter
    def rubles(self, rubles):
        self.__rubles = rubles

    def __str__(self):
        return (
            str(round(self.__dollars, 2))
            + "$"
            + "\t"
            + str(round(self.__euros, 2))
            + "€"
            + "\t"
            + str(round(self.__rubles, 2))
            + "₽"
        )
