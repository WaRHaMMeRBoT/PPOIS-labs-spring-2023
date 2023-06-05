from src.entity_class.prey import Prey


class Sturmschwein(Prey):
    def __init__(self, coords):
        super().__init__(idf='sturmschwein',
                         coord2d=coords,
                         speed=5,
                         movepts=3,
                         max_hp=40,
                         damage=8,
                         saturation_cap=40,
                         regen_rate=6,
                         reproduction_rate=10,
                         max_age=21)