from src.entity_class.animal import Animal
from src.util.coordinates2d import *


class Prey(Animal):

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

    def action(self, game_map):
        self.aging_event(game_map)
        self.regenerate()
        self.starving_event(game_map)
        self.reproduction_event(game_map)
        self.wander(game_map)
        game_map.update()

    def starving_event(self, game_map):
        if self.current_saturation == 0:
            self.receive_damage(1, game_map)

        entity = game_map.get_nearest_plant(self.coord2d)
        if entity is None:
            return

        if self.current_saturation < self.saturation_cap * 0.9:
            self.move_to(entity.get_coords())
            self.try_attack(entity)

    def try_attack(self, entity):
        diff = entity.get_coords() - self.coord2d
        if abs(diff.x) + abs(diff.y) <= 1:
            damage = entity.receive_damage(self.damage)
            self.current_saturation += damage
