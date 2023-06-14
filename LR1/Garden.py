import json
from Patch import Patch
from Plant import Plant, NAME_PLANT
from Weed import Weed, NAME_WEED
from Pests import Pests, NAME_PESTS
from Timer import Timer

class Garden():
    def __init__(self):
        self.__patches = []
    def addPatch(self):
        self.__patches.append(Patch())
        print("Patch added successfully")
    @property
    def patches(self):
        return self.__patches
    def addPlantToGarden(self, number, name):
        if(number < len(self.__patches)):
            if not(name in NAME_PLANT):
                return print("Such a plant doesn't exist")
            plant = Plant(name, Plant.amountHP(name), 0, Plant.maximumAge(name))
            self.__patches[number].plants.append(plant)
            print("Plant successfully added to patch #" + str(number))
        else:
            print("There is no such garden. Available patch numbers:")
            counter = 1
            array = []
            if(len(self.__patches) != 0):
                for i in self.__patches:
                    array.append(counter)
                    counter += 1
                print(", ".join(map(str, array)))
            else:
                print("No patches created.")
    def addWeedToGarden(self, number, name):
        if(number < len(self.__patches)):
            weed = Weed(name, Weed.createDamage(name))
            self.__patches[number].weeds.append(weed)
            print("Weed successfully added to patch #" + str(number))
        else:
            print("There is no such garden. Available patch numbers:")
            counter = 1
            array = []
            if(len(self.__patches) != 0):
                for i in self.__patches:
                    array.append(counter)
                    counter += 1
                print(", ".join(map(str, array)))
            else:
                print("No patches created.")
    def addPestToGarden(self, number, name):
        if(number < len(self.__patches)):
            pest = Pests(name, Pests.createDamage(name))
            self.__patches[number].pests.append(pest)
            print("Pest successfully added to patch #" + str(number))
        else:
            print("There is no such garden. Available patch numbers:")
            counter = 1
            array = []
            if(len(self.__patches) != 0):
                for i in self.__patches:
                    array.append(counter)
                    counter += 1
                print(", ".join(map(str, array)))
            else:
                print("No patches created.")
    def makeWeedDamage(self):
        iter = 1
        for item in self.__patches:
            damage = 0
            for j in item.weeds:
                damage += j.damage
            counter = 0
            for j in item.plants:
                j.hp = -damage
                if(j.hp <= 0):
                    item.plants.pop(counter)
                    print("Plant " + "\"" + j.name + "\" has been removed from the patch #"+str(iter))
                counter += 1
            iter += 1
    def makePestDamage(self):
        iter = 1
        for item in self.__patches:
            damage = 0
            for j in item.pests:
                damage += j.damage
            counter = 0
            for j in item.plants:
                j.hp = -damage
                if(j.hp <= 0):
                    item.plants.pop(counter)
                    print("Plant " + "\"" + j.name + "\" has been removed from the patch #"+str(iter))
                counter += 1
            iter += 1
    def weatherImpact(self, weather):
        iter = 1
        for item in self.__patches:
            damage = 0
            if(weather.state == "Drizzling rain"):
                damage = -5
            if(weather.state == "Heat"):
                damage = 5
            if(weather.state == "Heavy rain"):
                damage = 2
            counter = 0
            for j in item.plants:
                j.hp = -damage
                if(j.hp <= 0):
                    item.plants.pop(counter)
                    print("Plant " + "\"" + j.name + "\" has been removed from the patch #"+str(iter))
                counter += 1
            iter += 1
    def showPatches(self):
        counter = 1
        if(len(self.__patches) == 0):
            return print("Garden is empty")
        for item in self.__patches:
            print("Patch number #" + str(counter) + ":")
            for j in item.plants:
                print("plant name: " + str(j.name) + "\t plant age: " + str(j.age) + "\tplant hp: " + str(j.hp) + "\tmaximum plant age: " + str(j.maxAge))
            for j in item.weeds:
                print("weed name: " + str(j.name) + "\t weed damage: " + str(j.damage))
            for j in item.pests:
                print("pest name: " + str(j.name) + "\t pest damage: " + str(j.damage))
            counter += 1

    def save(self, date):
        data = {
            'patches': [],
            'date': ''
        }
        for patch in self.__patches:
            plants = []
            weeds = []
            pests = []
            for plant in patch.plants:
                plants.append({
                    'name': plant.name,
                    'hp': plant.hp,
                    'age': plant.age,
                    'maxAge': plant.maxAge
                })
            for weed in patch.weeds:
                weeds.append({
                    'name': weed.name,
                    'damage': weed.damage
                })
            for pest in patch.pests:
                pests.append({
                    'name': pest.name,
                    'damage': pest.damage
                })
            data["patches"].append({
                'plants': plants,
                'weeds': weeds,
                'pests': pests
            })
        data["date"] = {'day': date.day, 'month': date.month, 'year': date.year}
        with open('data.json', 'w') as file:
            json.dump(data, file)

    def open(self, date):
        try:
            with open('data.json', 'r') as file:
                data = json.load(file)
        except:
            self.clear(Timer())
            with open('data.json', 'r') as file:
                data = json.load(file)
        self.__patches = []
        for patch in data['patches']:
            self.__patches.append(Patch())
            for plant in patch['plants']:
                self.__patches[-1].plants.append(Plant(plant['name'], plant['hp'], plant['age'], plant['maxAge']))
            for weed in patch['weeds']:
                self.__patches[-1].weeds.append(Weed(weed['name'], weed['damage']))
            for pest in patch['pests']:
                self.__patches[-1].pests.append(Pests(pest['name'], pest['damage']))
        return Timer(data['date']['day'], data['date']['month'], data['date']['year'])
        

    def clear(self, date):
        self.__patches = []
        self.save(date)

