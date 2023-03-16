from random import randrange

from core.animals.keta import Keta
from core.animals.shark import Shark
from core.internal_settings.screen.coordinates import Coordinates
from core.internal_settings.game_state import GameState
from core.internal_settings.screen.tile import Tile


class Field:
    def __init__(self, height: int, width: int):
        self.__height = height
        self.__width = width
        self.__tiles = [
            [Tile(Coordinates(x, y), self) for y in range(width)] for x in range(height)
        ]

    @property
    def tiles(self):
        return self.__tiles

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    def move_entity(self, from_cords: Coordinates, to_cords: Coordinates):
        tile_move_from = self.tiles[from_cords.x][from_cords.y]
        tile_move_to = self.tiles[to_cords.x][to_cords.y]
        if tile_move_to.entity is not None:
            return False
        entity_to_move = tile_move_from.entity
        entity_to_move.cords = tile_move_to.cords
        tile_move_from.remove_entity()
        tile_move_to.place_entity(entity_to_move)
        return True

    def spawn_animal_nearby(self, parent_cords: Coordinates, name: str):
        x = parent_cords.x
        y = parent_cords.y
        for i in range(-1, 2, 1):
            for j in range(-1, 2, 1):
                if self.if_legit_cords(x + i, y + j) and i != j != 0:
                    if self.tiles[x + i][y + j].entity is None:
                        if name == "Keta":
                            animal = Keta(Coordinates(x + i, y + j))
                        elif name == "Shark":
                            animal = Shark(Coordinates(x + i, y + j))
                        self.tiles[x + i][y + j].place_entity(animal)
                        GameState.addAnimal(animal)

    def spawn_animal_anywhere(self, name: str):
        cords = Coordinates(randrange(0, self.height), randrange(0, self.width))
        self.spawn_animal_nearby(cords, name)

    def if_legit_cords(self, x: int, y: int):
        return 0 <= x < self.height and 0 <= y < self.width
