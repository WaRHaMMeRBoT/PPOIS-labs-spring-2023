import pygame as pg

from entity import Entity
from const import *


class Spikes(Entity):
    def __init__(self, x_pos, y_pos):
        super().__init__()
        self.rect = pg.Rect(x_pos, y_pos, 32, 32)
        self.xVel = 0
        self.crushed = False
        self.image_tick = 0
        self.image = pg.image.load('images/spikes.png').convert_alpha()

    def check_collision_with_player(self, core):
        if self.collision:
            if self.rect.colliderect(core.get_map().get_player().rect):
                if core.get_map().get_player().xVel > 0 or core.get_map().get_player().xVel < 0:
                    core.get_map().get_player().xVel = 0
                if self.state != -1:
                    if core.get_map().get_player().yVel > 0:
                        if not core.get_map().get_player().unkillable:
                            core.get_map().get_player().set_powerlvl(0, core)

    def update_image(self):
        self.image_tick += 1
        if self.image_tick == 14:
            self.current_image = 1
        elif self.image_tick == 28:
            self.current_image = 0
            self.image_tick = 0

    def update(self, core):
        if self.state == 0:
            self.update_image()
            if not self.on_ground:
                self.yVel += GRAVITY
            blocks = core.get_map().get_blocks_for_collision(int(self.rect.x // 32), int(self.rect.y // 32))
            self.update_x_pos(blocks)
            self.update_y_pos(blocks)
            self.check_map_borders(core)
        elif self.state == -1:
            if self.crushed:
                self.image_tick += 1
                if self.image_tick == 50:
                    core.get_map().get_mobs().remove(self)
            else:
                self.yVel += GRAVITY
                self.rect.y += self.yVel
                self.check_map_borders(core)

    def render(self, core):
        core.screen.blit(self.image, core.get_map().get_camera().apply(self))
