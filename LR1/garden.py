import random
from plants.fruit_trees import Orange_tree
from plants.fruit_trees import Pear_tree
from plants.fruit_trees import Plum_tree
from plants.vegetables import Tomato
from plants.seeds import Seeds
from plants.weeds import Weed
from plants.weeds import Bugs
from plants.vegetables import Carrot
from plants.vegetables import Cucumber

class Weather:
    def __init__(self):
        self._today = 'sun'

    @property
    def today(self):
        return self._today

    @today.setter
    def today(self, value):
        self._today = value

    def update(self, garden):
        weath = ['sun', 'rain'] 
        self._today = random.choice(weath)
        days = len(garden._last_two_days)
        if days == 0:
            garden._last_two_days.append(self.today)
            return self.today
        if days == 1:
            garden._last_two_days.append(self.today)
        if days == 2:
            garden._last_two_days.pop(0)
        garden._last_two_days.append(self.today)
        if garden._last_two_days[0] == garden._last_two_days[1] and garden._last_two_days[0] == 'sun':
            return 'drought'
        return self.today

class Garden_bed:
    def __init__(self, _length):
        self._length = _length
        self._bed = []
        for i in range(0, self._length, 1):
            self._bed.append([])

class Garden:
    def __init__(self, _length):
        self._length = _length
        self._number_of_beds = 1
        self._garden_beds = [Garden_bed(_length)]
        self._last_two_days = []
        self._weather = Weather()
        self._veg_identifier = 1
        self._tree_identifier = 1
        self._seeds_identifier = 1
        self._pests_identifier = 1
        self._trees = []
        self._vegetables = []
        self._seeds = []
        self._pests = []
        
    @property
    def number_of_beds(self):
        return self._number_of_beds
    
    @property
    def length(self):
        return self._length
    
    @property
    def veg_identifier(self):
        return self._veg_identifier
    
    @property
    def tree_identifier(self):
        return self._tree_identifier
    
    @property
    def seeds_identifier(self):
        return self._seeds_identifier
    
    @property
    def weeds_identifier(self):
        return self._weeds_identifier

    def watering(self, obj, weather):
        if weather == 'drought':
            obj._water+=20
        if weather == 'sun':
            obj._water+=5
        if weather == 'rain':
            obj._water+=10

    def Next_move(self):
        weath = self._weather.update(self)
        for tree in self._trees:
            tree.next_move()
            self.watering(tree, weath)
            if not tree._alive: 
                x = tree._location[0]
                y = tree._location[1]
                self._garden_beds[x]._bed[y].pop(0)
                self._trees.remove(tree)
        
        for seed in self._seeds:
            seed.next_move(self)
            
        for veg in self._vegetables:
            tree.next_move()
            self.watering(veg, weath)
            if not veg._alive: 
                x = veg._location[0]
                y = veg._location[1]
                self._garden_beds[x]._bed[y].pop(0)
                self._vegetables.remove(veg)
    

        for pest in self._pests:
            pest.next_move()
            if not pest._alive: 
                x = pest._location[0]
                y = pest._location[1]
                self._garden_beds[x]._bed[y].pop(0)
                self._pests.remove(pest)

            
    def fertilizing(self):
        for i in range(0, len(self._trees), 1):
            self._trees[i].damage(0.75)

        for i in range(0, len(self._vegetables), 1):
            self._trees[i].damage(0.75)

    def grown_seed(self, seed):
        for i in range (0, len(self._seeds), 1):
            if seed._identifier == self._seeds[i]._identifier:
                x = self._seeds[i]._location[0]
                y = self._seeds[i]._location[1]
                new_plant = 0
                if seed._name == 'O ' : 
                    new_plant = Orange_tree(self._tree_identifier)
                    self._tree_identifier +=1
                    self._trees.append(new_plant)
                if seed._name == 'P ' : 
                    new_plant = Pear_tree(self._tree_identifier)
                    self._tree_identifier +=1
                    self._trees.append(new_plant)
                if seed._name == 'Pl' : 
                    new_plant = Plum_tree(self._tree_identifier)
                    self._tree_identifier +=1
                    self._trees.append(new_plant)
                if seed._name == 'T ':
                    new_plant = Tomato(self._veg_identifier)
                    self._veg_identifier +=1
                    self._vegetables.append(new_plant)
                if seed._name == 'Ca':
                    new_plant = Carrot(self._veg_identifier)
                    self._veg_identifier +=1
                    self._vegetables.append(new_plant)
                if seed._name == 'Cu':
                    new_plant = Cucumber(self._veg_identifier)
                    self._veg_identifier +=1
                    self._vegetables.append(new_plant)
                if y != 0:
                    if len(self._garden_beds[x]._bed[y-1])!=0:
                        if self._garden_beds[x]._bed[y-1][0]._name == 'bug' or self._garden_beds[x]._bed[y-1][0]._name == 'weed':
                            new_plant._damage *=self._garden_beds[x]._bed[y-1][0]._damage_power
                if y != self._length - 1:
                    if len(self._garden_beds[x]._bed[y+1])!=0:
                        if self._garden_beds[x]._bed[y+1][0]._name == 'bug' or self._garden_beds[x]._bed[y+1][0]._name == 'weed':
                            new_plant._damage*=self._garden_beds[x]._bed[y+1][0]._damage_power
                self._garden_beds[x]._bed[y][0] = new_plant
                self._seeds.pop(i)           
                break
    
    def find_empty_place(self, obj):
        while True:
            i = random.randrange(0, self._number_of_beds, 1)
            j = random.randrange(0, self._length, 1)
            if len(self._garden_beds[i]._bed[j]) == 0:
                self._garden_beds[i]._bed[j].append(obj)
                return [i, j]

    def add(self, who):
        if len(self._pests) + len(self._vegetables)+len(self._trees)+len(self._seeds) == self.number_of_beds * self.length:
            print('Мест нет')
        if who == 'T':
            seed_name = random.choice(['O ', 'P ', 'Pl'])
            seed_obj = Seeds(self._seeds_identifier, seed_name)
            self._seeds_identifier +=1
            seed_obj.location = self.find_empty_place(seed_obj)
            self._seeds.append(seed_obj)
        if who == 'V':
            seed_name = random.choice(['T ', 'Cu', 'Ca'])
            seed_obj = Seeds(self._seeds_identifier, seed_name)
            self._seeds_identifier +=1
            seed_obj.location = self.find_empty_place(seed_obj)
            self._seeds.append(seed_obj)
        if who == 'W':
            pests_obj = Weed(self._pests_identifier)
            self._pests_identifier += 1
            pests_obj.location = self.find_empty_place(pests_obj)
            self._pests.append(pests_obj)
            x = pests_obj._location[0]
            y = pests_obj._location[1]
            if y != 0:
                if len(self._garden_beds[x]._bed[y-1])!=0:
                    plant = self._garden_beds[x]._bed[y-1][0]._name
                    if plant == 'Orange' or plant == 'Pear  ' or plant == 'Plum  ' or plant == 'Tomato' or plant == 'Cucumber' or plant == 'Carrot':
                        self._garden_beds[x]._bed[y-1][0].damage*=self._garden_beds[x]._bed[y][0]._damage_power
            if y != self._length:
                if len(self._garden_beds[x]._bed[y+1])!=0:
                    plant = self._garden_beds[x]._bed[y+1][0]._name
                    if plant == 'Orange' or plant == 'Pear  ' or plant == 'Plum  ' or plant == 'Tomato' or plant == 'Cucumber' or plant == 'Carrot':
                        self._garden_beds[x]._bed[y+1][0].damage*=self._garden_beds[x]._bed[y][0]._damage_power
        if who == 'B':
            pests_obj = Bugs(self._pests_identifier)
            self._pests_identifier += 1
            pests_obj.location = self.find_empty_place(pests_obj)
            self._pests.append(pests_obj)
    
    def add_bed(self, new_bed):
        self._garden_beds.append(new_bed)
        self._number_of_beds +=1

    def del_veg(self):
        index = len(self._vegetables) - 1
        if index == -1: 
            print('Овощей нет')
            return
        self._vegetables[index]._alive = False

    def del_tree(self):
        index = len(self._trees) - 1
        if index == -1: 
            print('Деревьев нет')
            return
        self._trees[index]._alive = False

    def Show_field(self):
        for i in range(0, self._number_of_beds, 1):
            print('---------------------------------------------------------------------------------------------------')
            s = ''
            for j in range(0, self._length, 1):
                if len(self._garden_beds[i]._bed[j]) != 0:
                    s += f'{self._garden_beds[i]._bed[j][0]._name}{self._garden_beds[i]._bed[j][0]._identifier}  | '
                else: s+= '          | '
            print(s)
        for seed in self._seeds: seed.display_info()
        for veg in self._vegetables: veg.display_info()
        for tree in self._trees: tree.display_info()
        for pest in self._pests: pest.display_info()

class Actions:
    def actions(self, garden, action):
        if action == '-fertilize':
            garden.fertilizing()
        if action == '-add T':
            garden.add('T')
        if action == '-add V':
            garden.add('V')
        if action == '-add W':
            garden.add('W')
        if action == '-add B':
            garden.add('B')
        if action == '-add bed':
            garden.add_bed(Garden_bed(garden._length))
