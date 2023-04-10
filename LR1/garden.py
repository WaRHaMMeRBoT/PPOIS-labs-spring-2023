import json
import numpy
from plants import*
from weather import*
from soil import*
from random import randint


class Garden:
    def __init__(self, x, y, weather):
        self.x = x
        self.y = y
        self.area = numpy.empty((x, y), dtype="object")
        self.grow = numpy.empty((x, y), dtype="object")
        self.weather = weather
        self.soil = Soil()
    
    
    def remove(self, x, y):
        self.area[x][y] = None
        self.grow[x][y] = None
    
        
    def plantConstructorAccess(self, name)-> object:
        match name:
            case "corn":
                return Corn()
            case "garlic":
                return Garlic()
            case "onion":
                return Onion()
            case "melon":
                return Melon()
            case "spinach":
                return Spinach()
            case "weed":
                return Weed()
            case "rice":
                return Rice()
            case "cucumber":
                return Сucumber()
            case "broccoli":
                return Broccoli()


    def seedConstructorAccess(self, name)-> object:
        match name:
            case "corn":
                return CornSeed()
            case "garlic":
                return GarlicSeed()
            case "onion":
                return OnionSeed()
            case "melon":
                return MelonSeed()
            case "spinach":
                return SpinachSeed()
            case "rice":
                return RiceSeed()
            case "cucumber":
                return СucumberSeed()
            case "broccoli":
                return BroccoliSeed()
        
    
    def planting(self, x1, y1, x2, y2, type):
        seed = Seed
        seed = self.seedConstructorAccess(type)
        for i in range(x1 , (x2+1)):
            for j in range(y1 , (y2 + 1)):
                self.area[i][j] = seed
                self.grow[i][j] = 0
                
        
    def calculateSeedGrowingSpeed(self, seed):
        currentGrowingSpeed = seed.basicGrowingSpeed
        if self.soil.nutrients < seed.minNutrientNeed or self.soil.nutrients > seed.maxNutrientNeed: 
            currentGrowingSpeed *= 0.5
        if self.soil.waterLevel < seed.minWaterNeed or self.soil.waterLevel > seed.maxWaterNeed: 
            currentGrowingSpeed *= 0.5
        return currentGrowingSpeed
    
    
    def calculatePlantGrowingSpeed(self, plant):
        currentGrowingSpeed = plant.basicGrowingSpeed
        if self.soil.nutrients < plant.minNutrientNeed or self.soil.nutrients > plant.maxNutrientNeed: 
            currentGrowingSpeed *= 0.5
        if self.soil.waterLevel < plant.minWaterNeed or self.soil.waterLevel > plant.maxWaterNeed: 
            currentGrowingSpeed *= 0.5
        if self.weather.light < plant.minLightNeed or self.weather.light > plant.maxLightNeed: 
            currentGrowingSpeed *= 0.5
        return currentGrowingSpeed
    
    
    def skipTime(self, times):
        for a in range(times):   
            for i in range(self.x): 
                for j in range(self.y):
                    if self.area[i][j] is not None:
                        if self.area[i][j].type == 0: 
                            currentGrowingSpeed = self.calculateSeedGrowingSpeed(self.area[i][j])
                            self.grow[i][j] += currentGrowingSpeed
                            if currentGrowingSpeed == self.area[i][j].basicGrowingSpeed * 0.25:
                                self.area[i][j].health -= 20
                            if currentGrowingSpeed == self.area[i][j].basicGrowingSpeed and self.area[i][j].health < 100:
                                self.area[i][j].health += 20
                            currentGrowingSpeed = 0
                            if self.grow[i][j] >= 10:
                                self.area[i][j] = self.plantConstructorAccess(self.area[i][j].name)
                                if randint(1, 10) == 10:
                                    self.area[i][j] = self.plantConstructorAccess("weed")
                            if self.area[i][j].health <= 0:
                                print(f'{self.area[i][j].name} (x: {i} y: {j}) has been died\n')
                                self.remove(i, j)
                        else:
                            currentGrowingSpeed = self.calculatePlantGrowingSpeed(self.area[i][j])
                            self.grow[i][j] += currentGrowingSpeed
                            if currentGrowingSpeed == self.area[i][j].basicGrowingSpeed * 0.25:
                                self.area[i][j].health -= 20
                            if currentGrowingSpeed == self.area[i][j].basicGrowingSpeed * 0.125:
                                self.area[i][j].health -= 20
                            if currentGrowingSpeed == self.area[i][j].basicGrowingSpeed and self.area[i][j].health < 100:
                                self.area[i][j].health += 20
                            currentGrowingSpeed = 0
                            if self.grow[i][j] >= 100:
                                print(f'{self.area[i][j].name} (x: {i} y: {j}) has been fully grown\n')
                                self.remove(i, j)
                            if self.area[i][j].health <= 0:
                                print(f'{self.area[i][j].name} (x: {i} y: {j}) has been died\n')
                                self.remove(i, j)
            nextWeather = randint(1, 4)
            match nextWeather:
                case 1:
                    self.weather = Sunny()
                case 2:
                    self.weather = Overcast()
                case 3:
                    self.weather = Rainy()
                case 4:
                    self.weather = Drought()
            self.soil.nutrients -= 5
            if self.soil.nutrients < 0:
                self.soil.nutrients = 0
            if self.soil.nutrients > 100:
                self.soil.nutrients = 100
            self.soil.waterLevel += self.weather.humidity / 5
            self.soil.waterLevel -= 25
            if self.soil.waterLevel < 0:
                self.soil.waterLevel = 0
            if self.soil.waterLevel > 100:
                self.soil.waterLevel = 100
            
       
            
    def view (self):
        for i in range(self.x): 
            for j in range(self.y):
                if self.area[i][j] is not None:
                    print(self.area[i][j].icon, end=' ')
                else:
                    print(end='   ')
            print()
            
    
    def __str__(self, x, y):
        info = ''
        info += f'Type : {self.area[x][y].name}\n'
        info += f'Health : {self.area[x][y].health}\n'
        info += f'Grow : {self.grow[x][y]}\n'
        info += f'Current growing speed : {self.calculatePlantGrowingSpeed(self.area[x][y])}\n'
        print(info)
    
    
    def enviroment(self):
        info = ''
        info += self.weather.__str__()
        info += ''
        info += self.soil.__str__()
        print(info)
    
    
    def save(self):
        with open("C:\Work\PPOIS\Sem4\lab1\garden.json") as f:
            data = json.load(f)
        data["numbers"].clear()
        data["numbers"].append(self.x)
        data["numbers"].append(self.y)
        data["numbers"].append(self.soil.nutrients)
        data["numbers"].append(self.soil.waterLevel)
        data["line"] = self.weather.type
        data["line_list"].clear()
        data["number_list"].clear()
        for i in range(self.x):
            temp =[]
            temp1 = []
            for j in range(self.y):
                if self.area[i][j] is not None:
                    temp.append(self.area[i][j].name)
                    temp1.append(self.grow[i][j])
                else:
                    temp.append(None)
                    temp1.append(None)
            data["line_list"].append(temp)
            data["number_list"].append(temp1)
        with open("C:\Work\PPOIS\Sem4\lab1\garden.json", "w") as f:
            json.dump(data, f, indent=4)
            
            
    def weeding(self):
        for i in range(self.x): 
            for j in range(self.y):
                if self.area[i][j] is not None:
                    if self.area[i][j].name == "weed":
                        self.remove(i, j)
        
    
def loadFile()->Garden:
    with open("C:\Work\PPOIS\Sem4\lab1\garden.json") as f:
        data = json.load(f)
    data_numbers=data["numbers"]
    data_line=data["line"]
    data_line_list=data["line_list"]
    data_number_list=data["number_list"]
    weather = get_type_of_weather(data_line)

    garden = Garden(data_numbers[0], data_numbers[1], weather)
    garden.soil.nutrients = data_numbers[2]
    garden.soil.waterLevel = data_numbers[3]
    for i in range(garden.x):
        for j in range(garden.y):
            if data_number_list[i][j] is not None:
                if data_number_list[i][j] < 10:
                    garden.area[i][j] = garden.seedConstructorAccess(data_line_list[i][j])
                    garden.grow[i][j] = data_number_list[i][j]
                else:
                    garden.area[i][j] = garden.plantConstructorAccess(data_line_list[i][j])
                    garden.grow[i][j] = data_number_list[i][j]
            else:
                garden.area[i][j] = None
                garden.grow[i][j] = None
    return garden
                