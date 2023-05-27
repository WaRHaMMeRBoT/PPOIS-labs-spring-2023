from Plant import Plant

COMPOST_IMPACT = 20
WATERING_IMPACT = 15
ILLNESS_IMPACT = -20

class Patch():
    def __init__(self):
         self.__plants = []
         self.__weeds = []
         self.__pests = []
    @property
    def plants(self):
        return self.__plants
    @property
    def weeds(self):
        return self.__weeds
    @property
    def pests(self):
        return self.__pests
    def weeding(self):
        self.__weeds = []
        print("All weeds have been removed from the patch #", end = "")
    def killPests(self):
        self.__pests.clear()
        print("All pests have been removed from the patch #", end = "")
    def compost(self):
        for i in self.__plants:
            i.hp = COMPOST_IMPACT
    def watering(self):
        for i in self.__plants:
            i.hp = WATERING_IMPACT
    def illness(self):
        for i in self.plants:
            i.hp = ILLNESS_IMPACT