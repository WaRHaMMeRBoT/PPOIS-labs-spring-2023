import pygame_menu
import pygame
from pygame_menu import themes
import os

pygame.init()
surface = pygame.display.set_mode((600, 400))

def go_to_menu():
    os.system('py menu.py')
    quit()
    exit()

def restart():
    os.chdir('..')
    os.system('py pacman.py')
    quit()
    exit()

record = pygame_menu.Menu('New record', 600, 400, theme=themes.THEME_DARK)
finish = f"Мои поздравления! Ты прошел этот уровень. \n"
record.add.label(finish, max_char=-1, font_size=20)
record.add.button('Menu', go_to_menu)
record.add.button('Restart', restart)
record.mainloop(surface)