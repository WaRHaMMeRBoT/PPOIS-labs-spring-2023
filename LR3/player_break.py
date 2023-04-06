# Author Vodohleb04
from typing import NoReturn

import pygame
import config_controller
from my_sprite import MySprite


class Paddle(MySprite):
    def __init__(self, config_controller: config_controller.ConfigController, x, y, w, h, color, offset):
        MySprite.__init__(self, x, y, w, h)
        self._color = color
        self._offset = offset
        self.speed = self._offset, 0
        self._moving_left = False
        self._moving_right = False
        self.screen_width = config_controller.screen_width
        self._aceleration = 2 * config_controller.bowl_acceleration

    def accelerate(self) -> NoReturn:
        self.speed = self.speed[0] + self._aceleration, self.speed[1]

    def base_speed(self) -> NoReturn:
        self.speed = self._offset, 0

    def draw(self, surface) -> NoReturn:
        pygame.draw.rect(surface, self._color, self._bounds)

    def handle(self, key) -> NoReturn:
        if key == pygame.K_LEFT:
            self._moving_left = not self._moving_left
        else:
            self._moving_right = not self._moving_right

    def update(self) -> NoReturn:
        if self._moving_left:
            x_shift = -(min(self._offset, self.left))
        elif self._moving_right:
            x_shift = min(self._offset, self.screen_width - self.right)
        else:
            return
        self.move(x_shift, 0)

    @property
    def moving_left(self) -> bool:
        return self._moving_left

    @property
    def moving_right(self) -> bool:
        return self._moving_right
