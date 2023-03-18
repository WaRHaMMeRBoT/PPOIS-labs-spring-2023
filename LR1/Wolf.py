from LivingEntities import Animal


class Wolf(Animal):

    def __init__(self, x, y, age=None, saturation=None, gender=None, max_age=None, max_saturation=None):
        super().__init__(x, y, age, saturation, gender)
        if max_age is None or max_saturation is None:
            self.max_age = 15
            self.max_saturation = 10
        else:
            self.max_age = max_age
            self.max_saturation = max_saturation

    def is_ready_to_reproduction(self):
        return self.age > 4 and self.saturation > 3

    def is_ready_to_die(self):
        return self.age >= self.max_age or self.saturation <= 0

    def eat(self):
        self.saturation = self.max_saturation

    def move(self, map_size):
        super().move(map_size)

    def getting_old(self):
        super().getting_old()
