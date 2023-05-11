import json
from Objects import *
from RailRoadFile import *

path = 'Data.json'


def write(railroad):
    nodes = {'nodes': []}
    for node in railroad.nodes:
        with open(path, "w", encoding="utf-8") as file:
            json.dump(node.toJSON(), file, indent=1, sort_keys=False)


def from_json(json_object):
    if 'fname' in json_object:
        return RailStation(json_object['fname'])


def read(tournaments_list):
    with open(path, "r", encoding="utf-8") as file:
        data_base = json.load(file)
    f = json.JSONDecoder(object_hook=from_json).decode('{"fname": "/foo/bar"}')
    print('a')