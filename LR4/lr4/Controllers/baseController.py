from tokenize import String

from tabulate import tabulate

from lr4.garden.garden import load
from lr4.garden.plants import whatThePlant, whatTheSeed


class BaseController:
    def __init__(self):
        self.garden = load()

    def get_plants(self):
        return self.garden.model.matrix

    def view(self) -> str:
        print(tabulate(self.garden.model.print()))
        return tabulate(self.garden.model.print())

    def add(self, plant_name: str, x: int, y: int):
        plant = whatThePlant(plant_name)
        self.garden.model.addEntity(plant, x=x, y=y)
        self.garden.model.garbageCollector()
        self.garden.warp(1)
        self.garden.model.save()

    def add_seed(self, seed_name: str, x: int, y: int):
        seed = whatTheSeed(seed_name)
        self.garden.model.addEntity(seed, x, y)
        self.garden.model.garbageCollector()
        self.garden.warp(1)
        self.garden.model.save()

    def remove(self, x: int, y: int):
        self.garden.model.removeEntity(x, y)
        self.garden.model.garbageCollector()
        self.garden.warp(1)
        self.garden.model.save()

    def weather(self, type: str, time: int):
        self.garden.model.weather.weather = type
        self.garden.model.weather.time = time
        self.garden.model.garbageCollector()
        self.garden.warp(1)
        self.garden.model.save()

    def warp(self, time: int):
        for i in range(0, time):
            self.garden.warp(i)
            self.garden.model.garbageCollector()
        self.garden.model.save()
