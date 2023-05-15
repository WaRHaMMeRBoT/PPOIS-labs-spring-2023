from src.entity_class.predator import Predator


class Bear(Predator):
    def __init__(self, coords):
        super().__init__(idf='bear',
                         coord2d=coords,
                         speed=5,
                         movepts=5,
                         max_hp=80,
                         damage=25,
                         saturation_cap=60,
                         regen_rate=12,
                         reproduction_rate=22,
                         max_age=45)
