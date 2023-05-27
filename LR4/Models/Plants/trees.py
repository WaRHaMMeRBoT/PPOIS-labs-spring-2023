from Models.Plants.abstract_plants import Tree, Fruit

class OrangeTree(Tree):
    def create_fruit(self):
        if not self.fruit:
            self.fruit = Orange()
    def __str__(self):
        return 'Orange Tree'
class Orange(Fruit):
    ...

class PearTree(Tree):
    def create_fruit(self):
        if not self.fruit:
            self.fruit = Pear()
    def __str__(self):
        return 'Pear Tree'
class Pear(Fruit):
    ...

class PlumTree(Tree):
    def create_fruit(self):
        if not self.fruit:
            self.fruit = Plum()
    def __str__(self):
        return 'Plum Tree'
class Plum(Fruit):
    ...
