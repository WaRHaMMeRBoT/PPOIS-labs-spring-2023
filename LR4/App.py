from States import *
from AppendObjects import *
from RemoveOdjects import *


class MainWindow(QMainWindow):

    def init_button(self, lable, size_x, size_y, move_x, move_y, fun):
        button = QPushButton(lable, self)
        button.resize(size_x, size_y)
        button.move(move_x, move_y)
        button.clicked.connect(fun)
        return button

    def __init__(self, railroad):
        super().__init__()

        self.railroad = railroad

        size_x = 480
        size_y = 400

        self.setFixedSize(QSize(size_x, size_y))
        self.setWindowTitle("Железная дорога")

        self.nodes_state = self.init_button('Станции', 120, 40, 0, 0, self.the_nodes_state_was_clicked)
        self.nodes = StationState(self, self.railroad[0].nodes, 'Станции')

        self.edges_state = self.init_button('Пути', 120, 40, 0, 50, self.the_edges_state_was_clicked)
        self.edges = WaysState(self, self.railroad[0].nodes, self.railroad[0].edges, 'Пути')

        self.railway_state = self.init_button('Железная дорога', 120, 40, 0, 100, self.the_railway_state_was_clicked)
        self.railway = RailWayState(self, self.railroad[0].nodes, self.railroad[0].edges, self.railroad[0].trains,
                                    'Железная дорога')

        self.trains_state = self.init_button('Поезда', 120, 40, 0, 150, self.the_trains_state_was_clicked)
        self.trains = TrainsState(self, self.railroad[0].trains, 'Поезда')

        self.add_station_button = self.init_button('Добавить станцию', 200, 40, 140, 0,
                                                   self.the_add_station_button_was_clicked)
        self.add_station = AddStation(self)

        self.add_way_stations_button = self.init_button('Добавить путь', 200, 40, 140, 50,
                                                        self.the_add_way_stations_button_was_clicked)
        self.add_way_stations = AddWayStation(self)

        self.add_train_button = self.init_button('Добавить поезд', 200, 40, 140, 100,
                                                 self.the_add_train_button_was_clicked)
        self.add_train = AddTrain(self)

        self.add_goods_train_button = self.init_button('Добавить груз на поезд', 200, 40, 140, 150,
                                                       self.the_add_goods_train_button_was_clicked)
        self.add_goods_train = AddGoodsTrain(self)

        self.add_goods_station_button = self.init_button('Добавить груз на станцию', 200, 40, 140, 200,
                                                         self.the_add_goods_station_button_was_clicked)
        self.add_goods_station = AddGoodsStation(self)

        self.add_goods_train_from_station_button = self.init_button('Добавить груз на поезд со станции', 200, 40, 140,
                                                                    250,
                                                                    self.the_add_goods_train_from_station_button_was_clicked)
        self.add_goods_train_from_station = AddGoodsTrainFromStation(self)

        self.remove_way_stations = RemoveWayStation(self)
        self.remove_way_stations_button = self.init_button('Удалить путь', 120, 40, 360, 0,
                                                           self.the_remove_way_stations_button_was_clicked)

        self.remove_station_button = self.init_button('Удалить станцию', 120, 40, 360, 50,
                                                      self.the_remove_station_button_was_clicked)
        self.remove_station = RemoveStation(self)

        self.remove_train_button = self.init_button('Удалить поезд', 120, 40, 360, 100,
                                                    self.the_remove_train_button_was_clicked)
        self.remove_train = RemoveTrain(self)

        self.time_move_button = self.init_button('Промотать время', 120, 40, 180, 350,
                                                 self.the_time_move_button_was_clicked)

        self.add_station.submitClicked.connect(self.append_station)
        self.add_train.submitClicked.connect(self.append_train)
        self.add_way_stations.submitClicked.connect(self.append_way_stations)
        self.add_goods_train.submitClicked.connect(self.append_goods_train)
        self.add_goods_station.submitClicked.connect(self.append_goods_station)
        self.add_goods_train_from_station.submitClicked.connect(self.append_goods_train_from_station)
        self.remove_way_stations.submitClicked.connect(self.del_way_stations)
        self.remove_station.submitClicked.connect(self.del_station)
        self.remove_train.submitClicked.connect(self.del_train)

    def the_nodes_state_was_clicked(self):
        self.nodes.show()

    def the_edges_state_was_clicked(self):
        self.edges.show()

    def the_railway_state_was_clicked(self):
        self.railway.show()

    def the_trains_state_was_clicked(self):
        self.trains.show()

    def the_add_station_button_was_clicked(self):
        self.add_station.show()

    def the_add_train_button_was_clicked(self):
        self.add_train.show()

    def the_add_way_stations_button_was_clicked(self):
        self.add_way_stations.show()

    def the_add_goods_train_button_was_clicked(self):
        self.add_goods_train.show()

    def the_add_goods_train_from_station_button_was_clicked(self):
        self.add_goods_train_from_station.show()

    def the_add_goods_station_button_was_clicked(self):
        self.add_goods_station.show()

    def the_remove_way_stations_button_was_clicked(self):
        self.remove_way_stations.show()

    def the_remove_station_button_was_clicked(self):
        self.remove_station.show()

    def the_remove_train_button_was_clicked(self):
        self.remove_train.show()

    def the_time_move_button_was_clicked(self):
        self.railroad[0].time_move()
        self.nodes = StationState(self, self.railroad[0].nodes, 'Станции')
        self.trains = TrainsState(self, self.railroad[0].trains, 'Поезда')
        self.railway = RailWayState(self, self.railroad[0].nodes, self.railroad[0].edges, self.railroad[0].trains,
                                    'Железная дорога')

    def append_station(self, station):
        self.railroad[0].append_station(station)
        self.nodes = StationState(self, self.railroad[0].nodes, 'Станции')
        self.railway = RailWayState(self, self.railroad[0].nodes, self.railroad[0].edges, self.railroad[0].trains,
                                    'Железная дорога')

    def append_train(self, temp_list):
        self.railroad[0].append_train(temp_list[1], temp_list[0])
        self.trains = TrainsState(self, self.railroad[0].trains, 'Поезда')
        self.railway = RailWayState(self, self.railroad[0].nodes, self.railroad[0].edges, self.railroad[0].trains,
                                    'Железная дорога')

    def append_way_stations(self, temp_list):
        self.railroad[0].append_way_between_stations(temp_list[0], temp_list[1], temp_list[2])
        self.edges = WaysState(self, self.railroad[0].nodes, self.railroad[0].edges, 'Пути')
        self.railway = RailWayState(self, self.railroad[0].nodes, self.railroad[0].edges, self.railroad[0].trains,
                                    'Железная дорога')

    def append_goods_train(self, temp_list):
        self.railroad[0].append_goods_train(temp_list[0], temp_list[2], temp_list[1])
        self.trains = TrainsState(self, self.railroad[0].trains, 'Поезда')
        self.railway = RailWayState(self, self.railroad[0].nodes, self.railroad[0].edges, self.railroad[0].trains,
                                    'Железная дорога')

    def append_goods_station(self, temp_list):
        self.railroad[0].append_goods_station(temp_list[0], temp_list[1])
        self.nodes = StationState(self, self.railroad[0].nodes, 'Станции')
        self.railway = RailWayState(self, self.railroad[0].nodes, self.railroad[0].edges, self.railroad[0].trains,
                                    'Железная дорога')

    def append_goods_train_from_station(self, train_index):
        self.railroad[0].append_goods_train_from_station(train_index)
        self.trains = TrainsState(self, self.railroad[0].trains, 'Поезда')
        self.railway = RailWayState(self, self.railroad[0].nodes, self.railroad[0].edges, self.railroad[0].trains,
                                    'Железная дорога')

    def del_way_stations(self, temp_list):
        self.railroad[0].remove_way_between_stations(temp_list[0], temp_list[1])
        self.edges = WaysState(self, self.railroad[0].nodes, self.railroad[0].edges, 'Пути')
        self.railway = RailWayState(self, self.railroad[0].nodes, self.railroad[0].edges, self.railroad[0].trains,
                                    'Железная дорога')

    def del_station(self, station_name):
        self.railroad[0].remove_station(station_name)
        self.trains = TrainsState(self, self.railroad[0].trains, 'Поезда')
        self.nodes = StationState(self, self.railroad[0].nodes, 'Станции')
        self.edges = WaysState(self, self.railroad[0].nodes, self.railroad[0].edges, 'Пути')
        self.railway = RailWayState(self, self.railroad[0].nodes, self.railroad[0].edges, self.railroad[0].trains,
                                    'Железная дорога')

    def del_train(self, train_index):
        self.railroad[0].remove_train(train_index)
        self.trains = TrainsState(self, self.railroad[0].trains, 'Поезда')
        self.railway = RailWayState(self, self.railroad[0].nodes, self.railroad[0].edges, self.railroad[0].trains,
                                    'Железная дорога')
