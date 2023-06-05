import random
from plant import CellRand


class Predator:
    def __init__(self, column, row, health_points, vector_of_predators):
        self.age = 0
        self.row = row
        self.column = column
        self.health = health_points
        self.sex = "men" if random.randint(0, 1) else "women"
        self.live = True
        self.createdNow = True

    def move(self, world, random_number, vector_of_predators):
        if (self.health == 0):
            index_of_predator = 0
            world[self.row][self.column].predator -= 1
            for i in range(len(vector_of_predators)):
                if (vector_of_predators[i].health == 0):
                    index_of_predator == i
                    break
            vector_of_predators.pop(index_of_predator)
            return
        if (self.age < 10):
            self.age += 1
        else:
            index_of_predator = 0
            world[self.row][self.column].predator -= 1
            # find first zero element, it is our element
            for i in range(len(vector_of_predators)):
                if (vector_of_predators[i].age == 10):
                    index_of_predator = i
                    break

            vector_of_predators.pop(index_of_predator)
            return
        if (self.get_createdNow()):
            self.set_createdNow()
            return
        cells = []
        x = self.column
        y = self.row
        for i in [y - 1, y, y + 1]:
            for j in [x - 1, x, x + 1]:
                if (0 <= i < 9 and 0 <= j < 9 and world[i][j].countOfLivings != 4):
                    cell = CellRand(j, i)
                    if (cell.x >= 0 and cell.y >= 0):
                        cells.append(cell)

        if (random_number >= len(cells) - 1):
            self.column = cells[len(cells) - 1].x
            self.row = cells[len(cells) - 1].y
        else:
            self.column = cells[random_number].x
            self.row = cells[random_number].y

        world[self.column][self.row].countOfLivings += 1
        world[self.column][self.row].predator += 1

        world[x][y].countOfLivings -= 1
        world[x][y].predator -= 1

        self.health -= 25

    def get_createdNow(self):
        return self.createdNow

    def get_sex(self):
        return self.sex

    def set_createdNow(self):
        self.createdNow = False

    def eating(self, world, vector_of_herbivores):
        x = self.column
        y = self.row
        if (world[x][y].herbivore > 0):
            world[x][y].herbivore -= 1
        index_of_herbivore = -1
        for i in range(len(vector_of_herbivores)):
            if (vector_of_herbivores[i].get_column() == x and vector_of_herbivores[i].get_row() == y):
                index_of_herbivore = i
                break
        if (index_of_herbivore != -1):
            vector_of_herbivores.pop(index_of_herbivore)

    def reproduction(self, world, vector_of_predators):
        sex = self.get_sex()
        if (world[self.get_column()][self.get_row()].predator >= 2
                and world[self.get_column()][self.get_row()].countOfLivings < 4):
            if (sex == "men"):
                for predator in vector_of_predators:
                    if (predator.get_column() == self.get_column() and predator.get_row() == self.get_row):
                        if (predator.get_sex() == "women" and predator.get_createdNow() == False):
                            new_predator = Predator(self.get_column(),
                                              self.get_row(), 100, vector_of_predators)
                            world[self.get_column()][self.get_row()].predator += 1
                            vector_of_predators.append(new_predator)

    def get_column(self):
        return self.column

    def get_row(self):
        return self.row
