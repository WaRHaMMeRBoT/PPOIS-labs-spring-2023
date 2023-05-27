import random
from Grass import CellRand
from Rabbit import getId


class Fox:
    def __init__(self, c, r, health, vectorOfFoxes):
        self.age = 0
        self.row = r
        self.column = c
        self.health = health
        self.sex = "men" if random.randint(0, 1) else "women"
        self.live = True
        self.createdNow = True
        self.id = getId(vectorOfFoxes)

    def move(self, world, randNumber, vectorOfFoxes):
        if (self.health == 0):
            indexOfFoxZero = 0
            world[self.column][self.row].fox -= 1
            for i in range(len(vectorOfFoxes)):
                if (vectorOfFoxes[i].health == 0):
                    indexOfFoxZero = i
                    break
            vectorOfFoxes.pop(indexOfFoxZero)
            return
        if (self.age < 10):
            self.age += 1
        else:
            indexOfFoxZero = 0
            world[self.column][self.row].fox -= 1
            # find first zero element, it is our element
            for i in range(len(vectorOfFoxes)):
                if (vectorOfFoxes[i].age == 10):
                    indexOfFoxZero = i
                    break

            vectorOfFoxes.pop(indexOfFoxZero)  # Delete first zero grass
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
        world[self.column][self.row].fox += 1

        world[x][y].countOfLivings -= 1
        world[x][y].fox -= 1

        self.health -= 25

    def get_createdNow(self):
        return self.createdNow

    def get_sex(self):
        return self.sex

    def set_createdNow(self):
        self.createdNow = False

    def eating(self, world, vectorOfRabbits):
        x = self.column
        y = self.row
        if (world[x][y].rabbit > 0):
            world[x][y].rabbit -= 1
        indexOfRabbitTarget = -1
        for i in range(len(vectorOfRabbits)):
            if (vectorOfRabbits[i].get_column() == x and vectorOfRabbits[i].get_row() == y):
                indexOfRabbitTarget = i
                break
        if (indexOfRabbitTarget != -1):
            vectorOfRabbits.pop(indexOfRabbitTarget)
            self.health += 100

    def reproduction(self, world, vectorOfFoxes):
        sex = self.get_sex()
        if (world[self.get_column()][self.get_row()].fox >= 2
                and world[self.get_column()][self.get_row()].countOfLivings < 4):
            if (sex == "men"):
                for fox in vectorOfFoxes:
                    if (fox.get_column() == self.get_column() and fox.get_row() == self.get_row):
                        if (fox.get_sex() == "women" and fox.get_createdNow() == False):
                            newFox = Fox(self.get_column(),
                                         self.get_row(), 100, vectorOfFoxes)
                            world[self.get_column()][self.get_row()].fox += 1
                            vectorOfFoxes.append(newFox)

    def get_column(self):
        return self.column

    def get_row(self):
        return self.row
