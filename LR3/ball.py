import random
import pygame
from obj import Obj

class Ball(Obj):
    def __init__(self, x, y, radius, color, speed, acceleration):
        Obj.__init__(self, x - radius, y - radius, radius * 2, radius * 2, speed)
        self.radius = radius
        self.diameter = radius * 2
        self._color = color
        self._acceleration = acceleration
        
    def draw(self, surface):
        pygame.draw.circle(surface, self._color, self.center, self.radius)

    def update(self):
        super().update()

    def _zero_speed_case(self):
        new_x_speed = 0
        new_y_speed = 0
        if self._speed[0] == 0:
            sign = random.randint(0, 1)
            new_x_speed = (-1) ** sign * self._acceleration
            if self._speed[1] != 0:
                new_y_speed = (abs(self._speed[1]) + self._acceleration) * (self.speed[1] / abs(self._speed[1]))
        if self._speed[1] == 0:
            sign = random.randint(0, 1)
            new_y_speed = (-1) ** sign * self._acceleration
            if self._speed[1] != 0:
                new_x_speed = (abs(self._speed[0]) + self._acceleration) * (self.speed[0] / abs(self._speed[0]))
        return new_x_speed, new_y_speed

    def accelerate(self):
        new_x_speed = 0
        new_y_speed = 0
        zero_flag = False
        if 0 in self._speed:
            zero_flag = True
            new_x_speed, new_y_speed = self._zero_speed_case()
        if not zero_flag:
            new_x_speed = (abs(self._speed[0]) + self._acceleration) * (self.speed[0] / abs(self._speed[0]))
            new_y_speed = (abs(self._speed[1]) + self._acceleration) * (self.speed[1] / abs(self._speed[1]))
        self.speed = new_x_speed, new_y_speed

    @property
    def speed(self):
        return self._speed

    @speed.setter
    def speed(self, new_speed):
        self._speed = new_speed
        if self._speed[1] == 0:
            self._speed = self._speed[0], self._speed[1] + self._acceleration
