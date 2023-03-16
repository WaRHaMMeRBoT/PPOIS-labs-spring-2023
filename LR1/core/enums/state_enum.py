from enum import Enum


class StateEnum(Enum):
    MATING = (0,)
    IDLING = (1,)

    LOOKING_FOR_FOOD = (2,)
    HUNTING = (3,)
    EATING = (4,)

    HIDING = (5,)
    RUNNING = (6,)

    LOOKING_FOR_MATE = 7
