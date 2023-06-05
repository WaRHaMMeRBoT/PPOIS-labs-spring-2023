import json
from plant import Plant
from herbivore import Herbivore
from predator import Predator

class functionsJson:
    
    def __init__(self) -> None:
        pass
    
    def save_json(self, world):
        data = {}
        data['plants'] = []
        data['herbivores'] = []
        data['predators'] = []
        for plant in world.vectorOfPlants:
            data['plants'].append(
                {
                    'row': plant.row,
                    'column': plant.column,
                    'health': plant.health
                }
            )
        for herbivore in world.vectorOfHerbivores:
            data['herbivores'].append(
                {
                    'row': herbivore.row,
                    'column': herbivore.column,
                    'health' : herbivore.health,
                    'sex': herbivore.sex,
                    'createdNow': herbivore.createdNow,
                    'live': herbivore.live,
                    'age': herbivore.age,
                    'id': herbivore.id
                }
            )
        for predator in world.vectorOfPredators:
            data['predators'].append(
                {
                    'row': predator.row,
                    'column': predator.column,
                    'health' : predator.health,
                    'sex': predator.sex,
                    'createdNow': predator.createdNow,
                    'age': predator.age,
                    'live': predator.live
                }
            )
        with open('data.txt', 'w') as outfile:
            json.dump(data, outfile)

    def read_json(self, world):
        with open('data.txt') as json_file:
            data = json.load(json_file)
            for item in data['plants']:
                plant = Plant(item['column'], item['row'], item['health'])
                world.vectorOfPlants.append(plant)
            for item in data['herbivores']:
                herbivore = Herbivore(item['column'], item['row'], item['health'],
                                      world.vectorOfHerbivores)
                world.vectorOfHerbivores.append(herbivore)
            for item in data['predators']:
                predator = Predator(item['column'], item['row'], item['health'])
                world.vectorOfPredators.append(predator)
            for plant in world.vectorOfPlants:
                world.world[plant.row][plant.column].plant = plant
            for herbivore in world.vectorOfHerbivores:
                world.world[herbivore.row][herbivore.column].herbivore = herbivore
            for predator in world.vectorOfPredators:
                world.world[predator.row][predator.column].predator = predator
            