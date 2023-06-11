import random
from grass import CellRand


def getId(vector):
    max = 0
    for i in range(len(vector)):
        if (max > vector[i].id):
            max = vector[i].id
    return max + 1


class Rabbit:
    def __init__(self, c, r, health, vectorOfRabbits):
        self.age = 0
        self.row = r
        self.column = c
        self.health = health
        self.sex = "men" if random.randint(0, 1) else "women"
        self.live = True
        self.createdNow = True
        self.id = getId(vectorOfRabbits)

    def move(self, world, randNumber, vectorOfRabbits):
        if (self.health == 0):
            indexOfRabbitZero = 0
            world[self.column][self.row].rabbit -= 1
            for i in range(len(vectorOfRabbits)):
                if (vectorOfRabbits[i].health == 0 and vectorOfRabbits[i].id == self.id):
                    indexOfRabbitZero = i
                    break
            vectorOfRabbits.pop(indexOfRabbitZero)
            return
        if (self.age < 6):  # 6
            self.age += 1
        else:
            indexOfRabbitZero = 0
            world[self.column][self.row].rabbit -= 1
            # find first zero element, it is our element
            for i in range(len(vectorOfRabbits)):
                if (vectorOfRabbits[i].age == 6 and vectorOfRabbits[i].id == self.id):
                    indexOfRabbitZero = i
                    break

            vectorOfRabbits.pop(indexOfRabbitZero)
            return
        if (self.get_createdNow()):
            self.set_createdNow()
            return
        cells = []
        x = self.column
        y = self.row
        for i in [y - 1, y, y + 1]:
            for j in [x - 1, x, x + 1]:
                if (0 <= i < 9 and 0 <= j < 9 and world[j][i].countOfLivings != 4):
                    cell = CellRand(j, i)
                    if (cell.x >= 0 and cell.y >= 0):
                        cells.append(cell)
        if (randNumber >= len(cells) - 1):
            self.column = cells[len(cells) - 1].x
            self.row = cells[len(cells) - 1].y
        else:
            self.column = cells[randNumber].x
            self.row = cells[randNumber].y

        world[self.column][self.row].countOfLivings += 1
        world[self.column][self.row].rabbit += 1

        world[x][y].countOfLivings -= 1
        world[x][y].rabbit -= 1

        self.health -= 25

    def eating(self, world, vectorOfGrass):
        x = self.column
        y = self.row
        if (world[x][y].grass == 1):
            world[x][y].grass = 0
        indexOfGrassTarget = -1
        for i in range(len(vectorOfGrass)):
            if (vectorOfGrass[i].get_column() == x and vectorOfGrass[i].get_row() == y):
                indexOfGrassTarget = i
                break
        if (indexOfGrassTarget != -1):
            vectorOfGrass.pop(indexOfGrassTarget)

    def reproduction(self, world, vectorOfRabbits):
        sex = self.get_sex()
        if (world[self.get_column()][self.get_row()].rabbit >= 2 and world[self.get_column()][self.get_row()].countOfLivings < 4):
            if (sex == "men"):
                for rabbit in vectorOfRabbits:
                    if (rabbit.get_column() == self.get_column()
                       and rabbit.get_row() == self.get_row()):
                        if (rabbit.get_sex() == "women"
                           and rabbit.get_createdNow() == False):
                            newRabbit = Rabbit(
                                self.get_column(), self.get_row(), 100, vectorOfRabbits)
                            world[self.get_column()][self.get_row()
                                                     ].rabbit += 1
                            vectorOfRabbits.append(newRabbit)

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
