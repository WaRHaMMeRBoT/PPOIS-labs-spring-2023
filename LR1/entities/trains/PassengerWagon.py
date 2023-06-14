from entities.trains.Wagon import Wagon
from utility.Types import ContentType


class PassengerWagon(Wagon):
    def __init__(self, capacity: int, init_amount: int = 0) -> None:
        super().__init__(capacity, init_amount, ContentType.PASSENGER)
