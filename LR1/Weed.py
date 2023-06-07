from Plant import Plant

NAME_WEED = ["Cowweed", "Wheatgrass", "Bodyak", "Sow-thistle", "Dandelion"]

DAMAGE1 = 1
DAMAGE2 = 2
DAMAGE3 = 3
DAMAGE4 = 4
DAMAGE5 = 5

class Weed():
    def __init__(self, name, damage):
        self.__name = name
        self.__damage = damage
    @property
    def name(self):
        return self.__name
    @property
    def damage(self):
        return self.__damage
    @staticmethod
    def createName():
        counter = 0
        print("Valid plant names:")
        print(", ".join(NAME_WEED))
        print("Write the name of weed:")
        name = input()
        flag = False
        for i in NAME_WEED:
            if(name == NAME_WEED[counter]):
                flag = True
                break
            counter += 1
        if(flag == False):
            while(flag == False):
                counter = 0
                print("Choose from the list offered:")
                name = input()
                for i in NAME_WEED:
                    if(name == NAME_WEED[counter]):
                        flag = True
                        break
                    counter += 1
        return name
    @staticmethod
    def createDamage(name):
        if(name == "Cowweed"):
            return DAMAGE5
        if(name == "Wheatgrass"):
            return DAMAGE4
        if(name == "Bodyak"):
            return DAMAGE3
        if(name == "Sow-thistle"):
            return DAMAGE2
        if(name == "Dandelion"):
            return DAMAGE1