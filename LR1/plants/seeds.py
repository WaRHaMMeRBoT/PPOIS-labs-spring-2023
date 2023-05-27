class Seeds:
    def __init__(self, _identifier, _name):
        self._identifier = _identifier
        self._name = _name
        self._water = 100
        self._location = []
        self._growth_time = 3

    @property
    def identifier(self):
        return self._identifier
    
    @property
    def name(self):
        return self._name
    
    @property
    def water(self):
        return self._water
    
    @property
    def location(self):
        return self._location

    @water.setter
    def water(self, value):
        self._water += value
        if self._water > 100:
            self._water = 100

    @location.setter
    def location(self, value):
        self._location = value

    def display_info(self):
        print(f"Name:{self._name}{self._identifier} Left to grow:{self._growth_time}")

    def next_move(self, garden):
        self._growth_time -= 1
        self._water -= 20
        if self._growth_time == 0:
            garden.grown_seed(self)
        