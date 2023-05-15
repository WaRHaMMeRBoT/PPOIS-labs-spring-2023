from src.entity_class.prey import Prey


class Horse(Prey):
    def __init__(self, coords):
        super().__init__(idf='horse',
                         coord2d=coords,
                         speed=5,
                         movepts=7,
                         max_hp=35,
                         damage=6,
                         saturation_cap=45,
                         regen_rate=5,
                         reproduction_rate=12,
                         max_age=22)
