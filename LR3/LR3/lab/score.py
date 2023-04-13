import pygame


class Score(pygame.sprite.Sprite):
    def __init__(self, engine):
        pygame.sprite.Sprite.__init__(self)
        self.engine = engine
        self.image = engine.font.render("Score: " + str(self.engine.score), True, (255, 255, 255))
        self.rect = self.image.get_rect()
        self.rect.center = (100, 40)

    def update(self):
        self.image = self.engine.font.render("Score: " + str(self.engine.score), True, (255, 255, 255))
