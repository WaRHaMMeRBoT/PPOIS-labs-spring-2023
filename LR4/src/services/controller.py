from src.simulation import *
from src.view.view import *


class Controller:
    def __init__(self, repository: Simulation):
        self.repository = repository
        self.view = View(self)

    def get_root_view(self):
        return self.view.root

    def close_dialog(self):
        self.view.close_dialog()

    def add_item(self):
        data = self.view.dialog.content_cls.ids

        item = Item(data.name,
                    data.health,
                    data.state)

        self.repository.add_item(item)

        self.view.close_dialog()
        self.view.update_table()

    def open_add_watering(self):
        return Simulation.run('w')

    def open_add_drought(self):
        return Simulation.run('d')

    def open_add_fertiliser(self):
        return Simulation.run('f')

    def open_add_weeding(self):
        return Simulation.run('d')

    def open_add_rain(self):
        return Simulation.run('e')

    def open_add_disease(self):
        return Simulation.run('i')

    def get_items(self):
         return self.repository.to_dict()
