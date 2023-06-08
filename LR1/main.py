# This is a sample Python script.
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import random
import os

width = 45
height = 30
world = [[" "] * width] * height


class living():
    def __init__(self):
        pass

    def place(self, y, x, poisk):
        for j in range(y - 1, y + 2):
            for i in range(x - 1, x + 2):
                if (width > i) and (i > -1) and (height > j) and (j > -1) and (world[j][i][0] is poisk) and (
                        world[j][i] != world[y][x]):
                    pl = [i, j]
                    return pl
        return []

    def Eat(self, y, x):
        global extraction
        if world[y][x][2] != '-':
            if world[y][x][0] is 'P':
                extraction = 'H'
            elif world[y][x][0] is 'H':
                extraction = 'G'

            age = int(world[y][x][2])
            pl = self.place(y, x, extraction)
            if len(pl) > 0:
                X = pl[0]
                Y = pl[1]
                world[Y][X] = " "
                age = age + 1
                world[y][x] = world[y][x][0] + world[y][x][1] + str(age)

    def moving(self, y, x):
        if world[y][x][2] != '-':
            pl = self.place(y, x, ' ')
            if len(pl) > 0:
                X = pl[0]
                Y = pl[1]
                world[Y][X] = world[y][x]
                world[y][x] = " "


class predator(living):
    def __init__(self, y, x):
        super().__init__()
        self.y = y
        self.x = x

    def reproduction(self):
        partner = super().place(self.y, self.x, 'P')
        if len(partner) > 0 and world[partner[1]][partner[0]][2] != '-':
            child = super().place(self.y, self.x, ' ')
            if len(child) > 0:
                X = child[0]
                Y = child[1]
                world[Y][X] = "P|5"
            X = partner[0]
            Y = partner[1]
            age = int(world[Y][X][2])
            age = age - 1
            world[Y][X] = world[Y][X][0] + world[Y][X][1] + str(age)


class herbivore(living):
    def __init__(self, y, x):
        super().__init__()
        self.y = y
        self.x = x

    def reproduction(self):
        partner = super().place(self.y, self.x, 'H')
        if len(partner) > 0 and world[partner[1]][partner[0]][2] != '-':
            child = super().place(self.y, self.x, ' ')
            if len(child) > 0:
                X = child[0]
                Y = child[1]
                world[Y][X] = "H|6"
            X = partner[0]
            Y = partner[1]
            age = int(world[Y][X][2])
            age = age - 1
            world[Y][X] = world[Y][X][0] + world[Y][X][1] + str(age)


class grass(living):
    def __init__(self, y, x):
        super().__init__()
        self.y = y
        self.x = x

    def reproduction(self):
        if world[self.y][self.x][2] != '-':
            child = super().place(self.y, self.x, ' ')
            if len(child) > 0:
                X = child[0]
                Y = child[1]
                world[Y][X] = "G|4"
            age = int(world[self.y][self.x][2])
            age = age - 1
            world[self.y][self.x] = world[self.y][self.x][0] + world[self.y][self.x][1] + str(age)


def live():
    for y in range(height):
        for x in range(width):
            if world[y][x] != " " and world[y][x] != "" and world[y][x][2] != '-':
                age = int(world[y][x][2])
                age = age - 1
                world[y][x] = world[y][x][0] + world[y][x][1] + str(age)
                if world[y][x][0] is 'P':
                    pred = predator(y, x)
                    pred.reproduction()
                    pred.Eat(y, x)
                    pred.moving(y, x)
                elif world[y][x][0] is 'H':
                    herb = herbivore(y, x)
                    herb.reproduction()
                    herb.Eat(y, x)
                    herb.moving(y, x)
                elif world[y][x][0] is 'G':
                    plant = grass(y, x)
                    plant.reproduction()
            else:
                world[y][x] = " "


def stop():
    check = input("\n if you want finish program enter x: ")
    if check is 'x':
        return False
    else:
        return True


def playground(amount, animal):
    for j in range(amount):
        x = random.randint(1, width - 2)
        y = random.randint(1, height - 2)
        world[y][x] = animal
    return world


def show():
    clear = lambda: os.system('cls')
    clear()
    for i in range(width):
        print('#', end='')
    print('\n', end='')

    for i in range(height):
        for j in range(width):
            if j is 0 or j is (width - 1):
                print('#', end='')
            elif world[i][j] == "" or world[i][j] == "a":
                print("", end='')
            else:
                print(world[i][j][0], end='')
        print('\n', end='')

    for i in range(width):
        print('#', end='')

def save():
    file = open('./SavedPlayground.txt', 'w')
    for y in range(height):
        for x in range(width):
            file.write(world[y][x][0]+',')
        file.write('\n')
    file.close()

def playground1(choice):
    file = open(choice, 'r')
    for column in range(height):
        array = file.readline().split(',')
        for element in range(len(array)):
            if array[element] is 'H':
                array[element] = array[element][0] + '|' + '6'
            elif array[element] is 'P':
                array[element] = array[element][0] + '|' + '5'
            elif array[element] is 'G':
                array[element] = array[element][0] + '|' + '4'
        world[column] = array
    file.close()
    return world


# Press the green button in the gutter to run the script.
if __name__ == "__main__":
    choose = input("Choose file for download playground:\n 1)New playground\n 2)Saved playground\n")
    if choose is '1':
        choose = './playground.txt'
    else:
        choose = './SavedPlayground.txt'
    cycle = 0
    print("Cycle: " + str(cycle))
    playground1(choose)
    show()
    while stop():
        cycle = cycle + 1
        print("Cycle: " + str(cycle))
        live()
        show()
    save()
