import pygame


class Pill(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.color_list = [(0, 0, 0), (255, 255, 255)]
        self.image = pygame.Surface((10, 10))
        self.image.fill(self.color_list[1])
        self.rect = self.image.get_rect(center=pos)
        self.counter = 0
        self.color_index = 0
        self.animation_speed = 10
