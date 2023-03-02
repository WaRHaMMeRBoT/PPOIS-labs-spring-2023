import random

class Weather():
    def __init__(self):
        self._is_sunny: bool = random.choice([True, False])
        self._is_rainy: bool = True if random.randint(1, 4) == 2 else False

    def next_day(self):
        self.is_sunny: bool = random.choice([True, False])
        self.is_rainy: bool = True if random.randint(1, 4) == 2 else False

    @property
    def is_sunny(self):
        return self._is_sunny

    @property
    def is_rainy(self):
        return self._is_rainy

    @is_sunny.setter
    def is_sunny(self, value: bool):
        self._is_sunny = value

    @is_rainy.setter
    def is_rainy(self, value: bool):
        self._is_rainy = value

    def __str__(self):
        tmp_1 = 'Cloudy' if not self._is_sunny else 'Sunny'
        tmp_2 = ', Rainy' if self._is_rainy else ''
        return tmp_1 + tmp_2
