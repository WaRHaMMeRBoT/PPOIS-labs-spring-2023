import pygame.gfxdraw


WIDTH = 800
HEIGHT = 600
FPS = 60

rating = []
SOUND_VOLUME = 10
MUSIC = True
SFX = True

pygame.init()
pygame.display.set_caption("Crimsoland")

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

background_image = pygame.image.load("img/land.png").convert()
background_image = pygame.transform.scale(background_image, (1600, 1200))

font = pygame.font.SysFont('Bodoni 72 Book', 60)

