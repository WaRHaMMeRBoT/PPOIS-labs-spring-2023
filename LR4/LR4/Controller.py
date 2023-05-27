import msvcrt
from random import randint, randrange
import random
from Model.Field import Field
from Model.Coordinates import Coordinates
from Model.GameState import GameState
from Model.Entities import Animal, Gazelle, Tiger, Tree, Wall, Status
from Model.Object import Object
from Model.Tile import DisplayedSprite

class Controller():
    def __init__(self, field):
        self.field = field

    def updateGame(self):
        if msvcrt.kbhit():
            key = msvcrt.getch()
            if key == b'q':
                return
            elif key == b'g':
                self.spawnAnimalAnywhere("Gazelle")
            elif key == b't':
                self.spawnAnimalAnywhere("Tiger")
            elif key == b's':
                input("Simulation is paused. Press enter to resume...")
            elif key == b'e':
                Controller.save()

        self.iterateGameState()
        for i in range(0, self.field.height, 1):
            for j in range(0, self.field.width, 1):
                self.trySpawnCycle(self.field.tiles[i][j], self.field)

        for i in GameState.animalList:
            self.animalAct(i, self.field)
            i.tookTurn = False
            i.mateCooldown -= 1
            self.takeDamage(i, 1, self.field)

    def tryMoveEntity(self, field, fromCords: Coordinates, toCords: Coordinates):
        tileToMoveFrom = field.tiles[fromCords.x][fromCords.y]
        tileToMoveTo = field.tiles[toCords.x][toCords.y]
        if tileToMoveTo.entity != None:
            return False
        entityToMove = tileToMoveFrom.entity
        entityToMove.cords = tileToMoveTo.cords
        self.removeEntity(tileToMoveFrom)
        self.placeEntity(tileToMoveTo, entityToMove)
        return True

    def spawnAnimalNearby(self, field, parentCords: Coordinates, name: str):
        x = parentCords.x
        y = parentCords.y
        for i in range(-1, 2, 1):
            for j in range(-1, 2, 1):
                if (self.areLegitCoordinates(field, x + i, y + j) and i!=j!=0):
                    if (field.tiles[x + i][y + j].entity == None):
                        if (name == "Gazelle"):
                            animal = Gazelle(Coordinates(x + i, y + j))
                        elif (name == "Tiger"):
                            animal = Tiger(Coordinates(x + i, y + j))
                        self.placeEntity(field.tiles[x + i][y + j], animal)
                        self.addAnimal(animal)

    def spawnAnimalAnywhere(self, name: str):
        cords = Coordinates(randrange(0, self.height), randrange(0, self.width))
        self.spawnAnimalNearby(cords, name)

    def areLegitCoordinates(self, field, x: int, y: int):
        return x >= 0 and y >= 0 and x < field.height and y < field.width

    def addAnimal(self, animal: Animal):
        GameState.speciesDictionary[animal.name] += 1
        GameState.animalList.append(animal)
        if (GameState.speciesDictionary[animal.name] == 3):
            GameState.extinctionList.remove(animal.name)

    def removeAnimal(self, animal: Animal):
        GameState.speciesDictionary[animal.name] -= 1
        GameState.animalList.remove(animal)
        if (GameState.speciesDictionary[animal.name] == 2):
            GameState.extinctionList.append(animal.name)

    def iterateGameState(self):
        GameState.iteration += 1

    def tryRepopulate(self, tile, species):
        if (randrange(100000) <= GameState.CONST_REPOPULATION_CHANCE):
            if (species == "Gazelle"):
                tile.entity = Gazelle(tile.cords)
            elif (species == "Tiger"):
                tile.entity = Tiger(tile.cords)
            self.resetDisplayedSprite(tile)
            self.addAnimal(tile.entity)
            return True
        return False

    def placeEntity(self, tile, entity):
        tile.entity = entity
        self.resetDisplayedSprite(tile)

    def removeEntity(self, tile):
        tile.entity = None
        self.resetDisplayedSprite(tile)

    def removeObject(self, tile):
        tile.object = None
        self.resetDisplayedSprite(tile)

    def placeObject(self, tile, newObject):
        tile.object = newObject
        self.resetDisplayedSprite(tile)

    def tryPlaceEntity(self, tile, entity, chance: int):
        if (randrange(100000) <= chance):
            self.placeEntity(tile, entity)
            return True
        return False

    def tryPlaceObject(self, tile, theObject, chance: int):
        if (randrange(100000) <= chance):
            self.placeObject(tile, theObject)
            return True
        return False

    def tryRemoveObject(self, tile, chance: int):
        if (randrange(100000) <= chance):
            self.removeObject(tile)
            return True
        return False

    def tryRemoveEntity(self, tile, chance: int):
        if (randrange(100000) <= chance):
            self.removeEntity(tile)
            return True
        return False
    
    def killEntity(self, tile):
        if (isinstance(tile.entity, Animal)):
            if (tile.entity.isCarnivorous == False):
                tile.object = Object.meat
            self.removeAnimal(tile.entity)
        self.removeEntity(tile)

    def inTreeProximity(self, tile, field):
        x = tile.cords.x
        y = tile.cords.y
        for i in range(-1, 2, 1):
            for j in range(-1, 2, 1):
                if (self.areLegitCoordinates(field, x + i, y + j)):
                    if (isinstance(tile.field.tiles[x + i][y + j].entity, Tree)):
                        return True
        return False

    def isBorderTile(self, tile):
        x = tile.cords.x
        y = tile.cords.y
        return x == 0 or y == 0 or x == tile.field.height - 1 or y == tile.field.width - 1

    def resetDisplayedSprite(self, tile):
        if (tile.entity != None):
            if (isinstance(tile.entity, Gazelle)):
                tile.displayedSprite = DisplayedSprite.gazelle
            elif (isinstance(tile.entity, Tiger)):
                tile.displayedSprite = DisplayedSprite.tiger
            elif (isinstance(tile.entity, Wall)):
                tile.displayedSprite = DisplayedSprite.wall
            elif (isinstance(tile.entity, Tree)):
                tile.displayedSprite = DisplayedSprite.tree
        elif (tile.object != None):
            if (tile.object == Object.fruit):
                tile.displayedSprite = DisplayedSprite.fruit
            elif (tile.object == Object.meat):
                tile.displayedSprite = DisplayedSprite.meat
            elif (tile.object == Object.bush):
                tile.displayedSprite = DisplayedSprite.bush
        else:
            tile.displayedSprite = DisplayedSprite.empty

    def trySpawnCycle(self, tile, field):
        if (tile.entity == None and tile.object == None):
            if (self.isBorderTile(tile)):
                for species in GameState.extinctionList:
                    if (self.tryRepopulate(tile, species)):
                        return
            elif (self.tryPlaceEntity(tile, Tree(), GameState.CONST_TREE_GROWTH_CHANCE)):
                return
            elif (self.tryPlaceEntity(tile, Wall(), GameState.CONST_WALL_APPEAR_CHANCE)):
                return
            elif (self.tryPlaceObject(tile, Object.bush, GameState.CONST_BUSH_GROWTH_CHANCE)):
                return
            elif (self.inTreeProximity(tile, field)):
                if (self.tryPlaceObject(tile, Object.fruit, GameState.CONST_FRUIT_TREE_PROXIMITY_APPEAR_CHANCE)):
                    return
            else:
                if (self.tryPlaceObject(tile, Object.fruit, GameState.CONST_FRUIT_APPEAR_CHANCE)):
                    return
        elif (tile.entity == None):
            if (tile.object == Object.fruit):
                self.tryRemoveObject(tile, GameState.CONST_FRUIT_DISAPPEAR_CHANCE)
            elif (tile.object == Object.bush):
                self.tryRemoveObject(tile, GameState.CONST_BUSH_DEATH_CHANCE)
            elif (tile.object == Object.meat):
                self.tryRemoveObject(tile, GameState.CONST_MEAT_DISAPPEAR_CHANCE)
        else:
            if (isinstance(tile.entity, Tree)):
                self.tryRemoveEntity(tile, GameState.CONST_TREE_DEATH_CHANCE)
            elif (isinstance(tile.entity, Wall)):
                self.tryRemoveEntity(tile, GameState.CONST_WALL_DISAPPEAR_CHANCE)

    def actCarnivorous(self, animal, field):
        if (self.isHungry(animal)):
            if (self.lookForFood(animal, field, self.isMeat)):
                return
            else:
                if self.hunt(animal, field):
                    return
                else:
                    self.wander(animal, field)
            return
        elif (animal.mateCooldown <= 0 and self.lookForMate(animal, field)):
            return
        else:
            self.wander(animal, field)

    def actHerbivorous(self, animal, field):
        if (self.lookForHunters(animal, field)):
            return
        elif (self.isHungry(animal)):
            self.lookForFood(animal, field, self.isFruit)
            return
        elif (animal.mateCooldown <= 0 and self.lookForMate(animal, field)):
            return
        else:
            self.wander(animal, field)

    def animalAct(self, animal, field):
        if (animal.tookTurn == False):
            animal.tookTurn = True
            if animal.isCarnivorous == True:
                self.actCarnivorous(animal, field)
            else:
                self.actHerbivorous(animal, field)

    def isHungry(self, animal):
        return animal.stats.currentHealth < 0.75 * animal.stats.health

    def hunt(self, animal, field):
        deltas = self.search(animal, field, self.isPrey)
        if len(deltas) > 0:
            if abs(deltas[0]) < 2 and abs(deltas[1]) < 2:
                 self.takeDamage(field.tiles[animal.cords.x + deltas[0]][animal.cords.y + deltas[1]].entity, animal.stats.damage, field)
            animal.status = Status.Hunting
            self.goTowards(animal, deltas[0], deltas[1], field)
            return True
        return False

    def isPrey(self, animal, tile):
        return isinstance(tile.entity, Animal) and tile.entity.isCarnivorous == False

    def lookForHunters(self, animal, field):
        deltas = self.search(animal, field, self.isThreat)
        if len(deltas) > 0:
            animal.status = Status.Running
            self.run(animal, deltas[0], deltas[1], field)
            return True
        return False

    def run(self, animal, i: int, j: int, field):
        x = animal.cords.x
        y = animal.cords.y
        currentCords = animal.cords

        modifier = 0
        while modifier < animal.stats.speed:
            if (i < 0):
                newX = min(x + animal.stats.speed - modifier, field.height - 1)
            elif(i > 0):
                newX = max(x - animal.stats.speed + modifier, 0)
            else:
                newX = x
            if (j < 0):
                newY = min(y + animal.stats.speed - modifier, field.width - 1)
            elif(j > 0):
                newY = max(y - animal.stats.speed + modifier, 0)
            else:
                newY = y
            if(self.tryMoveEntity(field, currentCords, Coordinates(newX, newY)) == False):
                modifier += 1
            else:
                return

    def lookForFood(self, animal, field, function):
        animal.status = Status.LookingForFood
        if (function(animal, field.tiles[animal.cords.x][animal.cords.y])):
            self.eat(animal, field.tiles[animal.cords.x][animal.cords.y].object)
            self.removeObject(field.tiles[animal.cords.x][animal.cords.y])
            return True
        
        deltas = self.search(animal, field, function)
        if len(deltas) > 0:
            animal.status = Status.LookingForFood
            self.goTowards(animal, deltas[0], deltas[1], field)
            return True
        
        if (animal.isCarnivorous == True):
            return False

        speed = animal.stats.speed
        x = animal.cords.x
        y = animal.cords.y
        newX = max(min(random.choice([x - speed, x + speed]), field.height - 1), 0)
        newY = max(min(random.choice([y - speed, y + speed]), field.width - 1), 0)

        self.tryMoveEntity(field, animal.cords, Coordinates(newX, newY))
        return True

    def goTowards(self, animal, i: int, j: int, field):
        speed = animal.stats.speed
        currentCords = animal.cords
        x = currentCords.x
        y = currentCords.y
        modifier = 0
        while modifier < animal.stats.speed:
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
            if(self.tryMoveEntity(field, currentCords, Coordinates(newX, newY)) == False):
                modifier += 1
            else:
                return

    def eat(self, animal, theObject: Object):
        currentHealth = animal.stats.currentHealth
        health = animal.stats.health

        animal.status = Status.Eating
        if theObject == Object.fruit:
            animal.stats.currentHealth = min(currentHealth + 10, health)
        if theObject == Object.meat:
            animal.stats.currentHealth = min(currentHealth + 30, health)

    def takeDamage(self, animal, dmg: int, field):
        animal.stats.currentHealth -= dmg
        if (animal.stats.currentHealth < 0):
            self.killEntity(field.tiles[animal.cords.x][animal.cords.y])

    def lookForMate(self, animal, field):
        deltas = self.search(animal, field, self.isMate)
        if len(deltas) > 0:
            animal.status = Status.LookingForMate
            if abs(deltas[0]) < 2 and abs(deltas[1]) < 2:
                self.mate(animal, field)
                return True
            self.goTowards(animal, deltas[0], deltas[1], field)
            return True
        return False

    def mate(self, animal, field):
        animal.status = Status.Mating
        if (animal.isCarnivorous == True):
            animal.mateCooldown = 20
        else:
            animal.mateCooldown = 4
        self.spawnAnimalNearby(field, animal.cords, animal.name)
    
    def wander(self, animal, field):
        speed = animal.stats.speed
        currentCords = animal.cords
        x = currentCords.x
        y = currentCords.y

        animal.status = Status.Idling
        newX = max(min(randint(x - speed / 2, x + speed / 2), field.height - 1), 0)
        newY = max(min(randint(y - speed / 2, y + speed / 2), field.width - 1), 0)
        self.tryMoveEntity(field, currentCords, Coordinates(newX, newY))

    def search(self, animal, field, function):
        x = animal.cords.x
        y = animal.cords.y
        sight = animal.stats.sight

        for i in range(-sight, sight + 1, 1):
            for j in range(-sight, sight + 1, 1):
                if (self.areLegitCoordinates(field, x + i, y + j) and i!=j!=0):
                    if (function(animal, field.tiles[x + i][y + j])):
                        return [i,j]
        return []

    def isThreat(self, animal, tile):
        return isinstance(tile.entity, Animal) and tile.entity.isCarnivorous == True

    def isMate(self, animal, tile):
        return isinstance(tile.entity, Animal) and tile.entity.name == animal.name

    def isFruit(self, animal, tile):
        return (tile.object == Object.fruit)

    def isMeat(self, animal, tile):
        return (tile.object == Object.meat)

    def getField(self):
        return self.field