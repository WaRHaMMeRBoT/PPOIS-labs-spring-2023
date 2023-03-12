from .constans import Flag
from .items import Item
from typing import Optional

class Func:
    @staticmethod
    def _check_state(item: Item) -> Optional[Flag]:
        if item.health <= 0:
            return Flag.NEED_TO_DELETE
        if item.health < 20 and item.state == 'tree':
            return Flag.NEED_TO_DELETE
        if item.health >= 20:
            item.state = 'tree'
        if item.health >= 30:
            item.state = 'tree with fruits'
            return Flag.NEED_TO_CLONE
        return None

    @staticmethod
    def watering(item: Item) -> Optional[Flag]:
        item.health += 5
        return Func._check_state(item)

    @staticmethod
    def drought(item: Item) -> Optional[Flag]:
        item.health -= 5
        Func._check_state(item)
        return Func._check_state(item)

    @staticmethod
    def fertiliser(item: Item) -> Optional[Flag]:
        item.health += 5
        return Func._check_state(item)

    @staticmethod
    def weeding(item: Item) -> Optional[Flag]:
        item.health += 1
        return Func._check_state(item)

    @staticmethod
    def rain(item: Item) -> Optional[Flag]:
        item.health += 3
        return Func._check_state(item)

    @staticmethod
    def disease(item: Item) -> Optional[Flag]:
        item.health -= 4
        return Func._check_state(item)