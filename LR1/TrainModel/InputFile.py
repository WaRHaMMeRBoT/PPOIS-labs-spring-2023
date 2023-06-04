from Objects import Train
from Objects import RailStation
import re
import json


def data_about_state(edges, nodes, trains):
    print("Stations:")
    for i in range(0, len(nodes)):
        nodes[i].__str__()
    print("Trains:")
    for i in range(0, len(trains)):
        trains[i].__str__()
    print(f"\nWays between stations: {edges}\n")


def find_integers(begin_string):
    pattern = r"\d+"
    integers = re.findall(pattern, begin_string)
    integer_string = ''.join(integers)
    return integer_string


def create_stations(nodes, storage):
    result = []
    for i in range(0, len(nodes)):
        result.append(RailStation(nodes[i], storage[i]))
    return result


def find_edges(data_for_rail):
    edges = {}
    for i in range((data_for_rail.index("Graph:") + 1), data_for_rail.index("RSLocation:")):
        edges[i] = data_for_rail[i]
    return edges


def find_stations_storage(data_for_rail):
    storage = []
    for i in range((data_for_rail.index("RSLocation:") + 1), data_for_rail.index("Trains:")):
        storage.append(data_for_rail[i])
    return storage


def find_route(data_for_rails):
    i = data_for_rails.index("Routes:") + 1
    b = 0
    data_for_routes = []
    while i < (len(data_for_rails)-1):
        data_for_routes.append(find_integers(data_for_rails[i]))
        b += 1
        i += 1
    return data_for_routes


def find_trains(data_for_rail):
    route = find_route(data_for_rail)
    trains = []
    b = 0
    for i in range((data_for_rail.index("Trains:") + 1), data_for_rail.index("Routes:")):
        temp_list = data_for_rail[i].split()
        trains.append(Train(temp_list[0], temp_list[1], route[b]))
        b += 1
    return trains


def end_of_formatting(edges, stations, trains):  # Now we should create JSON-file and then dump dictionary there
    data = ""
    for i in range(1, len(edges)):
        data += f"{edges[i]}\n"
    data += "\n"
    for i in range(0, len(stations)):
        data += f"{stations[i].storage.strip()}\n"
    data += "\n"
    for i in range(0, len(trains)):
        data += f"{trains[i].goods} {trains[i].speed}\n"
    data += "\n"
    for i in range(0, len(trains)):
        data += f"{' -> '.join(trains[i].route)}\n"
    sections = data.strip().split("\n\n")
    keys = ["Graph", "RSLocation", "Trains", "Routes"]
    dict_data = dict(zip(keys, sections))
    with open(r"C:\Users\vladi\Desktop\4\PPois\TrainModel\test1.json", "w") as end_file:
        json.dump(dict_data, end_file, indent=4)
