import pygame
import config_controller
from obj import Obj

class Paddle(Obj):
    def __init__(self, config_controller: config_controller.ConfigController, x, y, w, h, color, offset):
        Obj.__init__(self, x, y, w, h)
        self._color = color
        self._offset = offset
        self.speed = self._offset, 0
        self._moving_left = False
        self._moving_right = False
        self.screen_width = config_controller.screen_width
        self._aceleration = 2 * config_controller.ball_acceleration

    def accelerate(self):
        self.speed = self.speed[0] + self._aceleration, self.speed[1]

    def base_speed(self):
        self.speed = self._offset, 0

    def draw(self, surface):
        pygame.draw.rect(surface, self._color, self._bounds)

    def handle(self, key):
        if key == pygame.K_LEFT:
            self._moving_left = not self._moving_left
        else:
            self._moving_right = not self._moving_right

    def update(self):
        if self._moving_left:
            x_shift = -(min(self._offset, self.left))
        elif self._moving_right:
            x_shift = min(self._offset, self.screen_width - self.right)
        else:
            return
        self.move(x_shift, 0)

    @property
    def moving_left(self):
        return self._moving_left

    @property
    def moving_right(self):
        return self._moving_right
