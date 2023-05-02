from typing import *
import json
from garden import *


def create_data_for_file(garden_list: List[object], weather: object) -> None:
    '''Функция для сохранения данных в json файл.'''
    data: List[Dict[str, object]] = []

    for i in garden_list:
        if i.type != '0':
            data.append({
                'name': i.name,
                'type': i.type,
                'product_name': i.plant_data.product.product_data[1],
                'amount_product': i.plant_data.product.product_data[0],
                'health': i.plant_data.health,
                'water_lavel': i.plant_data.water_lavel,
                'die': i.die,
                'inside_step': i.step,
                'state': i.get_state
            })
        else:
            data.append({
                'name': i.name,
                'type': i.type,
                'product_name': '0',
            })

    data.append({
        'weather': weather.get_name,
        'weather_days': weather.get_days
    })

    with open('garden.json', 'w', ) as file:
        json.dump(data, file, ensure_ascii=False, indent=4)


def load_from_file(object: Garden) -> None:
    '''Фукнци, которая загружает и восстанавливает состаяния сущностей сада.'''
    with open('/home/konstantin/ppois/lab1/garden.json', 'r') as file:
        data: List[Dict[str, object]] = json.load(file)

    for i in data:
        if not i.get('weather'):
            if i.get('type') != '0':
                object.add_garden_bed()
                object.garden[-1]: GardenBed = GardenBed(
                    i.get('name'), i.get('product_name'), i.get('type'))
                object.garden[-1].plant()
                object.garden[-1].die: bool = i.get('die')
                object.garden[-1].plant_data.load_health(i.get('health'))
                object.garden[-1].plant_data.water_lavel: int = i.get(
                    'water_lavel')
                object.garden[-1].plant_data.product.product_data: int = i.get(
                    'amount_product')
                object.garden[-1].get_state: List[str] = i.get('state')
                object.garden[-1].step: int = i.get('inside_step')
                object.harvest(-1)
            else:
                object.add_garden_bed()
    if data[-1].get('weather') == 'солнце':
        object.weather: Weather = Sun()
    else:
        object.weather: Weather = Rain()

    object.weather.get_days: int = data[-1].get('weather_days')
