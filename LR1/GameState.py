from typing import List
from Animal import Animal


class GameState:

    CONST_REPOPULATION_CHANCE: int = 1000
    CONST_TREE_GROWTH_CHANCE: int = 10
    CONST_TREE_DEATH_CHANCE: int = 200
    CONST_BUSH_GROWTH_CHANCE: int = 8
    CONST_BUSH_DEATH_CHANCE: int = 400
    CONST_WALL_APPEAR_CHANCE: int = 1
    CONST_WALL_DISAPPEAR_CHANCE: int = 100
    CONST_FRUIT_APPEAR_CHANCE: int = 30
    CONST_FRUIT_TREE_PROXIMITY_APPEAR_CHANCE: int = 6000
    CONST_FRUIT_DISAPPEAR_CHANCE: int = 10000
    CONST_MEAT_DISAPPEAR_CHANCE: int = 1000

    __extinctionList: List[str] = ["Gazelle", "Tiger"]
    __speciesDictionary = dict(Gazelle=0, Tiger=0)
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
        if (GameState.__speciesDictionary[animal.name] == 3):
            GameState.__extinctionList.remove(animal.name)

    @staticmethod
    def removeAnimal(animal: Animal):
        GameState.__speciesDictionary[animal.name] -= 1
        GameState.__animalList.remove(animal)
        if (GameState.__speciesDictionary[animal.name] == 2):
            GameState.__extinctionList.append(animal.name)

    @staticmethod
    def iterate():
        GameState.__iteration += 1
