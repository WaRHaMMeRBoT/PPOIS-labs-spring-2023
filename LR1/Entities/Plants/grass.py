from SRC.Entity_class.plant import Plant


class Grass(Plant):
    def __init__(self, coords):
        super().__init__(idf='grass',
                         coord2d=coords,
                         max_hp=8,
                         regen_rate=2,
                         reproduction_rate=5,
                         max_age=11)
