from abc import ABC, abstractmethod
from random import choice


class Food(ABC):
    energy_value: int
    for_herbivorous: bool


class Animal(Food):
    health: int
    age: int
    hunger: int
    lifespan: int

    def __init__(
        self,
        health: int,
        age: int,
        lifespan: int,
        energy_value: int,
        for_herbivorous: bool,
        hunger: int = 100,
    ) -> None:
        self.health = health
        self.age = age
        self.lifespan = lifespan
        self.energy_value = energy_value
        self.for_herbivorous = for_herbivorous
        self.hunger = hunger

    def move(self) -> str:
        self.age += 1
        return choice(["up", "down", "left", "right"])

    @abstractmethod
    def eat(self, meal: Food) -> None:
        pass

    @abstractmethod
    def reproduct(self) -> "Animal":
        pass

    @abstractmethod
    def class_name(self) -> str:
        pass

    def starve(self) -> None:
        if self.hunger > 0:
            self.hunger -= 10
        elif self.hunger == 0:
            self.health -= 10

    def death(self) -> bool:
        return self.health <= 0 or self.age > self.lifespan

    pass


class Predator(Animal):
    def eat(self, meal: Food) -> None:
        if not meal.for_herbivorous:
            self.hunger += meal.energy_value
            self.health += 5

    pass


class Herbivorous(Animal):
    def eat(self, meal: Food) -> None:
        if meal.for_herbivorous:
            self.hunger += meal.energy_value
            self.health += 5

    pass


class Plant(Food):
    lifespan: int
    for_herbivorous = True

    def __init__(self, lifespan: int, energy_value: int) -> None:
        self.lifespan = lifespan
        self.energy_value = energy_value

    pass


class Area:
    area: tuple[int, int]
    livings: dict[Animal, tuple[int, int]]
    plants: dict[Plant, tuple[int, int]]

    def __init__(
        self, size: tuple[int, int], livings: dict = dict(), plants: dict = dict()
    ) -> None:
        self.area = size
        self.livings = livings
        self.plants = plants

    def add_animal(self, new_animal: Animal, position: tuple[int, int]) -> None:
        if (
            len(
                list(
                    filter(
                        lambda a: a.class_name() == new_animal.class_name(),
                        self.livings,
                    )
                )
            )
            > 10
        ):
            return
        self.livings.update({new_animal: position})

    def add_plant(self, new_plant: Plant, position: tuple[int, int]) -> None:
        if len(self.plants) > 10:
            return
        self.plants.update({new_plant: position})

    def remove_animal(self, animal: Animal) -> None:
        if animal in self.livings:
            self.livings.pop(animal)

    def remove_plant(self, plant: Plant) -> None:
        if plant in self.plants:
            self.plants.pop(plant)
