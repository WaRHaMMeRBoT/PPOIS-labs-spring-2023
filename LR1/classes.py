import random, json
from abc import ABC, abstractmethod

COMPOST_IMPACT = 15
DISEASE_MAX_DAMAGE = 10
PESTS_MAX_DAMAGE = 15
WEATHER_IMPACT = 10
WEATHER_MAX_DURATION = 3
PATCH_SIZE = 20
PLANT_MAX_HP = 100
WEED_MAX_HP = 150


class Garden:
    def __init__(self):
        self.__patches = []
        self.__weather = Weather()

    def update(self):
        self.__weather.update()
        self.__weather.affect_plants(self.__patches)
        for patch in self.__patches:
            patch.update()

    def add_patch(self):
        self.__patches.append(Patch())

    def remove_patch(self, index):
        try: self.__patches.pop(index)
        except IndexError: raise ExceptionNonExistentPatch

    @property
    def patches(self):
        return self.__patches

    def info(self):
        print("Patches:")
        for (i, patch) in enumerate(self.__patches):
            print(f"patch_{i}(pests: {patch.pests}, disease: {patch.disease})")
            for plant in patch.plants:
                print(plant.name + "(" + "hp: " + str(plant.hp) + ")")
        print("Weather: " + self.__weather.state)
    
    def save(self):
        data = {
            'patches': [],
            'weather': {
                'state': self.__weather.state,
                'impact': self.__weather.impact,
                'duration': self.__weather.duration,
                'current-duration': self.__weather.current_duration
            }
        }
        for patch in self.__patches:
            plants = []
            for plant in patch.plants:
                plants.append({
                    'name': plant.name,
                    'hp': plant.hp
                })
            data['patches'].append({
                'plants': plants,
                'weeds': patch.weeds,
                'pests': patch.pests,
                'disease': patch.disease
            })
        with open('data.json', 'w') as file:
            json.dump(data, file)
    
    def open(self):
        try:
            with open('data.json', 'r') as file:
                data = json.load(file)
        except: 
            self.clear()
            with open('data.json', 'r') as file:
                data = json.load(file)

        self.__weather.state = data['weather']['state']
        self.__weather.impact = data['weather']['impact']
        self.__weather.duration = data['weather']['duration']
        self.__weather.current_duration = data['weather']['current-duration']
        self.__patches = []
        for patch in data['patches']:
            self.__patches.append(Patch())
            self.__patches[-1].weeds = patch['weeds']
            self.__patches[-1].pests = patch['pests']
            self.__patches[-1].disease = patch['disease']
            for plant in patch['plants']:
                self.__patches[-1].plants = Plant(plant['name'], plant['hp'])
        
    def clear(self):       
        self.__patches = []
        self.save()
        

class Patch:
    def __init__(self):
        self.__plants = []
        self.__weeds = 0
        self.__pests = False
        self.__disease = False

    def update(self):
        self.__weeds *= 2
        for i in range(self.__weeds):
            if self.__plants == PATCH_SIZE:
                break
            self.__plants.append(Weed())
        try: self.__pests.destroy_plants(self.__plants)
        except: pass
        for plant in self.__plants:
            plant.hp = -5
            if plant.hp <= 0:
                self.__plants.remove(plant)

    def add_plant(self, name):
        if len(self.__plants) < PATCH_SIZE:
            plant = Plant(name, None)
            self.__plants.append(plant)
        else: raise ExceptionPatchOverflow

    def remove_plant(self, plant_name):
        for plant in self.__plants:
            if plant.name == plant_name:
                self.__plants.remove(plant)
                return
        raise ExceptionNonExistentPlant(self.__plants)

    def add_pests(self):
        self.__pests = Pests()

    def add_disease(self):
        self.__disease = Disease()

    def add_weed(self):
        self.__weeds = random.randint(0, 3)

    def remove_weed(self):
        self.__weeds = 0
        for plant in self.__plants:
            if plant.name == 'weed':
                self.__plants.remove(plant)

    def compost(self):
        self.__pests = None
        self.__disease = None
        for plant in self.__plants:
            plant.hp += COMPOST_IMPACT
    
    @property
    def plants(self):
        return self.__plants
    @plants.setter
    def plants(self, plant):
        self.__plants.append(plant)

    @property
    def weeds(self):
        return self.__weeds
    @weeds.setter
    def weeds(self, weeds):
        self.__weeds = weeds

    @property
    def pests(self):
        if self.__pests != False:
            return True
        return False
    @pests.setter
    def pests(self, pests):
        self.__pests = pests

    @property
    def disease(self):
        if self.__disease != False:
            return True
        return False
    @disease.setter
    def disease(self, disease):
        self.__disease = disease



class Plant:
    def __init__(self, name, hp):
        self.__name = name
        if hp == None:
            self.__hp = random.randrange(50, PLANT_MAX_HP, 5)
        else:
            self.__hp = hp
    @property
    def name(self):
        return self.__name
    @property
    def hp(self):
        return self.__hp
    @hp.setter
    def hp(self, impact):
        self.__hp += impact



class Weather:
    def __init__(self):
        self.impact = 0
        self.__change()

    __states = ['dry', 'rain']

    def update(self):
        if self.current_duration < self.duration:
            self.current_duration += 1
        else: self.__change()
    
    def __change(self):
        self.current_duration = 0
        self.duration = random.randint(1, WEATHER_MAX_DURATION)
        self.state = self.__states[random.randint(0, len(self.__states)-1)]
        self.impact = self.__init_impact()

    def __init_impact(self):
        if self.state == 'dry': return -WEATHER_IMPACT
        elif self.state == 'rain': return WEATHER_IMPACT

    def affect_plants(self, patches):
        for patch in patches:
            for plant in patch.plants:
                plant.hp = self.impact


class Threat(ABC):
    @abstractmethod
    def __init__(self, max_damage):
        self.damage = random.randint(3, max_damage)
    def destroy_plants(self, plants):
        for plant in plants:
            plant.hp -= self.damage

class Disease(Threat):
    def __init__(self):
        super().__init__(DISEASE_MAX_DAMAGE)

class Pests(Threat):
    def __init__(self):
        super().__init__(PESTS_MAX_DAMAGE)
    

class Weed(Plant):
    def __init__(self):
        self.name = 'weed'
        self.hp = random.randrange(50, WEED_MAX_HP, 5)


class ExceptionGarden(Exception):
    @staticmethod
    def print_error(str):
        print("\n","\033[0m\033[31m{}\033[0m".format(str))
        
class ExceptionNonExistentPatch(ExceptionGarden):
    @staticmethod
    def message(patches):
        ExceptionGarden.print_error("Non-existent patch.")
        print("Available patches:")
        for (i, patch) in enumerate(patches):
            print(f"patch_{i}(pests: {patch.pests}, disease: {patch.disease}:")
        print("\n")

class ExceptionNonExistentPlant(ExceptionGarden):
    @staticmethod
    def message(plants):
        ExceptionGarden.print_error("Non-existent plant.")
        print("Available plants in this patch:")
        for plant in plants:
            print(plant.name + "(" + "hp: " + str(plant.hp) + ")")
        print("\n")

class ExceptionPatchOverflow(ExceptionGarden):
    @staticmethod
    def message():
        ExceptionGarden.print_error("Patch overflow.")
        print("\n")

class ExceptionUnknownCommand(ExceptionGarden):
    @staticmethod
    def message():
        ExceptionGarden.print_error("Unknown command.")
        print("Enter \"help\" to show list of available commands.")
        print("\n")
    
    
class Commander:
    def __init__(self, garden):
        self.__garden = garden
    __commands = [
        "help",
        "add-patch",
        "remove-patch",
        "add-plant",
        "remove-plant",
        "compost-patch",
        "add-pests",
        "add-disease",
        "add-weed",
        "remove-weed",
        "show-garden",
        "next",
        "clear-garden"
    ]
    def start(self, args):
        self.__garden.open()
        self.define_command(args[0], args[1:])
        self.__garden.save()

    def define_command(self, command, args):
        try:
            if command == 'help':
                for command in self.__commands:
                    print(command)
                print("")
                return
            if command == 'add-patch':
                self.__garden.add_patch()
                return
            if command == 'remove-patch':
                try: self.__garden.remove_patch(int(args[0]))
                except ExceptionNonExistentPatch: ExceptionNonExistentPatch.message(self.__garden.patches)
                return
            if command == 'add-plant':
                try: self.__garden.patches[int(args[1])].add_plant(args[0])
                except ExceptionPatchOverflow: pass
                return
            if command == 'remove-plant':
                try: self.__garden.patches[int(args[1])].remove_plant(args[0])
                except ExceptionNonExistentPlant: pass
                return
            if command == 'compost-patch':
                self.__garden.patches[int(args[0])].compost()
                return
            if command == 'add-pests':
                self.__garden.patches[int(args[0])].add_pests()
                return
            if command == 'add-disease':
                self.__garden.patches[int(args[0])].add_disease()
                return
            if command == 'add-weed':
                self.__garden.patches[int(args[0])].add_weed()
                return
            if command == 'remove-weed':
                self.__garden.patches[int(args[0])].remove_weed()
                return
            if command == 'show-garden':
                self.__garden.info()
                return
            if command == 'next':
                if not args[0]:
                    args[0] = 1
                for i in range(int(args[0])):
                    self.__garden.update()
                return
            if command == 'clear-garden':
                self.__garden.clear()
                return
            ExceptionUnknownCommand.message()
        except IndexError: ExceptionGarden.print_error("Args error.")
    



