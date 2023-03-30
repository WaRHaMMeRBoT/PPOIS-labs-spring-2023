import pygame
import toolbox
import math
import image_util

class Bullet(pygame.sprite.Sprite):
    def __init__(self, screen, x, y, angle, damage, speed):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.screen = screen
        self.x = x
        self.y = y
        self.angle = angle
        self.image = pygame.image.load(image_util.getImage("bullet.png"))
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)
        self.image, self.rect = toolbox.getRotatedImage(self.image, self.rect, self.angle)
        self.speed = speed
        self.angle_rads = math.radians(self.angle)
        self.x_move = math.cos(self.angle_rads) * self.speed
        self.y_move = -math.sin(self.angle_rads) * self.speed
        self.damage = damage

    def update(self):
        self.x += self.x_move
        self.y += self.y_move

        self.rect.center = (self.x, self.y)

        if self.x < -self.image.get_width():
            self.kill()
        elif self.x > self.screen.get_width() + self.image.get_width():
            self.kill()
        elif self.y < -self.image.get_height():
            self.kill()
        elif self.y > self.screen.get_height() + self.image.get_height():
            self.kill()

        self.screen.blit(self.image, self.rect)


    def explode(self):
        self.kill()