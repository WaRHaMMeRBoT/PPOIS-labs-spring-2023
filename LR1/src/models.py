from .model_entity import *


class GameBoard:

    def __init__(self, size=0):
        if size <= 1 or size >= 10:
            raise Exception("Недопустимый размер поля")
        self.__length = size
        self.__board = [[Cell() for _ in range(size)] for _ in range(size)]

    def __call__(self):
        for i in range(self.__length):
            for j in range(self.__length):
                print(self.__board[i][j], end=" ")
            print()

    def __getitem__(self, x):
        if x >= self.__length or x < 0:
            raise Exception("Выход за пределы поля")
        return self.__board[x]

    def set_board(self, board: list):
        self.__board = board

    def move(self):
        used = []
        for i in range(self.__length):
            for j in range(self.__length):
                for k in self.__board[i][j].get_entity():
                    if str(k) == "P" or k in used:
                        continue
                    used.append(k)
                    move_x = randint(-1, 1)
                    move_y = randint(-1, 1)
                    while i + move_x < 0 or move_x + i >= self.__length:
                        move_x = randint(-1, 1)
                    while j + move_y < 0 or move_y + j >= self.__length:
                        move_y = randint(-1, 1)
                    if self.__board[i + move_x][j + move_y].is_free():
                        self.__board[i][j].delete_entity(k)
                        self.__board[i + move_x][j + move_y].put_entity(k)

    def plant_reproduction(self):
        used = []
        for i in range(self.__length):
            for j in range(self.__length):
                for k in self.__board[i][j].get_entity():
                    if str(k) == "P" and k not in used:
                        plant = Plant()
                        used.extend([k, plant])
                        move_x = randint(-1, 1)
                        move_y = randint(-1, 1)
                        while i + move_x < 0 or move_x + i >= self.__length:
                            move_x = randint(-1, 1)
                        while j + move_y < 0 or move_y + j >= self.__length:
                            move_y = randint(-1, 1)

                        if self.__board[i + move_x][j + move_y].get_plant():
                            self.__board[i + move_x][j + move_y].get_plant().heal_plant()

                        elif self.__board[i + move_x][j + move_y].is_free():
                            self.__board[i + move_x][j + move_y].put_entity(plant)

    def iteration(self):
        for i in range(self.__length):
            for j in range(self.__length):
                self.__board[i][j].nutrition()

        self.move()

        self.plant_reproduction()

        for i in range(self.__length):
            for j in range(self.__length):
                self.__board[i][j].reproduction()

        for i in range(self.__length):
            for j in range(self.__length):
                self.__board[i][j].iteration()

        for i in range(self.__length):
            for j in range(self.__length):
                self.__board[i][j].death()

    def to_dict(self):
        data = dict()
        data['length'] = self.__length
        data['board'] = [[cell.to_dict() for cell in x] for x in self.__board]
        return data


class Cell:
    max_entity = 4

    def __init__(self, herbivore=None, predator=None, plant=None):
        if predator is None:
            predator = []
        if herbivore is None:
            herbivore = []

        self.__herbivore = herbivore
        self.__predator = predator
        self.__plant = plant

    def __len__(self):
        if self.__plant:
            return len(self.__herbivore) + len(self.__predator) + 1
        else:
            return len(self.__herbivore) + len(self.__predator)

    def __str__(self):
        res = ''
        for i in self.__herbivore:
            res += str(i)
        for i in self.__predator:
            res += str(i)
        if self.__plant:
            res += str(self.__plant)
        while len(res) != 4:
            res += "*"
        return f"{res[:2]}{res[2:]}"

    def to_dict(self):
        data = dict()
        data["herbivore"] = [h.to_dict() for h in self.__herbivore]
        data["predator"] = [p.to_dict() for p in self.__predator]
        if self.__plant:
            data["plant"] = self.__plant.to_dict()
        else:
            data["plant"] = None
        return data

    def get_entity(self):
        entity = []
        entity.extend(self.__herbivore)
        entity.extend(self.__predator)
        if self.__plant:
            entity.append(self.__plant)
        return entity

    def get_plant(self):
        return self.__plant

    def put_entity(self, entity):
        if self.is_free():
            if isinstance(entity, Wolf | Fox | Bear):
                self.__herbivore.append(entity)
            elif isinstance(entity, Rabbit | Deer):
                self.__predator.append(entity)
            elif isinstance(entity, Plant) and not self.__plant:
                self.__plant = entity
            else:
                raise Exception("Данный объект не является подходящим классом")
        else:
            raise Exception("Для объекта нет места на клетке")

    def delete_entity(self, entity):
        if entity in self.__herbivore:
            self.__herbivore.remove(entity)
        elif entity in self.__predator:
            self.__predator.remove(entity)
        elif entity == self.__plant:
            self.__plant = None
        else:
            raise Exception("Объект не находится в этой клетке")

    def clear_cell(self):
        self.__herbivore = []
        self.__predator = []
        self.__plant = None

    def is_free(self):
        return len(self) < Cell.max_entity

    def contains(self, name: str) -> list:
        lst = []
        entity = self.get_entity()
        for i in entity:
            if name == str(i):
                lst.append(i)
        return lst

    def iteration(self):
        for i in self.__herbivore:
            i.iteration()
        for i in self.__predator:
            i.iteration()
        if self.__plant:
            self.__plant.iteration()

    def death(self):
        for i in self.__herbivore:
            if i.is_dead():
                self.delete_entity(i)
        for i in self.__predator:
            if i.is_dead():
                self.delete_entity(i)
        if self.__plant and self.__plant.is_dead():
            self.delete_entity(self.__plant)

    @staticmethod
    def adding_child(lst: list):
        male = False
        female = False
        for i in lst:
            if i.get_sex() == 0:
                male = True
            else:
                female = True
        return male and female

    def reproduction(self):
        if self.is_free():
            if len(self.contains("W")) > 1:
                if self.adding_child(self.contains("W")):
                    self.put_entity(Wolf())

            if self.is_free():
                if len(self.contains("F")) > 1:
                    if self.adding_child(self.contains("F")):
                        self.put_entity(Fox())

            if self.is_free():
                if len(self.contains("B")) > 1:
                    if self.adding_child(self.contains("B")):
                        self.put_entity(Bear())

            if self.is_free():
                if len(self.contains("R")) > 1:
                    if self.adding_child(self.contains("R")):
                        self.put_entity(Rabbit())

            if self.is_free():
                if len(self.contains("D")) > 1:
                    if self.adding_child(self.contains("D")):
                        self.put_entity(Deer())

    def nutrition(self):
        #Травоядное ест растение
        if self.__plant and self.__predator:
            self.__predator[0].nutrition(self.__plant)
            self.__plant = None
        #Хищник есть травоядного
        if self.__predator and self.__herbivore:
            for i in self.__herbivore:
                for j in self.__predator:
                    if i.get_size() >= j.get_size() and not self.__predator[0].chance_to_escape():
                        i.nutrition(j)
                        self.delete_entity(j)
