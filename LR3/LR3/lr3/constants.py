import json
import os

import pygame


BLACK = (0, 0, 0)
BLUE = (0, 0, 255)

SCALE = 50

game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, 'assets')
config_folder = img_folder + '/config.json'

with open(img_folder + '/config.json') as f:
    data = json.load(f)

WIDTH = data["WIDTH"]
HEIGHT = data["HEIGHT"]
FPS = data["FPS"]


player_img = [pygame.image.load(os.path.join(img_folder, 'pacman/1.png')),
              pygame.image.load(os.path.join(img_folder, 'pacman/2.png')),
              pygame.image.load(os.path.join(img_folder, 'pacman/2.png'))]

blue_ghost_img = [pygame.image.load(os.path.join(img_folder, 'ghosts/blue/down_1.png')),
                  pygame.image.load(os.path.join(img_folder, 'ghosts/blue/down_2.png')),
                  pygame.image.load(os.path.join(img_folder, 'ghosts/blue/left_1.png')),
                  pygame.image.load(os.path.join(img_folder, 'ghosts/blue/left_2.png')),
                  pygame.image.load(os.path.join(img_folder, 'ghosts/blue/right_1.png')),
                  pygame.image.load(os.path.join(img_folder, 'ghosts/blue/right_2.png')),
                  pygame.image.load(os.path.join(img_folder, 'ghosts/blue/up_1.png')),
                  pygame.image.load(os.path.join(img_folder, 'ghosts/blue/up_2.png'))]

red_ghost_img = [pygame.image.load(os.path.join(img_folder, 'ghosts/red/down_1.png')),
                 pygame.image.load(os.path.join(img_folder, 'ghosts/red/down_2.png')),
                 pygame.image.load(os.path.join(img_folder, 'ghosts/red/left_1.png')),
                 pygame.image.load(os.path.join(img_folder, 'ghosts/red/left_2.png')),
                 pygame.image.load(os.path.join(img_folder, 'ghosts/red/right_1.png')),
                 pygame.image.load(os.path.join(img_folder, 'ghosts/red/right_2.png')),
                 pygame.image.load(os.path.join(img_folder, 'ghosts/red/up_1.png')),
                 pygame.image.load(os.path.join(img_folder, 'ghosts/red/up_2.png'))]

orange_ghost_img = [pygame.image.load(os.path.join(img_folder, 'ghosts/orange/down_1.png')),
                    pygame.image.load(os.path.join(img_folder, 'ghosts/orange/down_2.png')),
                    pygame.image.load(os.path.join(img_folder, 'ghosts/orange/left_1.png')),
                    pygame.image.load(os.path.join(img_folder, 'ghosts/orange/left_2.png')),
                    pygame.image.load(os.path.join(img_folder, 'ghosts/orange/right_1.png')),
                    pygame.image.load(os.path.join(img_folder, 'ghosts/orange/right_2.png')),
                    pygame.image.load(os.path.join(img_folder, 'ghosts/orange/up_1.png')),
                    pygame.image.load(os.path.join(img_folder, 'ghosts/orange/up_2.png'))]

pink_ghost_img = [pygame.image.load(os.path.join(img_folder, 'ghosts/pink/down_1.png')),
                  pygame.image.load(os.path.join(img_folder, 'ghosts/pink/down_2.png')),
                  pygame.image.load(os.path.join(img_folder, 'ghosts/pink/left_1.png')),
                  pygame.image.load(os.path.join(img_folder, 'ghosts/pink/left_2.png')),
                  pygame.image.load(os.path.join(img_folder, 'ghosts/pink/right_1.png')),
                  pygame.image.load(os.path.join(img_folder, 'ghosts/pink/right_2.png')),
                  pygame.image.load(os.path.join(img_folder, 'ghosts/pink/up_1.png')),
                  pygame.image.load(os.path.join(img_folder, 'ghosts/pink/up_2.png'))]

muted_ghost_img = [pygame.image.load(os.path.join(img_folder, 'ghosts/muted/1.png')),
                   pygame.image.load(os.path.join(img_folder, 'ghosts/muted/2.png'))]

dead_ghost_img = [pygame.image.load(os.path.join(img_folder, 'ghosts/dead/1.png')),
                  pygame.image.load(os.path.join(img_folder, 'ghosts/dead/2.png'))]
