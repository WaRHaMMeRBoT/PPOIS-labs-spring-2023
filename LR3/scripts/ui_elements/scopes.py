import pygame
import math
import scripts.configs as cf
from typing import Any


class Cross(pygame.sprite.Sprite):
    def __init__(self, group):
        super(Cross, self).__init__()
        self.add(group)
        self.__image = pygame.image.load(cf.UI_SPRITES_IMG['cursor']).convert_alpha()
        self.__image = pygame.transform.smoothscale(self.__image, (int(cf.SCREEN_WIDTH * 0.02),
                                                                   int(cf.SCREEN_WIDTH * 0.02)))
        self.__rect = self.__image.get_rect()

    @property
    def image(self):
        return self.__image

    @property
    def rect(self):
        return self.__rect

    def update(self, *args: Any, **kwargs: Any) -> None:
        self.__rect.center = kwargs['mouse_pos']


class Sight(pygame.sprite.Sprite):
    def __init__(self, group, sight_speed: int):
        super(Sight, self).__init__()
        self.add(group)
        self.image = pygame.image.load(cf.UI_SPRITES_IMG['sight']).convert_alpha()
        self.image = pygame.transform.smoothscale(self.image, (int(cf.SCREEN_WIDTH * 0.10),
                                                               int(cf.SCREEN_HEIGHT * 0.10)))
        self.rect = self.image.get_rect(center=(cf.SCREEN_WIDTH // 2, cf.SCREEN_HEIGHT // 2))
        self.sight_speed = sight_speed

    def update(self, *args: Any, **kwargs: Any) -> None:
        delta_x = kwargs['mouse_pos'][0] - self.rect.centerx
        delta_y = kwargs['mouse_pos'][1] - self.rect.centery
        if abs(delta_x) > cf.SCREEN_WIDTH % 11 or abs(delta_y) > cf.SCREEN_WIDTH % 11:
            angle = math.atan2(delta_x, delta_y)
            move_x = self.sight_speed * math.sin(angle)
            move_y = self.sight_speed * math.cos(angle)
            self.rect.center = (self.rect.centerx + move_x, self.rect.centery + move_y)
        else:
            self.rect.center = kwargs['mouse_pos']
