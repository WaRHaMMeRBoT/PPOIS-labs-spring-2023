from dataclasses import Field
from enum import Enum
from random import randrange
from typing import List
from GameState import GameState
from Gazelle import Gazelle
from Object import Object
from Tree import Tree
from Wall import Wall
from Animal import Animal
from Coordinates import Coordinates
from Entity import Entity
from Tiger import Tiger


class DisplayedSprite(Enum):
    empty = 0,
    fruit = 1,
    meat = 2,
    bush = 3,
    tree = 4,
    wall = 5,
    gazelle = 6,
    tiger = 7


class Tile:
    def __init__(self, cords: Coordinates, field):
        self.__object: Object = None
        self.__entity: Entity = None
        self.__cords: Coordinates = cords
        self.__field: Field = field
        self.__displayedSprite: DisplayedSprite = DisplayedSprite.empty

    @property
    def object(self):
        return self.__object

    @property
    def entity(self):
        return self.__entity

    @property
    def cords(self):
        return self.__cords

    @property
    def field(self):
        return self.__field

    @property
    def displayedSprite(self):
        return self.__displayedSprite

    def trySpawnCycle(self, field):
        if (self.entity == None and self.object == None):
            if (self.isBorderTile()):
                for species in GameState.getExtinctionList():
                    if (self.__tryRepopulate(species)):
                        return
            elif (self.__tryPlaceEntity(Tree(), GameState.CONST_TREE_GROWTH_CHANCE)):
                return
            elif (self.__tryPlaceEntity(Wall(), GameState.CONST_WALL_APPEAR_CHANCE)):
                return
            elif (self.__tryPlaceObject(Object.bush, GameState.CONST_BUSH_GROWTH_CHANCE)):
                return
            elif (self.__inTreeProximity(field)):
                if (self.__tryPlaceObject(Object.fruit, GameState.CONST_FRUIT_TREE_PROXIMITY_APPEAR_CHANCE)):
                    return
            else:
                if (self.__tryPlaceObject(Object.fruit, GameState.CONST_FRUIT_APPEAR_CHANCE)):
                    return
        elif (self.entity == None):
            if (self.object == Object.fruit):
                self.__tryRemoveObject(GameState.CONST_FRUIT_DISAPPEAR_CHANCE)
            elif (self.object == Object.bush):
                self.__tryRemoveObject(GameState.CONST_BUSH_DEATH_CHANCE)
            elif (self.object == Object.meat):
                self.__tryRemoveObject(GameState.CONST_MEAT_DISAPPEAR_CHANCE)
        else:
            if (isinstance(self.entity, Tree)):
                self.__tryRemoveEntity(GameState.CONST_TREE_DEATH_CHANCE)
            elif (isinstance(self.entity, Wall)):
                self.__tryRemoveEntity(GameState.CONST_WALL_DISAPPEAR_CHANCE)

    def __tryRepopulate(self, species: List[str]):
        if (randrange(100000) <= GameState.CONST_REPOPULATION_CHANCE):
            if (species == "Gazelle"):
                self.__entity = Gazelle(self.cords)
            elif (species == "Tiger"):
                self.__entity = Tiger(self.cords)
            self.__resetDisplayedSprite()
            GameState.addAnimal(self.entity)
            return True
        return False

    def placeEntity(self, entity: Entity):
        self.__entity = entity
        self.__resetDisplayedSprite()

    def removeEntity(self):
        self.__entity = None
        self.__resetDisplayedSprite()

    def removeObject(self):
        self.__object = None
        self.__resetDisplayedSprite()

    def placeObject(self, newObject: Object):
        self.__object = newObject
        self.__resetDisplayedSprite()

    def __tryPlaceEntity(self, entity, chance: int):
        if (randrange(100000) <= chance):
            self.placeEntity(entity)
            return True
        return False

    def __tryPlaceObject(self, theObject, chance: int):
        if (randrange(100000) <= chance):
            self.placeObject(theObject)
            return True
        return False

    def __tryRemoveObject(self, chance: int):
        if (randrange(100000) <= chance):
            self.removeObject()
            return True
        return False

    def __tryRemoveEntity(self, chance: int):
        if (randrange(100000) <= chance):
            self.removeEntity()
            return True
        return False

    def killEntity(self):
        if (isinstance(self.entity, Animal)):
            if (self.entity.isCarnivorous == False):
                self.__object = Object.meat
            GameState.removeAnimal(self.entity)
        self.removeEntity()

    def __inTreeProximity(self, field):
        x = self.cords.x
        y = self.cords.y
        for i in range(-1, 2, 1):
            for j in range(-1, 2, 1):
                if (field.areLegitCoordinates(x + i, y + j)):
                    if (isinstance(self.field.tiles[x + i][y + j].entity, Tree)):
                        return True
        return False

    def isBorderTile(self):
        x = self.cords.x
        y = self.cords.y
        return x == 0 or y == 0 or x == self.field.height - 1 or y == self.field.width - 1

    def __resetDisplayedSprite(self):
        if (self.entity != None):
            if (isinstance(self.entity, Gazelle)):
                self.__displayedSprite = DisplayedSprite.gazelle
            elif (isinstance(self.entity, Tiger)):
                self.__displayedSprite = DisplayedSprite.tiger
            elif (isinstance(self.entity, Wall)):
                self.__displayedSprite = DisplayedSprite.wall
            elif (isinstance(self.entity, Tree)):
                self.__displayedSprite = DisplayedSprite.tree
        elif (self.object != None):
            if (self.object == Object.fruit):
                self.__displayedSprite = DisplayedSprite.fruit
            elif (self.object == Object.meat):
                self.__displayedSprite = DisplayedSprite.meat
            elif (self.object == Object.bush):
                self.__displayedSprite = DisplayedSprite.bush
        else:
            self.__displayedSprite = DisplayedSprite.empty
