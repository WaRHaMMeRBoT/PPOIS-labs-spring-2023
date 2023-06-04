import time
import InputFile
import json
import click
import Objects
import random

with open(r"C:\Users\vladi\Desktop\4\PPois\TrainModel\test1.json", "r") as file:
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


@click.group()
def cli():
    pass


@click.command()
def data_about_state():
    InputFile.data_about_state(edges, nodes, trains)


@click.command()
@click.argument('goods')
@click.argument('speed')
@click.argument('route')
def add_train(goods, speed, route):
    trains.append(Objects.Train(goods, speed, route))
    print(f"Add train with goods {goods}, speed {speed} and route {route}")
    InputFile.end_of_formatting(edges, nodes, trains)


@click.command()
@click.argument('amount')
@click.argument('trainnum')
@click.argument('stationnum')
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


@click.command()
@click.argument('amount')
@click.argument('trainnum')
@click.argument('stationnum')
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


@click.command()
@click.argument('storage_station')
def add_station(storage_station):
    name = len(nodes) + 1
    nodes.append(Objects.RailStation(name, storage_station))
    edges[len(edges) + 1] = f"{nodes[len(nodes) - 2].name} {nodes[len(nodes) - 1].name}"
    print(f"Add station {name} with goods {storage_station}")
    InputFile.end_of_formatting(edges, nodes, trains)

@click.command()
# @click.argument('itterations_amount')
def auto_trip():
    i = 0
    while True:
        amount = random.randint(0, 200)
        train = trains[random.randint(0, len(trains)-1)]
        station = nodes[random.randint(0, len(nodes)-1)]
        operation = random.randint(0, 1)       
        if operation:
            print("Before :")
            train.__str__()
            station.__str__()
            while True:
                if amount <= float(station.storage):
                    break
                else:
                    amount = random.randint(0, 100)
            station.change_amount_of_storage(-amount)
            train.change_amount_of_goods(amount)
            print("After :")
            train.__str__()
            station.__str__()
            InputFile.end_of_formatting(edges, nodes, trains)
        elif not operation:
            print("Before :")
            train.__str__()
            station.__str__()
            while True:
                if amount <= float(station.storage):
                    break
                else:
                    amount = random.randint(0, 100)
            station.change_amount_of_storage(amount)
            train.change_amount_of_goods(-amount)
            print("After :")
            train.__str__()
            station.__str__()
            InputFile.end_of_formatting(edges, nodes, trains)          
        InputFile.data_about_state(edges, nodes, trains)
        i += 1    
        if i == 10:
           break   
        print('======================================')
        time.sleep(1)        

   

cli.add_command(data_about_state)
cli.add_command(add_train)
cli.add_command(append_goods_from_station)
cli.add_command(append_goods_to_station)
cli.add_command(add_station)
cli.add_command(auto_trip)

if __name__ == '__main__':
    cli()
