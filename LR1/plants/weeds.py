from .basic_classes import Plants 
import random

class Pests:
    def __init__(self, _identifier, _name):
        self._identifier = _identifier
        self._name = _name
        self._damage = 1
        self._alive = True
        self._life_span = 5
        self._location = []
        self._damage_power = random.choice([1.25, 1.5, 1.75])

    @property
    def identifier(self):
        return self._identifier
    
    @property
    def name(self):
        return self._name
    
    @property
    def location(self):
        return self._location

    @location.setter
    def location(self, value):
        self._location = value

    def display_info(self):
        print(f"Name:{self._name} Left to live:{self._life_span}")

    def next_move(self):
        self._life_span -= self._damage
        if self._life_span <= 0: 
            self._alive = False
    
class Weed(Pests):
    def __init__(self, _identifier):
        super().__init__(_identifier, 'weed')

class Bugs(Pests):
    def __init__(self, _identifier):
        super().__init__(_identifier, 'bug')