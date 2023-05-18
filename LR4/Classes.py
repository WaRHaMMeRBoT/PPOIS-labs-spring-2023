import copy
import random


class Animal:
    def __init__(self, satiety=100, age=0, body_size=1.0, name="Wild creature", coordinates=[0, 0], gender=""):
        self.__satiety = satiety
        self.__age = age
        self.__body_size = body_size
        self.__name = name
        self.__coordinates = coordinates
        self.__dead = False
        self.__specie = ""
        self.__gender = gender

    def move(self, finish: list):
        self.__coordinates[0] = finish[0]
        self.__coordinates[1] = finish[1]

    def death(self):
        print(self.__name + " has died in the age of " + str(self.__age))

    def get_satiety(self) -> int:
        return self.__satiety

    def get_age(self) -> int:
        return self.__age

    def get_body_size(self) -> float:
        return self.__body_size

    def get_name(self) -> str:
        return self.__name

    def get_coordinates(self) -> list:
        return self.__coordinates

    def feed(self, food_mass: float):
        self.__satiety += food_mass

    def grow(self):
        self.__age += 1
        self.__satiety -= 10
        self.__body_size = 1.1 * self.__body_size

    def get_gender(self):
        return self.__gender

    def decrease_satiety(self, amount: int)->int:
        self.__satiety -= amount
        return self.__satiety

    def satiety_setter(self, satiety: int):
        self.__satiety = satiety

    def age_setter(self, age: int):
        self.__age = age

    def body_size_setter(self, body_size: float):
        self.__body_size = body_size

    def name_setter(self, name):
        self.__name = name

    def coordinates_setter(self, coordinates: list):
        self.__coordinates = coordinates

    def gender_setter(self, gender: str):
        self.__gender = gender


class Plant:
    def __init__(self, age=0, size=0.1, name="Wild plant", coordinates=(0, 0)):
        self.__age = age
        self.__age: int
        self.__size = size
        self.__name = name
        self.__coordinates = coordinates

    def grow(self):
        self.__age = self.__age + 1
        self.__size += 0.1

    def get_age(self) -> int:
        return int(self.__age)

    def get_size(self) -> float:
        return self.__size

    def being_eaten(self)->float:
        eaten_part = self.__size*0.1
        self.__size -= self.__size*0.1
        return eaten_part

    def get_coordinates(self)->list:
        return self.__coordinates

    def death(self):
        print(self.__name + " has been vanished in the age of " + str(self.__age))

    def get_name(self)->str:
        return self.__name

    def age_setter(self, age: int):
        self.__age = age

    def size_setter(self, size: float):
        self.__size = size

    def name_setter(self, name: str):
        self.__name = name

    def coordinates_setter(self, coordinates: list):
        self.__coordinates = coordinates


class GrassFeeding(Animal):
    def __init__(self, can_eat_grass=True, can_hide=False):
        Animal.__init__(self, body_size=1.25)
        self.__can_eat_grass = can_eat_grass
        self.__can_hide = can_hide

    def get_food_type(self)->bool:
        return self.__can_eat_grass

    def get_hide_ability(self)->bool:
        return self.__can_hide


class Deer(GrassFeeding, Animal):
    def __init__(self, satiety: int, age: int, coordinates: list, gender: str, body_size=1.0, specie="Deer", name=""):
        GrassFeeding.__init__(self)
        Animal.__init__(self, satiety, age, body_size, name, coordinates, gender)
        self.__specie = specie
        self.satiety_setter(satiety)
        self.age_setter(age)
        self.coordinates_setter(coordinates)
        self.gender_setter(gender)
        self.body_size_setter(body_size)
        self.name_setter(name)


class Bison(GrassFeeding, Animal):
    def __init__(self, satiety: int, age: int, coordinates: list, gender: str, body_size=2.0, specie="Bison", name=""):
        GrassFeeding.__init__(self)
        Animal.__init__(self, satiety, age, body_size, name, coordinates, gender)
        self.__specie = specie
        self.satiety_setter(satiety)
        self.age_setter(age)
        self.coordinates_setter(coordinates)
        self.gender_setter(gender)
        self.body_size_setter(body_size)
        self.name_setter(name)


class Mouse(GrassFeeding, Animal):
    def __init__(self, satiety: int, age: int, coordinates: list, gender: str, body_size=0.1, specie="Mouse", name=""):
        GrassFeeding.__init__(self, can_hide=True)
        Animal.__init__(self, satiety, age, body_size, name, coordinates, gender)
        self.__specie = specie
        self.satiety_setter(satiety)
        self.age_setter(age)
        self.coordinates_setter(coordinates)
        self.gender_setter(gender)
        self.body_size_setter(body_size)
        self.name_setter(name)


class Predator(Animal):
    def __init__(self, can_eat_grass=False, can_hide=False):
        Animal.__init__(self)
        self.__can_eat_grass = can_eat_grass
        self.__can_hide = can_hide

    def get_food_type(self)->bool:
        return self.__can_eat_grass


class Wolf(Predator, Animal):
    def __init__(self, satiety: int, age: int, coordinates: list, gender: str, body_size=0.25, specie="Wolf", name=""):
        Animal.__init__(self, satiety, age, body_size, name, coordinates, gender)
        Predator.__init__(self)
        self.__specie = specie
        self.satiety_setter(satiety)
        self.age_setter(age)
        self.coordinates_setter(coordinates)
        self.gender_setter(gender)
        self.body_size_setter(body_size)
        self.name_setter(name)


class Owl(Predator, Animal):
    def __init__(self,  satiety: int, age: int, coordinates: list, gender: str, body_size=0.25, specie="Owl", name=""):
        Animal.__init__(self, satiety, age, body_size, name, coordinates, gender)
        Predator.__init__(self, can_eat_grass=False)
        self.__specie = specie
        self.satiety_setter(satiety)
        self.age_setter(age)
        self.coordinates_setter(coordinates)
        self.gender_setter(gender)
        self.body_size_setter(body_size)
        self.name_setter(name)


class Tree(Plant):
    def __init__(self, age=0, size=0, name="Wild plant", coordinates=(0, 0), can_die=True):
        Plant.__init__(self, age, size, name, coordinates)
        self.can_die=can_die
        self.age_setter(age)
        self.name_setter(name)
        self.coordinates_setter(coordinates)
        self.size_setter(size)


class Grass(Plant):
    def __init__(self, age=0, size=0, name="Wild plant", coordinates=(0, 0), can_die=False):
        Plant.__init__(self, age, size, name, coordinates)
        self.can_die=can_die
        self.age_setter(age)
        self.name_setter(name)
        self.coordinates_setter(coordinates)
        self.size_setter(size)


class Cell:
    def __init__(self, content=None, size=0):
        if content is None:
            content = []
        self._size = size
        self._content = content

    def set_content(self, content: list):
        self._content = content

    def kill(self, creature):
        creature.death()
        self._content.remove(creature)

    def full(self) -> bool:
        if self._size <= len(self._content):
            return True
        else:
            return False

    def add(self, addable: Animal):
        self._content.append(copy.copy(addable))

    def remove(self, removable):
        if removable in self._content:
            self._content.remove(removable)

    def get_content(self)->list:
        return self._content

    def get_number_of_creatures(self)->int:
        return len(self._content)


class Field:
    def __init__(self, matrix: list):
        self.__matrix = matrix

    def get_matrix(self):
        return self.__matrix

    def set_matrix(self, new_matrix: list):
        self.__matrix = new_matrix

    def preadator_feed(self, preadator: Predator, prey: GrassFeeding):
        self.__matrix[prey.get_coordinates()[0]][prey.get_coordinates()[1]].move(preadator)
        self.__matrix[preadator.get_coordinates()[0]][preadator.get_coordinates()[1]].remove(preadator)
        preadator.move(prey.get_coordinates())
        preadator.feed(int(75*prey.get_body_size()))
        self.__matrix[prey.get_coordinates()[0]][prey.get_coordinates()[1]].kill(prey)

    def get_adjacent_cells(self, coordinates: list):
        list_of_adjacent = []
        if coordinates[1] > 0:
            list_of_adjacent.append(self.__matrix[coordinates[0]][coordinates[1]-1])
        elif coordinates[1] <len(self.__matrix)-1:
            list_of_adjacent.append(self.__matrix[coordinates[0]][coordinates[1]+1])
        elif coordinates[0] > 0:
            list_of_adjacent.append(self.__matrix[coordinates[0]-1][coordinates[1]])
        elif coordinates[0] < len(self.__matrix)-1:
            list_of_adjacent.append(self.__matrix[coordinates[0]+1][coordinates[1]])
        elif coordinates[1] > 0 and coordinates[0] > 0:
            list_of_adjacent.append(self.__matrix[coordinates[0]-1][coordinates[1]-1])
        elif coordinates[0] > 0 and coordinates[1] < len(self.__matrix)-1:
            list_of_adjacent.append(self.__matrix[coordinates[0]-1][coordinates[1]+1])
        elif coordinates[0] < len(self.__matrix)-1 and coordinates[1] > 0:
            list_of_adjacent.append(self.__matrix[coordinates[0]+1][coordinates[1]-1])
        elif coordinates[0] < len(self.__matrix)-1 and coordinates[1] < len(self.__matrix)-1:
            list_of_adjacent.append(self.__matrix[coordinates[0]+1][coordinates[1]+1])
        return list_of_adjacent

    @staticmethod
    def grass_feeding(plant: Grass, animal: GrassFeeding):
        food_mass = plant.being_eaten()
        animal.feed(food_mass)

    def breed(self, creature_1: Animal, creature_2: Animal):
        gender = random.choice(["Female", "Male"])
        child_name = "Offspring of " + creature_1.get_name() + " and " + creature_2.get_name()
        if creature_2 == "Owl":
            child = Owl(50, 0, [creature_1.get_coordinates()[0], creature_1.get_coordinates()[1]], gender, 0.1, "Owl",
                        child_name)
        elif creature_2 == "Wolf":
            child = Wolf(50, 0, [creature_1.get_coordinates()[0], creature_1.get_coordinates()[1]], gender, 0.20,
                         "Wolf", child_name)
        elif creature_2 == "Mouse":
            child = Mouse(50, 0, [creature_1.get_coordinates()[0], creature_1.get_coordinates()[1]], gender, 0.01,
                          "Mouse", child_name)
        elif creature_2 == "Deer":
            child = Deer(50, 0, [creature_1.get_coordinates()[0], creature_1.get_coordinates()[1]], gender, 0.25,
                         "Deer", child_name)
        else:
            child = Bison(50, 0, [creature_1.get_coordinates()[0], creature_1.get_coordinates()[1]], gender, 0.4,
                          "Bison", child_name)
        self.__matrix[creature_1.get_coordinates()[0]][creature_1.get_coordinates()[1]].add(child)

    def move(self, creature, where: list):
        creature: Animal
        current_coordinates = creature.get_coordinates()
        self.__matrix[where[0]][where[1]].add(creature)
        self.__matrix[current_coordinates[0]][current_coordinates[1]].remove(creature)
        creature.move(where)

    def create_animal(self, creature, where: list):
        self.__matrix[where[0]][where[1]].add(creature)
