import random

from Controllers.print_garden import print_garden
from Models.serializers import load_state, write_state
from cli import field_collection, FieldAction, BaseGarden, PLANT_COLLECTION, Field


def init_handler(update_garden, garden):
    garden = BaseGarden(random.choices(field_collection, k=3))
    update_garden(garden=garden)


def hydate_handler(arg: int, update_garden, garden):
    FieldAction(garden.fields[int(arg.get()) - 1]).hydrate_field()
    update_garden(arg=arg, garden=garden)
    
    
def heal_hendler(arg: int, update_garden, garden): 
    FieldAction(garden.fields[int(arg.get()) - 1]).fertilizing()
    update_garden(arg=arg, garden=garden)

def desinfect_handler(arg: int, update_garden, garden):
    FieldAction(garden.fields[int(arg.get()) - 1]).desinfect_plant()
    update_garden(arg=arg, garden=garden)

def weeding_hangler(arg: int, update_garden, garden): 
    weeding, plant = arg.get().split(' ')
    plant = PLANT_COLLECTION.get(plant)
    print(len(garden.fields))
    FieldAction(garden.fields[int(weeding) - 1]).weeding(plant())
    update_garden(arg=arg, garden=garden)

def kill_handler(arg: int, update_garden, garden):
    FieldAction(garden.fields[int(arg.get()) - 1]).kill_plant()
    update_garden(arg=arg, garden=garden)

def nextday_handler(update_garden, garden):
    garden.next_day()
    update_garden(garden=garden)
