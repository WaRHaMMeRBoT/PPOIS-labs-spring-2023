from abc import abstractmethod

from Models.Plants.abstract_plants import BasePlant

from Models.Plants.trees import AppleTree, PearTree
from Models.Plants.vegetables import Cucumber


class Seed(BasePlant):
    def __init__(self, health: int = 100,
                 hydration_level: int = 100, age: int = 0, plant=None):
        self._ready_plant: None | BasePlant = plant
        super().__init__(health=health, hydration_level=hydration_level, age=age)

    @property
    def ready_plant(self):
        return self._ready_plant

    @ready_plant.setter
    def ready_plant(self, plant):
        self._ready_plant = plant

    def grow(self):
        if self.age == 5:
            self.set_plant()
        super().grow()

    @abstractmethod
    def set_plant(self):
        ...


class AppleSeed(Seed):
    def set_plant(self):
        self.ready_plant = AppleTree()


class CucumberSeed(Seed):
    def set_plant(self):
        self.ready_plant = PearTree()


class PearSeed(Seed):
    def set_plant(self):
        self.ready_plant = PearTree()
