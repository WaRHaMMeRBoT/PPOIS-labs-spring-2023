from Animal import Animal
from Status import Status
from Stats import Stats
from Coordinates import Coordinates


class Gazelle (Animal):
    def __init__(self, cords: Coordinates):
        super().__init__("Gazelle", cords, Stats(20, 2, 1, 3), Status.Idling, False)
