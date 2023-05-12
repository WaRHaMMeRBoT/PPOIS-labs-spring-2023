from src.entity_class.prey import Prey


class Pig(Prey):
    def __init__(self, coords):
        super().__init__(idf='pig',
                         coord2d=coords,
                         speed=3,
                         movepts=4,
                         max_hp=35,
                         damage=2,
                         saturation_cap=40,
                         regen_rate=4,
                         reproduction_rate=8,
                         max_age=16)
