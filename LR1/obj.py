import sys


def dijkstra_algorithm(graph, start_node):
    unvisited_nodes = list(graph.get_nodes())
    shortest_path = {}
    previous_nodes = {}
    max_value = sys.maxsize
    for node in unvisited_nodes:
        shortest_path[node] = max_value
    shortest_path[start_node] = 0
    while unvisited_nodes:
        current_min_node = None
        for node in unvisited_nodes:
            if current_min_node is None:
                current_min_node = node
            elif shortest_path[node] < shortest_path[current_min_node]:
                current_min_node = node
        neighbors = graph.get_outgoing_edges(current_min_node)
        for neighbor in neighbors:
            tentative_value = shortest_path[current_min_node] + graph.value(current_min_node, neighbor)
            if tentative_value < shortest_path[neighbor]:
                shortest_path[neighbor] = tentative_value
                previous_nodes[neighbor] = current_min_node
        unvisited_nodes.remove(current_min_node)
    return previous_nodes, shortest_path


class Goods:
    def __init__(self, target_point, goods=[]):
        self.goods = goods
        self.target_point = target_point

    def action(self):
        pass

    def append_good(self, good):
        self.goods.append(good)


class Storage:
    def __init__(self):
        storage_goods = []
        self.storage_goods = storage_goods

    def set_goods(self, goods):
        self.storage_goods.append(goods)

    def get_goods(self):
        return self.storage_goods.pop(0)

    def action(self):
        pass


class RStat:
    def __init__(self, name=''):
        self.name = name
        storage = Storage()
        self.storage = storage

    def set_storage(self, good):
        self.storage.set_goods(good)

    def action(self):
        pass


class Train:
    def __init__(self, speed=0, start_point=RStat(), goods=[]):
        self.goods = goods
        if not goods:
            self.target_point = RStat()
        else:
            self.target_point = goods[0].target_point
        self.current_point = start_point
        self.speed = speed
        self.distance = 0

    def way_check(self, graph):
        previous_nodes, shortest_path = dijkstra_algorithm(graph, self.current_point)
        if shortest_path[self.target_point] == 9223372036854775807:
            return False
        self.distance = shortest_path[self.target_point]
        return True

    def action(self):
        pass

    def move(self):
        self.distance -= self.speed
        if not self.goods:
            return False
        if self.distance <= 0:
            self.distance = 0
            self.current_point = self.target_point
            return True
        return False

    def get_goods(self):
        return self.goods.pop(0)

    def append_goods(self, good):
        self.goods.append(good)

    def set_speed(self, speed):
        self.speed = speed


class Semaphore:
    def __init__(self):
        self.signal = True

    def action(self):
        pass


class RailroadCrossing:
    def __init__(self):
        pass
