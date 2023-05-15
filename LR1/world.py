from random import randint

class world:
    def __init__(self, file):
        f = open(file)
        size = f.readline().split()
        self.n = int(size[0])
        self.m = int(size[1])
        self.field = [[cell() for j in range(self.m)] for i in range(self.n)]
        self.everyone = []
        
        while True:
            inf = f.readline().split()
            if inf[0] == '.':
                break
            self.field[int(inf[1])][int(inf[2])].livings.append(eval(inf[0])(self, *inf))
            self.everyone.append(self.field[int(inf[1])][int(inf[2])].livings[-1])
        f.close()

    def add(self, kind, x=-1, y=-1, l='', sd='0', s=''):
        if l == '':
            l = eval(kind).max_lives
        elif int(l) > int(eval(kind).max_lives):
            raise Exception(kind + ' cannot have more then ' + str(eval(kind).max_lives) + ' lives') 
        if x == -1:
            x = randint(0, self.n-1)
        elif x > self.n:
            raise Exception('nonexistant coordinate x, this world is not so big')
        if y == -1:
            y = randint(0, self.m-1)
        elif y > self.m:
            raise Exception('nonexistant coordinate y, this world is not so big')
        inf = [kind, str(x), str(y), l]
        if kind != 'plant':
            if s == '':
                if randint(0,2) == 0:
                    s = 'm'
                else:
                    s = 'f'
            inf = inf + [sd, s]
        self.field[x][y].livings.append(eval(inf[0])(self, *inf))
        self.everyone.append(self.field[x][y].livings[-1])
        with open('info.txt', 'r+') as f:
            lines = f.readlines()
            f.seek(0)
            f.truncate()
            f.writelines(lines[:-1])
            f.write(self.field[x][y].livings[-1].id() + '.')

    def find(self, x, y, kind, s = ''):
        for i in range(len(self.field[x][y].livings)):
            if self.field[x][y].livings[i].who() == kind:
                if s == '':
                    return self.field[x][y].livings[i]
                else:
                    if self.field[x][y].livings[i].sex == s:
                        return self.field[x][y].livings[i]
                    
    
    def decay(self):
        i = 0
        while i < len(self.everyone):
            if self.everyone[i].who() == 'corpse':
                self.everyone.pop(i)
            else:
                i+=1

    def next(self):
        self.decay()
        for i in range (len(self.everyone)):
            if self.everyone[i].who() != 'corpse':
                self.everyone[i].next()
        i = 0
        self.decay()
        for i in range (len(self.everyone)):
            if self.everyone[i].who() != 'plant':
                    self.everyone[i].move()
        

    def show_info(self):
        print("\nSize of the world: " + str(self.n) +'*'+ str(self.m))
        print("\nanimal\tx\ty\tlives\tstarve days\tsex")
        for i in range (len(self.everyone)):
            if self.everyone[i].who() != 'plant':
                print(self.everyone[i].who()+'\t'+str(self.everyone[i].x)+'\t'+str(self.everyone[i].y)+'\t'
                      +str(self.everyone[i].lives)+'  \t'+str(self.everyone[i].starve_days)+'\t\t'+self.everyone[i].sex)
        print("\nplants:\n")
        for i in range (len(self.everyone)):
            if self.everyone[i].who() == 'plant':
                print(self.everyone[i].who()+'\t'+str(self.everyone[i].x)+'\t'+str(self.everyone[i].y)+'\t'
                      +str(self.everyone[i].lives))

class cell:
    def __init__(self):
        self.livings = list()

class living:
    def __init__(self, world, *inf):
        self.home = world
        self.x = int(inf[1])
        self.y = int(inf[2])
        self.lives = int(inf[3])
        if len(inf) > 4:
            self.starve_days = int(inf[4])
            self.sex = inf[5]
    
    def who(self):
        kind = str(self.__class__)
        kind = kind[14:len(kind)-2]
        return kind
    
    def id(self):
        string = self.who() + ' ' + str(self.x) + ' ' + str(self.y) + ' ' + str(self.lives)
        if self.who() != 'plant':
            string = string + ' ' + str(self.starve_days) + ' ' + self.sex 
        string = string + '\n'
        return string
    
    def change(self, new_state):
        with open('info.txt') as f:
            lines = f.readlines()
        with open('info.txt', 'w') as f:
            for line in lines:
                if line != self.id():
                    f.write(line)
                else:
                    f.write(new_state)

    def die(self):
        string = ''
        self.change(string)
        i = 0
        while i < len(self.home.field[self.x][self.y].livings):
            if self.home.field[self.x][self.y].livings[i] == self:
                self.home.field[self.x][self.y].livings.pop(i)
            i+=1
        for i in range(len(self.home.everyone)):
            if self.home.everyone[i] == self:
                self.home.everyone[i] = corpse(self.home)

    def lose_life(self, a):
        info = self.id().split()
        info[3] = str(int(info[3])-a)
        weaker = ' '.join(info) + '\n'
        self.change(weaker)
        self.lives = self.lives - a

class corpse(living):
    def __init__(self, world):
        self.home = world

class plant(living):
    max_lives = '9'

    def type(self):
        return 'plant'

    def where(self):
        x = self.x
        y = self.y
        if randint(0,2) == 0:
            if randint(0,2) == 0:
                if x > 0:
                    x-=1
                else:
                    x+=1
            else:
                if x < self.home.n-1:
                    x+=1
                else:
                    x-=1
        else:
            if randint(0,2) == 0:
                if y > 0:
                    y-=1
                else:
                    y+=1
            else:
                if y < self.home.m-1:
                    y+=1
                else:
                    y-=1
        return x, y
    
    def heal(self):
        info = self.id().split()
        info[3] = self.max_lives
        new = ' '.join(info) + '\n'
        self.change(new)
        self.lives = int(plant.max_lives)
    
    def vermehren(self):
        x, y = self.where()
        if self.home.find(x, y, 'plant') != None:
            self.home.find(x, y, 'plant').heal()
        else:
            self.home.add('plant', x = x, y = y)

    def next(self):
        if randint(0,2) == 0:
            self.vermehren()
        self.lose_life(1)
        if self.lives < 1:
            self.die
    
class animal(living):

    def give_birth(self):
        inf = [self.who(), str(self.x), str(self.y), self.max_lives, '0']
        if randint(0,2) == 0:
            sex = 'm'
        else:
            sex = 'f'
        inf.append(sex)
        self.home.field[self.x][self.y].livings.append(eval(self.who())(self.home, *inf))
        self.home.everyone.append(self.home.field[self.x][self.y].livings[-1])
        plus_one = self.id() + self.home.field[self.x][self.y].livings[-1].id()
        self.change(plus_one)
    
    def where(self, old_pos, distance):
        if old_pos < distance:
            new_pos = old_pos + distance
        elif self.home.n-old_pos <= distance:
            new_pos = old_pos - distance
        else:
            if randint(0,2) == 0:
                new_pos = old_pos + distance
            else:
                new_pos = old_pos - distance
        return new_pos

    def move(self):
        distance_x = randint(0, self.max_distance + 1)
        distance_y = randint(0, self.max_distance - distance_x+1)
        info = self.id().split()
        new_x = self.where(self.x, distance_x)
        new_y = self.where(self.y, distance_y)
        info[1] = str(new_x)
        info[2] = str(new_y)
        new_pos = ' '.join(info) + '\n'
        self.change(new_pos)
        i = 0
        while i < len(self.home.field[self.x][self.y].livings):
            if self.home.field[self.x][self.y].livings[i] == self:
                self.home.field[self.x][self.y].livings.pop(i)
                break
            i+=1
        self.home.field[new_x][new_y].livings.append(self)
        self.x = new_x
        self.y = new_y
    
    def starve(self):
        info = self.id().split()
        info[4] = str(self.starve_days + 1)
        new = ' '.join(info) + '\n'
        self.change(new)
        self.starve_days+=1

    def find_prey(self):
        for i in range(len(self.home.field[self.x][self.y].livings)):
            if self.home.field[self.x][self.y].livings[i].type() == 'herbivore':
                if self.size >= self.home.field[self.x][self.y].livings[i].size:
                    return self.home.field[self.x][self.y].livings[i]

class predator(animal):
    def type(self):
        return 'predator'
    
    def eat(self, other):
        other.die()
        info = self.id().split()
        info[4] = '0'
        not_hungry = ' '.join(info) + '\n'
        self.change(not_hungry)
        self.starve_days = 0

    def next(self):
        if self.sex == 'f' and self.home.find(self.x, self.x, self.who(), s = 'm'):
            self.give_birth()
            print('on cell  ' + str(self.x) + ' ' + str(self.y) + ' new ' + self.who() + ' was born')
        if self.find_prey() != None:
            print(self.who() + ' eats ' + self.find_prey().who() + ' on cell ' + str(self.x) + ' ' + str(self.y))
            self.eat(self.find_prey())
        else:
            self.starve()
            if self.starve_days >= self.max_starve:
                self.die()
                print(self.who() + ' of cell ' + str(self.x) +' ' + str(self.y) + ' starved to death')
        self.lose_life(1)
        if self.lives < 1:
            print(self.who() + ' of cell ' + str(self.x) +' ' + str(self.y) + ' passed away, rest in peace')
            self.die()

class wolf(predator):
    size = 2
    max_lives = '7'
    max_distance = 3
    max_starve = 4

class fox(predator):
    size = 1
    max_lives = '6'
    max_distance = 2
    max_starve = 5

class herbivore(animal):
    def type(self):
        return 'herbivore'
    
    def eat(self, other):
        other.lose_life(self.voracity)
        if other.lives <= 0:
            other.die()
        info = self.id().split()
        info[4] = '0'
        not_hungry = ' '.join(info) + '\n'
        self.change(not_hungry)
        self.starve_days = 0
    
    def next(self):
        if self.sex == 'f' and self.home.find(self.x, self.x, self.who(), s = 'm'):
            self.give_birth()
            print('on cell  ' + str(self.x) + ' ' + str(self.y) + ' new ' + self.who() + ' was born')
        if self.home.find(self.x, self.y, 'plant') != None:
            self.eat(self.home.find(self.x, self.y, 'plant'))
        else:
            self.starve()
            if self.starve_days >= self.max_starve:
                self.die()
                print(self.who() + ' of cell ' + str(self.x) +' ' + str(self.y) + ' starved to death')
        self.lose_life(1)
        if self.lives < 1:
            print(self.who() + ' of cell ' + str(self.x) +' ' + str(self.y) + ' passed away')
            self.die()

class hare(herbivore):
    size = 1
    max_lives = '5'
    max_starve = 3
    max_distance = 2
    voracity = 1

class moose(herbivore):
    size = 2
    max_lives = '11'
    max_starve = 5
    max_distance = 1
    voracity = 4
