import pygame

from lr3.constants import WIDTH, player_img, SCALE, HEIGHT, img_folder


class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.last_update = 0
        self.speedy = 0
        self.speedx = 0
        self.image = pygame.transform.scale(player_img[0], (SCALE, SCALE))
        self.rect = self.image.get_rect()
        self.rect.center = ((WIDTH / 2), HEIGHT / 1.5)
        self.iter = 0
        self.pos = 0
        self.eat_effect = pygame.mixer.Sound(img_folder+'/pacman.wav')

    def keystatments(self):
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT]:
            self.speedx = -8
            self.speedy = 0
            self.pos = 180
        if keystate[pygame.K_RIGHT]:
            self.speedx = 8
            self.speedy = 0
            self.pos = 0
        if keystate[pygame.K_DOWN]:
            self.speedy = 8
            self.speedx = 0
            self.pos = 270
        if keystate[pygame.K_UP]:
            self.speedy = -8
            self.speedx = 0
            self.pos = 90

    def borders(self):
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT
        if self.rect.bottom < self.rect.height:
            self.rect.bottom = self.rect.height

    def ticking(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > 60:
            self.last_update = now
            self.image = pygame.transform.rotate(player_img[self.iter], self.pos)
            self.image = pygame.transform.scale(self.image, (SCALE, SCALE))
        if self.iter >= 2:
            self.iter = 0
        else:
            self.iter += 1

    def update(self):

        self.ticking()
        self.keystatments()
        self.borders()
        self.rect.x += self.speedx
        self.rect.y += self.speedy

