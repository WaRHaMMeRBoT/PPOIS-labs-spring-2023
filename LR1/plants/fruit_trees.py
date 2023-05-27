from .basic_classes import Plants
from .basic_classes import Fruit

class Tree(Plants):
    def __init__(self, _identifier, _name):
        super().__init__(_identifier, _name, 20)
        self._fruit = 0
        self._fruits = []
        self._fruit_id = 1

    def display_info(self):
        print(f"Name:{self._name}{self._identifier} Diseases:{self._diseases} Left to live:{self._life_span} Fruits:{self._fruit}")

class Orange_tree(Tree):
    def __init__(self, _identifier):
        super().__init__(_identifier, 'Orange')

    def create_fruit(self):
        if self._water >=30 :
            self.fruit += 1
            self.fruits.append(Orange(self.fruit_id))
            self.fruit_id +=1

class Pear_tree(Tree):
    def __init__(self, _identifier):
        super().__init__(_identifier, 'Pear  ')

    def create_fruit(self):
        if self._water >=30 :
            self.fruit += 1
            self.fruits.append(Pear(self.fruit_id))
            self.fruit_id +=1

class Plum_tree(Tree):
    def __init__(self, _identifier):
        super().__init__(_identifier, 'Plum  ')

    def create_fruit(self):
        if self._water >=30 :
            self.fruit += 1
            self.fruits.append(Plum(self.fruit_id))
            self.fruit_id +=1
    
class Orange(Fruit):
    def __init__(self, _identifier):
        super().__init__ (_identifier, 'orange fruit')

class Pear(Fruit):
    def __init__(self, _identifier):
        super().__init__ (_identifier, 'pear fruit')

class Plum(Fruit):
    def __init__(self, _identifier):
        super().__init__ (_identifier, 'plum fruit')
