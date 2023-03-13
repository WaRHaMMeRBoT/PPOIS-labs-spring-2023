import os

import pygame

WIDTH = 1000
HEIGHT = 600
FPS = 15

# Задаем цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

SCALE = 50

game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, 'assets')
player_img = [pygame.image.load(os.path.join(img_folder, 'pacman/1.png')),
              pygame.image.load(os.path.join(img_folder, 'pacman/2.png')),
              pygame.image.load(os.path.join(img_folder, 'pacman/2.png'))]