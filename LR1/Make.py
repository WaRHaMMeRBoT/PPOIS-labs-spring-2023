import random


class Station: # Станция

    def __init__(self):
        self.number = -1
        self.storage = {}
        self.queue = []# Очередь поездов на станции
        self.roads = []
        self.train_number = -1# Номер поезда, который выполняет действие на сстанции


class Carriage: # Вагон

    def __init__(self, products):
        self.product = random.choice(products)
        self.coll_product = 0


class Make(Carriage, Station): # Поезд

    def __init__(self, products, way):
        Carriage.__init__(self, products)
        Station.__init__(self)
        self.train = {}
        self.station = {}
        self.train_list = []
        self.station_list = []
        self.products = products
        self.way = way

    def Make_Train(self):
        for i in range(0, random.choice(range(1, len(self.products) + 1))):
            train = {}
            c = Carriage(self.products)
            self.train[c.product] = c.coll_product
            train['train'] = self.train
            train['list'] = []
            train['make'] = False
        return train

    def Make_Trane_list(self):

        for i in range(0, random.choice(range(3, len(self.way)))):
            train = Make(self.products, self.way)
            self.train_list.append(train.Make_Train())
        return self.train_list

    def Make_Station(self, number):

        station = Station()
        self.station['number'] = number
        storeg = {}
        storeg[random.choice(self.products)] = random.choice(range(100, 200))
        self.station['storage'] = storeg
        self.station['queue'] = []
        list = []
        for i in range(0, len(self.way[number])):
            if self.way[number][i] == 1:
                list.append(i)
        self.station['roads'] = list
        self.station['train_number'] = -1

        return self.station

    def Make_Station_list(self):

        for i in range(0, len(self.way)):
            station = Make(self.products, self.way)
            self.station_list.append(station.Make_Station(i))
        return self.station_list