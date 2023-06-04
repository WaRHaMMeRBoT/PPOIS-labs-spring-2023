from SRC.Entity_class.herbivores import Herbivores


class Capybara(Herbivores):
    def __init__(self, coords):
        super().__init__(idf='capybara',
                         coord2d=coords,
                         speed=5,
                         movepts=5,
                         max_hp=1000,
                         damage=50,
                         saturation_cap=100,
                         regen_rate=100,
                         reproduction_rate=1,
                         max_age=1000)
