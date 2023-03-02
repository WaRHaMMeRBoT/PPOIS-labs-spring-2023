import InputFile
import commands
import json

with open(r"C:\sem3_ppois_lab1\test1.json", "r") as file:
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
InputFile.data_about_state(edges, nodes, trains)
commands.working_with_railmap(edges, nodes, trains)
