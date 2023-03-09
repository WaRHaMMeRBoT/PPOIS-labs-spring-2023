import random
from Object import Object
from Coordinates import Coordinates
from Status import Status
from Stats import Stats
from Entity import Entity


class Animal(Entity):
    def __init__(self, name, cords, stats, status, isCarnivorous):
        self.__name: str = name
        self.__cords: Coordinates = cords
        self.__stats: Stats = stats
        self.__status: Status = status
        self.__isCarnivorous: bool = isCarnivorous
        self.__tookTurn: bool = False
        self.__mateCooldown: int = 3

    @property
    def name(self):
        return self.__name

    @property
    def cords(self):
        return self.__cords

    @cords.setter
    def cords(self, newCords: Coordinates):
        self.__cords = newCords

    @property
    def stats(self):
        return self.__stats

    @property
    def status(self):
        return self.__status

    @status.setter
    def status(self, newStatus: Status):
        self.__status = newStatus

    @property
    def isCarnivorous(self):
        return self.__isCarnivorous

    @property
    def tookTurn(self):
        return self.__tookTurn
    
    @tookTurn.setter
    def tookTurn(self, new: bool):
        self.__tookTurn = new

    @property
    def mateCooldown(self):
        return self.__mateCooldown
    
    @mateCooldown.setter
    def mateCooldown(self, newCd: int):
        self.__mateCooldown = newCd
    
    def __actCarnivorous(self, field):
        if (self.__isHungry()):
            if (self.__lookForFood(field, self.__isMeat)):
                return
            else:
                if self.__hunt(field):
                    return
                else:
                    self.__wander(field)
            return
        elif (self.mateCooldown <= 0 and self.__lookForMate(field)):
            return
        else:
            self.__wander(field)

    def __actHerbivorous(self, field):
        if (self.__lookForHunters(field)):
            return
        elif (self.__isHungry()):
            self.__lookForFood(field, self.__isFruit)
            return
        elif (self.mateCooldown <= 0 and self.__lookForMate(field)):
            return
        else:
            self.__wander(field)

    def act(self, field):
        if (self.__tookTurn == False):
            self.__tookTurn = True
            if self.isCarnivorous == True:
                self.__actCarnivorous(field)
            else:
                self.__actHerbivorous(field)

    def __isHungry(self):
        return self.stats.currentHealth < 0.75 * self.stats.health

    def __hunt(self, field):
        deltas = self.__search(field, self.__isPrey)
        if len(deltas) > 0:
            if abs(deltas[0]) < 2 and abs(deltas[1]) < 2:
                field.tiles[self.cords.x + deltas[0]][self.cords.y + deltas[1]] \
                    .entity.takeDamage(self.stats.damage, field)
            self.status = Status.Hunting
            self.__goTowards(deltas[0], deltas[1], field)
            return True
        return False

    def __isPrey(self, tile):
        return isinstance(tile.entity, Animal) and tile.entity.isCarnivorous == False

    def __lookForHunters(self, field):
        deltas = self.__search(field, self.__isThreat)
        if len(deltas) > 0:
            self.status = Status.Running
            self.__run(deltas[0], deltas[1], field)
            return True
        return False

    def __run(self, i: int, j: int, field):
        x = self.cords.x
        y = self.cords.y
        currentCords = self.cords

        modifier = 0
        while modifier < self.stats.speed:
            if (i < 0):
                newX = min(x + self.stats.speed - modifier, field.height - 1)
            elif(i > 0):
                newX = max(x - self.stats.speed + modifier, 0)
            else:
                newX = x
            if (j < 0):
                newY = min(y + self.stats.speed - modifier, field.width - 1)
            elif(j > 0):
                newY = max(y - self.stats.speed + modifier, 0)
            else:
                newY = y
            if(field.tryMoveEntity(currentCords, Coordinates(newX, newY)) == False):
                modifier += 1
            else:
                return

    def __lookForFood(self, field, function):
        self.status = Status.LookingForFood
        if (function(field.tiles[self.cords.x][self.cords.y])):
            self.__eat(field.tiles[self.cords.x][self.cords.y].object)
            field.tiles[self.cords.x][self.cords.y].removeObject()
            return True
        
        deltas = self.__search(field, function)
        if len(deltas) > 0:
            self.status = Status.LookingForFood
            self.__goTowards(deltas[0], deltas[1], field)
            return True
        
        if (self.isCarnivorous == True):
            return False

        speed = self.stats.speed
        x = self.cords.x
        y = self.cords.y
        newX = max(min(random.choice([x - speed, x + speed]), field.height - 1), 0)
        newY = max(min(random.choice([y - speed, y + speed]), field.width - 1), 0)

        field.tryMoveEntity(self.cords, Coordinates(newX, newY))
        return True


    def __goTowards(self, i: int, j: int, field):
        speed = self.stats.speed
        currentCords = self.cords
        x = currentCords.x
        y = currentCords.y
        modifier = 0
        while modifier < self.stats.speed:
            if (i > 0):
                newX = min(x + speed - modifier, x + i)
            elif(i < 0):
                newX = max(x - speed + modifier, x + i)
            else:
                newX = x
            if (j > 0):
                newY = min(y + speed - modifier, y + j)
            elif(j < 0):
                newY = max(y - speed + modifier, y + j)
            else:
                newY = y
            if(field.tryMoveEntity(currentCords, Coordinates(newX, newY)) == False):
                modifier += 1
            else:
                return

    def __eat(self, theObject: Object):
        currentHealth = self.stats.currentHealth
        health = self.stats.health

        self.status = Status.Eating
        if theObject == Object.fruit:
            self.stats.currentHealth = min(currentHealth + 10, health)
        if theObject == Object.meat:
            self.stats.currentHealth = min(currentHealth + 30, health)

    def takeDamage(self, dmg: int, field):
        self.stats.currentHealth -= dmg
        if (self.stats.currentHealth < 0):
            field.tiles[self.cords.x][self.cords.y].killEntity()

    def __lookForMate(self, field):
        deltas = self.__search(field, self.__isMate)
        if len(deltas) > 0:
            self.status = Status.LookingForMate
            if abs(deltas[0]) < 2 and abs(deltas[1]) < 2:
                self.__mate(field)
                return True
            self.__goTowards(deltas[0], deltas[1], field)
            return True
        return False

    def __mate(self, field):
        self.status = Status.Mating
        if (self.isCarnivorous == True):
            self.mateCooldown = 20
        else:
            self.mateCooldown = 4
        field.spawnAnimalNearby(self.cords, self.name)

    
    def __wander(self, field):
        speed = self.stats.speed
        currentCords = self.cords
        x = currentCords.x
        y = currentCords.y

        self.status = Status.Idling
        newX = max(min(random.randint(x - speed / 2, x + speed / 2), field.height - 1), 0)
        newY = max(min(random.randint(y - speed / 2, y + speed / 2), field.width - 1), 0)
        field.tryMoveEntity(currentCords, Coordinates(newX, newY))

    def __search(self, field, function):
        x = self.cords.x
        y = self.cords.y
        sight = self.stats.sight

        for i in range(-sight, sight + 1, 1):
            for j in range(-sight, sight + 1, 1):
                if (field.areLegitCoordinates(x + i, y + j) and i!=j!=0):
                    if (function(field.tiles[x + i][y + j])):
                        return [i,j]
        return []

    def __isThreat(self, tile):
        return isinstance(tile.entity, Animal) and tile.entity.isCarnivorous == True

    def __isMate(self, tile):
        return isinstance(tile.entity, Animal) and tile.entity.name == self.name

    def __isFruit(self, tile):
        return (tile.object == Object.fruit)

    def __isMeat(self, tile):
        return (tile.object == Object.meat)
    