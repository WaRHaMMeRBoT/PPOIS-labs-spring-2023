import random

import pygame

from constants import SCALE
from LR3.lab.pacman import Player


class StaticGhost(pygame.sprite.Sprite):
    def __init__(self, ghost_img, pos: tuple, walls):
        pygame.sprite.Sprite.__init__(self)
        random.seed(version=2)
        self.last_update = 0
        self.speedy = 0
        self.speedx = 0
        self.direction = "up"
        self.left_ghost_img = [ghost_img[0], ghost_img[1]]
        self.right_ghost_img = [ghost_img[0], ghost_img[1]]
        self.down_ghost_img = [ghost_img[0], ghost_img[1]]
        self.up_ghost_img = [ghost_img[0], ghost_img[1]]
        self.image = pygame.transform.scale(ghost_img[0], (SCALE, SCALE))
        self.rect = self.image.get_rect()
        self.rect.center = pos
        self.walls = walls
        self.last_dir = "left"
        self.iter = 0
        self.pos = 0

    def random_direction(self):

        match random.randint(0, 3):
            case 0:
                if self.direction != "right" and self.direction == "up" or self.direction == "down":
                    self.direction = "left"
            case 1:
                if self.direction != "left" and self.direction == "up" or self.direction == "down":
                    self.direction = "right"
            case 2:
                if self.direction != "up" and self.direction == "left" or self.direction == "right":
                    self.direction = "down"
            case 3:
                if self.direction != "down" and self.direction == "left" or self.direction == "right":
                    self.direction = "up"

    def find_walls(self) -> bool:
        for i in self.walls:
            if self.rect.colliderect(i.rect):
                return False
        return True

    def ticking(self):
        pass

    def find_pacman(self, pacman: Player):

        pass

    def update(self):

        self.ticking()

