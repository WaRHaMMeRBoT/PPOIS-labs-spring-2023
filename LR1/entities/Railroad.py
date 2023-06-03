import logging

from entities.stations.Station import Station
from entities.stations.MixedStation import MixedStation
from utility.Types import ContentType


def refill_station(index: int, station: Station):
    if station.amount < station.get_capacity():
        refill = int(station.get_capacity() * 0.075)
        adj = station.change_amount(refill)
        logging.info("Station {0} refilled by {1} resource points, current amount {2}".format(index, refill,
                                                                                              station.amount))


def refill_mixed(index: int, station: MixedStation):
    if station.amount < station.get_full_capacity():
        refill_pass = int(station.get_capacity() * 0.075)
        refill_cargo = int(station.get_capacity_cargo() * 0.075)
        adj_cargo = station.change_amount_cargo(refill_cargo)
        adj_pass = station.change_amount(refill_pass)
        logging.info("Station {0} refilled by {1} resource points, current amount {2} = Cargo {3} + "
                     "Passenger {4}".format(index, refill_pass + refill_cargo, station.get_full_amount(),
                                           station.get_amount_cargo(), station.get_amount()))


class Railroad:
    def __init__(self) -> None:
        self.__graph: list[list[tuple[int, int]]] = []
        self.__stations: list[Station] = []

    def get_graph(self) -> list[list[tuple[int, int]]]:
        return self.__graph

    def get_stations(self) -> list[Station]:
        return self.__stations

    def push_line(self, node: list[tuple[int, int]]) -> None:
        self.__graph.append(node)

    def add_edge(self, u: int, v: int, w: int = 0) -> None:
        self.get_graph()[u].append((v, w))
        self.get_graph()[v].append((u, w))

    def add_station(self, station: Station) -> None:
        self.__stations.append(station)

    def set_station(self, index: int, station: Station) -> None:
        self.__stations[index] = station

    def get_station(self, index: int) -> Station:
        return self.__stations[index]

    def direct_path_length(self, u: int, v: int):
        neighbours = self.__graph[u]
        for t in neighbours:
            if t[0] == v:
                return t[1]
        return -1

    def direct_path_exists(self, u: int, v: int) -> bool:
        return self.direct_path_length(u, v) != -1

    def tick(self):
        for i in range(len(self.__stations)):
            station = self.__stations[i]
            if station.get_type() == ContentType.MIXED:
                refill_mixed(i, station)
            else:
                refill_station(i, station)
