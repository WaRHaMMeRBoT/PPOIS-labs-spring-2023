import random
from random import randint

from core.enums.object_enum import ObjectEnum
from core.enums.state_enum import StateEnum
from core.internal_settings.screen.coordinates import Coordinates
from core.internal_settings.entity import Entity
from core.internal_settings.stats import Stats


class Animal(Entity):
    def __init__(self, name, cords, stats, status, is_carnivorous):
        self.__name: str = name
        self.__cords: Coordinates = cords
        self.__stats: Stats = stats
        self.__status: StateEnum = status
        self.__is_carnivorous: bool = is_carnivorous
        self.__took_turn: bool = False
        self.__friend_cool_down: int = 3

    @property
    def name(self):
        return self.__name

    @property
    def cords(self):
        return self.__cords

    @cords.setter
    def cords(self, new_cords: Coordinates):
        self.__cords = new_cords

    @property
    def stats(self):
        return self.__stats

    @property
    def status(self):
        return self.__status

    @status.setter
    def status(self, new_status: StateEnum):
        self.__status = new_status

    @property
    def is_carnivorous(self):
        return self.__is_carnivorous

    @property
    def took_turn(self):
        return self.__took_turn

    @took_turn.setter
    def took_turn(self, new: bool):
        self.__took_turn = new

    @property
    def friend_cool_down(self):
        return self.__friend_cool_down

    @friend_cool_down.setter
    def friend_cool_down(self, new_cd: int):
        self.__friend_cool_down = new_cd

    def __act_carnivorous(self, field):
        if self.__is_hungry():
            if self.__look_for_food(field, self.__is_meat):
                return
            else:
                if self.__hunt(field):
                    return
                else:
                    self.__wander(field)
            return
        elif self.friend_cool_down <= 0 and self.__look_for_friend(field):
            return
        else:
            self.__wander(field)

    def __act_herbivorous(self, field):
        if self.__look_for_hunters(field):
            return
        elif self.__is_hungry():
            self.__look_for_food(field, self.__is_fruit)
            return
        elif self.friend_cool_down <= 0 and self.__look_for_friend(field):
            return
        else:
            self.__wander(field)

    def act(self, field):
        if not self.__took_turn:
            self.__took_turn = True
            if self.is_carnivorous:
                self.__act_carnivorous(field)
            else:
                self.__act_herbivorous(field)

    def __is_hungry(self):
        return self.stats.currentHealth < 0.75 * self.stats.health

    def __hunt(self, field):
        deltas = self.__search(field, self.__is_prey)
        if len(deltas) > 0:
            if abs(deltas[0]) < 2 and abs(deltas[1]) < 2:
                field.tiles[self.cords.x + deltas[0]][
                    self.cords.y + deltas[1]
                ].entity.take_damage(self.stats.damage, field)
            self.status = StateEnum.HUNTING
            self.__go_towards(deltas[0], deltas[1], field)
            return True
        return False

    def __is_prey(self, tile):
        return isinstance(tile.entity, Animal) and tile.entity.is_carnivorous == False

    def __look_for_hunters(self, field):
        deltas = self.__search(field, self.__is_threat)
        if len(deltas) > 0:
            self.status = StateEnum.RUNNING
            self.__run(deltas[0], deltas[1], field)
            return True
        return False

    def __run(self, i: int, j: int, field):
        x = self.cords.x
        y = self.cords.y
        current_cords = self.cords

        modifier = 0
        while modifier < self.stats.speed:
            if i < 0:
                new_x = min(x + self.stats.speed - modifier, field.height - 1)
            elif i > 0:
                new_x = max(x - self.stats.speed + modifier, 0)
            else:
                new_x = x
            if j < 0:
                new_y = min(y + self.stats.speed - modifier, field.width - 1)
            elif j > 0:
                new_y = max(y - self.stats.speed + modifier, 0)
            else:
                new_y = y
            if not field.move_entity(current_cords, Coordinates(new_x, new_y)):
                modifier += 1
            else:
                return

    def __look_for_food(self, field, function):
        self.status = StateEnum.LOOKING_FOR_FOOD
        if function(field.tiles[self.cords.x][self.cords.y]):
            self.__eat(field.tiles[self.cords.x][self.cords.y].object)
            field.tiles[self.cords.x][self.cords.y].remove_object()
            return True

        deltas = self.__search(field, function)
        if len(deltas) > 0:
            self.status = StateEnum.LOOKING_FOR_FOOD
            self.__go_towards(deltas[0], deltas[1], field)
            return True

        if self.is_carnivorous:
            return False

        speed = self.stats.speed
        x = self.cords.x
        y = self.cords.y
        new_x = max(min(random.choice([x - speed, x + speed]), field.height - 1), 0)
        new_y = max(min(random.choice([y - speed, y + speed]), field.width - 1), 0)

        field.move_entity(self.cords, Coordinates(new_x, new_y))
        return True

    def __go_towards(self, i: int, j: int, field):
        speed = self.stats.speed
        current_cords = self.cords
        x = current_cords.x
        y = current_cords.y
        modifier = 0
        while modifier < self.stats.speed:
            if i > 0:
                new_x = min(x + speed - modifier, x + i)
            elif i < 0:
                new_x = max(x - speed + modifier, x + i)
            else:
                new_x = x
            if j > 0:
                new_y = min(y + speed - modifier, y + j)
            elif j < 0:
                new_y = max(y - speed + modifier, y + j)
            else:
                new_y = y
            if not field.move_entity(current_cords, Coordinates(new_x, new_y)):
                modifier += 1
            else:
                return

    def __eat(self, obj: ObjectEnum):
        current_hp = self.stats.currentHealth
        health = self.stats.health

        self.status = StateEnum.EATING
        if obj == ObjectEnum.FRUIT:
            self.stats.currentHealth = min(current_hp + 10, health)
        if obj == ObjectEnum.MEAT:
            self.stats.currentHealth = min(current_hp + 30, health)

    def take_damage(self, dmg: int, field):
        self.stats.currentHealth -= dmg
        if self.stats.currentHealth < 0:
            field.tiles[self.cords.x][self.cords.y].kill_entity()

    def __look_for_friend(self, field):
        deltas = self.__search(field, self.__is_friend)
        if len(deltas) > 0:
            self.status = StateEnum.LOOKING_FOR_MATE
            if abs(deltas[0]) < 2 and abs(deltas[1]) < 2:
                self.__friend(field)
                return True
            self.__go_towards(deltas[0], deltas[1], field)
            return True
        return False

    def __friend(self, field):
        self.status = StateEnum.MATING
        if self.is_carnivorous:
            self.friend_cool_down = 20
        else:
            self.friend_cool_down = 4
        field.spawn_animal_nearby(self.cords, self.name)

    def __wander(self, field):
        speed = self.stats.speed
        current_cords = self.cords
        x = current_cords.x
        y = current_cords.y

        self.status = StateEnum.IDLING
        new_x = max(min(randint(x - speed / 2, x + speed / 2), field.height - 1), 0)
        new_y = max(min(randint(y - speed / 2, y + speed / 2), field.width - 1), 0)
        field.move_entity(current_cords, Coordinates(new_x, new_y))

    def __search(self, field, function):
        x = self.cords.x
        y = self.cords.y
        sight = self.stats.sight

        for i in range(-sight, sight + 1, 1):
            for j in range(-sight, sight + 1, 1):
                if field.if_legit_cords(x + i, y + j) and i != j != 0:
                    if function(field.tiles[x + i][y + j]):
                        return [i, j]
        return []

    def __is_threat(self, tile):
        return isinstance(tile.entity, Animal) and tile.entity.is_carnivorous == True

    def __is_friend(self, tile):
        return isinstance(tile.entity, Animal) and tile.entity.name == self.name

    def __is_fruit(self, tile):
        return tile.object == ObjectEnum.FRUIT

    def __is_meat(self, tile):
        return tile.object == ObjectEnum.MEAT
