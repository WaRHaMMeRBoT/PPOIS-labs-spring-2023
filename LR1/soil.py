class Soil:
    def __init__(self):
        self.waterLevel = 50
        self.nutrients = 50
        
    
    def __str__(self):
        info = ''
        info += f'Water level : {self.waterLevel}\n'
        info += f'Nutrients : {self.nutrients}\n'
        return  info
    
    
    def fertilizing(self, quantity):
        self.nutrients += quantity
        
        
    def watering(self, quantity):
        self.waterLevel += quantity