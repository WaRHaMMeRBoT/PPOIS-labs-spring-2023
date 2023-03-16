from core.animals.keta import Keta
from core.animals.shark import Shark
from core.enums.object_enum import ObjectEnum
from core.internal_settings.screen.field import Field
from core.internal_settings.game_state import GameState
from core.objects.plankton import Plankton
from core.objects.obstacle import Obstacle
from core.settings import settings


class FieldLoader:
    @staticmethod
    def load(file: str):
        with open(file, "r") as f:
            line = f.readline()
            splitted = line.split(" ")
            GameState.CONST_REPOPULATION_CHANCE = int(splitted[0])
            GameState.CONST_TREE_GROWTH_CHANCE = int(splitted[1])
            GameState.CONST_TREE_DEATH_CHANCE = int(splitted[2])
            GameState.CONST_BUSH_GROWTH_CHANCE = int(splitted[3])
            GameState.CONST_BUSH_DEATH_CHANCE = int(splitted[4])
            GameState.CONST_OBSTACLE_APPEAR_CHANCE = int(splitted[5])
            GameState.CONST_OBSTACLE_DISAPPEAR_CHANCE = int(splitted[6])
            GameState.CONST_FRUIT_APPEAR_CHANCE = int(splitted[7])
            GameState.CONST_FRUIT_TREE_PROXIMITY_APPEAR_CHANCE = int(splitted[8])
            GameState.CONST_FRUIT_DISAPPEAR_CHANCE = int(splitted[9])
            GameState.CONST_MEAT_DISAPPEAR_CHANCE = int(splitted[10])
            GameState.__iteration = int(splitted[11])
            height = int(splitted[12])
            width = int(splitted[13])
            field = Field(height, width)
            for i in range(0, height, 1):
                line = f.readline()
                for j in range(0, width, 1):
                    splitted = line.split(" ")
                    entity_char = splitted[j][0]
                    obj_char = splitted[j][1]
                    if entity_char == "G":
                        keta = Keta(field.tiles[i][j].cords)
                        field.tiles[i][j].place_entity(keta)
                        GameState.addAnimal(keta)
                    elif entity_char == "T":
                        shark = Shark(field.tiles[i][j].cords)
                        field.tiles[i][j].place_entity(shark)
                        GameState.addAnimal(shark)
                    elif entity_char == "t":
                        field.tiles[i][j].place_entity(Plankton())
                    elif entity_char == "w":
                        field.tiles[i][j].place_entity(Obstacle())

                    if obj_char == "f":
                        field.tiles[i][j].place_object(ObjectEnum.FRUIT)
                    elif obj_char == "m":
                        field.tiles[i][j].place_object(ObjectEnum.MEAT)
                    elif obj_char == "b":
                        field.tiles[i][j].place_object(ObjectEnum.BUSH)
            return field

    @staticmethod
    def save(field: Field):
        with open(settings.FILE_PATH, "w") as f:
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
            f.write(str(GameState.CONST_OBSTACLE_APPEAR_CHANCE))
            f.write(" ")
            f.write(str(GameState.CONST_OBSTACLE_DISAPPEAR_CHANCE))
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
                    if isinstance(entity, Keta):
                        f.write("G")
                    elif isinstance(entity, Shark):
                        f.write("T")
                    elif isinstance(entity, Plankton):
                        f.write("t")
                    elif isinstance(entity, Obstacle):
                        f.write("w")
                    else:
                        f.write("n")

                    obj = field.tiles[i][j].object
                    if obj == ObjectEnum.FRUIT:
                        f.write("f")
                    elif obj == ObjectEnum.MEAT:
                        f.write("m")
                    elif obj == ObjectEnum.BUSH:
                        f.write("b")
                    else:
                        f.write("n")
                    f.write(" ")
