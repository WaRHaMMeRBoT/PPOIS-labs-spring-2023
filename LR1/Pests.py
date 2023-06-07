NAME_PESTS = ["Aphid", "Ant", "Slug", "Whitefly", "Nematode", "Leaf beetle", "Moth", "Mouse", "Rat", "Mole"]

DAMAGE_PEST5 = 5
DAMAGE_PEST6 = 6
DAMAGE_PEST10 = 10

class Pests:
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
        print("Valid pests names:")
        print(", ".join(NAME_PESTS))
        print("Write the name of pest:")
        name = input()
        flag = False
        for i in NAME_PESTS:
            if(name == NAME_PESTS[counter]):
                flag = True
                break
            counter += 1
        if(flag == False):
            while(flag == False):
                counter = 0
                print("Choose from the list offered:")
                name = input()
                for i in NAME_PESTS:
                    if(name == NAME_PESTS[counter]):
                        flag = True
                        break
                    counter += 1
        return name
    @staticmethod
    def createDamage(name):
        counter = 0
        for i in NAME_PESTS:
            if(name == NAME_PESTS[counter]):
                if(counter < 3):
                    return DAMAGE_PEST5
                elif(counter > 2 and counter < 8):
                    return DAMAGE_PEST6
                else:
                    return DAMAGE_PEST10
                break
            counter += 1