from src.entity_class.predator import Predator


class Wolf(Predator):
    def __init__(self, coords):
        super().__init__(idf='wolf',
                         coord2d=coords,
                         speed=7,
                         movepts=4,
                         max_hp=55,
                         damage=20,
                         saturation_cap=55,
                         regen_rate=15,
                         reproduction_rate=18,
                         max_age=38)
