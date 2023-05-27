from Weed import Weed, NAME_WEED
from Pests import Pests, NAME_PESTS
import random

SIZE = 5
DAYS31 = 31
DAYS30 = 30
DAYS28 = 28
MONTH1 = 1
MONTH2 = 2
MONTH3 = 3
MONTH4 = 4
MONTH5 = 5
MONTH6 = 6
MONTH7 = 7
MONTH8 = 8
MONTH9 = 9
MONTH10 = 10
MONTH11 = 11
MONTH12 = 12


class Timer():
    def __init__ (self, day=1, month=1, year=2023):
        self.__day = day
        self.__month = month
        self.__year = year
    @property
    def day(self):
        return self.__day
    @property
    def month(self):
        return self.__month
    @property
    def year(self):
        return self.__year
    def nextDay(self, garden):
        if(self.__day % 10 == 0):
            if(len(garden.patches) > 0):
                number = random.randrange(len(garden.patches))
                numberName = random.randint(0, 4)
                garden.addWeedToGarden(number, NAME_WEED[numberName])
                print("A new weed has grown in the patch #" + str(number))
        if(self.__day % 15 == 0):
            if(len(garden.patches) > 0):
                number = random.randrange(len(garden.patches))
                numberName = random.randint(0, 9)
                garden.addPestToGarden(number, NAME_PESTS[numberName])
                print("A new pest has grown in the patch #" + str(number))
        self.__day += 1
        if((self.__day > DAYS31) and ((self.__month == MONTH1) or (self.__month == MONTH3) or (self.__month == MONTH5) or (self.__month == MONTH7) or (self.__month == MONTH8) or (self.__month == MONTH10) or (self.__month == MONTH12))):
            self.__day = 1;
            self.__month += 1
        elif((self.__day > DAYS30) and ((self.__month == MONTH4) or (self.__month == MONTH6) or (self.__month == MONTH9) or (self.__month == MONTH11))):
            self.__day = 1
            self.__month += 1
        elif((self.__day > DAYS28) and (self.__month == MONTH2)):
            self.__day = 1
            self.__month += 1
        if(self.__month > 12):
            self.__month = 1
            self.__year += 1
        for item in garden.patches:
            counter = 0
            for j in item.plants:
                x = 1
                j.age = x
                if(j.age > (j.maxAge / 2)):
                    y = -1
                    j.hp = y
                if(j.age > j.maxAge):
                    item.plants.pop(counter)
                    print("Plant " + "\"" + j.name + "\" has been removed from the patch #"+str(counter))
                counter += 1
    def showData(self):
        dayZero = "0"
        monthZero = "0"
        if(self.__day > 9):
            dayZero = ""
        if(self.__month > 9):
            dayMonth = ""
        print(f'{dayZero}%s.{monthZero}%s.%s'%(self.__day, self.__month, self.__year))