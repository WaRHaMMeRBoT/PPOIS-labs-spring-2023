from random import randrange
from Coordinates import Coordinates
from Tile import Tile
from Gazelle import Gazelle
from Tiger import Tiger
from GameState import GameState


class Field:

    def __init__(self, height: int, width: int):
        self.__height = height
        self.__width = width
        self.__tiles = [[Tile(Coordinates(x, y), self) for y in range(width)]
                        for x in range(height)]

    @property
    def tiles(self):
        return self.__tiles

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    def tryMoveEntity(self, fromCords: Coordinates, toCords: Coordinates):
        tileToMoveFrom = self.tiles[fromCords.x][fromCords.y]
        tileToMoveTo = self.tiles[toCords.x][toCords.y]
        if tileToMoveTo.entity != None:
            return False
        entityToMove = tileToMoveFrom.entity
        entityToMove.cords = tileToMoveTo.cords
        tileToMoveFrom.removeEntity()
        tileToMoveTo.placeEntity(entityToMove)
        return True

    def spawnAnimalNearby(self, parentCords: Coordinates, name: str):
        x = parentCords.x
        y = parentCords.y
        for i in range(-1, 2, 1):
            for j in range(-1, 2, 1):
                if (self.areLegitCoordinates(x + i, y + j) and i != j != 0):
                    if (self.tiles[x + i][y + j].entity == None):
                        if (name == "Gazelle"):
                            animal = Gazelle(Coordinates(x + i, y + j))
                        elif (name == "Tiger"):
                            animal = Tiger(Coordinates(x + i, y + j))
                        self.tiles[x + i][y + j].placeEntity(animal)
                        GameState.addAnimal(animal)

    def spawnAnimalAnywhere(self, name: str):
        cords = Coordinates(randrange(0, self.height),
                            randrange(0, self.width))
        self.spawnAnimalNearby(cords, name)

    def areLegitCoordinates(self, x: int, y: int):
        return x >= 0 and y >= 0 and x < self.height and y < self.width
