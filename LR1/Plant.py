NAME_PLANT = ["Rose", "Tulip", "Orchid", "Chrysanthemum", "Cornflower", "Lily of the Valley", "Chamomile", "Peonies", "Narcissus", "Buttercup",
              "Peach", "Pineapple", "Nectarine", "Banana", "Mango", "Orange", "Apple", "Pear", "Plums", "Apricot",
              "Cucumber", "Cabbage", "Dill", "Carrot", "Beetroot", "Onion", "Potato", "Garlic", "Yam", "Broccoli",
              "Birch", "Oak", "Maple", "Poplar", "Willow", "Linden", "Ale", "Pine", "Palm", "Baobab"]

class Plant:
    def __init__(self, name, hp, age, maxAge):
        self.__age = age
        self.__name = name
        self.__hp = hp
        self.__maxAge = maxAge
    @property
    def age(self):
        return self.__age
    @property
    def name(self):
        return self.__name
    @property
    def hp(self):
        return self.__hp
    @property
    def maxAge(self):
        return self.__maxAge
    @property
    def timeLife(self):
        return self.__timeLife
    @age.setter
    def age(self, x):
        self.__age += x
    @hp.setter
    def hp(self, x):
        self.__hp += x
    @staticmethod
    def createName():
        counter = 0
        print("Valid plant names:")
        print(", ".join(NAME_PLANT))
        print("Write the name of plant:")
        name = input()
        flag = False
        for i in NAME_PLANT:
            if(name == NAME_PLANT[counter]):
                flag = True
                break
            counter += 1
        if(flag == False):
            while(flag == False):
                counter = 0
                print("Choose from the list offered:")
                name = input()
                for i in NAME_PLANT:
                    if(name == NAME_PLANT[counter]):
                        flag = True
                        break
                    counter += 1
        return name
    @staticmethod
    def amountHP(name):
        counter = 0
        for i in NAME_PLANT:
            if(name == NAME_PLANT[counter]):
                if(counter < 10):
                    hp = 50
                elif(counter > 9 and counter < 20):
                    hp = 60
                elif(counter > 19 and counter < 30):
                    hp = 60
                else:
                    hp = 150
                break
            counter += 1
        return hp
    @staticmethod
    def maximumAge(name):
        counter = 0
        for i in NAME_PLANT:
            if(name == NAME_PLANT[counter]):
                if(counter < 10):
                    maxAge = 100
                elif(counter > 9 and counter < 20):
                    maxAge = 90
                elif(counter > 19 and counter < 30):
                    maxAge = 90
                else:
                    maxAge = 200
                break
            counter += 1
        return maxAge