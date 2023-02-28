from Simulation import Simulation
from Field import Field
from FieldLoader import FieldLoader
from GameState import GameState
import sys

loaded = False
treeSpawnChance = 10
iterationsToSkip = 0
height = 20
width = 40

for i in range(1, len(sys.argv)):
    if (sys.argv[i] == "-load"):
        loaded = True
        path = sys.argv[i + 1]
        i += 1
    elif (sys.argv[i] == "-skip"):
        iterationsToSkip = int(sys.argv[i + 1])
        i += 1
    elif (sys.argv[i] == "-h"):
        height = int(sys.argv[i + 1])
        i += 1
    elif (sys.argv[i] == "-w"):
        width = int(sys.argv[i + 1])
        i += 1
    elif (sys.argv[i] == "-tgc"):
        GameState.CONST_TREE_GROWTH_CHANCE = int(sys.argv[i + 1])
        i += 1
    elif (sys.argv[i] == "-tdc"):
        GameState.CONST_TREE_DEATH_CHANCE = int(sys.argv[i + 1])
        i += 1
    elif (sys.argv[i] == "-fac"):
        GameState.CONST_FRUIT_APPEAR_CHANCE = int(sys.argv[i + 1])
        i += 1
    elif (sys.argv[i] == "-fatc"):
        GameState.CONST_FRUIT_TREE_PROXIMITY_APPEAR_CHANCE = int(sys.argv[i + 1])
        i += 1
    elif (sys.argv[i] == "-fdc"):
        GameState.CONST_FRUIT_DISAPPEAR_CHANCE = int(sys.argv[i + 1])
        i += 1

if loaded:
    field = FieldLoader.load(path)
else:
    field = Field(height, width)

Simulation.start(field, iterationsToSkip)


