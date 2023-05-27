import pygame
from obj import Obj

class Brick(Obj):
    def __init__(self, x, y, w, h, color, special_effect=None):
        Obj.__init__(self, x, y, w, h)
        self._color = color
        self._special_effect = special_effect

    def draw(self, surface):
        pygame.draw.rect(surface, self._color, self._bounds)

    @property
    def special_effect(self):
        return self._special_effect
