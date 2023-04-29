from Map import Map, Cell
from Wolf import Wolf
from Rabbit import Rabbit
from Grass import Grass
import json


class MapEncoder(json.JSONEncoder):

    def default(self, obj):
        if isinstance(obj, Map):
            return {'size': obj.size,
                    'cells': obj.cells,
                    'num_of_rabbits': obj.num_of_rabbits,
                    'num_of_wolfs': obj.num_of_wolfs,
                    'num_of_grass': obj.num_of_grass}
        elif isinstance(obj, Cell):
            return {'x': obj.x,
                    'y': obj.y,
                    'rabbits': obj.rabbits,
                    'wolfs': obj.wolfs,
                    'grass': obj.grass,
                    'entities': obj.entities,
                    'num_of_wolfs': obj.num_of_wolfs,
                    'num_of_grass': obj.num_of_grass,
                    'num_of_rabbits': obj.num_of_rabbits,
                    'num_of_entities': obj.num_of_entities}
        elif isinstance(obj, Rabbit):
            return {'x': obj.x,
                    'y': obj.y,
                    'age': obj.age,
                    'gender': obj.gender,
                    'saturation': obj.saturation,
                    'max_age': obj.max_age,
                    'max_saturation': obj.max_saturation}
        elif isinstance(obj, Wolf):
            return {'x': obj.x,
                    'y': obj.y,
                    'age': obj.age,
                    'gender': obj.gender,
                    'saturation': obj.saturation,
                    'max_age': obj.max_age,
                    'max_saturation': obj.max_saturation}
        elif isinstance(obj, Grass):
            return {'x': obj.x,
                    'y': obj.y,
                    'age': obj.age,
                    'max_age': obj.max_age}
        else:
            return json.JSONEncoder.default(self, obj)


class MapDecoder:
    @staticmethod
    def dict_to_object(dct):
        cell_objs = []
        if 'size' in dct:
            for row in dct['cells']:
                cell_row = []

                for cell_dict in row:
                    cell = Cell(cell_dict['x'], cell_dict['y'], cell_dict['num_of_wolfs'],
                                cell_dict['num_of_rabbits'], cell_dict['num_of_grass'])
                    cell.rabbits = [Rabbit(rabbit_dict['x'], rabbit_dict['y']) for rabbit_dict in cell_dict['rabbits']]
                    cell.wolfs = [Wolf(wolf_dict['x'], wolf_dict['y']) for wolf_dict in cell_dict['wolfs']]
                    cell.grass = [Grass(grass_dict['x'], grass_dict['y']) for grass_dict in cell_dict['grass']]
                    cell_row.append(cell)
                cell_objs.append(cell_row)

            map_obj = Map(dct['size'], dct['num_of_rabbits'], dct['num_of_wolfs'], dct['num_of_grass'])
            map_obj.cells = cell_objs
            return map_obj
