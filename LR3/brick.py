# Author Vodohleb04
from typing import NoReturn

import pygame

from my_sprite import MySprite


class Brick(MySprite):
    def __init__(self, x, y, w, h, color, special_effect=None):
        MySprite.__init__(self, x, y, w, h)
        self._color = color
        self._special_effect = special_effect

    def draw(self, surface) -> NoReturn:
        pygame.draw.rect(surface, self._color, self._bounds)

    @property
    def special_effect(self):
        return self._special_effect
