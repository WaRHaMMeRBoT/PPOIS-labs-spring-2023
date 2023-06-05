from entities.stations.Station import Station
from utility.Types import ContentType


class MixedStation(Station):
    def __init__(self, capacity_civ: int, capacity_cargo: int, init_amount: int = 0,
                 init_amount_cargo: int = 0) -> None:
        super().__init__(capacity_civ, init_amount, ContentType.MIXED)
        self.__capacity_cargo = capacity_cargo
        self.amount_cargo = init_amount_cargo

    def get_capacity_cargo(self) -> int:
        return self.__capacity_cargo

    def get_full_capacity(self) -> int:
        return self.get_capacity() + self.get_capacity_cargo()

    def get_typed_capacity(self, content_type: ContentType) -> int:
        match content_type:
            case ContentType.PASSENGER:
                return self.get_capacity()
            case ContentType.CARGO:
                return self.get_capacity_cargo()
            case ContentType.MIXED:
                return self.get_full_capacity()

    def get_full_amount(self) -> int:
        return self.amount + self.amount_cargo

    def get_amount_cargo(self) -> int:
        return self.amount_cargo

    def change_amount_cargo(self, amount: int, simulate: bool = False) -> int:
        old = self.amount_cargo
        amount = old if (old + amount) < 0 else amount
        amount = self.get_capacity_cargo() - old if (old + amount) > self.get_capacity_cargo() else amount
        if not simulate:
            self.amount_cargo += amount
        return abs(amount)
