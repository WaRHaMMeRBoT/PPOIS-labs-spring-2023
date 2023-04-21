from view.view import *
from services.base_controller import *


class Controller:
    def __init__(self):
        self.base_controller = BaseController()
        self.view = View(self)

    def get_root_view(self):
        return self.view.root

    def close_dialog(self):
        self.view.close_dialog()

    def open_add_dialog(self):
        self.view.open_add_dialog()

    def add_entity(self):
        data = self.view.dialog.content_cls.ids

        entity = data.entity.text
        position = (data.pos_x.text, data.pos_y.text)

        if entity == 'Wolf':
            entity = Wolf()
        if entity == 'Fox':
            entity = Fox()
        if entity == 'Bear':
            entity = Bear()
        if entity == 'Deer':
            entity = Deer()
        if entity == 'Rabbit':
            entity = Rabbit()
        if entity == 'Plant':
            entity = Plant()

        self.base_controller.add(entity=entity, x=int(position[0]), y=int(position[1]))

        self.view.update_table()
        self.view.close_dialog()

    def open_warp_dialog(self):
        self.view.open_warp_dialog()

    def warp(self):
        data = self.view.dialog.content_cls.ids
        size = int(data.size.text)

        self.base_controller.create_new_game_board(size)

        self.view.update_table()
        self.view.close_dialog()

    def play(self):
        self.base_controller.play()
        self.view.update_table()
        self.view.close_dialog()
