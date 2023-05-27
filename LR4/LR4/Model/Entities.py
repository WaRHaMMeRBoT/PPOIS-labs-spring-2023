from random import randint
from Model import Coordinates
from Model import Object
from enum import Enum
import random

class Entity:
    pass

class Status(Enum):
    Mating = 0,
    Idling = 1,
    LookingForFood = 2,
    Hunting = 3,
    Eating = 4,
    Hiding = 5,
    Running = 6,
    LookingForMate = 7

class Animal(Entity):
    def __init__(self, name, cords, stats, status, isCarnivorous):
        self.__name: str = name
        self.__cords: Coordinates = cords
        self.__stats: Stats = stats
        self.__status: Status = status
        self.__isCarnivorous: bool = isCarnivorous
        self.__tookTurn: bool = False
        self.__mateCooldown: int = 3

    @property
    def name(self):
        return self.__name

    @property
    def cords(self):
        return self.__cords

    @cords.setter
    def cords(self, newCords: Coordinates):
        self.__cords = newCords

    @property
    def stats(self):
        return self.__stats

    @property
    def status(self):
        return self.__status

    @status.setter
    def status(self, newStatus: Status):
        self.__status = newStatus

    @property
    def isCarnivorous(self):
        return self.__isCarnivorous

    @property
    def tookTurn(self):
        return self.__tookTurn
    
    @tookTurn.setter
    def tookTurn(self, new: bool):
        self.__tookTurn = new

    @property
    def mateCooldown(self):
        return self.__mateCooldown
    
    @mateCooldown.setter
    def mateCooldown(self, newCd: int):
        self.__mateCooldown = newCd

class Tree(Entity):
    pass

class Wall(Entity):
    pass

class Gazelle (Animal):
    def __init__(self, cords: Coordinates):
        super().__init__("Gazelle", cords, Stats(20,2,1,3), Status.Idling, False)

class Tiger(Animal):
    def __init__(self, cords: Coordinates):
        super().__init__("Tiger", cords, Stats(30,2,10,5), Status.Idling, True)

class Stats:
    def __init__(self, health: int, speed: int, damage: int, sight: int):
        self.health = health
        self.currentHealth = health / 2
        self.speed = speed
        self.damage = damage
        self.sight = sight


