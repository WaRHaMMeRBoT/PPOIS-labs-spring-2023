class Weed:
    def __init__(self):
        self._health = 100

    @property
    def health(self):
        return self._health

    @health.setter
    def health(self, value: int):
        self._health = value
        if self._health == 0:
            self.die()

    def die(self):
        del self
