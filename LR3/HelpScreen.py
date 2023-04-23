import pygame
import sys
from pygame.locals import *
import random
import time
import datetime
import sqlite3
import math
import sys


pygame.init()
pygame.display.set_caption('Jewel quest')
screen = pygame.display.set_mode((400, 425),0,32)

width = 400
height = 400
scoreboard_height = 25


start_ticks=pygame.time.get_ticks() 

clock = pygame.time.Clock()

font = pygame.font.SysFont(None, 30)
candy_colors = ['blue', 'green', 'orange', 'pink', 'purple', 'red', 'teal', 'yellow'] 
candy_width = 40
candy_height = 40
candy_size = (candy_width, candy_height)

def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)
    
    
def complete_level_screen():
    font = pygame.font.Font(None, 32)
    running = True
    while running:
        screen.fill((0, 255, 153))
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
        draw_text('Level complete', font, (0,0,0), screen, 90, 200)
        
        pygame.display.update()

def help():
    running = True
    while running:
        screen.fill((255, 242, 145))
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
        draw_text('Rules', font, (0,0,0), screen, 80, 40)
        draw_text('Classic match-tree rules', font, (0,0,0), screen, 80, 80)
        draw_text('Time: Play until time end', font, (0,0,0), screen, 80, 120)
        draw_text('Score *: 3 level with limit score', font, (0,0,0), screen, 80, 160)
        pygame.display.update()    
    