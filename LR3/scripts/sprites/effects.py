import pygame
from typing import Any
import scripts.configs as cf
import random


class Explosion(pygame.sprite.Sprite):
    def __init__(self, group, spawn_x, spawn_y, owner_rect):
        super(Explosion, self).__init__()
        self.add(group)
        self.frames = []
        animation_frames_path = cf.EFFECTS_IMG['explosion']
        random_size_coef = random.uniform(1.2, 1.4)
        for frame in animation_frames_path:
            image = pygame.image.load(frame)
            image = pygame.transform.smoothscale(image, (int(owner_rect.w / random_size_coef),
                                                         int(owner_rect.w / random_size_coef)))
            self.frames.append(image)
        self.index = 0
        self.image = self.frames[self.index % len(self.frames)]
        self.rect = self.image.get_rect(center=(spawn_x, spawn_y))
        self.counter = 0

    def update(self, *args: Any, **kwargs: Any) -> None:
        animation_speed = 4
        self.counter += 1
        if self.counter >= animation_speed:
            self.counter = 0
            self.index += 1
            self.image = self.frames[self.index % len(self.frames)]

        if self.index >= len(self.frames):
            self.kill()
