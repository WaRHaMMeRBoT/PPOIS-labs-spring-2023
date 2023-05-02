from typing import *
import sys
import os

sys.path.insert(1, os.path.join(sys.path[0], '..'))
import create_and_update_file

class Model:
    def __init__(self, garden) -> None:
        create_and_update_file.load_from_file(garden.garden)
        self.garden = garden
        self.garden_list: Dict[List] = self.create_table_lines(self.garden)
    
    def create_table_lines(self, garden):
        data = garden.garden.garden
        table = list()
        for i in data:
            if i.type != '0':
                table.append([i.name,
                              i.plant_data.health,
                              i.plant_data.water_lavel,
                              i.get_state['Вредители'],
                              i.get_state['Сорняки'],
                              i.get_state['Засыхает'],
                              i.get_state['Болезни'],
                              i.get_state['Урожай']])
            else:
                table.append([0, 0, 0, 0, 0, 0, 0, 0])
        return table
    
    def update_table(self):
        create_and_update_file.create_data_for_file(self.garden.garden.garden, self.garden.garden.weather)
        self.garden.garden.garden.clear()
        create_and_update_file.load_from_file(self.garden.garden)
        self.garden_list: Dict[List] = self.create_table_lines(self.garden)

    def init_view(self, view):
        self.view = view