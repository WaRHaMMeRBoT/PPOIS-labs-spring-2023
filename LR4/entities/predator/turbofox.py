from src.entity_class.predator import Predator


class Turbofox(Predator):
    def __init__(self, coords):
        super().__init__(idf='turbofox',
                         coord2d=coords,
                         speed=9,
                         movepts=5,
                         max_hp=35,
                         damage=12,
                         saturation_cap=40,
                         regen_rate=10,
                         reproduction_rate=14,
                         max_age=25)
