from Animal import Animal
from Status import Status
from Stats import Stats
from Coordinates import Coordinates


class Tiger(Animal):
    def __init__(self, cords: Coordinates):
        super().__init__("Tiger", cords, Stats(30, 2, 10, 5), Status.Idling, True)
