from SRC.Entity_class.plant import Plant


class Birch(Plant):
    def __init__(self, coords):
        super().__init__(idf='birch',
                         coord2d=coords,
                         max_hp=100,
                         regen_rate=10,
                         reproduction_rate=7,
                         max_age=50)
