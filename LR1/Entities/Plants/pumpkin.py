from SRC.Entity_class.plant import Plant


class Pumpkin(Plant):
    def __init__(self, coords):
        super().__init__(idf='pumpkin',
                         coord2d=coords,
                         max_hp=25,
                         regen_rate=5,
                         reproduction_rate=7,
                         max_age=16)
