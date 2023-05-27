from Model.Coordinates import Coordinates
from Model.Tile import Tile

class Field:
    def __init__(self, height: int, width: int):
        self.__height = height
        self.__width = width
        self.__tiles = [[Tile(Coordinates(x,y), self) for y in range(width)]
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

