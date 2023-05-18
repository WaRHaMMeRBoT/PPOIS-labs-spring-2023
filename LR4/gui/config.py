import pygame
import time

WIDTH = 800
HEIGHT = 600
FPS = 60

BOOL_SWITCH = False

timer = 0.0
clock = time.time()

pygame.init()
pygame.display.set_caption("ATM model")
screen = pygame.display.set_mode((WIDTH, HEIGHT))

ACCOUNTS = None
CARDS = None
REPOSITORY = None
ATM = None
BANK = None
