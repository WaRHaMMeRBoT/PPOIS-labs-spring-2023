class Banknote:
    def __init__(self, value: int):
        self.__value: int = value

    @property
    def value(self) -> int:
        return self.__value

    def __eq__(self, other):
        if isinstance(other, Banknote):
            return self.__value == other.value
        elif isinstance(other, int):
            return self.__value == other
        else:
            return False

    def __ne__(self, other):
        if isinstance(other, Banknote):
            return self.__value != other.value
        elif isinstance(other, int):
            return self.__value != other
        else:
            return False

    def __lt__(self, other):
        if isinstance(other, Banknote):
            return self.__value < other.value
        elif isinstance(other, int):
            return self.__value < other
        else:
            return False

    def __gt__(self, other):
        if isinstance(other, Banknote):
            return self.__value > other.value
        elif isinstance(other, int):
            return self.__value > other
        else:
            return False

    def __le__(self, other):
        if isinstance(other, Banknote):
            return self.__value <= other.value
        elif isinstance(other, int):
            return self.__value <= other
        else:
            return False

    def __ge__(self, other):
        if isinstance(other, Banknote):
            return self.__value >= other.value
        elif isinstance(other, int):
            return self.__value >= other
        else:
            return False

    def __str__(self):
        return f"{self.__value}"
