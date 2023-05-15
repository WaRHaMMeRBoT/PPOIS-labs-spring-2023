import models.ocean as ocean


def next(field: ocean.Ocean, number_of_steps: int, update_callback=None):
    ocean.skip(field, number_of_steps)
    if update_callback:
        update_callback()


def add_instance(field: ocean.Ocean, type: str, update_callback=None):
    if type != "plant":
        ocean.add_animal(field, type)
    else:
        ocean.add_plant(field, 10, 30)
    if update_callback:
        update_callback()
