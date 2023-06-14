import pickle
from random import randint

class Animal:
    def __init__(self, x, y, energy):
        self.x = x
        self.y = y
        self.energy = energy

    def move(self):
        dx = randint(-1, 1)
        dy = randint(-1, 1)
        new_x = self.x + dx
        new_y = self.y + dy
        if new_x < 0 or new_x >= FIELD_SIZE or new_y < 0 or new_y >= FIELD_SIZE:
            return
        field[self.x][self.y], field[new_x][new_y] = None, field[self.x][self.y]
        self.x, self.y = new_x, new_y
        self.energy -= 1

    def eat(self):
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                x, y = self.x + dx, self.y + dy
                if 0 <= x < FIELD_SIZE and 0 <= y < FIELD_SIZE:
                    if isinstance(field[x][y], Plant):
                        self.energy += field[x][y].nutrition
                        field[x][y] = None
                        return

    def reproduce(self):
        if self.energy >= 10:
            dx = randint(-1, 1)
            dy = randint(-1, 1)
            new_x = self.x + dx
            new_y = self.y + dy
            if new_x < 0 or new_x >= FIELD_SIZE or new_y < 0 or new_y >= FIELD_SIZE:
                return
            if field[new_x][new_y] is None:
                field[new_x][new_y] = type(self)(new_x, new_y, self.energy // 2)
                self.energy //= 2

    def die(self):
        if self.energy <= 0:
            field[self.x][self.y] = None
        elif self.energy >= 20:
            field[self.x][self.y] = type(Plant)(self.x, self.y, 5)

class Plant:
    def __init__(self, x, y, nutrition):
        self.x = x
        self.y = y
        self.nutrition = nutrition

    def reproduce(self):
        if self.nutrition >= 10:
            dx = randint(-1, 1)
            dy = randint(-1, 1)
            new_x = self.x + dx
            new_y = self.y + dy
            if new_x < 0 or new_x >= FIELD_SIZE or new_y < 0 or new_y >= FIELD_SIZE:
                return
            if field[new_x][new_y] is None:
                field[new_x][new_y] = type(self)(new_x, new_y, self.nutrition // 2)
                self.nutrition //= 2

    def die(self):
        if self.nutrition <= 0:
            field[self.x][self.y] = None

field = []

#считывание сохранений
with open("data_file.pickle","rb") as read_file:
    field = pickle.load(read_file)

if field == []:
     # параметры поля
    FIELD_SIZE = int(input("Введите размер поля: "))
    ANIMAL_COUNT = int(input("Введите количество животных: "))
    PLANT_COUNT = int(input("Введите количество растений: "))

    # поле
    field = [[None] * FIELD_SIZE for _ in range(FIELD_SIZE)]

    # создаем животных и растения
    for i in range(ANIMAL_COUNT):
        x = randint(0, FIELD_SIZE - 1)
        y = randint(0, FIELD_SIZE - 1)
        field[x][y] = Animal(x, y, 10)

    for i in range(PLANT_COUNT):
        x = randint(0, FIELD_SIZE - 1)
        y = randint(0, FIELD_SIZE - 1)
        field[x][y] = Plant(x, y, 5)
else:

    #считывание данных
    FIELD_SIZE = len(field)
    ANIMAL_COUNT = 0
    PLANT_COUNT = 0

    for row in field:
            for cell in row:
                if isinstance(cell, Animal):
                    ANIMAL_COUNT = ANIMAL_COUNT + 1
                elif isinstance(cell, Plant):
                    PLANT_COUNT = PLANT_COUNT + 1


key = 1
while True:

    # списки изменений
    move_list = []
    reproduce_list = []
    death_list = []

    # движение животных и добавление в список перемещений
    for x in range(FIELD_SIZE):
        for y in range(FIELD_SIZE):
            if isinstance(field[x][y], Animal):
                move_list.append((x, y))

    # перемещаем животных
    for x, y in move_list:
        field[x][y].move()

        # добавляем животных для размножения или удаления в соответствующий список
        if field[x][y]: 
            if field[x][y].energy >= 10:
                reproduce_list.append((x, y))
            elif field[x][y].energy <= 0 or field[x][y].energy >= 20:
                death_list.append((x, y))

    # размножаем и добавляем в список
    for x in range(FIELD_SIZE):
        for y in range(FIELD_SIZE):
            if isinstance(field[x][y], Animal):
                if (x, y) in reproduce_list:
                    field[x][y].reproduce()
            elif isinstance(field[x][y], Plant):
                if (x, y) in reproduce_list:
                    field[x][y].reproduce()

    # удаление животных и растений из списка мертвывх
    for x, y in death_list:
        if isinstance(field[x][y], Animal):
            field[x][y].die()
        elif isinstance(field[x][y], Plant):
            field[x][y].die()

    # печатаем состояние поля
    for row in field:
        for cell in row:
            if cell is None:
                print('.', end='')
            elif isinstance(cell, Animal):
                print('A', end='')
            elif isinstance(cell, Plant):
                print('P', end='')
        print()
    print("\n")

    # выгрузка состояния
    with open("data_file.pickle","wb") as write_file:
        pickle.dump(field, write_file)


    # симуляция заканчивается, если не осталось животных
    if all(all(cell is None or isinstance(cell, Plant) for cell in row) for row in field):
        field = []
        with open("data_file.pickle","wb") as write_file:
            pickle.dump(field, write_file)
        break

    # авто итерция
    key = key - 1
    if key <= 0:
        print("Введите число итераций:")
        key = int(input())
