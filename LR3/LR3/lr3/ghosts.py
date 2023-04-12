import random

import pygame

from constants import SCALE
from player import Player


class Ghost(pygame.sprite.Sprite):
    def __init__(self, ghost_img, pos: tuple, walls):
        pygame.sprite.Sprite.__init__(self)
        random.seed(version=2)
        self.last_update = 0
        self.speedy = 0
        self.speedx = 0
        self.direction = "up"
        self.left_ghost_img = [ghost_img[2], ghost_img[3]]
        self.right_ghost_img = [ghost_img[4], ghost_img[5]]
        self.down_ghost_img = [ghost_img[0], ghost_img[1]]
        self.up_ghost_img = [ghost_img[6], ghost_img[7]]
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
        now = pygame.time.get_ticks()
        if self.iter > 1:
            self.iter = 0
        if now - self.last_update > 60:
            self.last_update = now
            match self.direction:
                case "left":
                    self.image = pygame.transform.rotate(self.left_ghost_img[self.iter], self.pos)
                    self.speedx = -4
                    self.speedy = 0
                case "right":
                    self.image = pygame.transform.rotate(self.right_ghost_img[self.iter], self.pos)
                    self.speedx = 4
                    self.speedy = 0
                case "up":
                    self.image = pygame.transform.rotate(self.up_ghost_img[self.iter], self.pos)
                    self.speedx = 0
                    self.speedy = -4
                case "down":
                    self.image = pygame.transform.rotate(self.down_ghost_img[self.iter], self.pos)
                    self.speedx = 0
                    self.speedy = 4

            self.image = pygame.transform.scale(self.image, (SCALE, SCALE))
            self.iter += 1

    def find_pacman(self, pacman: Player):

        for i in range(1, 25):
            if self.rect.x + i == pacman.rect.x and (1 <= abs(self.rect.y - pacman.rect.y) <= 5):
                self.last_dir = self.direction
                self.direction = "up"
            elif self.rect.x - i == pacman.rect.x and (1 <= abs(self.rect.y - pacman.rect.y) <= 5):
                self.last_dir = self.direction
                self.direction = "down"

            elif self.rect.y + i == pacman.rect.y and (1 <= abs(self.rect.x - pacman.rect.x) <= 5):
                self.last_dir = self.direction
                self.direction = "left"

            elif self.rect.y - i == pacman.rect.y and (1 <= abs(self.rect.x - pacman.rect.x) <= 5):
                self.last_dir = self.direction
                self.direction = "right"
            else:
                self.ticking()

    def update(self):

        self.ticking()

        self.rect.x += self.speedx
        self.rect.y += self.speedy
