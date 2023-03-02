class RailStation:
    def __init__(self, name, storage):
        self.name = name
        self.storage = storage
    def __str__(self):
        print(f"Station = {self.name}, Storage = {self.storage}")
    def change_amount_of_storage(self, amount):
        self.storage = str(int((float(self.storage) + amount)))


class Train:
    def __init__(self, goods, speed, route):
        self.goods = goods
        self.speed = float(speed)
        self.route = route
        self.start_point = route[0]
        self.previous_stations = 0
        self.time_to_next_station = 1/self.speed
        self.length_of_the_path = len(self.route)
    def __str__(self):
        print(f"Route = {self.route}, speed = {self.speed}, goods = {self.goods}")
    def change_start_point(self):
        self.previous_stations += 1
        self.start_point = self.route[self.previous_stations]
        self.route = self.route[1:]
        self.time_to_next_station = 1 / self.speed
    def change_time_to_next_station(self, number):
        self.time_to_next_station -= number
    def change_amount_of_goods(self, amount):
        self.goods = str(int(float(self.goods) + amount))