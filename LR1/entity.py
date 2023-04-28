from util import clamp
from random import randrange, randint, random
from abc import ABC, abstractmethod


class entity:
    def __init__(self, name: str, health, max_health, size, eats, data) -> None:
        self.name = name
        self.max_health = max_health if max_health > 0 else 0
        self.health = clamp(health, 0, self.max_health)
        self.size = size if size > 0 else 0
        self.is_die = not bool(clamp(self.health, 0, self.max_health))
        self.callback = None
        self.eats = eats
        self.data = data

    def __repr__(self) -> str:
        return f"{self.name}: {self.health}"

    def dump(self):
        ent_data = dict(self.__dict__)
        ent_data.pop('health', None)
        ent_data.pop('name', None)
        ent_data.pop('is_die', None)
        ent_data['type'] = self.__class__.__name__
        return ent_data

    def info(self):
        return [self.health]

    @abstractmethod
    def move(self):
        pass

    def process(self):
        if self.callback:
            self.callback()

        self.is_die = not bool(clamp(self.health, 0, self.max_health))


MALE = 0
FEMALE = 1


class animal(entity):
    def __init__(self, name="animal", health=0, sex=MALE, **kwargs) -> None:
        super().__init__(name, health, kwargs['max_health'],
                         kwargs['size'], kwargs['eats'], kwargs['data'])
        self.starving = clamp(kwargs['starving'], 0, 1)
        self.speed = kwargs['speed'] if kwargs['speed'] > 0 else 0
        self.dodge_chance = kwargs['dodge_chance']
        self.sex = MALE if sex == 'MALE' else FEMALE
        self.callback = self._process

    def _process(self):
        self.health -= self.max_health*self.starving

    def __repr__(self) -> str:
        return super().__repr__() + (' F' if self.sex else ' M')

    def info(self):
        inf = super().info()
        inf.append("FEMALE" if self.sex else "MALE")
        return inf

    def dump(self):
        ent_data = dict(self.__dict__)
        ent_data.pop('health', None)
        ent_data.pop('name', None)
        ent_data.pop('is_die', None)
        ent_data.pop('sex')
        ent_data.pop('callback')
        ent_data['type'] = self.__class__.__name__
        return ent_data

    def move(self):
        return (randint(-1, 1)*randint(1, self.speed),
                randint(-1, 1)*randint(1, self.speed))

    def is_love(self, other):
        return self.sex != other.sex

    def is_dodge(self):
        return random() < self.dodge_chance


class plant(entity):
    def __init__(self, name="plant", health=0, **kwargs) -> None:
        super().__init__(name, health, kwargs['max_health'],
                         kwargs['size'], kwargs['eats'], kwargs['data'])

    def dump(self):
        ent_data = dict(self.__dict__)
        ent_data.pop('health', None)
        ent_data.pop('name', None)
        ent_data.pop('is_die', None)
        ent_data['type'] = self.__class__.__name__
        return ent_data

    def move(self):
        return (0, 0)
