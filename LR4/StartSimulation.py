from Controller import Controller
from View import View
from Model.Field import Field
from FieldLoader import FieldLoader
from Model.GameState import GameState
from main import PrintWorld
import sys

loaded = False
treeSpawnChance = 10
iterationsToSkip = 0
height = 20
width = 20


def startWindow():
    if loaded:
        field = FieldLoader.load(path)
    else:
        field = Field(height, width)

    controller = Controller(field)
    View(controller)


for i in range(1, len(sys.argv)):
    if (sys.argv[i] == "-load"):
        loaded = True
        path = sys.argv[i + 1]
        i += 1
    elif (sys.argv[i] == "-first"):
        test = PrintWorld(6, 5, 2)

        test.print()
        test.initWorld()
        test.printStage()
        for i in range(10):
            test.oneIneration()
    elif (sys.argv[i] == "-second"):
        startWindow()
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
        GameState.CONST_FRUIT_TREE_PROXIMITY_APPEAR_CHANCE = int(
            sys.argv[i + 1])
        i += 1
    elif (sys.argv[i] == "-fdc"):
        GameState.CONST_FRUIT_DISAPPEAR_CHANCE = int(sys.argv[i + 1])
        i += 1