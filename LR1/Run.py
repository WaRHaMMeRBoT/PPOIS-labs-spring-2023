import random


class Run:
    def __init__(self, station_list, train_list, task: str):
        self.station_list = station_list
        self.train_list = train_list
        self.task = task

    def handler(self):
        list = self.task.split()
        print(list)
        start = False
        myself = False
        day = 0
        for i in range(0, len(list)):
            if list[i].lower() == 'start':
                start = True
            if list[i].lower() == 'myself':
                myself = True
                day = int(list[-1])
        if start and not myself:
            while True:
                run = Run(self.station_list, self.train_list, self.task)
                event = input('==> ')
                run.First_step()
                if event.lower() == 'погрузка':
                    run.Second_step()
                elif event.lower() == 'разгрузка':
                    run.Fouth_step()
                elif event.lower() == 'переезд':
                    run.Third_step()
                elif event.lower() == 'выход':
                    break
        elif start and myself:
            run = Run(self.station_list, self.train_list, self.task)
            a = [1, 2, 3, 2]
            task = []
            while not len(task) == day:
                for i in range(0, len(a)):
                    task.append(a[i])
                    if len(task) == day:
                        break
            run.First_step()
            print('====================')
            for i in range(0, len(task)):
                if task[i] == 1:
                    run.Second_step()
                    print('====================')
                elif task[i] == 2:
                    run.Third_step()
                    print('====================')
                elif task[i] == 3:
                    run.Fouth_step()
                    print('====================')

    def First_step(self):#Распределение всех поездов по станциям
        i = 0
        while True:
            station = random.choice(self.station_list)
            if station['train_number'] == -1:
                station['train_number'] = i
                station['queue'].append(i)
                self.train_list[i]['list'].append(station['number'])
            else:
                self.train_list[i]['list'].append(station['number'])
                station['queue'].append(i)
            i += 1
            if i == len(self.train_list):
                break

    def Second_step(self):# Погрузка
        for i in range(0, len(self.station_list)):
            if not self.station_list[i]['train_number'] < 0:
                keys = list(self.train_list[self.station_list[i]['train_number']]['train'].keys())
                key = list(self.station_list[i]['storage'].keys())
                for j in range(0, len(keys)):
                    if key[0] == keys[j]:
                        a = self.station_list[i]['storage']
                        b = int(a[key[0]])
                        c = int(random.choice(range(0, b)))
                        d = b - c
                        self.train_list[self.station_list[i]['train_number']]['train'][keys[j]] += c
                        self.station_list[i]['storage'][key[0]] = d
                        break
                self.station_list[i]['queue'].remove(self.station_list[i]['train_number'])
                self.train_list[self.station_list[i]['train_number']]['make'] = True
                if len(self.station_list[i]['queue']) == 0:
                    self.station_list[i]['train_number'] = -1
                else:
                    self.station_list[i]['train_number'] = self.station_list[i]['queue'][0]
        for i in range(0, len(self.station_list)):
            print(self.station_list[i])
        for i in range(0, len(self.train_list)):
            print('{}:{}'.format(i, self.train_list[i]))


    def Third_step(self):#  Переезд
        for i in range(0, len(self.train_list)):
            if self.train_list[i]['make'] == True:
                while True:
                    next_station = random.choice(range(0, len(self.station_list)))
                    if not next_station == self.train_list[i]['list'][-1]:
                        break
                self.train_list[i]['list'].append(next_station)
                for j in range(0, len(self.station_list)):
                    if self.station_list[j]['number'] == next_station:
                        self.train_list[i]['make'] = False
                        self.station_list[j]['queue'].append(i)
                        if self.station_list[j]['train_number'] == -1:
                            self.station_list[j]['train_number'] = i
                        break
        for i in range(0, len(self.train_list)):
            print('{}:{}'.format(i, self.train_list[i]))

    def Fouth_step(self): # Разгрузка
        for i in range(0, len(self.station_list)):
            if not self.station_list[i]['train_number'] < 0:
                keys = list(self.train_list[self.station_list[i]['train_number']]['train'].keys())
                key = list(self.station_list[i]['storage'].keys())
                for j in range(0, len(keys)):
                    if key[0] == keys[j]:
                        a = int(self.train_list[self.station_list[i]['train_number']]['train'][key[0]])
                        if a == 0:
                            break
                        b = int(random.choice(range(0, a)))
                        self.station_list[i]['storage'][key[0]] += b
                        self.train_list[self.station_list[i]['train_number']]['train'][key[0]] -= b
                        break
                self.station_list[i]['queue'].remove(self.station_list[i]['train_number'])
                self.train_list[self.station_list[i]['train_number']]['make'] = True
                if len(self.station_list[i]['queue']) == 0:
                    self.station_list[i]['train_number'] = -1
                else:
                    self.station_list[i]['train_number'] = self.station_list[i]['queue'][0]
        for i in range(0, len(self.station_list)):
            print(self.station_list[i])
        for i in range(0, len(self.train_list)):
            print('{}:{}'.format(i, self.train_list[i]))