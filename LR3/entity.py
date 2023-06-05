import pygame as pg
from const import *


class Entity(object):
    def __init__(self):
        self.state = 0
        self.xVel = 0
        self.yVel = 0
        self.move_direction = True
        self.on_ground = False
        self.collision = True
        self.image = None
        self.rect = None

    def update_x_pos(self, blocks):
        self.rect.x += self.xVel
        for block in blocks:
            if block != 0 and block.type != 'BGObject':
                if pg.Rect.colliderect(self.rect, block.rect):
                    if self.xVel > 0:
                        self.rect.right = block.rect.left
                        self.xVel = - self.xVel
                    elif self.xVel < 0:
                        self.rect.left = block.rect.right
                        self.xVel = - self.xVel

    def update_y_pos(self, blocks):
        self.rect.y += self.yVel * FALL_MULTI
        self.on_ground = False
        for block in blocks:
            if block != 0 and block.type != 'BGObject':
                if pg.Rect.colliderect(self.rect, block.rect):
                    if self.yVel > 0:
                        self.on_ground = True
                        self.rect.bottom = block.rect.top
                        self.yVel = 0

    def check_map_borders(self, core):
        if self.rect.y >= 448:
            self.die(core, True, False)
        if self.rect.x <= 1 and self.xVel < 0:
            self.xVel = - self.xVel

    def die(self, core, instantly, crushed):
        pass

    def render(self, core):
        pass
