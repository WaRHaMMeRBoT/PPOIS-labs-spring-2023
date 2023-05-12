
from entities.plant.cabbage import Cabbage
from entities.plant.grass import Grass
from entities.predator.bear import Bear
from entities.predator.fox import Fox
from entities.predator.turbofox import Turbofox
from entities.predator.wolf import Wolf
from entities.prey.horse import Horse
from entities.prey.pig import Pig
from entities.prey.pigboss import Pigboss
from entities.prey.rabbit import Rabbit
from entities.prey.sturmschwein import Sturmschwein
from src.entity_class.corpse import Corpse

from src.entity_class.entity import Entity


class Initializer:
    def __init__(self):
        self.entity_dict = {str: Entity}
        self.icon_dict = {str: str}

        self.add(Corpse, 'corpse', 'C')
        self.add(Cabbage, 'cabbage', '*')
        self.add(Grass, 'grass', '.')

        self.add(Fox, 'fox', 'F')
        self.add(Turbofox, 'turbofox', 'T')
        self.add(Wolf, 'wolf', 'W')
        self.add(Bear, 'bear', 'B')

        self.add(Rabbit, 'rabbit', 'R')
        self.add(Pig, 'pig', 'P')
        self.add(Pigboss, 'pigboss', 'B')
        self.add(Sturmschwein, 'sturmschwein', 'S')
        self.add(Horse, 'horse', 'H')

    def get_entity_dict(self):
        return self.entity_dict

    def get_icon_dict(self):
        return self.icon_dict

    def add(self, new_class, idf, icon):
        self.entity_dict[idf] = new_class
        self.icon_dict[idf] = icon
