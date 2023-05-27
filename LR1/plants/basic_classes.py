import random

class Diseases:
    def set_desiases():
        return random.choice([False, False, True])

class Plants:
    def __init__(self, _identifier, _name, _life_span):
        self._identifier = _identifier
        self._name = _name
        self._damage = 1
        self._diseases  = False
        self._water = 100
        self._alive = True
        self._life_span = _life_span
        self._location = []

    @property
    def identifier(self):
        return self._identifier
    
    @property
    def name(self):
        return self._name
    
    @property
    def damage(self):
        return self._damage

    @property
    def diseases(self):
        return self._diseases
    
    @property
    def water(self):
        return self._water
    
    @property
    def location(self):
        return self._location

    @damage.setter
    def damage(self, value):
        self._damage *= value

    @diseases.setter
    def diseases(self, value):
        self._diseases = value if self._diseases != False else False

    @water.setter
    def water(self, value):
        self._water += value
        if self._water > 100:
            self._water = 100

    @location.setter
    def location(self, value):
        self._location = value

    def next_move(self):
        self._life_span -= self.damage
        self._water -=10 
        if self._life_span <= 0 or self._water <= 0: 
            self._alive = False

class Fruit:
    def __init__(self, _identifier, _name):
        self._identifier = _identifier
        self._name = _name

    @property
    def identifier(self):
        return self._identifier
    
    @property
    def name(self):
        return self._name
