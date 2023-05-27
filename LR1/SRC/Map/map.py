
from API.initializer import Initializer
from SRC.Entity_class.animal import Animal
from SRC.Entity_class.corpse import Corpse
from SRC.Entity_class.entity import Entity
from SRC.Entity_class.plant import Plant
from SRC.Entity_class.herbivores import Herbivores
from SRC.Utility.coordinates2d import Coord2d
import random


class Map:
    def __init__(self, _height=35, _width=35):
        self.height = _height
        self.width = _width
        self.game_map = {(x, y): None for x in range(self.width) for y in range(self.height)}
        self.entity_list = list()
        initializer = Initializer()
        self.entity_dict = initializer.get_entity_dict()
        self.icon_dict = initializer.get_icon_dict()

    def print_map(self):
        print('#'*(self.width + 2))
        for y in range(self.height):
            out = '#'
            for x in range(self.width):
                icon = self.icon_dict[self.game_map[(x, y)].get_idf()] if self.game_map[(x, y)] is not None else ' '
                out += icon
            out += '#'
            print(out)
        print('#'*(self.width + 2))

    def get_entity_dict(self):
        return self.entity_dict

    def get_nearest_tile_by_condition(self, coord2d, condition_check=lambda x: None, max_radius=None):

        x, y = coord2d.x, coord2d.y
        if max_radius is None:
            radius = range(max(self.width, self.height))
        else:
            radius = range(max_radius + 1)

        for i in radius:
            rlist = [*range(-i, i + 1)]
            random.shuffle(rlist)
            for a in rlist:
                for b in rlist:
                    if 0 < x + a < self.width and 0 < y + b < self.height:
                        if condition_check(self.game_map[(x + a, y + b)]):
                            if self.game_map[(x + a, y + b)] is not None:
                                return self.game_map[(x + a, y + b)]
                            else:
                                return Coord2d(x + a, y + b)
        return None

    def get_nearest_free_tile(self, coord2d, max_radius=None):
        _lambda = lambda x: x is None
        tile = self.get_nearest_tile_by_condition(coord2d, _lambda, max_radius)
        return tile

    def get_nearest_pair(self, coord2d, idf, sex):
        _lambda = lambda x: x is not None and (x.get_idf() is idf) and (x.sex is not sex)
        return self.get_nearest_tile_by_condition(coord2d, _lambda)

    def get_nearest_herbivores(self, coord2d):
        _lambda = lambda x: x is not None and issubclass(x.__class__, Herbivores)
        return self.get_nearest_tile_by_condition(coord2d, _lambda)

    def get_nearest_plant(self, coord2d):
        _lambda = lambda x: x is not None and issubclass(x.__class__, Plant)
        return self.get_nearest_tile_by_condition(coord2d, _lambda)

    def get_nearest_corpse(self, coord2d):
        _lambda = lambda x: x is not None and issubclass(x.__class__, Corpse)
        return self.get_nearest_tile_by_condition(coord2d, _lambda)

    def add_entity(self, idf, coords=None):
        if coords is None:
            coords = Coord2d(random.randint(0, self.width), random.randint(0, self.height))
        self.entity_list.append(self.entity_dict[idf](coords))

    def get_entity(self, x, y):
        return self.game_map[(x, y)]

    def clear_state(self):
        self.entity_list = list()
        self.game_map = {(x, y): None for x in range(self.width) for y in range(self.height)}

    def reset_turn_sequence(self):
        if self.entity_list is not None:
            self.entity_list.sort()

    def kill(self, coords):
        entity = self.game_map[(coords.x, coords.y)]
        self.game_map[(coords.x, coords.y)] = None
        if entity in self.entity_list:
            self.entity_list.remove(entity)

    def get_entity_list(self):
        return self.entity_list

    def update(self):
        self.game_map = {(x, y): None for x in range(self.width) for y in range(self.height)}
        for entity in self.entity_list:
            if not entity.is_alive():
                self.entity_list.remove(entity)
                continue
            coords = entity.get_coords()
            x, y = coords.x, coords.y
            self.game_map[(x, y)] = entity
