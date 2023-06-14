import test
import obj
import roads


def AddTrain(railroad):
    start_point = input('Start point: ')
    speed = int(input('Speed:'))
    railroad.append_train(speed, start_point)


def AddStation(railroad):
    name = input('Station name: ')
    railroad.append_station(name)


def AddWay(railroad):
    name_1 = input('First station name: ')
    name_2 = input('Second station name: ')
    distance = int(input('Distance :'))
    railroad.append_way_between_stations(name_1, name_2, distance)


def AddGoodsTrain(railroad):
    target_node = input('Target station: ')
    goods_to_append = input('Goods: ')
    train_index = int(input('Train index :'))
    railroad.append_goods_train(target_node, train_index, goods_to_append)


def AddGoodsStation(railroad):
    target_node = input('Target station: ')
    goods_to_append = input('Goods: ')
    railroad.append_goods_station(target_node, goods_to_append)


def AddGoodsTrainFromStation(railroad):
    train_index = int(input('Train index :'))
    railroad.append_goods_train_from_station(train_index)


def RemoveTrain(railroad):
    train_index = int(input('Train index :'))
    railroad.remove_train(train_index)


def RemoveWay(railroad):
    name_1 = input('First station name: ')
    name_2 = input('Second station name: ')
    railroad.remove_way_between_stations(name_1, name_2)


def RemoveStation(railroad):
    name = input('Station name: ')
    railroad.remove_station(name)


def get_command(railroad):
    command = input().lower()
    if command == "test":
        railroad[0] = test.rail
    elif command == "get_stations":
        railroad[0].state_nodes()
    elif command == "get_ways":
        railroad[0].state_edges()
    elif command == "get_railway_trains":
        railroad[0].state_trains()
    elif command == "add_station":
        AddStation(railroad[0])
    elif command == "add_train":
        AddTrain(railroad[0])
    elif command == "add_way":
        AddWay(railroad[0])
    elif command == "add_goods_train":
        AddGoodsTrain(railroad[0])
    elif command == "add_goods_station":
        AddGoodsStation(railroad[0])
    elif command == "add_goods_train_from_station":
        AddGoodsTrainFromStation(railroad[0])
    elif command == "remove_train":
        RemoveTrain(railroad[0])
    elif command == "remove_way":
        RemoveWay(railroad[0])
    elif command == "remove_station":
        RemoveStation(railroad[0])
    elif command == "step":
        railroad[0].step()
        railroad[0].state_trains()
    if command == "end_session":
        return True
    else:
        return False