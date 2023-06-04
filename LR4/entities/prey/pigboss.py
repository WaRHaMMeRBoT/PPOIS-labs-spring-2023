from src.entity_class.prey import Prey


class Pigboss(Prey):
    def __init__(self, coords):
        super().__init__(idf='pigboss',
                         coord2d=coords,
                         speed=2,
                         movepts=2,
                         max_hp=80,
                         damage=5,
                         saturation_cap=100,
                         regen_rate=8,
                         reproduction_rate=10,
                         max_age=24)
