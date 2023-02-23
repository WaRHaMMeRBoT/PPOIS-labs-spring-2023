import Test
import Objects
import RailRoadFile


def add_train(railroad):
    start_point = input('Start point: ')
    speed = int(input('Speed:'))
    railroad.append_train(speed, start_point)


def add_station(railroad):
    name = input('Station name: ')
    railroad.append_station(name)


def add_way_between_stations(railroad):
    name_1 = input('First station name: ')
    name_2 = input('Second station name: ')
    distance = int(input('Distance :'))
    railroad.append_way_between_stations(name_1, name_2, distance)


def add_goods_train(railroad):
    target_node = input('Target station: ')
    goods_to_append = input('Goods: ')
    train_index = int(input('Train index :'))
    railroad.append_goods_train(target_node, train_index, goods_to_append)


def add_goods_station(railroad):
    target_node = input('Target station: ')
    goods_to_append = input('Goods: ')
    railroad.append_goods_station(target_node, goods_to_append)


def add_goods_train_from_station(railroad):
    train_index = int(input('Train index :'))
    railroad.append_goods_train_from_station(train_index)


def remove_train(railroad):
    train_index = int(input('Train index :'))
    railroad.remove_train(train_index)


def remove_way_between_stations(railroad):
    name_1 = input('First station name: ')
    name_2 = input('Second station name: ')
    railroad.remove_way_between_stations(name_1, name_2)


def remove_station(railroad):
    name = input('Station name: ')
    railroad.remove_station(name)


def get_command(railroad):
    command = input().lower()
    if command == "test":
        railroad[0] = Test.rail
    elif command == "get_rail_stations_state":
        railroad[0].state_nodes()
    elif command == "get_rail_stations_way_state":
        railroad[0].state_edges()
    elif command == "get_rail_state":
        railroad[0].state_nodes()
        railroad[0].state_edges()
        railroad[0].state_trains()
    elif command == "get_railway_trains_state":
        railroad[0].state_trains()
    elif command == "add_station":
        add_station(railroad[0])
    elif command == "add_train":
        add_train(railroad[0])
    elif command == "add_way_between_stations":
        add_way_between_stations(railroad[0])
    elif command == "add_goods_train":
        add_goods_train(railroad[0])
    elif command == "add_goods_station":
        add_goods_station(railroad[0])
    elif command == "add_goods_train_from_station":
        add_goods_train_from_station(railroad[0])
    elif command == "time_move":
        railroad[0].time_move()
    elif command == "remove_train":
        remove_train(railroad[0])
    elif command == "remove_way_between_stations":
        remove_way_between_stations(railroad[0])
    elif command == "remove_station":
        remove_station(railroad[0])
    if command == "end_session":
        return True
    else:
        return False
