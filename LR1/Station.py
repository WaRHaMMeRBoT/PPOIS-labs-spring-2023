import enum
from enum import Enum

class StationType(enum.IntEnum):
    PASS_FREIGHT_STATION = 1
    PASS_STATION = 2
    FREIGHT_STATION = 3


class Station:
    def __init__(self, stationName, stationType, distanceToNextStation):
        self.stationName = stationName
        self.stationType = stationType
        self.distanceToNextStation = distanceToNextStation

    def setDistanceToNextStation(self, distanceToNextStation):
        self.distanceToNextStation = distanceToNextStation

    def getStationType(self):
        return self.stationType

    def getStationName(self):
        return self.stationName

    def getDistanceToNextStation(self):
        return self.distanceToNextStation

