import logging
from entities.Railroad import Railroad
from entities.trains.Train import Train
from entities.trains.Train import Action
from entities.stations.CargoStation import CargoStation
from entities.stations.MixedStation import MixedStation
from entities.stations.PassengerStation import PassengerStation
from entities.trains.CargoWagon import CargoWagon
from entities.trains.PassengerWagon import PassengerWagon


def print_graph(graph: list[list[tuple[int, int]]]) -> None:
    logging.info('Railroad graph structure: ')
    for i in range(len(graph)):
        for j in range(len(graph[i])):
            print("    {0}-[{1}]->{2}".format(i - 1,
                  graph[i][j][1], graph[i][j][0]))


def before_delim(string: str, delim: str) -> str:
    return string[0:string.index(delim)]


def after_delim(string: str, delim: str) -> str:
    return string[string.index(delim) + len(delim)]


def create_railroad(read_from: str) -> Railroad:
    instance = Railroad()
    file = open(read_from, 'r')
    lines = file.readlines()
    for line in lines:
        if '---' in line:
            break
        index = lines.index(line)
        buf = []
        for token in line.split(';')[:-1]:
            if lines.index(line) == 0:
                read_capacity = 0
                try:
                    read_capacity = int(token[1:len(token)])
                except Exception as e:
                    logging.error(e)
                match(token[0]):
                    case '$': instance.add_station(CargoStation(capacity=read_capacity))
                    case '@': instance.add_station(PassengerStation(capacity=read_capacity))
                    case '&': instance.add_station(MixedStation(capacity_civ=read_capacity,
                                                                capacity_cargo=read_capacity))
            else:
                adj = 0
                weight = 0
                try:
                    adj = int(before_delim(token, '^'))
                    weight = int(after_delim(token, '^'))
                except Exception as e:
                    logging.error(e)
                buf.append((adj, weight))
        if lines.index(line) != 0:
            instance.push_line(buf)
    file.close()
    return instance


def create_trains(read_from: str, railroad: Railroad) -> list[Train]:
    file = open(read_from, 'r')
    delimiter_met = False
    lines = file.readlines()
    trains = []
    train = None
    offset = 1
    for line in lines:
        if '---' in line:
            delimiter_met = True
        if not delimiter_met:
            offset += 1
            continue
        index = -1
        prev_id = -1
        read_capacity = 0
        token_index = -1
        train = None
        for token in line.split(';')[:-1]:
            token_index += 1
            match token_index:
                case 0:
                    train = Train(token, 4, railroad)
                case 1:
                    for path_token in token.split('-'):
                        try:
                            index = int(path_token[1:len(path_token)])
                        except Exception as e:
                            logging.error(e)
                        if (index != -1) and (prev_id != -1):
                            if not railroad.direct_path_exists(prev_id, index):
                                print(prev_id, index)
                                logging.error(
                                    "The path from {0} to {1} is not traversable or does not exist!".format(prev_id,
                                                                                                            index))
                            elif index > (len(railroad.get_stations())):
                                logging.error(
                                    "Station index {0} is out of described stations bounds!".format(index))
                        match path_token[0]:
                            case '<':
                                train.add_checkpoint(index, Action.LOAD)
                            case '>':
                                train.add_checkpoint(index, Action.UNLOAD)
                            case '!':
                                train.add_checkpoint(index, Action.WAIT)
                            case '#':
                                train.add_checkpoint(index, Action.SKIP)
                        prev_id = index
                case 2:
                    for wagon_token in token.split(','):
                        try:
                            read_capacity = int(wagon_token[1:])
                        except Exception as e:
                            logging.error(e)
                        match wagon_token[0]:
                            case '$':
                                train.add_wagon(CargoWagon(read_capacity))
                            case '@':
                                train.add_wagon(PassengerWagon(read_capacity))
        if train is not None:
            trains.append(train)
    return trains
