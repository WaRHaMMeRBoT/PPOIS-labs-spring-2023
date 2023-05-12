import random

from src.entity_class.entity import Entity


class Plant(Entity):

    def __init__(self, idf, coord2d, max_hp, regen_rate, reproduction_rate, max_age):
        super().__init__(idf, coord2d, max_hp, 0, max_age)
        self.regen_rate = regen_rate
        self.reproduction_rate = reproduction_rate
        self.reproduction_bar = 0

    def action(self, game_map):
        self.aging_event(game_map)

        def regenerate():
            if self.max_hp - self.current_hp < self.regen_rate:
                self.current_hp += self.regen_rate
            else:
                self.current_hp = self.max_hp
        regenerate()

        def reproduction_event():
            self.reproduction_bar += 1

            if self.reproduction_bar >= self.reproduction_rate:
                if random.randint(0, 5) == 1:
                    self.reproduction_bar = 0
                    self.reproduce(game_map, 1)
        reproduction_event()

        game_map.update()
