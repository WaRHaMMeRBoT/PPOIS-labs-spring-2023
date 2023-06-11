from test import cell
from grass import Grass
from rabbit import Rabbit
from fox import Fox
import random
import json


class PrintWorld:
    def __init__(self, grass, rabbits, foxes):
        self.world = [[0 for i in range(9)] for j in range(9)]
        # self.a = cell(0, foxes, rabbits, grass)

        for i in range(9):
            for j in range(9):
                a = cell(0, 0, 0, 0)
                self.world[i][j] = a
        self.startCountOfGrass = grass
        self.startCountOfRabbits = rabbits
        self.startCountOfFoxes = foxes

        self.vectorOfGrass = []
        self.vectorOfRabbits = []
        self.vectorOfFoxes = []

    def initGrass(self):
        for i in range(self.startCountOfGrass):
            xCoord = random.randint(0, 8)
            yCoord = random.randint(0, 8)
            generation = True
            while generation:
                if (self.world[xCoord][yCoord].grass == 1):
                    xCoord = random.randint(0, 8)
                    yCoord = random.randint(0, 8)
                    generation = True
                elif self.world[xCoord][yCoord].grass == 0:
                    a = Grass(xCoord, yCoord, 100, self.vectorOfGrass)
                    self.world[xCoord][yCoord].grass = 1
                    self.world[xCoord][yCoord].countOfLivings += 1
                    self.vectorOfGrass.append(a)
                    generation = False
        print("Init Grass")

    def initRabbits(self):
        for i in range(self.startCountOfRabbits):
            xCoord = random.randint(0, 8)
            yCoord = random.randint(0, 8)
            generation = True
            while generation:
                if (self.world[xCoord][yCoord].countOfLivings == 4):
                    xCoord = random.randint(0, 8)
                    yCoord = random.randint(0, 8)
                    generation = True
                elif self.world[xCoord][yCoord].countOfLivings < 4:
                    a = Rabbit(xCoord, yCoord, 100, self.vectorOfRabbits)
                    self.world[xCoord][yCoord].rabbit += 1
                    self.world[xCoord][yCoord].countOfLivings += 1
                    self.vectorOfRabbits.append(a)
                    generation = False
        print('init Rabbits')

    def initFoxes(self):
        for i in range(self.startCountOfFoxes):
            xCoord = random.randint(0, 8)
            yCoord = random.randint(0, 8)
            generation = True
            while generation:
                if (self.world[xCoord][yCoord].countOfLivings == 4):
                    xCoord = random.randint(0, 8)
                    yCoord = random.randint(0, 8)
                    generation = True
                elif self.world[xCoord][yCoord].countOfLivings < 4:
                    a = Fox(xCoord, yCoord, 100, self.vectorOfFoxes)
                    self.world[xCoord][yCoord].fox += 1
                    self.world[xCoord][yCoord].countOfLivings += 1
                    self.vectorOfFoxes.append(a)
                    generation = False
        print('init Foxes')

    def initWorld(self):
        self.initGrass()
        self.initRabbits()
        self.initFoxes()

    @staticmethod
    def print():
        for i in range(9):
            for j in range(9):
                print("      |", end='')
            print('')
            for j in range(9):
                print("      |", end='')
            print('')
            for j in range(9):
                print("-------", end='')
            print('')

    def printStage(self):
        for i in range(9):
            for j in range(9):
                counter = 0
                if (self.world[i][j].grass):
                    print('G', end='')
                    counter += 1
                for k in range(self.world[i][j].rabbit):
                    print('R', end='')
                    counter += 1
                for l in range(self.world[i][j].fox):
                    print('F', end='')
                    counter += 1
                if (counter == 0):
                    print('      |', end='')
                elif (counter == 1):
                    print(' ' * 5 + '|', end='')
                elif (counter == 2):
                    print(' ' * 4 + '|', end='')
                elif (counter == 3):
                    print(' ' * 3 + '|', end='')
                elif (counter == 4):
                    print(' ' * 2 + '|', end='')
            print('')
            for j in range(9):
                print(' ' * 6 + '|', end='')
            print('')
            for j in range(9):
                print('-' * 7, end='')
            print('')

    def movementStage(self):
        oldGrassLen = len(self.vectorOfGrass)
        k = 0
        while k < oldGrassLen:
            tempGrassLen = len(self.vectorOfGrass)
            self.vectorOfGrass[k].move(
                self.world, random.randint(0, 8), self.vectorOfGrass)
            k += 1
            if (len(self.vectorOfGrass) == tempGrassLen - 1):
                k -= 1
                oldGrassLen = len(self.vectorOfGrass)
                continue

        oldRabbitLen = len(self.vectorOfRabbits)
        i = 0
        while i < oldRabbitLen:
            self.vectorOfRabbits[i].move(
                self.world, random.randint(0, 8), self.vectorOfRabbits)
            i += 1
            if (len(self.vectorOfRabbits) == oldRabbitLen - 1):
                i -= 1
                oldRabbitLen = len(self.vectorOfRabbits)
                continue

        oldFoxLen = len(self.vectorOfFoxes)
        j = 0
        while j < oldFoxLen:
            self.vectorOfFoxes[j].move(
                self.world, random.randint(0, 8), self.vectorOfFoxes)
            j += 1
            if (len(self.vectorOfFoxes) == oldFoxLen - 1):
                j -= 1
                oldFoxLen = len(self.vectorOfFoxes)
                continue

    def eatStage(self):
        for rabbit in self.vectorOfRabbits:
            rabbit.eating(self.world, self.vectorOfGrass)

        for fox in self.vectorOfFoxes:
            fox.eating(self.world, self.vectorOfRabbits)

    def reproductionStage(self):
        for rabbit in self.vectorOfRabbits:
            rabbit.reproduction(self.world, self.vectorOfRabbits)

        for fox in self.vectorOfFoxes:
            fox.reproduction(self.world, self.vectorOfFoxes)

    def oneIneration(self):
        print("---------- stage ----------")
        self.movementStage()
        print("---------- movement stage ----------")
        self.printStage()
        self.eatStage()
        print("---------- eat stage ----------")
        self.printStage()
        self.reproductionStage()
        print("---------- reproduction stage ----------")
        self.printStage()
        print("---------- end stage ----------")

    def testRun(self):
        self.movementStage()
        self.eatStage()
        self.reproductionStage()
        self.printStage()

    def addRabbit(self, x, y):
        rabbit = Rabbit(x, y, 100, self.vectorOfRabbits)
        if (self.world[x][y].countOfLivings != 4):
            self.world[x][y].rabbit += 1
            self.vectorOfRabbits.append(rabbit)
        else:
            print("No space in this Cell")

    def addFox(self, x, y):
        fox = Fox(x, y, 100, self.vectorOfFoxes)
        if (self.world[x][y].countOfLivings != 4):
            self.world[x][y].fox += 1
            self.vectorOfFoxes.append(fox)
        else:
            print("No space in this Cell")

    def addGrass(self, x, y):
        grass = Grass(x, y, 100, self.vectorOfGrass)
        if (self.world[x][y].grass != 1):
            self.world[x][y].grass = 1
            self.vectorOfGrass.append(grass)
        else:
            print("No space in this Cell")

    def saveWorld(self):
        data = {}

        for i in range(len(self.world)):
            data[str(i)] = []
            for j in range(len(self.world[i])):
                data[str(i)].append({
                    'grass': self.world[i][j].grass,
                    'rabbit': self.world[i][j].rabbit,
                    'fox': self.world[i][j].fox
                })
            with open('data.txt', 'w') as outfile:
                json.dump(data, outfile)

    def loadWorld(self):
        with open('data.txt') as json_file:
            data = json.load(json_file)

        vectorOfGrass = []
        vectorOfRabbits = []
        vectorOfFoxes = []

        world = [[0 for i in range(9)] for j in range(9)]

        for i in range(9):
            for j in range(9):
                a = cell(0, 0, 0, 0)
                world[i][j] = a
        k = 0
        for i in range(9):
            for j in range(9):
                a = cell(data[str(i)][j]['grass'] + data[str(i)][j]['rabbit'] + data[str(i)][j]['fox'],
                         data[str(i)][j]['fox'], data[str(i)][j]['grass'], data[str(i)][j]['rabbit'])
                world[i][j] = a

        self.world = world

        for i in range(len(world)):
            for j in range(len(world[i])):
                if (world[i][j].grass == 1):
                    grass = Grass(j, i, 100, vectorOfGrass)
                    vectorOfGrass.append(grass)
                cRabbits = world[i][j].rabbit
                while cRabbits > 0:
                    rabbit = Rabbit(j, i, 100, vectorOfRabbits)
                    vectorOfRabbits.append(rabbit)
                    cRabbits -= 1
                cFoxes = world[i][j].fox
                while cFoxes > 0:
                    fox = Fox(j, i, 100, vectorOfFoxes)
                    vectorOfFoxes.append(fox)
                    cFoxes -= 1


test = PrintWorld(6, 5, 2)

test.print()
test.initWorld()
# test.printStage()
# print('------------------ INIT -------------------------------')
# test.saveWorld()
# test.loadWorld()
# test.printStage()

print("Choose:")
print("1. new game")
print("2. load prev. saving")
chosenVar = int(input())
if (chosenVar == 1):
    print("You want to add new:\n1.grass\n2.rabbit\n3.fox\n4.no, thanks")
    chosenVar2 = int(input())
    if(chosenVar2 < 4):
        print("Count:")
        chosenVar3 = int(input())
        for i in range(chosenVar3):
            if (chosenVar2 == 1):
                x = int(input())
                y = int(input())
                test.addGrass(x, y)
            elif (chosenVar2 == 2):
                x = int(input())
                y = int(input())
                test.addRabbit(x, y)
            elif (chosenVar2 == 3):
                x = int(input())
                y = int(input())
                test.addFox(x, y)
    for i in range(5):
        test.oneIneration()
    test.saveWorld()
elif (chosenVar == 2):
    test.loadWorld()
    for i in range(5):
        test.oneIneration()
    test.saveWorld()
else:
    print("Invalid variant")


test.saveWorld()
# print("grass - " + str(len(test.vectorOfGrass)))
# print("grass vector", test.vectorOfGrass)
# print("rabbit - " + str(len(test.vectorOfRabbits)))
# print("rabbit vector", test.vectorOfRabbits)
# print("fox - " + str(len(test.vectorOfFoxes)))
