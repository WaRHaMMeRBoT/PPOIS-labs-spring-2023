from src.entity_class.plant import Plant


class Cabbage(Plant):
    def __init__(self, coords):
        super().__init__(idf='cabbage',
                         coord2d=coords,
                         max_hp=25,
                         regen_rate=5,
                         reproduction_rate=7,
                         max_age=16)
