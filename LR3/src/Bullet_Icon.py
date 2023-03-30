import pygame
from pygame.math import Vector2
import random

screen_height = 600


class BulletIcon(pygame.sprite.Sprite):
    def __init__(self, position, delta_time, img_list):
        super().__init__()
        self.img_list = img_list

        self.image = self.img_list[0]
        self.rect = self.image.get_rect()
        self.rect.center = self.position = Vector2(position)
        self.velocity = Vector2(random.uniform(0.1, 0.6), random.uniform(-1.3, -0.3))
        self.acceleration = Vector2(0, 0.006)
        self.delta_t = delta_time
        self.quit_trigger = False
        self.rotate_angle = 0
        self.delta_angle = 0

    def update(self):
        if self.quit_trigger:
            self.quit_animation()

    def quit_animation(self):
        self.image = pygame.transform.rotozoom(self.img_list[1], self.rotate_angle, 1)
        self.rect = self.image.get_rect(center=self.rect.center)
        self.velocity += self.acceleration * self.delta_t
        self.position += self.velocity * self.delta_t
        self.rect.center = self.position
        self.rotate_angle += self.delta_angle * self.delta_t

        if self.rect.top >= screen_height:
            self.kill()
            self.quit_trigger = False

    def set_quit_trigger(self):
        self.quit_trigger = True
        self.rotate_angle = random.randint(-30, 30)
        self.delta_angle = random.uniform(-3, 3)
        self.image = pygame.transform.rotozoom(self.img_list[1], self.rotate_angle, 1)
        self.rect = self.image.get_rect(center=self.rect.center)

    def is_quit_trigger(self):
        return self.quit_trigger


class RenderText:
    def __init__(self, font):
        self.font = font
        self.text = None
        self.surface = None
        self.color = None

    def render(self, text, color):
        if text == self.text and color == self.color:
            return self.surface

        self.text = text
        self.color = color
        self.surface = self.font.render(text, True, color)
        return self.surface
