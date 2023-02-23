import Objects
import RailRoadFile
from RailRoadFile import RailRoad

nodes = []
Reykjavik = Objects.RailStation("Reykjavik")
nodes.append(Reykjavik)
Oslo = Objects.RailStation("Oslo")
nodes.append(Oslo)
Moscow = Objects.RailStation("Moscow")
nodes.append(Moscow)
London = Objects.RailStation("London")
nodes.append(London)
Rome = Objects.RailStation("Rome")
nodes.append(Rome)
Berlin = Objects.RailStation("Berlin")
nodes.append(Berlin)
Belgrade = Objects.RailStation("Belgrade")
nodes.append(Belgrade)
Athens = Objects.RailStation("Athens")
nodes.append(Athens)

init_graph = {}
for node in nodes:
    init_graph[node] = {}

init_graph[Reykjavik][Oslo] = 50
init_graph[Reykjavik][London] = 40
init_graph[Oslo][Berlin] = 10
init_graph[Oslo][Moscow] = 30
init_graph[Moscow][Belgrade] = 40
init_graph[Moscow][Athens] = 40
init_graph[Rome][Berlin] = 20
init_graph[Rome][Athens] = 20

train_1 = Objects.Train(40, Reykjavik, [Objects.Goods(Rome, '100'), Objects.Goods(Berlin, '50')])
train_2 = Objects.Train(20, Rome, [Objects.Goods(Moscow, '200'), Objects.Goods(Oslo, '80')])
train_3 = Objects.Train(60, Moscow, [Objects.Goods(London, '30'), Objects.Goods(Belgrade, '150')])
rail: RailRoad = RailRoadFile.RailRoad(nodes, init_graph, [train_1, train_2, train_3])
train_1.way_check(rail.graph)
train_2.way_check(rail.graph)
train_3.way_check(rail.graph)
