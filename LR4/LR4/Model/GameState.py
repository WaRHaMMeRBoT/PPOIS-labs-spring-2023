from typing import List
from Model.Entities import Animal

class GameState:
    
    CONST_REPOPULATION_CHANCE: int = 1000
    CONST_TREE_GROWTH_CHANCE: int  = 10
    CONST_TREE_DEATH_CHANCE: int  = 200
    CONST_BUSH_GROWTH_CHANCE: int  = 8
    CONST_BUSH_DEATH_CHANCE: int  = 400
    CONST_WALL_APPEAR_CHANCE: int  = 1
    CONST_WALL_DISAPPEAR_CHANCE: int  = 100
    CONST_FRUIT_APPEAR_CHANCE: int  = 30
    CONST_FRUIT_TREE_PROXIMITY_APPEAR_CHANCE: int  = 6000
    CONST_FRUIT_DISAPPEAR_CHANCE: int  = 10000
    CONST_MEAT_DISAPPEAR_CHANCE: int  = 1000

    extinctionList: List[str] = ["Gazelle", "Tiger"]
    speciesDictionary = dict(Gazelle = 0, Tiger = 0)
    animalList = []
    iteration = 0



