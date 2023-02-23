import Objects
import GraphFile


class RailRoad:
    def __init__(self, nodes, edges, trains):
        self.trains = trains
        self.edges = edges
        self.nodes = nodes
        self.graph = GraphFile.Graph(self.nodes, self.edges)

    def is_node_exist(self, node):
        return next(filter(lambda n: n.name == node, self.nodes), None)

    def append_station(self, station_name):
        try:
            time_node = self.is_node_exist(station_name)
            if time_node:
                raise Exception('Station is existed')
        except Exception as ex:
            print(ex.args[0])
        else:
            self.nodes.append(Objects.RailStation(station_name))
            self.graph = GraphFile.Graph(self.nodes, self.edges)

    def append_way_between_stations(self, station_name_1, station_name_2, distance):
        time_node_1 = self.is_node_exist(station_name_1)
        time_node_2 = self.is_node_exist(station_name_2)
        try:
            if not time_node_1 or not time_node_2:
                raise Exception('Station is not existed')
            if time_node_1 == time_node_2:
                raise Exception('Stations is same')
            if self.edges[time_node_1].get(time_node_2):
                raise Exception('Way between stations is existed')
        except Exception as ex:
            print(ex.args[0])
        else:
            self.edges[time_node_1][time_node_2] = distance
            self.graph = GraphFile.Graph(self.nodes, self.edges)

    def time_move(self):
        for train in self.trains:
            if train.move():
                train.target_point.set_storage(train.get_goods())
                if train.goods:
                    train.target_point = train.goods[0].target_point
                    train.way_check(self.graph)

    def state_nodes(self):
        try:
            if not self.nodes:
                raise Exception('There are no stations')
        except Exception as ex:
            print(ex.args[0])
        else:
            for node in self.nodes:
                print('Station name: ' + node.name + '.\nGoods: ')
                for good in node.storage.storage_goods:
                    print(good.goods)

    def state_edges(self):
        try:
            if not self.edges:
                raise Exception('There are no ways between stations')
        except Exception as ex:
            print(ex.args[0])
        else:
            for node_1 in self.nodes:
                for node_2 in self.nodes:
                    if self.edges[node_1].get(node_2):
                        print(node_1.name + '-' + node_2.name + ' ' + str(self.edges[node_1].get(node_2)))

    def state_trains(self):
        try:
            if not self.trains:
                raise Exception('There are no trains')
        except Exception as ex:
            print(ex.args[0])
        else:
            for train in self.trains:
                print('Train index : ' + str(self.trains.index(train)) + '\nCurrent point and distance : ' +
                      train.current_point.name + ' ' + str(train.distance) + '\nSpeed: ' + str(
                    train.speed) + '\nGoods : ')
                for good in train.goods:
                    print(good.goods)

    def append_train(self, speed, start_point):
        time_node = self.is_node_exist(start_point)
        try:
            if not time_node:
                raise Exception('Station is not existed')
        except Exception as ex:
            print(ex.args[0])
        else:
            self.trains.append(Objects.Train(speed, time_node))

    def append_goods_train(self, target_node, train_index, goods_to_append):
        time_node = self.is_node_exist(target_node)
        time_train = self.trains[train_index]
        try:
            if not time_node:
                raise Exception('Station is not existed')
        except Exception as ex:
            print(ex.args[0])
        else:
            time_train.append_goods(Objects.Goods(time_node, goods_to_append))
            time_train.way_check(self.graph)

    def append_goods_station(self, target_node, goods_to_append):
        time_node = self.is_node_exist(target_node)
        try:
            if not time_node:
                raise Exception('Station is not existed')
        except Exception as ex:
            print(ex.args[0])
        else:
            time_node.storage.set_goods(Objects.Goods(time_node, goods_to_append))

    def append_goods_train_from_station(self, train_index):
        try:
            time_train = self.trains[train_index]
        except IndexError:
            print('There are no train with this index')
        else:
            time_train.append_goods(time_train.current_point.storage.get_goods())
            time_train.way_check(self.graph)

    def remove_train(self, train_index):
        try:
            time_train = self.trains[train_index]
        except IndexError:
            print('There are no train with this index')
        else:
            self.trains.remove(time_train)

    def remove_way_between_stations(self, station_name_1, station_name_2):
        time_node_1 = self.is_node_exist(station_name_1)
        time_node_2 = self.is_node_exist(station_name_2)
        try:
            if not time_node_1 or not time_node_2:
                raise Exception('Station is not existed')
            if time_node_1 == time_node_2:
                raise Exception('Stations is same')
            if not self.edges[time_node_1].get(time_node_2):
                raise Exception('Way between stations is not existed')
        except Exception as ex:
            print(ex.args[0])
        else:
            self.edges[time_node_1].pop(time_node_2)
            self.edges[time_node_2].pop(time_node_1)
            self.graph = GraphFile.Graph(self.nodes, self.edges)

    def remove_station(self, station_name):
        time_node = self.is_node_exist(station_name)
        try:
            if not time_node:
                raise Exception('Station is not existed')
        except Exception as ex:
            print(ex.args[0])
        else:
            for node in self.nodes:
                if self.edges[time_node].get(node):
                    self.edges[time_node].pop(node)
                if self.edges[node].get(time_node):
                    self.edges[node].pop(time_node)
            self.nodes.remove(time_node)
            self.graph = GraphFile.Graph(self.nodes, self.edges)
            for train in self.trains:
                for good in train.goods:
                    if good.target_point == time_node:
                        train.goods.remove(good)
                        train.target_point = train.goods[0].target_point
                        train.way_check(self.graph)

