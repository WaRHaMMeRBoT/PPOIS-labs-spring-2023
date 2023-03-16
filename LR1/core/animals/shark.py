from core.animals.animal import Animal
from core.enums.state_enum import StateEnum
from core.internal_settings.screen.coordinates import Coordinates
from core.internal_settings.stats import Stats


class Shark(Animal):
    def __init__(self, cords: Coordinates):
        super().__init__("Shark", cords, Stats(30, 2, 10, 5), StateEnum.IDLING, True)
