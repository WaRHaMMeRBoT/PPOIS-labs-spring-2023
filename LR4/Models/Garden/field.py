import random
from Models.Plants.weed import Weed

class Field:
    def __init__(self, plant):
        self._weed = Weed() if random.randint(1, 5) == 2 else None
        if not self._weed:
            self._plant = plant
        else:
            self._plant = None

    def grow(self):
        if self.weed and self.plant:
            self.plant.health -= 10
            self.plant.get_dehydrated(5)
        if self.plant is not None:
            self.plant.grow()

    @property
    def weed(self):
        return self._weed

    @weed.setter
    def weed(self, value):
        self._weed = value

    @property
    def plant(self):
        return self._plant

    @plant.setter
    def plant(self, value):
        self._plant = value

class FieldAction:
    def __init__(self, field):
        self.field = field

    def weeding(self, plant):
        if self.field.weed is not None:
            self.field.weed = None
            self.field.plant = plant
        return self.field

    def desinfect_plant(self):
        if self.field.plant:
            self.field.plant.pests.destruction_power = 0
            self.field.plant.illness.destruction_power = 0
        return self.field

    def kill_plant(self):
        self.field.plant.die()

    def hydrate_field(self):
        if self.field.plant:
            self.field.plant.get_hydrated()
        return self.field

    def fertilizing(self):
        if self.field.plant:
            self.field.plant.health += 20
        return self.field
