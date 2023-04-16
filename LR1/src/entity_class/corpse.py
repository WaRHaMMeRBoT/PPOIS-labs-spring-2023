from src.entity_class.entity import Entity
from src.util.coordinates2d import Coord2d


class Corpse(Entity):

    def __init__(self, coord2d, _max_hp=35):
        super().__init__('corpse', coord2d, _max_hp, 0, 50)

    def action(self, game_map):
        self.aging_event(game_map)
        self.receive_damage(1, game_map)
