from core.animals.animal import Animal
from core.enums.state_enum import StateEnum
from core.internal_settings.screen.coordinates import Coordinates
from core.internal_settings.stats import Stats


class Keta(Animal):
    def __init__(self, cords: Coordinates):
        super().__init__("Keta", cords, Stats(20, 2, 1, 3), StateEnum.IDLING, False)
