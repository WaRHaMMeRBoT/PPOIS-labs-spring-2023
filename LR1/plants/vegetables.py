from .basic_classes import Plants

class Vegetables(Plants):
    def __init__(self, _identifier, _name):
        super().__init__(_identifier, _name, 10)

    def display_info(self):
        print(f"Name:{self._name}{self._identifier} Diseases:{self._diseases} Left to live:{self._life_span}")

class Tomato(Vegetables):
    def __init__(self, _identifier):
        super().__init__(_identifier, 'Tomato')

class Cucumber(Vegetables):
    def __init__(self, _identifier):
        super().__init__(_identifier, 'Cucumber')

class Carrot(Vegetables):
    def __init__(self, _identifier):
        super().__init__(_identifier, 'Carrot')
