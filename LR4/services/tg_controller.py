from view.telegram_view import TelegramView
from services.base_controller import *


class TelegramController:
    def __init__(self):
        self.base_controller = BaseController()
        self.view = TelegramView(self)

    def add_entity(self, data: str) -> None:
        entity_with_pos = data.split()

        entity = entity_with_pos[0]
        position = (entity_with_pos[1], entity_with_pos[2])

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

    def play(self):
        self.base_controller.play()

