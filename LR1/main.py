from cell import Cell
from plant import Plant
from herbivore import Herbivore
from predator import Predator
from funJson import functionsJson
import random
import sys
import json
import argparse


class PrintWorld:
    def __init__(self, plants, herbivores, predators):
        self.world = [[0 for i in range(9)] for j in range(9)]

        for i in range(9):
            for j in range(9):
                a = Cell(0, 0, 0, 0)
                self.world[i][j] = a
        self.startCountOfPlants = plants
        self.startCountOfHerbivores = herbivores
        self.startCountOfPredators = predators

        self.vectorOfPlants = []
        self.vectorOfHerbivores = []
        self.vectorOfPredators = []

    def init_plants(self):
        for i in range(self.startCountOfPlants):
            x_coord = random.randint(0, 8)
            y_coord = random.randint(0, 8)
            generation = True
            while generation:
                if (self.world[x_coord][y_coord].plant == 1):
                    x_coord = random.randint(0, 8)
                    y_coord = random.randint(0, 8)
                    generation = True
                elif self.world[x_coord][y_coord].plant == 0:
                    a = Plant(x_coord, y_coord, 100, self.vectorOfPlants)
                    self.world[x_coord][y_coord].plant = 1
                    self.world[x_coord][y_coord].countOfLivings += 1
                    self.vectorOfPlants.append(a)
                    generation = False
        print("Init Plants")

    def init_herbivores(self):
        for i in range(self.startCountOfHerbivores):
            x_coord = random.randint(0, 8)
            y_coord = random.randint(0, 8)
            generation = True
            while generation:
                if (self.world[x_coord][y_coord].countOfLivings == 4):
                    x_coord = random.randint(0, 8)
                    y_coord = random.randint(0, 8)
                    generation = True
                elif self.world[x_coord][y_coord].countOfLivings < 4:
                    a = Herbivore(x_coord, y_coord, 100, self.vectorOfHerbivores)
                    self.world[x_coord][y_coord].herbivore += 1
                    self.world[x_coord][y_coord].countOfLivings += 1
                    self.vectorOfHerbivores.append(a)
                    generation = False
        print('init Herbivores')

    def init_predators(self):
        for i in range(self.startCountOfPredators):
            x_coord = random.randint(0, 8)
            y_coord = random.randint(0, 8)
            generation = True
            while generation:
                if (self.world[x_coord][y_coord].countOfLivings == 4):
                    x_coord = random.randint(0, 8)
                    y_coord = random.randint(0, 8)
                    generation = True
                elif self.world[x_coord][y_coord].countOfLivings < 4:
                    a = Predator(x_coord, y_coord, 100, self.vectorOfPredators)
                    self.world[x_coord][y_coord].predator += 1
                    self.world[x_coord][y_coord].countOfLivings += 1
                    self.vectorOfPredators.append(a)
                    generation = False
        print('init Predators')

    def init_world(self):
        self.init_plants()
        self.init_herbivores()
        self.init_predators()

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

    def print_stage(self):
        for i in range(9):
            for j in range(9):
                counter = 0
                if (self.world[i][j].plant):
                    print('P', end='')
                    counter += 1
                for k in range(self.world[i][j].herbivore):
                    print('H', end='')
                    counter += 1
                for l in range(self.world[i][j].predator):
                    print('W', end='')
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

    def movement_stage(self):
        len_plants = len(self.vectorOfPlants)
        len_herbivores = len(self.vectorOfHerbivores)
        len_predators = len(self.vectorOfPredators)
        for i in range(len_plants):
            self.vectorOfPlants[i].move(
                self.world, random.randint(0, 8), self.vectorOfPlants)
        for herbivore in self.vectorOfHerbivores:
            herbivore.move(
                self.world, random.randint(0, 8), self.vectorOfHerbivores)

        for predator in self.vectorOfPredators:
            predator.move(
                self.world, random.randint(0, 8), self.vectorOfPredators)

    def nutrition_stage(self):
        for herbivore in self.vectorOfHerbivores:
            herbivore.eating(self.world, self.vectorOfPlants)

        for predator in self.vectorOfPredators:
            predator.eating(self.world, self.vectorOfHerbivores)

    def reproduction_stage(self):
        for herbivore in self.vectorOfHerbivores:
            herbivore.reproduction(self.world, self.vectorOfHerbivores)

        for predator in self.vectorOfPredators:
            predator.reproduction(self.world, self.vectorOfPredators)

    def one_iteration(self):
        print("---------- stage ----------")
        self.movement_stage()
        print("---------- movement stage ----------")
        self.print_stage()
        self.nutrition_stage()
        print("---------- nutrition stage ----------")
        self.print_stage()
        self.reproduction_stage()
        print("---------- reproduction stage ----------")
        self.print_stage()
        print("---------- final stage ----------")

    def save_world(self):
        data = {}

        for i in range(len(self.world)):
            data[str(i)] = []
            for j in range(len(self.world[i])):
                data[str(i)].append({
                    'plant': self.world[i][j].plant,
                    'herbivore': self.world[i][j].herbivore,
                    'predator': self.world[i][j].predator
                })
            with open('data.txt', 'w') as outfile:
                json.dump(data, outfile)

    def load_world(self):
        with open('data.txt') as json_file:
            data = json.load(json_file)

        vectorOfPlants = []
        vectorOfHerbivores = []
        vectorOfPredators = []

        world = [[0 for i in range(9)] for j in range(9)]

        for i in range(9):
            for j in range(9):
                a = Cell(0, 0, 0, 0)
                world[i][j] = a
                
        for i in range(9):
            for j in range(9):
                a = Cell(data[str(i)][j]['plant'] + data[str(i)][j]['herbivore'] + data[str(i)][j]['predator'],
                         data[str(i)][j]['predator'], data[str(i)][j]['plant'], data[str(i)][j]['herbivore'])
                world[i][j] = a

        self.world = world

        for i in range(len(world)):
            for j in range(len(world[i])):
                if (world[i][j].plant == 1):
                    plant = Plant(j, i, 100, vectorOfPlants)
                    vectorOfPlants.append(plant)
                cHerbivores = world[i][j].plant
                while cHerbivores > 0:
                    herbivore = Herbivore(j, i, 100, vectorOfHerbivores)
                    vectorOfHerbivores.append(herbivore)
                    cHerbivores -= 1
                cPredators = world[i][j].predator
                while cPredators > 0:
                    predator = Predator(j, i, 100, vectorOfPredators)
                    vectorOfPredators.append(predator)
                    cPredators -= 1


if __name__ == "__main__":
    if len(sys.argv) == 1:
        world = PrintWorld(7, 5, 2)
        world.init_world()
        for i in range(4):
            world.one_iteration()

    elif len(sys.argv) == 3:
        cmd_type = sys.argv[1]
        quantity_of_pl = int(sys.argv[2])
        world = PrintWorld(quantity_of_pl)
        world.init_world()
        if cmd_type == '--load' or '-l':
            world.load_world()
            for i in range(4):
                world.one_iteration()
        elif cmd_type == '--save' or '-s':
            for i in range(4):
                world.one_iteration()
            world.save_world()

    elif len(sys.argv) == 4:
        cmd_type = sys.argv[1]
        quantity_of_pl = int(sys.argv[2])
        quantity_of_he = int(sys.argv[3])
        world = PrintWorld(quantity_of_pl, quantity_of_he)
        world.init_world()
        if cmd_type == '--load' or '-l':
            world.load_world()
            for i in range(4):
                world.one_iteration()
        elif cmd_type == '--save' or '-s':
            for i in range(4):
                world.one_iteration()
            world.save_world()

    elif len(sys.argv) == 5:
        cmd_type = sys.argv[1]
        quantity_of_pl = int(sys.argv[2])
        quantity_of_he = int(sys.argv[3])
        quantity_of_pr = int(sys.argv[4])
        world = PrintWorld(quantity_of_pl, quantity_of_he, quantity_of_pr)
        world.init_world()
        if cmd_type == '--load' or '-l':
            world.load_world()
            for i in range(4):
                world.one_iteration()
        elif cmd_type == '--save' or '-s':
            for i in range(4):
                world.one_iteration()
            world.save_world()
