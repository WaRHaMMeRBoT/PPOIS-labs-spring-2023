import InputFile
import Objects
import json


with open(r"C:\Users\vladi\Desktop\4семестр\ППОИС\TrainModel\test1.json", "r") as file:
    file_for_data = json.load(file)
data_for_rail = ""
for key, value in file_for_data.items():
    data_for_rail += f"{key}:\n{value}\n"
data_for_rail = data_for_rail.split("\n")  
data_for_rail[:] = [c.strip("\n") for c in data_for_rail[:]]
edges = InputFile.find_edges(data_for_rail)
storage = InputFile.find_stations_storage(data_for_rail)
nodes = InputFile.create_stations(list(edges.keys()), storage)
trains = InputFile.find_trains(data_for_rail)

def add_train(goods, speed, route):
    trains.append(Objects.Train(goods, speed, route))
    print(f"Add train with goods {goods}, speed {speed} and route {route}")
    InputFile.end_of_formatting(edges, nodes, trains)

def append_goods_from_station(amount, trainnum, stationnum):
    amount = int(amount)
    train = trains[int(trainnum) - 1]
    station = nodes[int(stationnum) - 1]
    print("Before :")
    train.__str__()
    station.__str__()
    while True:
        if amount <= float(station.storage):
            break
        else:
            print("Invalid input. Please enter a valid number.")
    station.change_amount_of_storage(-amount)
    train.change_amount_of_goods(amount)
    print("After :")
    train.__str__()
    station.__str__()
    InputFile.end_of_formatting(edges, nodes, trains)


def append_goods_to_station(amount, trainnum, stationnum):
    amount = int(amount)
    train = trains[int(trainnum) - 1]
    station = nodes[int(stationnum) - 1]
    print("Before :")
    train.__str__()
    station.__str__()
    while True:
        if amount <= float(station.storage):
            break
        else:
            print("Invalid input. Please enter a valid number.")
    station.change_amount_of_storage(amount)
    train.change_amount_of_goods(-amount)
    print("After :")
    train.__str__()
    station.__str__()
    InputFile.end_of_formatting(edges, nodes, trains)    


def add_station(storage_station):
    name = len(nodes) + 1
    nodes.append(Objects.RailStation(name, storage_station))
    edges[len(edges) + 1] = f"{nodes[len(nodes) - 2].name} {nodes[len(nodes) - 1].name}"
    print(f"Add station {name} with goods {storage_station}")
    InputFile.end_of_formatting(edges, nodes, trains)    