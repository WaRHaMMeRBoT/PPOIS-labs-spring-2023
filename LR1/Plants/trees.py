from Plants.abstract_plants import Tree, Fruit


class AppleTree(Tree):
    def create_fruit(self):
        if not self.fruit:
            self.fruit = Apple()

    def __str__(self):
        return 'Apple Tree'


class Apple(Fruit):
    ...


class PearTree(Tree):
    def create_fruit(self):
        if not self.fruit:
            self.fruit = Pear()

    def __str__(self):
        return 'Pear Tree'


class Pear(Fruit):
    ...


class PeachTree(Tree):
    def create_fruit(self):
        if not self.fruit:
            self.fruit = Peach()

    def __str__(self):
        return 'Pear Tree'


class Peach(Fruit):
    ...
