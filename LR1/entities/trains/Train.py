from entities.Railroad import Railroad
from entities.trains.Wagon import Wagon
from entities.stations.Station import Station
import logging
from math import ceil


class Action:
    UNLOAD = 0
    LOAD = 1
    WAIT = 2
    SKIP = 3


class Train:
    def __init__(self, name: str, power: int, railroad: Railroad) -> None:
        self.__name = name
        self.__power = power
        self.__wait_timer = 0
        self.__finished = False
        self.__path: list[int] = []
        self.__actions: list[Action] = []
        self.__location = 0
        self.__railroad = railroad
        self.__wagons: list[Wagon] = []
        self.__inited = False
        self.__travel_timer = 0
        
    def get_railroad(self) -> Railroad:
        return self.__railroad

    def get_name(self) -> str:
        return self.__name

    def get_power(self) -> int:
        return self.__power

    def travel_speed(self) -> float:
        return len(self.__wagons) * 0.1 - self.__power * 0.075 + 1.0

    def get_wait_timer(self) -> int:
        return self.__wait_timer

    def get_location(self) -> int:
        return self.__location

    def is_waiting(self) -> bool:
        return self.__wait_timer > 0

    def add_checkpoint(self, station_id: int, action: Action) -> None:
        self.__path.append(station_id)
        self.__actions.append(action)

    def add_wagon(self, wagon: Wagon) -> None:
        self.__wagons.append(wagon)

    def traverse(self) -> bool:
        looped = False
        current_index = self.__path.index(self.__location)
        if current_index >= (len(self.__path) - 1):
            return False
        else:
            next_index = current_index + 1
        self.__location = self.__path[next_index]
        return looped

    def get_station_action(self, index: int) -> Action:
        return self.__actions[self.__path.index(index)]

    def get_current_action(self) -> Action:
        return self.get_station_action(self.__location)

    def wait(self) -> None:
        self.__wait_timer -= 1
        logging.info('[%s] is waiting on station [%i], [%i] days left to wait...', self.__name, self.__location,
                     self.__wait_timer)

    def next_station(self) -> int:
        current_index = self.__path.index(self.__location)
        if current_index >= (len(self.__path) - 1):
            return -1
        else:
            next_index = current_index + 1
        return self.__path[next_index]

    def tick(self) -> None:
        if not self.__inited:
            logging.info("[%s] forwarding to station [%i]", self.__name, self.next_station())
            self.__travel_timer = self.__travel_timer = int(
                self.__railroad.direct_path_length(self.get_location(), self.next_station()) * self.travel_speed())
            self.__inited = True

        if self.is_waiting():
            self.wait()
            if not self.is_waiting():
                self.__finished = True
            return

        if not self.__finished:
            match (self.get_current_action()):
                case Action.UNLOAD:
                    for i in range(len(self.__wagons)):
                        if self.__wagons[i].can_load_into(self.__railroad.get_station(self.get_location())):
                            if self.__railroad.get_station(self.get_location()).missing_amount() > 0:
                                logging.info("[%s] performs unload operation on station [%i], wagon [%i]\t",
                                            self.__name, self.__location, i)
                                self.__wagons[i].load_into(
                                    self.__railroad.get_station(self.get_location()).missing_amount(),
                                    self.__railroad.get_station(self.__location))
                    self.__finished = True
                case Action.LOAD:
                    for i in range(len(self.__wagons)):
                        if self.__wagons[i].can_unload_from(self.__railroad.get_station(self.__location)):
                            if self.__wagons[i].missing_amount() > 0:
                                logging.info("[%s] performs load operation on station [%i], wagon [%i]\t", self.__name,
                                            self.__location, i)
                                self.__wagons[i].unload_from(self.__wagons[i].missing_amount(),
                                                            self.__railroad.get_station(self.__location))
                    self.__finished = True
                case Action.WAIT:
                    self.__wait_timer = 4
                    logging.info('[%s] is waiting on station [%i], [%i] days left to wait...', self.__name, self.__location,
                        self.__wait_timer)

        if not self.is_waiting():
            logging.info("[%s] is in travel, [%i] days left until arrival...", self.__name, self.__travel_timer)
            if self.__travel_timer <= 0:
                if self.next_station() == -1:
                    logging.info("[%s] stays at final destination, station [%i]", self.__name, self.__location)
                    return
                else:
                    self.traverse()
                    logging.info("[%s] arrived on station [%i]", self.__name, self.get_location())
                    self.__finished = False
                    self.__travel_timer = int(ceil(
                        self.__railroad.direct_path_length(self.get_location(), self.next_station()) * self.travel_speed()))
            else:
                self.__travel_timer -= 1
                return
