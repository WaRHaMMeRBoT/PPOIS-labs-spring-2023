from Entities.Herbivores.capybara import Capybara
from Entities.Herbivores.deer import Deer
from Entities.Herbivores.rabbit import Rabbit
from Entities.Plants.birch import Birch
from Entities.Plants.grass import Grass
from Entities.Plants.pumpkin import Pumpkin
from Entities.Predators.bear import Bear
from Entities.Predators.fox import Fox
from Entities.Predators.wolf import Wolf
from SRC.Entity_class.corpse import Corpse
from SRC.Entity_class.entity import Entity


class Initializer:
    def __init__(self):
        self.entity_dict = {str: Entity}
        self.icon_dict = {str: str}

        self.add(Capybara, 'capybara', 'P')
        self.add(Deer, 'deer', 'D')
        self.add(Rabbit, 'rabbit', 'R')

        self.add(Birch, 'birch', '|')
        self.add(Pumpkin, 'pumpkin', '*')
        self.add(Grass, 'grass', '.')

        self.add(Fox, 'fox', 'F')
        self.add(Wolf, 'wolf', 'W')
        self.add(Bear, 'bear', 'B')

        self.add(Corpse, 'corpse', 'C')


    def get_icon_dict(self):
        return self.icon_dict

    def add(self, new_class, idf, icon):
        self.entity_dict[idf] = new_class
        self.icon_dict[idf] = icon

    def get_entity_dict(self):
        return self.entity_dict
