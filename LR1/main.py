import Commands
import RailRoadFile


def work():
    railroad = [RailRoadFile.RailRoad([], {}, [])]
    while True:
        session_ended = Commands.get_command(railroad)
        if session_ended:
            break


work()
