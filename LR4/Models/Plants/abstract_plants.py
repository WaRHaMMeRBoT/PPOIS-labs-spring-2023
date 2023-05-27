import random
from abc import ABC, abstractmethod
from math import floor

class AbstractPlant(ABC):

    @abstractmethod
    def grow(self):
        raise NotImplementedError

    @abstractmethod
    def die(self):
        raise NotImplementedError

    @abstractmethod
    def get_dehydrated(self):
        raise NotImplementedError

    @abstractmethod
    def get_hydrated(self):
        raise NotImplementedError


class BasePlant(AbstractPlant):
    def __init__(self, health = 100,
                 hydration_level = 100, age = 0):
        self.illness = Illness()
        self._age = age
        self._health = health
        self._hydration_level = hydration_level
        self._dead = False
        self.pests = Pests()
        if random.randint(1, 4) == 1:
            self.pests.destruction_power = 0
        if random.randint(1, 4) == 2:
            self.illness.destruction_power = 0

    def grow(self):
        self.age += 1
        if self.hydration_level > 50:
            impact = floor(self.hydration_level * .1) \
                     - self.illness.destruction_power - self.pests.destruction_power
            self.health += impact
        else:
            self.health -= abs(
                floor(self.hydration_level * .1)) + self.illness.destruction_power + self.pests.destruction_power
        self.get_dehydrated()
        if self.health <= 0:
            self.die()

    def die(self):
        self._dead = True

    @property
    def dead(self):
        return self._dead

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        self._age = value

    @property
    def health(self):
        return self._health

    @health.setter
    def health(self, value):
        self._health = value
        if self._health > 100:
            self._health = 100

    @property
    def hydration_level(self):
        return self._hydration_level

    @hydration_level.setter
    def hydration_level(self, value):
        self._hydration_level = value
        if self._hydration_level > 100:
            self._hydration_level = 100

    def get_dehydrated(self, value = 15):
        self.hydration_level -= value
        if self.hydration_level <= 0:
            self.die()

    def get_hydrated(self, value = 15):
        self.hydration_level += value

    def __str__(self):
        return self.__class__.__name__

class Fruit(BasePlant):...

class Vegetable(BasePlant): ...

class Tree(BasePlant):
    def __init__(self, health = 100,
                 hydration_level = 100, age = 0, fruit=None):
        self._fruit = fruit
        super().__init__(health=health, hydration_level=hydration_level, age=age)

    def grow(self):
        if self.age > 5:
            self.create_fruit()
        super().grow()

    @abstractmethod
    def create_fruit(self):
        raise NotImplementedError

    @property
    def fruit(self):
        return self._fruit

    @fruit.setter
    def fruit(self, fruit):
        self._fruit = fruit

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        self._age = age
        if self.fruit:
            self.fruit.age = age - 5

    @property
    def health(self):
        return self._health

    @health.setter
    def health(self, value):
        self._health = value
        if self._health > 100:
            self._health = 100
        if self.fruit:
            self.fruit.health = self.health

    @property
    def hydration_level(self):
        return self._hydration_level

    @hydration_level.setter
    def hydration_level(self, value):
        self._hydration_level = value
        if self.hydration_level > 100:
            self._hydration_level = 100
        if self.fruit:
            self.fruit.hydration_level = self.hydration_level

    def get_dehydrated(self, value = 15):
        self.hydration_level -= value
        if self.hydration_level <= 0:
            self.die()

    def get_hydrated(self, value = 15):
        self.hydration_level += value


class Illness:
    def __init__(self):
        self._destruction_power = random.randint(10, 20)

    @property
    def destruction_power(self):
        return self._destruction_power

    @destruction_power.setter
    def destruction_power(self, value):
        self._destruction_power = value


class Pests:
    def __init__(self):
        self._destruction_power = random.randint(10, 20)

    @property
    def destruction_power(self):
        return self._destruction_power

    @destruction_power.setter
    def destruction_power(self, value):
        self._destruction_power = value
