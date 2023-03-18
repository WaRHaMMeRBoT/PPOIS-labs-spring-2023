def getId(vector):
    max = 0
    for i in range(len(vector)):
        if (max > vector[i].id):
            max = vector[i].id
    return max + 1


class CellRand:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Grass:
    def __init__(self, c, r, health, vectorOfGrass):
        self.row = r
        self.column = c
        self.health = health
        self.age = 0
        self.id = getId(vectorOfGrass)

    def who():
        return "GRASS"

    def move(self, world, randNumber, vectorOfGrass):
        if (self.health == 0):
            indexOfGrassZero = 0
            world[self.column][self.row].grass = 0
            for i in range(len(vectorOfGrass)):
                if (vectorOfGrass[i].health == 0 and vectorOfGrass[i].id == self.id):
                    indexOfGrassZero = i
                    break
            vectorOfGrass.pop(indexOfGrassZero)
            return
        if (self.age < 10):

            if (self.age == 0):
                self.age += 1
                return
        else:
            indexOfGrassZero = 0
            world[self.column][self.row].grass = 0
            for i in range(len(vectorOfGrass)):
                if (vectorOfGrass[i].age == 10 and vectorOfGrass[i].id == self.id):
                    indexOfGrassZero = i
                    break
            vectorOfGrass.pop(indexOfGrassZero)
            return
        cells = []
        x = self.column
        y = self.row
        for i in [y - 1, y, y + 1]:
            for j in [x - 1, x, x + 1]:
                if (0 <= i < 9 and 0 <= j < 9 and world[j][i].grass != 1):
                    a = CellRand(j, i)
                    if (a.x >= 0 and a.y >= 0):
                        cells.append(a)
        childGrassX = 0
        childGrassY = 0
        if (len(cells) and randNumber >= len(cells) - 1):
            childGrassX = cells[len(cells) - 1].x
            childGrassY = cells[len(cells) - 1].y
        elif (len(cells) and randNumber < len(cells) - 1):
            childGrassX = cells[randNumber].x
            childGrassY = cells[randNumber].y

        childGrass = Grass(childGrassX, childGrassY, 100, vectorOfGrass)

        world[childGrassX][childGrassY].countOfLivings += 1
        world[childGrassX][childGrassY].grass = 1

        vectorOfGrass.append(childGrass)

        self.health -= 25

    def set_column(self, column):
        self.column = column

    def set_row(self, row):
        self.row = row

    def get_column(self):
        return self.column

    def get_row(self):
        return self.row
