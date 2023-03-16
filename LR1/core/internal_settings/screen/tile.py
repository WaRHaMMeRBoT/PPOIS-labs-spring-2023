from dataclasses import Field
from random import randrange
from typing import List

from core.animals.animal import Animal
from core.animals.keta import Keta
from core.animals.shark import Shark
from core.enums.displayed_sprite_enum import DisplayedSprite
from core.enums.object_enum import ObjectEnum
from core.internal_settings.screen.coordinates import Coordinates
from core.internal_settings.entity import Entity
from core.internal_settings.game_state import GameState
from core.objects.plankton import Plankton
from core.objects.obstacle import Obstacle


class Tile:
    def __init__(self, cords: Coordinates, field):
        self.__object: ObjectEnum = None
        self.__entity: Entity = None
        self.__cords: Coordinates = cords
        self.__field: Field = field
        self.__displayedSprite: DisplayedSprite = DisplayedSprite.void

    @property
    def object(self):
        return self.__object

    @property
    def entity(self):
        return self.__entity

    @property
    def cords(self):
        return self.__cords

    @property
    def field(self):
        return self.__field

    @property
    def displayedSprite(self):
        return self.__displayedSprite

    def try_spawn_cycle(self, field):
        if not (self.entity and self.object):
            if self.is_border_tile():
                for species in GameState.getExtinctionList():
                    if self.__repopulate(species):
                        return
            elif self.__try_place_entity(Plankton(), GameState.CONST_TREE_GROWTH_CHANCE):
                return
            elif self.__try_place_entity(Obstacle(), GameState.CONST_OBSTACLE_APPEAR_CHANCE):
                return
            elif self.__try_place_object(
                ObjectEnum.BUSH, GameState.CONST_BUSH_GROWTH_CHANCE
            ):
                return
            elif self.__in_three_proximity(field):
                if self.__try_place_object(
                    ObjectEnum.FRUIT, GameState.CONST_FRUIT_TREE_PROXIMITY_APPEAR_CHANCE
                ):
                    return
            else:
                if self.__try_place_object(
                    ObjectEnum.FRUIT, GameState.CONST_FRUIT_APPEAR_CHANCE
                ):
                    return
        elif not self.entity:
            if self.object == ObjectEnum.FRUIT:
                self.__try_remove_object(GameState.CONST_FRUIT_DISAPPEAR_CHANCE)
            elif self.object == ObjectEnum.BUSH:
                self.__try_remove_object(GameState.CONST_BUSH_DEATH_CHANCE)
            elif self.object == ObjectEnum.MEAT:
                self.__try_remove_object(GameState.CONST_MEAT_DISAPPEAR_CHANCE)
        else:
            if isinstance(self.entity, Plankton):
                self.__try_remove_entity(GameState.CONST_TREE_DEATH_CHANCE)
            elif isinstance(self.entity, Obstacle):
                self.__try_remove_entity(GameState.CONST_OBSTACLE_DISAPPEAR_CHANCE)

    def __repopulate(self, species: List[str]):
        if randrange(100000) <= GameState.CONST_REPOPULATION_CHANCE:
            if species == "Keta":
                self.__entity = Keta(self.cords)
            elif species == "Shark":
                self.__entity = Shark(self.cords)
            self.__reset_displayed_sprite()
            GameState.addAnimal(self.entity)
            return True
        return False

    def place_entity(self, entity: Entity):
        self.__entity = entity
        self.__reset_displayed_sprite()

    def remove_entity(self):
        self.__entity = None
        self.__reset_displayed_sprite()

    def remove_object(self):
        self.__object = None
        self.__reset_displayed_sprite()

    def place_object(self, new_obj: ObjectEnum):
        self.__object = new_obj
        self.__reset_displayed_sprite()

    def __try_place_entity(self, entity, chance: int):
        if randrange(100000) <= chance:
            self.place_entity(entity)
            return True
        return False

    def __try_place_object(self, obj, chance: int):
        if randrange(100000) <= chance:
            self.place_object(obj)
            return True
        return False

    def __try_remove_object(self, chance: int):
        if randrange(100000) <= chance:
            self.remove_object()
            return True
        return False

    def __try_remove_entity(self, chance: int):
        if randrange(100000) <= chance:
            self.remove_entity()
            return True
        return False

    def kill_entity(self):
        if isinstance(self.entity, Animal):
            if not self.entity.is_carnivorous:
                self.__object = ObjectEnum.MEAT
            GameState.removeAnimal(self.entity)
        self.remove_entity()

    def __in_three_proximity(self, field):
        x = self.cords.x
        y = self.cords.y
        for i in range(-1, 2, 1):
            for j in range(-1, 2, 1):
                if field.if_legit_cords(x + i, y + j):
                    if isinstance(self.field.tiles[x + i][y + j].entity, Plankton):
                        return True
        return False

    def is_border_tile(self):
        x = self.cords.x
        y = self.cords.y
        return (
            x == 0 or y == 0 or x == self.field.height - 1 or y == self.field.width - 1
        )

    def __reset_displayed_sprite(self):
        if self.entity is not None:
            if isinstance(self.entity, Keta):
                self.__displayedSprite = DisplayedSprite.keta
            elif isinstance(self.entity, Shark):
                self.__displayedSprite = DisplayedSprite.shark
            elif isinstance(self.entity, Obstacle):
                self.__displayedSprite = DisplayedSprite.obstacle
            elif isinstance(self.entity, Plankton):
                self.__displayedSprite = DisplayedSprite.tree
        elif self.object is not None:
            if self.object == ObjectEnum.FRUIT:
                self.__displayedSprite = DisplayedSprite.alga
            elif self.object == ObjectEnum.MEAT:
                self.__displayedSprite = DisplayedSprite.flesh
            elif self.object == ObjectEnum.BUSH:
                self.__displayedSprite = DisplayedSprite.shellfish
        else:
            self.__displayedSprite = DisplayedSprite.void
