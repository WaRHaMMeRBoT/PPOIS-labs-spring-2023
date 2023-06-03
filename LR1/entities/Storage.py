from utility.Types import ContentType


class Storage:
    def __init__(self, capacity: int, init_amount: int = 0, content_type: ContentType = ContentType.UNKNOWN) -> None:
        self.__capacity = capacity
        self.amount = init_amount
        self.__type = content_type

    def get_capacity(self) -> int:
        return self.__capacity

    def get_amount(self) -> int:
        return self.amount

    def change_amount(self, amount: int, simulate: bool = False) -> int:
        old = self.amount
        amount = old if (old + amount) < 0 else amount
        amount = self.get_capacity() - old if (old + amount) > self.get_capacity() else amount
        if not simulate:
            self.amount += amount
        return abs(amount)

    def missing_amount(self) -> int:
        return self.__capacity - self.amount

    def get_type(self) -> ContentType:
        return self.__type
