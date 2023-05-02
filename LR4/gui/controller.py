
import sys
import os
sys.path.insert(1, os.path.join(sys.path[0], '..'))

from gui.view import View
from gui.model import Model

import garden


class Controller:
    def __init__(self, app_object, garden) -> None:
        self.model = Model(garden)
        self.garden = garden
        self.view = View(self, app_object, garden)
        self.model.init_view(self.view)
        self.delete_student_list = []
        
    
    def get_root_view(self):
        return self.view.base_view
    
    def get_garden(self):
        return self.model.garden_list
    
    def add_new_garden_bed(self):
        self.garden.garden.add_garden_bed()
        self.model.update_table()
        self.view.update_table()
    
    def show_garden_general_data(self):
        self.view.show_general_data_dialog()

    def close_ganeral_data(self):
        self.view.close_general_info_dialog()

    def next_garden_step(self):
        self.garden.next_step()
        self.model.update_table()
        self.view.update_table()

    def take_garden_harvest(self):
        for i in range(len(self.garden.garden.garden)):
            if self.garden.garden.garden[i].type != '0':
                self.garden.garden.garden[i].take_harvest()
                self.garden.garden.harvest(i)
        self.model.update_table()
        self.view.update_table()
        
    def add_new_plant(self):
        self.view.add_new_dialog()
        
    def close_add_window(self):
        self.view.add_new_entity.dismiss()
        
    def add_plant_in_table(self):
        self.close_add_window()
        
        data_from_add_dialog_window = self.view.add_new_entity.content_cls.ids
        self.garden.garden.garden[int(data_from_add_dialog_window.gardenbed.text)] = garden.GardenBed(data_from_add_dialog_window.name.text,
                                                                                                      data_from_add_dialog_window.product_name.text,
                                                                                                      data_from_add_dialog_window.type.text)
        self.garden.garden.garden[int(data_from_add_dialog_window.gardenbed.text)].plant()
        self.model.update_table()
        self.view.update_table()
        
    def open_action_window(self):
        self.view.launch_action_window()
        
    def close_action_window(self):
        self.view.action_window.dismiss()
    
    def action_window(self):
        self.close_action_window()
        data = self.view.action_window.content_cls.ids 
        gardenbed = int(data.gardenbed.text)
        action = data.actions.text
        if action == 'удалить грядку':
            self.garden.garden.delete_garden_bed(gardenbed)
        elif action == 'удобрить грядку':
            self.garden.garden.fertilizer.save(self.garden.garden.garden[gardenbed])
            self.garden.garden.fertilizer.fertilize()
        elif action == 'полить грядку':
            self.garden.garden.watering.save(self.garden.garden.garden[gardenbed], self.garden.garden.weather)
            self.garden.garden.watering.water()
        elif action == 'вылечить грядку':
            self.garden.garden.disease.save(self.garden.garden.garden[gardenbed])
            self.garden.garden.disease.treat()
        elif action == 'уничтожить вредителей':
            self.garden.garden.pests.save(self.garden.garden.garden[gardenbed])
            self.garden.garden.pests.kill_pests()
        elif action == 'прополоть грядку':
            self.garden.garden.weed.save(self.garden.garden.garden[gardenbed])
            self.garden.garden.weed.weed()
        
        self.model.update_table()
        self.view.update_table()
    
        
            
   