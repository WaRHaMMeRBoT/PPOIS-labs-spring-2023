from abc import ABC
from animal import Animal
from plant import Plant
from typing import List, NoReturn
from ocean import SqrKm
import random


class Herbivore(Animal, ABC):

    #_required_nutritional_value: int

    def _eat(self, eatable: Plant) -> bool:
        if isinstance(eatable, Plant):
            if eatable.power() <= self.power():
                self._food_energy += eatable.be_eaten(self._required_nutritional_value)
                return True
        return False

    def _count_amount_of_eatable_plants(self, creations: List) -> int:
        amount_of_plants = 0
        for creation in creations:
            if isinstance(creation, Plant) and creation.power() <= self.power():
                amount_of_plants += 1
        return amount_of_plants

    def search_for_food(self, sqrkm: SqrKm) -> NoReturn:
        if not isinstance(sqrkm, SqrKm):
            raise TypeError
        if not self.is_dead():
            if self._count_amount_of_eatable_plants(sqrkm.creations) > 0:
                amount_of_eaten = random.randint(1, self._count_amount_of_eatable_plants(sqrkm.creations))
                eaten_counter = 0
                while eaten_counter < amount_of_eaten:
                    if Herbivore._eat(self, random.choice(sqrkm.creations)):
                        eaten_counter += 1


class Predator(Animal, ABC):

    def _eat(self, eatable: Animal) -> bool:
        if isinstance(eatable, Animal) and not isinstance(eatable, type(self)):
            if eatable.power() <= self.power():
                if not eatable.protect(self):
                    eatable.die()
                    self._food_energy += eatable.be_eaten(eatable._nutritional_value)
                return True
        return False

    def _count_amount_of_eatable(self, creations: List) -> int:
        amount_of_eatable = 0
        for entity in creations:
            if isinstance(entity, Animal) and entity.power() <= self.power() and not isinstance(entity, type(self)):
                amount_of_eatable += 1
        return amount_of_eatable

    def search_for_food(self, sqrkm: SqrKm) -> NoReturn:
        if not isinstance(sqrkm, SqrKm):
            raise TypeError
        if not self.is_dead():
            if self._count_amount_of_eatable(sqrkm.creations) > 0:
                while not Predator._eat(self, random.choice(sqrkm.creations)):
                    continue


class Predator(Predator, Herbivore, ABC):

    def search_for_food(self, sqrkm: SqrKm) -> NoReturn:
        if not isinstance(sqrkm, SqrKm):
            raise TypeError
        food_choice = random.randint(1, 4)
        if food_choice == 1:
            Predator.search_for_food(self, sqrkm)
        else:
            Herbivore.search_for_food(self, sqrkm)