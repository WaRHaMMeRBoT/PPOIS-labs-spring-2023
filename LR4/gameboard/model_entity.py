from .model_animal import Animal
from random import randint


class Wolf(Animal):
    def __init__(self, age=10, size=2, hunger=60, sex=None):
        super().__init__(age, size, hunger, sex)

    def __str__(self):
        return "W"


class Rabbit(Animal):
    def __init__(self, age=10, size=1, hunger=70, sex=None):
        super().__init__(age, size, hunger, sex)

    @staticmethod
    def chance_to_escape():
        return randint(0, 100) > 30

    def __str__(self):
        return "R"


class Plant:
    def __init__(self, age=8, size=1):
        self.__age = age
        self.__size = size

    def __str__(self):
        return "P"

    def to_dict(self):
        data = dict()
        data["name"] = "Plant"
        data["age"] = self.__age
        data["size"] = self.__size
        return data

    def get_size(self):
        return self.__size

    def heal_plant(self):
        self.__age = 8

    def iteration(self):
        self.__age -= 1

    def is_dead(self):
        return self.__age <= 0
