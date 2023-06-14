from entities.stations.Station import Station
from utility.Types import ContentType


class PassengerStation(Station):
    def __init__(self, capacity: int, init_amount: int = 0) -> None:
        super().__init__(capacity, init_amount, ContentType.PASSENGER)
