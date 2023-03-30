import pygame, pygame.gfxdraw, math
from wave import Wave
from game import *
import  menu

class WaveController:
    def __init__(self, screen, maxX, maxY, *groups):
        self.wave_number = 0
        self.screen = screen
        self.groups = groups
        self.amount = 8
        self.maxX = maxX
        self.maxY = maxY

        self.wave_cd_max = 540
        self.wave_cd = 0

    def new_wave(self, target):
        self.wave_cd = 0
        self.wave_number += 1
        wave = Wave(self.get_types(), self.screen, self.amount, self.maxX, self.maxY, self.groups)
        wave.start_wave(target)
        self.amount += 1

    def get_types(self):
        types = [ ]
        if self.wave_number >= 1:
            types.append("walker")
            types.append("crawler")
        if self.wave_number > 5:
            types.append("brute")
        if self.wave_number > 10:
            types.append("spider")
        if self.wave_number > 15:
            types.append("runner")
        if self.wave_number > 20:
            types.append("motorcycle")
        if self.wave_number > 25:
            types.append("helicopter")
        return types

    def draw_timer(self, screen, x: int, y: int):
        wave_percentage = int(self.wave_cd / self.wave_cd_max * 359)
        seconds = (self.wave_cd_max - self.wave_cd) / 60
        menu.print_text("0" + str(math.ceil(seconds)), x - 14, y - 10, font_clr=(255, 255, 255),font_type='Qore.otf', font_size=17)

        pygame.gfxdraw.arc(screen, x, y, 23, -90, wave_percentage - 90, (255, 255, 255))
        pygame.gfxdraw.arc(screen, x, y, 24, -90, wave_percentage - 90, (255, 255, 255))
        pygame.gfxdraw.arc(screen, x, y, 25, -90, wave_percentage - 90, (255, 255, 255))