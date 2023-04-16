class Seed:
    def __init__(self, name, health, basicGrowingSpeed, minNutrientNeed, maxNutrientNeed, minWaterNeed, maxWaterNeed):
        self.name = name
        self.health = health
        self.basicGrowingSpeed = basicGrowingSpeed
        self.minWaterNeed = minWaterNeed
        self.maxWaterNeed = maxWaterNeed
        self.maxNutrientNeed = maxNutrientNeed
        self.minNutrientNeed = minNutrientNeed
        self.icon = "🌱"
        self.type = 0
    
    
class Plant(Seed):
    def __init__(self, name, health, basicGrowingSpeed, minNutrientNeed, maxNutrientNeed, minWaterNeed, maxWaterNeed, minLightNeed, maxLightNeed):
        super().__init__(name, health, basicGrowingSpeed, minNutrientNeed, maxNutrientNeed, minWaterNeed, maxWaterNeed)
        self.type = 1
        self.minLightNeed = minLightNeed    
        self.maxLightNeed = maxLightNeed  
        
    
    def showNeed(self):
        info = ''
        info += f'Nutrient need : {self.minNutrientNeed} - {self.maxNutrientNeed} \n'
        info += f'Water need : {self.minWaterNeed} - {self.maxWaterNeed}\n'
        info += f'Light need : {self.minLightNeed} - {self.maxLightNeed}\n'
        print(info)
        
        
class Corn(Plant):
    def __init__(self):
        super().__init__("corn", 100, 2, 30, 80, 30, 80, 3, 4) 
        self.icon = "🌽"
        
        
class Garlic(Plant):
    def __init__(self):
        super().__init__("garlic", 100, 5, 50, 80, 50, 90, 2, 4)
        self.icon = "🧄"
        
        
class Onion(Plant):
    def __init__(self):
        super().__init__("onion", 100, 7, 40, 80, 50, 100, 2, 3)
        self.icon = "🧅"  


class Melon(Plant):
    def __init__(self):
        super().__init__("melon", 100, 4, 50, 80, 50, 60, 3, 4) 
        self.icon = "🍈" 


class Spinach(Plant):
    def __init__(self):
        super().__init__("spinach", 100, 4, 30, 80, 60, 80, 1, 2)
        self.icon = "🥬"
        
        
class Rice(Plant):
    def __init__(self):
        super().__init__("rice", 100, 2, 30, 80, 70, 100, 2, 4)
        self.icon = "🌾"
        
        
class Сucumber(Plant):
    def __init__(self):
        super().__init__("cucumber", 100, 4, 50, 80, 60, 80, 2, 4)
        self.icon = "🥒"
        
        
class Broccoli(Plant):
    def __init__(self):
        super().__init__("broccoli", 100, 4, 40, 70, 40, 80, 1, 4)  
        self.icon = "🥦"
        
        
class Weed(Plant):
    def __init__(self):
        super().__init__("weed", 100, 10, 20, 90, 20, 80, 1, 4)  
        self.icon = "🌿" 
        

class CornSeed(Seed):
    def __init__(self):
        super().__init__("corn", 100, 4, 20, 90, 20, 90)
        
        
class GarlicSeed(Seed):
    def __init__(self):
        super().__init__("garlic", 100, 4, 20, 90, 20, 90)
        
        
class OnionSeed(Seed):
    def __init__(self):
        super().__init__("onion", 100, 4, 20, 90, 20, 90)


class MelonSeed(Seed):
    def __init__(self):
        super().__init__("melon", 100, 4, 20, 90, 20, 90)


class SpinachSeed(Seed):
    def __init__(self):
        super().__init__("spinach", 100, 4, 20, 90, 20, 90)
        
        
class RiceSeed(Seed):
    def __init__(self):
        super().__init__("rice", 100, 4, 20, 90, 20, 90)
        
        
class СucumberSeed(Seed):
    def __init__(self):
        super().__init__("cucumber", 100, 4, 20, 90, 20, 90)
        
        
class BroccoliSeed(Seed):
    def __init__(self):
        super().__init__("broccoli", 100, 4, 20, 90, 20, 90)
    
    

    
    
    