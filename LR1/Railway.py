import Train


class Railway:
    def __init__(self, stations, train: Train):
        self.stations = stations
        self.train = train

    def start_train(self):
        size = len(self.stations)
        for i in range(size):
            if i == size - 1:
                current_station = self.stations[i]
                self.train.processStation(current_station, True)
            else:
                current_station = self.stations[i]
                self.train.processStation(current_station, False)
