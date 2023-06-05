import random
from plant import CellRand


def get_id(vector):
    id = 0
    for i in range(len(vector)):
        if (id > vector[i].id):
            id = vector[i].id
    return id + 1


class Herbivore:
    def __init__(self, column, row, health_points, vector_of_herbivore):
        self.age = 0
        self.row = row
        self.column = column
        self.health = health_points
        self.sex = "men" if random.randint(0, 1) else "women"
        self.live = True
        self.createdNow = True
        self.id = get_id(vector_of_herbivore)

    def move(self, world, random_number, vector_of_herbivore):
        if (self.health == 0):
            index_of_herbivore = 0
            world[self.row][self.column].herbivore -= 1
            for i in range(len(vector_of_herbivore)):
                if (vector_of_herbivore[i].health == 0 and vector_of_herbivore[i].id == self.id):
                    index_of_herbivore == i
                    break
            vector_of_herbivore.pop(index_of_herbivore)
            return
        #print('age')
        if (self.age < 6):
            self.age += 1
        else:
            index_of_herbivore = 0
            world[self.row][self.column].herbivore -= 1
            for i in range(len(vector_of_herbivore)):
                if (vector_of_herbivore[i].age == 6 and vector_of_herbivore[i].id == self.id):
                    index_of_herbivore = i
                    break

            vector_of_herbivore.pop(index_of_herbivore)
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
        world[self.column][self.row].herbivore += 1

        world[x][y].countOfLivings -= 1
        world[x][y].herbivore -= 1

        self.health -= 25

    def eating(self, world, vector_of_plants):
        x = self.column
        y = self.row
        if (world[x][y].plant == 1):
            world[x][y].plant = 0
        index_of_plant = -1
        for i in range(len(vector_of_plants)):
            if (vector_of_plants[i].get_column() == x and vector_of_plants[i].get_row() == y):
                index_of_plant = i
                break
        if (index_of_plant != -1):
            vector_of_plants.pop(index_of_plant)

    def reproduction(self, world, vector_of_herbivore):
        sex = self.get_sex()
        if (world[self.get_column()][self.get_row()].herbivore >= 2 and world[self.get_column()][self.get_row()].countOfLivings < 4):
            if (sex == "men"):
                for herbivore in vector_of_herbivore:
                    if (herbivore.get_column() == self.get_column()
                       and herbivore.get_row() == self.get_row()):
                        if (herbivore.get_sex() == "women"
                           and herbivore.get_createdNow() == False):
                            new_herbivore = Herbivore(
                                self.get_column(), self.get_row(), 100, vector_of_herbivore)
                            world[self.get_column()][self.get_row()
                                                     ].herbivore += 1
                            vector_of_herbivore.append(new_herbivore)

    def get_createdNow(self):
        return self.createdNow

    def get_sex(self):
        return self.sex

    def set_createdNow(self):
        self.createdNow = False

    def get_column(self):
        return self.column

    def get_row(self):
        return self.row
