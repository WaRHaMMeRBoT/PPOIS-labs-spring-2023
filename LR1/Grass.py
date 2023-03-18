from LivingEntities import LivingEntity


class Grass(LivingEntity):

    def __init__(self, x, y, age=None, max_age=None):
        self.x = x
        self.y = y
        super().__init__()
        if age is None or max_age is None:
            self.age = 0
            self.max_age = 4
        else:
            self.age = age
            self.max_age = max_age

    def is_ready_to_die(self):
        return self.age >= self.max_age

    def getting_old(self):
        self.age += 0.3
