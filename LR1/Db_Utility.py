import json
import Graph
import Train

def load_graph_data():
    with open("D:/university/python/RailwayModelSimulation/Railway_db.json") as f:
        data = json.load(f)
    nodes = data["nodes"]
    edges = data["edges"]
    gr=Graph.Graph()
    for node in nodes:
        gr.add_vertex(node["id"])
    for edge in edges:
        gr.add_edge(edge["source"],edge["target"],edge["weight"])
    return gr

def add_to_graph(graphElm:list):
    with open("D:/university/python/RailwayModelSimulation/Railway_db.json") as f:
        data = json.load(f)

    if len(graphElm)==1:
        for node in data["nodes"]:
            if node["id"] == graphElm[0]:
                return
        data["nodes"].append({"id":graphElm[0]})
        data["nodes"] = sorted(data["nodes"],key=lambda x:x ["id"])

    else:
        for edge in data["edges"]:
            if (edge["source"] == graphElm[0] and edge["target"] == graphElm[1]) \
            or (edge["source"] == graphElm[1] and edge["target"] == graphElm[0]) :
                return
            
        if  {"id":graphElm[0]} not in data["nodes"]:
                data["nodes"].append({"id":graphElm[0]})
        if  {"id":graphElm[1]} not in data["nodes"]:
                data["nodes"].append({"id":graphElm[1]})

        data["edges"].append({"source":graphElm[0],"target":graphElm[1],"weight":graphElm[2]})
        data["nodes"] = sorted(data["nodes"],key=lambda x:x ["id"])
        data["edges"] = sorted(data["edges"],key=lambda x:x ["source"])

    with open("D:/university/python/RailwayModelSimulation/Railway_Db.json","w") as f:
        json.dump(data, f, indent=4)

def del_from_graph(graphElm:list):
    with open("D:/university/python/RailwayModelSimulation/Railway_Db.json") as f:
        data = json.load(f)

    if len(graphElm)==1:
        nodes = [node for node in data["nodes"] if node["id"] != graphElm[0]]
        nodes = sorted(nodes,key=lambda x:x ["id"])
        data["nodes"]=nodes
        edges = [edge for edge in data["edges"] if edge["source"]!= graphElm[0]]
        edges = [edge for edge in edges if edge["target"]!=graphElm[0]]
        data["edges"]=edges                
        with open("D:/university/python/RailwayModelSimulation/Railway_Db.json","w") as f:
            json.dump(data, f, indent=4)

    else:
        for edge in data["edges"]:
             if edge["source"]==graphElm[0] and edge["target"]==graphElm[1]:
                  data["edges"].remove(edge)
                  
        with open("D:/university/python/RailwayModelSimulation/Railway_Db.json","w") as f:
            json.dump(data, f, indent=4)
 
def load_train_data():
        with open("D:/university/python/RailwayModelSimulation/Railway_Db.json") as f:
            data = json.load(f)
        trains = []
        for train in data["trains"]:
             trains.append(Train.Train(train["train_number"],train["locomotive_speed"],train["traincar_value"]))
        return trains

def add_to_trains(trainElm:list):
    with open("D:/university/python/RailwayModelSimulation/Railway_Db.json") as f:
        data = json.load(f)
    for train in data["trains"]:
            if (train["train_number"] == trainElm[0] or trainElm[1]<0):
                return
            
    data["trains"].append({"train_number":trainElm[0],"locomotive_speed":trainElm[1],"traincar_value":trainElm[2]})
    with open("D:/university/python/RailwayModelSimulation/Railway_Db.json","w") as f:
            json.dump(data, f, indent=4)

def del_from_trains(trainElm:list):
    with open("D:/university/python/RailwayModelSimulation/Railway_Db.json") as f:
        data = json.load(f)
    if (len(trainElm)==1):
        trains=[train for train in data["trains"] if train["train_number"]==trainElm[0]]
        data["trains"]=trains
        with open("D:/university/python/RailwayModelSimulation/Railway_Db.json","w") as f:
            json.dump(data, f, indent=4)
