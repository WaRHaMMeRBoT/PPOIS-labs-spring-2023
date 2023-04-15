import sys

from Garden.field import Field
from Garden.garden import BaseGarden
from Plants.abstract_plants import BasePlant


def print_plant(plant: BasePlant, file_to_write=sys.stdout):
    if hasattr(plant, 'fruit'):
        print(f'|\tAge: {plant.age}'.ljust(45),
              f'|\tFruit: {plant.fruit}'.ljust(45),
              f'|\tHealth: {plant.health}'.ljust(45),
              f'|\tHydration level: {plant.hydration_level}'.ljust(45),
              f'|\tIllness damage: {plant.illness.destruction_power}'.ljust(45),
              f'|\tPests damage: {plant.pests.destruction_power}'.ljust(45), sep='|\n', end='|\n', file=file_to_write)
    else:

        print(f'|\tAge: {plant.age}'.ljust(45),
              f'|\tHealth: {plant.health}'.ljust(45),
              f'|\tHydration level: {plant.hydration_level}'.ljust(45),
              f'|\tIllness damage: {plant.illness.destruction_power}'.ljust(45),
              f'|\tPests damage: {plant.pests.destruction_power}'.ljust(45), sep='|\n', end='|\n', file=file_to_write)


def print_field(field: Field, file_to_write=sys.stdout):
    print('_' * 47, file=file_to_write)
    if field.plant is not None:
        print(f'|\tPlant: {field.plant}'.ljust(45), end='|\n', file=file_to_write)
        # if hasattr(field.plant, 'ready_plant'):
        #     print(f'|\tage: {field.plant.age}'.ljust(45), end='|\n')
        # else:
        print_plant(field.plant, file_to_write)
    else:
        print(f'|\tPlant: Weed'.ljust(45),
              f'|\tHealth: {field.weed.health}'.ljust(45),
              sep='|\n', end='|\n', file=file_to_write)
    print('|' + '_' * 46 + '|', file=file_to_write)


def print_garden(garden: BaseGarden, file_to_write=sys.stdout):
    i = 1
    print(f'Weather: {garden.WEATHER}', file=file_to_write)
    for field in garden.fields:
        print(f'{i}.', file=file_to_write)
        print_field(field, file_to_write)
        i += 1
