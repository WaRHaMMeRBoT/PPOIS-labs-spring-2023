from typing import List

from core.animals.animal import Animal
from core.settings import settings


class GameState:
    CONST_REPOPULATION_CHANCE = settings.CONST_REPOPULATION_CHANCE
    CONST_TREE_GROWTH_CHANCE = settings.CONST_TREE_GROWTH_CHANCE
    CONST_TREE_DEATH_CHANCE = settings.CONST_TREE_DEATH_CHANCE
    CONST_BUSH_GROWTH_CHANCE = settings.CONST_BUSH_GROWTH_CHANCE
    CONST_BUSH_DEATH_CHANCE = settings.CONST_BUSH_DEATH_CHANCE
    CONST_OBSTACLE_APPEAR_CHANCE = settings.CONST_OBSTACLE_APPEAR_CHANCE
    CONST_OBSTACLE_DISAPPEAR_CHANCE = settings.CONST_OBSTACLE_DISAPPEAR_CHANCE
    CONST_FRUIT_APPEAR_CHANCE = settings.CONST_FRUIT_APPEAR_CHANCE
    CONST_FRUIT_TREE_PROXIMITY_APPEAR_CHANCE = (
        settings.CONST_FRUIT_TREE_PROXIMITY_APPEAR_CHANCE
    )
    CONST_FRUIT_DISAPPEAR_CHANCE = settings.CONST_FRUIT_DISAPPEAR_CHANCE
    CONST_MEAT_DISAPPEAR_CHANCE = settings.CONST_MEAT_DISAPPEAR_CHANCE

    __extinctionList: List[str] = ["Keta", "Shark"]
    __speciesDictionary = dict(Keta=0, Shark=0)
    __animalList = []
    __iteration = 0

    @staticmethod
    def getSpeciesDictionary():
        return GameState.__speciesDictionary

    @staticmethod
    def getExtinctionList():
        return GameState.__extinctionList

    @staticmethod
    def getAnimalList():
        return GameState.__animalList

    @staticmethod
    def getIteration():
        return GameState.__iteration

    @staticmethod
    def addAnimal(animal: Animal):
        GameState.__speciesDictionary[animal.name] += 1
        GameState.__animalList.append(animal)
        if GameState.__speciesDictionary[animal.name] == 3:
            GameState.__extinctionList.remove(animal.name)

    @staticmethod
    def removeAnimal(animal: Animal):
        GameState.__speciesDictionary[animal.name] -= 1
        GameState.__animalList.remove(animal)
        if GameState.__speciesDictionary[animal.name] == 2:
            GameState.__extinctionList.append(animal.name)

    @staticmethod
    def iterate():
        GameState.__iteration += 1
