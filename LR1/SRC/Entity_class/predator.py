from SRC.Entity_class.animal import Animal
from SRC.Entity_class.corpse import Corpse
from SRC.Utility.coordinates2d import *


class Predator(Animal):

    def __init__(self,
                 idf,
                 coord2d,
                 speed,
                 movepts,
                 max_hp,
                 damage,
                 saturation_cap,
                 regen_rate,
                 reproduction_rate,
                 max_age):
        super().__init__(idf, coord2d, max_hp, speed, movepts, damage, saturation_cap,
                         regen_rate, reproduction_rate, max_age)

    def action(self, map):
        self.aging_event(map)
        self.regenerate()
        self.starving_event(map)
        self.reproduction_event(map)
        self.wander(map)
        map.update()

    def try_attack(self, entity):
        diff = entity.get_coords() - self.coord2d
        if abs(diff.x) + abs(diff.y) <= 1:
            damage = entity.receive_damage(self.damage)
            if issubclass(entity, Corpse):
                self.current_saturation += damage

    def starving_event(self, map):
        if self.current_saturation == 0:
            self.receive_damage(3, map)

        if self.current_saturation > self.saturation_cap * 0.9:
            return

        entity = map.get_nearest_corpse()
        if entity is None:
            entity = map.get_nearest_herbivores()
        if entity is None:
            return

        if get_coord_radius(self.get_coords(), entity.get_coords()) < 6:
            self.move_to(entity.get_coords())
            self.try_attack(entity)

