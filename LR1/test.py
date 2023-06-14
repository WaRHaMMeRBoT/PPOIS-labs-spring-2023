import obj
import roads
from roads import RailR

nodes = []
Vilnus = obj.RStat("Vilnus")
nodes.append(Vilnus)
Paris = obj.RStat("Paris")
nodes.append(Paris)
Oslo = obj.RStat("Oslo")
nodes.append(Oslo)
Moscow = obj.RStat("Moscow")
nodes.append(Moscow)
London = obj.RStat("London")
nodes.append(London)
Kiev = obj.RStat("Kiev")
nodes.append(Kiev)
Berlin = obj.RStat("Berlin")
nodes.append(Berlin)
Athens = obj.RStat("Athens")
nodes.append(Athens)

init_graph = {}
for node in nodes:
    init_graph[node] = {}

init_graph[Vilnus][Oslo] = 50
init_graph[Vilnus][London] = 40
init_graph[Oslo][Berlin] = 10
init_graph[Oslo][Moscow] = 30
init_graph[Moscow][Paris] = 40
init_graph[Moscow][Athens] = 40
init_graph[Kiev][Berlin] = 20
init_graph[Kiev][Athens] = 20

train_1 = obj.Train(40, Vilnus, [obj.Goods(Kiev, '110'), obj.Goods(Berlin, '60')])
train_2 = obj.Train(20, Kiev, [obj.Goods(Moscow, '180'), obj.Goods(Oslo, '70')])
train_3 = obj.Train(60, Moscow, [obj.Goods(London, '30'), obj.Goods(Paris, '80')])
rail: RailR = roads.RailR(nodes, init_graph, [train_1, train_2, train_3])

train_1.way_check(rail.graph)
train_2.way_check(rail.graph)
train_3.way_check(rail.graph)