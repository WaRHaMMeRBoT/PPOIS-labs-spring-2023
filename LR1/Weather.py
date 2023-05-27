import random
NAME_STATE = ["Clear", "Drizzling rain", "Heat", "Heavy rain"]

class Weather:
    def __init__(self):
        self.__state = ""
        self.__impact = 0
    def changeState(self):
        number = random.randint(0, 3)
        self.__state = NAME_STATE[number]
        print("Weather now: "+self.__state)
    @property
    def state(self):
        return self.__state
    @property
    def impact(self):
        return self.__impact
    @state.setter
    def state(self, x):
        self.__state = x