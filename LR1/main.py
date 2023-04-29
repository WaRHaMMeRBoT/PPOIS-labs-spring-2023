import json
from Map import Map
from JsonSerializationHandler import MapEncoder, MapDecoder
from Logic import LogicHandler


def write_to_json(map, file_name):
    map_data = json.dumps(map, cls=MapEncoder)
    with open(file_name, 'w') as file:
        file.write(map_data)


def read_from_json(file_name):
    with open(file_name, 'r') as file:
        result = file.read()
        json_result = json.loads(result)
        return MapDecoder.dict_to_object(json_result)


choice = input()
if choice == "program_use_json":
    map = read_from_json('data.json')
    map.show_map_info()
elif choice == "program_new_generation":
    print("Enter the size of map")
    size = int(input())

    print("Enter count of rabbits")
    num_of_rabbits = int(input())

    print("Enter count of wolfs")
    num_of_wolfs = int(input())
    map = Map(size, num_of_rabbits, num_of_wolfs)
    map.map_initialization()
    map.show_map_info()
else:
    print("Unknown command")
    map = None

while True:
    choice = input()
    if choice == "program_end":
        write_to_json(map, 'data.json')
        break
    elif choice == "program_add_new_animals":
        map.locate_new_animals()
        map.show_map_info()
    elif choice == "program_next_step":
        LogicHandler.do_one_step(map)
        map.change_nums_of_entities()
        map.show_map_info()
        if map.get_num_of_grass() < map.size**3:
            map.locate_new_grass()
    else:
        print("Unknown command")
