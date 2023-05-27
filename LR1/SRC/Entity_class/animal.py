import random

from SRC.Entity_class.corpse import Corpse
from SRC.Entity_class.entity import Entity
from SRC.Utility.coordinates2d import Coord2d


class Animal(Entity):

    def __init__(self, idf, coord2d, max_hp, speed, movepts, damage,
                 saturation_cap, regen_rate, reproduction_rate, max_age):

        super().__init__(idf, coord2d, max_hp, speed, max_age)
        self.max_movepts = movepts
        self.cur_movepts = movepts
        self.damage = damage
        self.saturation_cap = saturation_cap
        self.current_saturation = saturation_cap
        self.regen_rate = regen_rate
        self.sex = random.randint(0, 1)
        self.reproduction_rate = reproduction_rate
        self.reproduction_bar = 0

    def action(self, map):
        raise NotImplementedError

    def starving_event(self, map):
        raise NotImplementedError

    def try_attack(self, entity):
        raise NotImplementedError

    def wander(self, map):
        rx, ry = random.randint(0, map.width), random.randint(0, map.height)
        coords = map.get_nearest_free_tile(Coord2d(rx, ry))
        self.move_to(coords)

    def move_to(self, coord2d):
        diff = coord2d - self.coord2d
        stepx = Coord2d(1 if diff.x > 0 else -1, 0)
        stepy = Coord2d(0, 1 if diff.y > 0 else -1)
        stepd = Coord2d(1 if diff.x > 0 else -1, 1 if diff.y > 0 else -1)
        di = min(abs(diff.x), abs(diff.y))
        xi = abs(diff.x) - di
        yi = abs(diff.y) - di
        while self.cur_movepts > 0 and (di + xi + yi) > 0:
            if xi > di and xi > yi:
                xi -= 1
                self.coord2d = self.coord2d + stepx
            elif yi > di and yi > xi:
                yi -= 1
                self.coord2d = self.coord2d + stepy
            else:
                di -= 1
                self.coord2d = self.coord2d + stepd
            self.cur_movepts -= 1

    def regenerate(self):
        regen = min(self.current_saturation, self.regen_rate, self.max_hp - self.current_hp)
        self.current_hp += regen
        self.current_saturation -= regen
        self.cur_movepts = self.max_movepts

    def die(self, map):
        self._is_alive = False
        map.kill(self.coord2d)
        map.get_entity_list().append(Corpse(self.coord2d, self.max_hp))

    def reproduction_event(self, map):
        if self.current_saturation < self.saturation_cap * 0.85:
            return

        self.reproduction_bar += 1

        entity = map.get_nearest_pair(self.coord2d, self.get_idf(), self.sex)
        if entity is None:
            return

        if self.reproduction_bar >= self.reproduction_rate:
            self.move_to(entity.get_coords())

            def try_reproduce():
                diff = entity.get_coords() - self.coord2d
                if abs(diff.x) + abs(diff.y) <= 1:
                    self.reproduction_bar = 0
                    entity.reproduction_bar = 0
                    self.reproduce(map)
            try_reproduce()
