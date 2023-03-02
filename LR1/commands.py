import Objects
import InputFile
from InputFile import data_about_state
from InputFile import end_of_formatting


def working_with_railmap(edges, nodes, trains):
    command = input("Starting work with rail map (Yes, No): ").lower()
    match command:
        case "yes":
            going_until_break(edges, nodes, trains)
        case "no":
            end_of_formatting(edges, nodes, trains)


def going_until_break(edges, stations, trains):
    number2 = 555
    number = 555
    for i in range(0, len(trains)):
        if trains[i].previous_stations == trains[i].length_of_the_path - 1:
            print(f"Train {i + 1} end his path\n")
            trains.pop(i)
    for i in range(0, len(trains)):
        if trains[i].previous_stations == trains[i].length_of_the_path - 1:
            print(f"Train {i + 1} end his path\n")
            trains.pop(i)
            continue
        if trains[i].time_to_next_station == min(trains, key=lambda obj: obj.time_to_next_station).time_to_next_station:
            trains[i].change_start_point()
            if number != 555:
                number2 = i
            else:
                number = i
            print(f"\nTrain number {i + 1} come to station {trains[i].start_point}")
        else:
            trains[i].change_time_to_next_station(
                min(trains, key=lambda obj: obj.time_to_next_station).time_to_next_station)
    if (number | number2) != 555:
        train_at_the_station(stations, trains[number])
        train_at_the_station(stations, trains[number2])
    else:
        train_at_the_station(stations, trains[number])
    choice_before_next_move(edges, stations, trains)


def train_at_the_station(stations, train):
    station = stations[int(train.start_point) - 1]
    train.__str__()
    station.__str__()
    command = input("What want you to do (Append goods from station, Append goods to station or Pass):").lower()
    match command:
        case "append goods from station":
            while True:
                amount = float(input("Amount of goods:"))
                if amount <= float(station.storage):
                    break
                else:
                    print("Invalid input. Please enter a valid number.")
            station.change_amount_of_storage(-amount)
            train.change_amount_of_goods(amount)
        case "append goods to station":
            while True:
                amount = float(input("Amount of goods:"))
                if amount <= float(train.goods):
                    break
                else:
                    print("Invalid input. Please enter a valid number.")
            station.change_amount_of_storage(amount)
            train.change_amount_of_goods(-amount)
        case "pass":
            pass


def choice_before_next_move(edges, stations, trains):
    while True:
        command = input(
            "What want you to do (Add train, Add station, Look at the status, Continue, End this):").lower()
        match command:
            case "add train":
                goods = int(input("Amount of goods in train: "))
                speed = float(input("Speed of train (part of way for 1 iteration): "))
                route = input("Route of train: ")
                trains.append(Objects.Train(goods, speed, route))
            case "add station":
                name = len(stations) + 1
                storage = int(input("Storage of station: "))
                stations.append(Objects.RailStation(name, storage))
                edges[len(edges) + 1] = f"{stations[-1].name} {stations[-2].name}"
            case "look at the status":
                data_about_state(edges, stations, trains)
            case "continue" | "end this":
                break
    match command:
        case "add train" | "add station" | "look at the status" | "continue":
            going_until_break(edges, stations, trains)
        case "end this":
            print("Bye!")
            InputFile.end_of_formatting(edges, stations, trains)
