from src.entity_class.predator import Predator


class Fox(Predator):
    def __init__(self, coords):
        super().__init__(idf='fox',
                         coord2d=coords,
                         speed=8,
                         movepts=4,
                         max_hp=30,
                         damage=12,
                         saturation_cap=35,
                         regen_rate=9,
                         reproduction_rate=12,
                         max_age=28)
