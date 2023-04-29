from abc import ABC, abstractmethod
import random


class LivingEntity(ABC):

    @abstractmethod
    def is_ready_to_die(self):
        pass


class Animal(LivingEntity):

    def __init__(self, x, y, age, saturation, gender):
        super().__init__()
        self.x = x
        self.y = y
        if age is None:
            self.age = 0
            self.gender = "M" if random.randint(0, 1) == 1 else "W"
            self.saturation = random.randint(4, 7)
        else:
            self.age = age
            self.saturation = saturation
            self.gender = gender

    @abstractmethod
    def is_ready_to_die(self):
        pass

    @abstractmethod
    def is_ready_to_reproduction(self):
        pass

    @abstractmethod
    def eat(self):
        pass

    @abstractmethod
    def move(self, map_size):
        new_x = random.randint(0, map_size - 1)
        new_y = random.randint(0, map_size - 1)
        self.x = new_x
        self.y = new_y

    @abstractmethod
    def getting_old(self):
        self.age += 0.3
        self.saturation -= 0.5
