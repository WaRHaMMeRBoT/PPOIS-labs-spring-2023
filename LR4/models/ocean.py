import json
from itertools import combinations, product
from random import randrange

import models.environment as env


class Ocean(env.Area):
    pass


class Shark(env.Predator):
    def __init__(self, health: int, age: int, hunger: int = 100) -> None:
        env.Predator.__init__(self, health, age, 6, 60, False, hunger)

    def class_name(self) -> str:
        return "shark"

    def reproduct(self) -> "Shark":
        return Shark(100, 0)

    pass


class Parrotfish(env.Herbivorous):
    def __init__(self, health: int, age: int, hunger: int = 100) -> None:
        env.Herbivorous.__init__(self, health, age, 5, 20, False, hunger)

    def class_name(self) -> str:
        return "parrotfish"

    def reproduct(self) -> "Parrotfish":
        return Parrotfish(100, 0)

    pass


class Barracuda(env.Predator):
    def __init__(self, health: int, age: int, hunger: int = 100) -> None:
        env.Predator.__init__(self, health, age, 6, 60, False, hunger)

    def class_name(self) -> str:
        return "barracuda"

    def reproduct(self) -> "Barracuda":
        return Barracuda(100, 0)

    pass


class Plant(env.Plant):
    pass


def parse_json(json_string: str) -> Ocean:
    text = json.loads(json_string)
    field = Ocean(text["area"])
    for animal in text["livings"]:
        if animal["type"] == "shark":
            shark = Shark(animal["health"], animal["age"], animal["hunger"])
            field.add_animal(shark, tuple(animal["position"]))
        elif animal["type"] == "parrotfish":
            parrotfish = Parrotfish(animal["health"], animal["age"], animal["hunger"])
            field.add_animal(parrotfish, tuple(animal["position"]))
        elif animal["type"] == "barracuda":
            barracuda = Barracuda(animal["health"], animal["age"], animal["hunger"])
            field.add_animal(barracuda, tuple(animal["position"]))
        else:
            print(f'Unknown animal name "{animal["type"]}!')

    for plant in text["plants"]:
        tasty_plant = env.Plant(plant["lifespan"], plant["energy_value"])
        field.add_plant(tasty_plant, tuple(plant["position"]))
    return field


def convert_to_json(field: Ocean) -> str:
    text = dict()
    text.update({"area": field.area})
    animals = list()
    for animal, position in field.livings.items():
        animals.append(
            {
                "type": animal.class_name(),
                "health": animal.health,
                "age": animal.age,
                "hunger": animal.hunger,
                "position": position,
            }
        )
    text.update({"livings": animals})
    plants = list()
    for plant, position in field.plants.items():
        plants.append(
            {
                "lifespan": plant.lifespan,
                "energy_value": plant.energy_value,
                "position": position,
            }
        )
    text.update({"plants": plants})

    text = json.dumps(text, indent=4, separators=(", ", ": "))
    return text


def add_animal(field: Ocean, animal_type: str):
    if animal_type == "shark":
        animal = Shark(100, 0)
        field.add_animal(animal, (randrange(field.area[0]), randrange(field.area[1])))
    elif animal_type == "parrotfish":
        animal = Parrotfish(100, 0)
        field.add_animal(animal, (randrange(field.area[0]), randrange(field.area[1])))
    elif animal_type == "barracuda":
        animal = Barracuda(100, 0)
        field.add_animal(animal, (randrange(field.area[0]), randrange(field.area[1])))
    else:
        print(f'Unknown animal name "{animal_type}"!')


def add_plant(field: Ocean, lifespan: int, energy_value: int):
    plant = Plant(lifespan, energy_value)
    field.add_plant(plant, (randrange(field.area[0]), randrange(field.area[1])))


def _change_position(field: env.Area, animal: env.Animal):
    direction = animal.move()
    if direction == "up":
        pos_list = list(field.livings[animal])
        pos_list[1] = (pos_list[1] - 1) % (field.area[1] - 1)
        field.livings[animal] = tuple(pos_list)
    elif direction == "down":
        pos_list = list(field.livings[animal])
        pos_list[1] = (pos_list[1] + 1) % (field.area[1] - 1)
        field.livings[animal] = tuple(pos_list)
    elif direction == "left":
        pos_list = list(field.livings[animal])
        pos_list[0] = (pos_list[0] - 1) % (field.area[0] - 1)
        field.livings[animal] = tuple(pos_list)
    elif direction == "right":
        pos_list = list(field.livings[animal])
        pos_list[0] = (pos_list[0] + 1) % (field.area[0] - 1)
        field.livings[animal] = tuple(pos_list)
    print(f"{animal.class_name()} moved to position {pos_list}")


def _feed(field, pair):
    if isinstance(pair[0], env.Predator) and isinstance(pair[1], env.Animal):
        if pair[0].class_name() == pair[1].class_name():
            return
        pair[0].eat(pair[1])
        field.remove_animal(pair[1])
        print(f"{pair[1].class_name()} has been eaten by {pair[0].class_name()}")
    elif isinstance(pair[1], env.Predator) and isinstance(pair[0], env.Animal):
        if pair[0].class_name() == pair[1].class_name():
            return
        pair[1].eat(pair[0])
        field.remove_animal(pair[0])
        print(f"{pair[0].class_name()} has been eaten by {pair[1].class_name()}")
    elif isinstance(pair[0], env.Herbivorous) and isinstance(pair[1], env.Plant):
        pair[0].eat(pair[1])
        field.remove_plant(pair[1])
        print(f"Plant has been eaten by {pair[0].class_name()}")
    elif isinstance(pair[1], env.Herbivorous) and isinstance(pair[0], env.Plant):
        pair[1].eat(pair[0])
        field.remove_plant(pair[0])
        print(f"Plant has been eaten by {pair[1].class_name()}")


def skip(field: Ocean, number_of_steps: int):
    for _ in range(number_of_steps):
        for x, y in product(range(field.area[0]), range(field.area[1])):
            buff_animals = list(
                filter(lambda a: field.livings[a] == (x, y), field.livings)
            )
            buff_plants = list(
                filter(lambda p: field.plants[p] == (x, y), field.plants)
            )
            if len(buff_animals) == 0:
                continue
            # Change position
            list(map(lambda a: _change_position(field, a), buff_animals))
            # Starve
            list(map(lambda a: a.starve(), buff_animals))
            # Reproduct
            if len(buff_animals) in range(2, 5):
                pairs = list(combinations(buff_animals, 2))
                to_reproduct = list(
                    filter(lambda a: a[0].class_name() == a[1].class_name(), pairs)
                )
                list(
                    map(
                        lambda a: field.add_animal(
                            a[0].reproduct(), field.livings[a[1]]
                        ),
                        to_reproduct,
                    )
                )
            # Feed
            if len(buff_animals + buff_animals) in range(2, 5):
                pairs = list(combinations(buff_animals + buff_plants, 2))
                list(map(lambda a: _feed(field, a), pairs))
                buff_animals = list(
                    filter(lambda a: field.livings[a] == (x, y), field.livings)
                )
            # Dead
            dead_list = list(filter(lambda a: a.death(), buff_animals))
            list(map(lambda a: field.remove_animal(a), dead_list))
