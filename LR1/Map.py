from Grass import Grass
from Wolf import Wolf
from Rabbit import Rabbit
import random


class Cell:

    def __init__(self, x, y, num_of_wolfs=0, num_of_rabbits=0, num_of_grass=0):
        self.x = x
        self.y = y
        self.rabbits = []
        self.wolfs = []
        self.grass = []
        self.entities = []
        self.num_of_wolfs = num_of_wolfs
        self.num_of_grass = num_of_grass
        self.num_of_rabbits = num_of_rabbits
        self.num_of_entities = num_of_wolfs + num_of_grass + num_of_rabbits

    def show_cell_info(self):
        print("Cell (" + str(self.x) + ", " + str(self.y) + "):")
        print("Rabbits count = " + str(self.num_of_rabbits))
        print("Wolfs count = " + str(self.num_of_wolfs))
        print("Grass count = " + str(self.num_of_grass) + "\n")


class Map:

    def __init__(self, size, start_num_of_rabbits=0, start_num_of_wolfs=0, start_num_of_grass=None):
        self.size = size
        self.cells = [[Cell(j, i, 0, 0, 0) for j in range(self.size)] for i in range(self.size)]
        self.num_of_rabbits = start_num_of_rabbits
        self.num_of_wolfs = start_num_of_wolfs
        if start_num_of_grass is None:
            self.num_of_grass = size ** 2 * 2
        else:
            self.num_of_grass = start_num_of_grass

    def locate_rabbits_on_the_map(self):
        for i in range(self.num_of_rabbits):
            x = random.randint(0, self.size - 1)
            y = random.randint(0, self.size - 1)
            while self.cells[x][y].num_of_rabbits > 2 and self.cells[x][y].num_of_entities > 4:
                x = random.randint(0, self.size - 1)
                y = random.randint(0, self.size - 1)
            self.cells[x][y].rabbits.append(Rabbit(x, y))
            self.cells[x][y].num_of_rabbits += 1

    def locate_wolfs_on_the_map(self):
        for i in range(self.num_of_wolfs):
            x = random.randint(0, self.size - 1)
            y = random.randint(0, self.size - 1)
            while self.cells[x][y].num_of_wolfs > 2 and self.cells[x][y].num_of_entities > 4:
                x = random.randint(0, self.size - 1)
                y = random.randint(0, self.size - 1)
            self.cells[x][y].wolfs.append(Wolf(x, y))
            self.cells[x][y].num_of_wolfs += 1

    def locate_start_grass_on_the_map(self):
        for i in range(self.size):
            for j in range(self.size):
                self.cells[i][j].grass.append(Grass(i, j))
                self.cells[i][j].grass.append(Grass(i, j))
                self.cells[i][j].num_of_grass += 2

    def map_initialization(self):
        self.locate_rabbits_on_the_map()
        self.locate_wolfs_on_the_map()
        self.locate_start_grass_on_the_map()

    def get_num_of_rabbits(self):
        num_of_rabbits = 0
        for i in range(self.size):
            for j in range(self.size):
                num_of_rabbits += self.cells[i][j].num_of_rabbits
        return num_of_rabbits

    def get_num_of_wolfs(self):
        num_of_wolfs = 0
        for i in range(self.size):
            for j in range(self.size):
                num_of_wolfs += self.cells[i][j].num_of_wolfs
        return num_of_wolfs

    def get_num_of_grass(self):
        num_of_grass = 0
        for i in range(self.size):
            for j in range(self.size):
                num_of_grass += self.cells[i][j].num_of_grass
        return num_of_grass

    def change_nums_of_entities(self):
        self.num_of_rabbits = self.get_num_of_rabbits()
        self.num_of_wolfs = self.get_num_of_wolfs()
        self.num_of_grass = self.get_num_of_grass()

    def locate_new_grass(self):
        for i in range(int(self.size ** 2 / 2)):
            x = random.randint(0, self.size - 1)
            y = random.randint(0, self.size - 1)
            self.cells[x][y].grass.append(Grass(x, y))
            self.cells[x][y].num_of_grass += 1

    def locate_new_animals(self):
        print("Enter x coordinate of new animal")
        x = int(input())
        while x > self.size-1 or x < 0:
            print("Incorrect input")
            x = int(input())
        print("Enter y coordinate of new animal")
        y = int(input())
        while y > self.size-1 or y < 0:
            print("Incorrect input")
            y = int(input())
        print("Enter count of animals")
        count = int(input())
        print("Choice the animal\n1. Rabbit\n2. Wolf")
        choice = int(input())
        if choice == 1:
            self.locate_new_rabbit(x, y, count)
        elif choice == 2:
            self.locate_new_wolf(x, y, count)

    def locate_new_wolf(self, x, y, count):
        for i in range(0, count):
            self.cells[x][y].wolfs.append(Wolf(x, y))
            self.cells[x][y].num_of_wolfs += 1
            self.num_of_wolfs += 1

    def locate_new_rabbit(self, x, y, count):
        for i in range(0, count):
            self.cells[x][y].rabbits.append(Rabbit(x, y))
            self.cells[x][y].num_of_rabbits += 1
            self.num_of_rabbits += 1

    def show_map_info(self):
        [[Cell.show_cell_info(self.cells[j][i]) for j in range(self.size)] for i in range(self.size)]
        print("")
        print("Total rabbits count = " + str(self.get_num_of_rabbits()))
        print("Total wolfs count = " + str(self.get_num_of_wolfs()))
        print("Total grass count = " + str(self.get_num_of_grass()))
