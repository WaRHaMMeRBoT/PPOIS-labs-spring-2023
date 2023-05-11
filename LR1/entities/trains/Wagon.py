from entities.Storage import Storage
from entities.stations.Station import Station
from utility.Types import ContentType


class Wagon(Storage):
    def __init__(self, capacity: int, init_amount: int = 0, content_type: ContentType = ContentType.UNKNOWN) -> None:
        super().__init__(capacity, init_amount, content_type)

    def can_load_into(self, load_into: Station) -> bool:
        type_check = (load_into.get_type() == ContentType.MIXED) or (load_into.get_type() == self.get_type())
        return type_check

    def can_unload_from(self, unload_from: Station) -> bool:
        return self.can_load_into(unload_from)

    def load_into(self, amount: int, load_into: Station) -> bool:
        if self.can_load_into(load_into):
            self.change_amount(-load_into.change_amount(amount))
            return True
        return False

    def unload_from(self, amount: int, unload_from: Station) -> bool:
        if self.can_unload_from(unload_from):
            if unload_from.get_type() == ContentType.MIXED:
                if self.get_type() == ContentType.CARGO:
                    self.change_amount(unload_from.change_amount_cargo(-amount))
                else:
                    self.change_amount(unload_from.change_amount(-amount))
            else:
                self.change_amount(unload_from.change_amount(-amount))

            return True
        return False
