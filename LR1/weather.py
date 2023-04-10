class Weather:
    def __init__(self, type, humidity, light):
        self.type = type
        self.humidity = humidity
        self.light = light
    
    
    def __str__(self):
        info = ''
        info += f'Weather : {self.type}\n'
        info += f'Humidity : {self.humidity}\n'
        info += f'Light level : {self.light}\n'
        return  info
        
        
class Sunny(Weather):
    def __init__(self):
        super().__init__('sunny', 50, 3)
    
    
class Overcast(Weather):
    def __init__(self):
        super().__init__('overcast', 70, 2)
        
        
class Rainy(Weather):
    def __init__(self):
        super().__init__('rainy', 90, 1)
        
        
class Drought(Weather):
    def __init__(self):
        super().__init__('drought', 20, 4)
        
        
def get_type_of_weather(data_line):
        match data_line:
            case "sunny":
                return Sunny()
            case "overcast":
                return Overcast()
            case "rainy":
                return Rainy()
            case "drought":
                return Drought()
            case _:
                return Sunny()