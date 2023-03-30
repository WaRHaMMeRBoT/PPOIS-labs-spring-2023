import pygame
from manager import Background
import image_util, toolbox

class Blood(pygame.sprite.Sprite):
    def __init__(self, screen, x, y):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.screen = screen
        self.x = x
        self.y = y

        self.image = pygame.image.load(image_util.getImage("blood.png"))
        self.image = pygame.transform.scale(self.image, (55,55))

        self.rect = self.image.get_rect()
        self.rect.center = [self.x, self.y]

    def update(self):
        self.rect.center = [self.x - Background.display_scroll[0], self.y - Background.display_scroll[1]]

        image_to_draw, image_rect = toolbox.getRotatedImage(self.image, self.rect, 0)
        self.screen.blit(image_to_draw, image_rect)


