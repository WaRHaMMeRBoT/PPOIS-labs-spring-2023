import random

class Weather():
    def __init__(self):
        self._is_sunny: bool = random.choice([True, False])

    def next_day(self):
        self.is_sunny: bool = random.choice([True, False])

    @property
    def is_sunny(self):
        return self._is_sunny

    @is_sunny.setter
    def is_sunny(self, value: bool):
        self._is_sunny = value

    def __str__(self):
        tmp_1 = 'Rain' if not self._is_sunny else 'Sunny'
        return tmp_1
