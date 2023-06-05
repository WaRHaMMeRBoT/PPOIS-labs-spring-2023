import pygame

GAMENAME = "JewelGame"
GRIDSIZE = 10
SCREENSIZE = 600
FONTSIZE = int(SCREENSIZE*(4/75))
SCOREBOARDRATIO = 0.5
FPS = 60 
INROW = 3
MOVERATIO = 0.05
FALLSTARTRATIO = 0.05
ACCELERATION = 1.025
CANDYSIZE = 0.8
LINESIZE = 0.03
LINECOLOR = (252, 233, 241)
BGCOLOR = (241, 212, 229)
SCOREBOARDCOLOR = (250,150,150)
SCORECOLOR = (255,255,255)

def set_gridsize(value):
    global GRIDSIZE, CELLSIZE, FALLSPEED, MOVESPEED, OFFSET, TEXTURES
    GRIDSIZE = value
    CELLSIZE = SCREENSIZE / GRIDSIZE
    FALLSPEED = CELLSIZE * FALLSTARTRATIO
    MOVESPEED = CELLSIZE * MOVERATIO
    OFFSET = (CELLSIZE - (CELLSIZE * CANDYSIZE)) / 2
    stone1 = pygame.transform.scale(pygame.image.load("images/Stone1.png"), (int(CELLSIZE * CANDYSIZE), int(CELLSIZE * CANDYSIZE)))
    stone2 = pygame.transform.scale(pygame.image.load("images/Stone2.png"), (int(CELLSIZE * CANDYSIZE), int(CELLSIZE * CANDYSIZE)))
    stone3 = pygame.transform.scale(pygame.image.load("images/Stone3.png"), (int(CELLSIZE * CANDYSIZE), int(CELLSIZE * CANDYSIZE)))
    stone4 = pygame.transform.scale(pygame.image.load("images/Stone4.png"), (int(CELLSIZE * CANDYSIZE), int(CELLSIZE * CANDYSIZE)))
    stone5 = pygame.transform.scale(pygame.image.load("images/Stone5.png"), (int(CELLSIZE * CANDYSIZE), int(CELLSIZE * CANDYSIZE)))
    stone6 = pygame.transform.scale(pygame.image.load("images/Stone6.png"), (int(CELLSIZE * CANDYSIZE), int(CELLSIZE * CANDYSIZE)))
    TEXTURES = [stone1, stone2, stone3, stone4, stone5, stone6]

CELLSIZE = SCREENSIZE / GRIDSIZE
FALLSPEED = CELLSIZE*FALLSTARTRATIO
MOVESPEED = CELLSIZE*MOVERATIO
OFFSET = (CELLSIZE-(CELLSIZE*CANDYSIZE))/2
SCOREBOARDSIZE = SCOREBOARDRATIO * SCREENSIZE

VIRSCORELOCATION = (3,5.5)
VIRHISCORELOCATION = (3,20)
SCORELOCATION = ((SCOREBOARDSIZE/20)*VIRSCORELOCATION[0], (SCREENSIZE/40)*VIRSCORELOCATION[1])
HISCORELOCATION = ((SCOREBOARDSIZE/20)*VIRHISCORELOCATION[0], (SCREENSIZE/40)*VIRHISCORELOCATION[1])
SCORESTARTSIZE = (200,100)

stone1 = pygame.transform.scale(pygame.image.load("images/Stone1.png"), (int(CELLSIZE*CANDYSIZE), int(CELLSIZE*CANDYSIZE)))
stone2 = pygame.transform.scale(pygame.image.load("images/Stone2.png"), (int(CELLSIZE*CANDYSIZE), int(CELLSIZE*CANDYSIZE)))
stone3 = pygame.transform.scale(pygame.image.load("images/Stone3.png"), (int(CELLSIZE*CANDYSIZE), int(CELLSIZE*CANDYSIZE)))
stone4 = pygame.transform.scale(pygame.image.load("images/Stone4.png"), (int(CELLSIZE*CANDYSIZE), int(CELLSIZE*CANDYSIZE)))
stone5 = pygame.transform.scale(pygame.image.load("images/Stone5.png"), (int(CELLSIZE*CANDYSIZE), int(CELLSIZE*CANDYSIZE)))
stone6 = pygame.transform.scale(pygame.image.load("images/Stone6.png"), (int(CELLSIZE*CANDYSIZE), int(CELLSIZE*CANDYSIZE)))

SCOREBOARDTEX = pygame.transform.scale(pygame.image.load("images/Scoreboard.png"), (int(SCOREBOARDSIZE), SCREENSIZE))


TEXTURES = [stone1, stone2, stone3, stone4, stone5, stone6]