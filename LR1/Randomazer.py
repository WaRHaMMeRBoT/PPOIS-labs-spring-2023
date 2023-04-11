import random

import Station

class Randomazer:

    def generateRandomValue(self, min, max):
        num = random.randint(min, max)
        return num

    def generateRandomStation(self):
        stations = []

        for i in range(10):
            station = Station.Station(f"Station_{i + 1}", random.randint(1, 3), self.generateRandomValue(30, 100))
            stations.append(station)
        return stations
