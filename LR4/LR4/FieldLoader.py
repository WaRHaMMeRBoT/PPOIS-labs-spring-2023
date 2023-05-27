from Model.Field import Field
from Model.GameState import GameState
from Model.Entities import Gazelle
from Model.Entities import Tiger
from Model.Object import Object
from Model.Entities import Wall
from Model.Entities import Tree


class FieldLoader:
    staticmethod

    def load(fileName: str):
        with open(fileName, 'r') as f:
            line = f.readline()
            splittedLine = line.split(' ')
            GameState.CONST_REPOPULATION_CHANCE = int(splittedLine[0])
            GameState.CONST_TREE_GROWTH_CHANCE = int(splittedLine[1])
            GameState.CONST_TREE_DEATH_CHANCE = int(splittedLine[2])
            GameState.CONST_BUSH_GROWTH_CHANCE = int(splittedLine[3])
            GameState.CONST_BUSH_DEATH_CHANCE = int(splittedLine[4])
            GameState.CONST_WALL_APPEAR_CHANCE = int(splittedLine[5])
            GameState.CONST_WALL_DISAPPEAR_CHANCE = int(splittedLine[6])
            GameState.CONST_FRUIT_APPEAR_CHANCE = int(splittedLine[7])
            GameState.CONST_FRUIT_TREE_PROXIMITY_APPEAR_CHANCE = int(
                splittedLine[8])
            GameState.CONST_FRUIT_DISAPPEAR_CHANCE = int(splittedLine[9])
            GameState.CONST_MEAT_DISAPPEAR_CHANCE = int(splittedLine[10])
            GameState.__iteration = int(splittedLine[11])
            height = int(splittedLine[12])
            width = int(splittedLine[13])
            field = Field(height, width)
            for i in range(0, height, 1):
                line = f.readline()
                for j in range(0, width, 1):
                    splittedLine = line.split(' ')
                    entityChar = splittedLine[j][0]
                    objectChar = splittedLine[j][1]
                    if entityChar == 'G':
                        gazelle = Gazelle(field.tiles[i][j].cords)
                        field.tiles[i][j].placeEntity(gazelle)
                        GameState.addAnimal(gazelle)
                    elif entityChar == 'T':
                        tiger = Tiger(field.tiles[i][j].cords)
                        field.tiles[i][j].placeEntity(tiger)
                        GameState.addAnimal(tiger)
                    elif entityChar == 't':
                        field.tiles[i][j].placeEntity(Tree())
                    elif entityChar == 'w':
                        field.tiles[i][j].placeEntity(Wall())

                    if objectChar == 'f':
                        field.tiles[i][j].placeObject(Object.fruit)
                    elif objectChar == 'm':
                        field.tiles[i][j].placeObject(Object.meat)
                    elif objectChar == 'b':
                        field.tiles[i][j].placeObject(Object.bush)
            return field

    staticmethod

    def save(field: Field):
        with open('save', 'w') as f:
            f.write(str(GameState.CONST_REPOPULATION_CHANCE))
            f.write(" ")
            f.write(str(GameState.CONST_TREE_GROWTH_CHANCE))
            f.write(" ")
            f.write(str(GameState.CONST_TREE_DEATH_CHANCE))
            f.write(" ")
            f.write(str(GameState.CONST_BUSH_GROWTH_CHANCE))
            f.write(" ")
            f.write(str(GameState.CONST_BUSH_DEATH_CHANCE))
            f.write(" ")
            f.write(str(GameState.CONST_WALL_APPEAR_CHANCE))
            f.write(" ")
            f.write(str(GameState.CONST_WALL_DISAPPEAR_CHANCE))
            f.write(" ")
            f.write(str(GameState.CONST_FRUIT_APPEAR_CHANCE))
            f.write(" ")
            f.write(str(GameState.CONST_FRUIT_TREE_PROXIMITY_APPEAR_CHANCE))
            f.write(" ")
            f.write(str(GameState.CONST_FRUIT_DISAPPEAR_CHANCE))
            f.write(" ")
            f.write(str(GameState.CONST_MEAT_DISAPPEAR_CHANCE))
            f.write(" ")
            f.write(str(GameState.getIteration()))
            f.write(" ")
            f.write(str(field.height))
            f.write(" ")
            f.write(str(field.width))
            for i in range(0, field.height, 1):
                f.write("\n")
                for j in range(0, field.width, 1):
                    entity = field.tiles[i][j].entity
                    if isinstance(entity, Gazelle):
                        f.write("G")
                    elif isinstance(entity, Tiger):
                        f.write("T")
                    elif isinstance(entity, Tree):
                        f.write("t")
                    elif isinstance(entity, Wall):
                        f.write("w")
                    else:
                        f.write("n")

                    theObject = field.tiles[i][j].object
                    if theObject == Object.fruit:
                        f.write("f")
                    elif theObject == Object.meat:
                        f.write("m")
                    elif theObject == Object.bush:
                        f.write("b")
                    else:
                        f.write("n")
                    f.write(" ")
