import pygame as pg

from entity import Entity
from const import *


class Spike(Entity):
    def __init__(self, x_pos, y_pos):
        super().__init__()
        self.image = pg.image.load('images/spikes.png').convert_alpha()
        self.rect = pg.Rect(x_pos, y_pos, 32, 32)

    def check_collision_with_player(self, core):
        if self.collision:
            if self.rect.colliderect(core.get_map().get_player().rect):
                if self.state != -1:
                    if core.get_map().get_player().yVel > 0:
                        if not core.get_map().get_player().unkillable:
                            core.get_map().get_player().set_powerlvl(0, core)

    def render(self, core):
        core.screen.blit(self.image, core.get_map().get_camera().apply(self))
