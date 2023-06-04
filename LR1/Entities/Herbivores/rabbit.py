from SRC.Entity_class.herbivores import Herbivores


class Rabbit(Herbivores):
    def __init__(self, coords):
        super().__init__(idf='rabbit',
                         coord2d=coords,
                         speed=3,
                         movepts=3,
                         max_hp=12,
                         damage=1,
                         saturation_cap=20,
                         regen_rate=3,
                         reproduction_rate=5,
                         max_age=11)
