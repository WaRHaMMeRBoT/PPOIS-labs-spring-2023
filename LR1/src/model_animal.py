from random import randint


class Animal:

    def __init__(self, age, size, hunger, sex=None):
        self._age = age
        self._size = size
        self._hunger = hunger
        if sex is None:
            self._sex = randint(1, 2)
        else:
            self._sex = sex

    def to_dict(self):
        data = dict()
        data["name"] = self.__class__.__name__
        data["age"] = self._age
        data["size"] = self._size
        data["hunger"] = self._hunger
        data["sex"] = self._sex
        return data

    def get_size(self):
        return self._size

    def get_age(self):
        return self._age

    def get_sex(self):
        return self._sex

    def get_hunger(self):
        return self._hunger

    def iteration(self):
        self._age -= 1
        self._hunger -= 10

    def nutrition(self, prey):
        self._hunger += prey.get_size() * 10

    def is_dead(self):
        return self._hunger <= 0 and self._age <= 0
