from dataclasses import Field
from enum import Enum
from random import randrange
from typing import List
from Model import GameState
from Model.Entities import Gazelle
from Model import Object
from Model.Entities import Tree
from Model.Entities import Wall
from Model.Entities import Animal
from Model import Coordinates
from Model.Entities import Entity
from Model.Entities import Tiger

class DisplayedSprite(Enum):
    empty = 0,
    fruit = 1,
    meat = 2,
    bush = 3,
    tree = 4,
    wall = 5,
    gazelle = 6,
    tiger = 7

class Tile:
    def __init__(self, cords: Coordinates, field):
        self.object: Object = None
        self.entity: Entity = None
        self.cords: Coordinates = cords
        self.field: Field = field
        self.displayedSprite: DisplayedSprite = DisplayedSprite.empty