import pygame_menu
import pygame
from pygame_menu import themes
import os

pygame.init()
surface = pygame.display.set_mode((600, 400))

def new_record():
    file = open('score.txt', 'r')
    score = int(file.readline())
    file.close()
    file1 = open('score.txt', 'w')
    file1.write(f'{score}\n{score}')
    file1.close()
    return score

def go_to_menu():
    os.system('py menu.py')
    quit()

def restart():
    os.chdir('..')
    os.system('py pacman.py')
    quit()


record = pygame_menu.Menu('New record', 600, 400, theme=themes.THEME_DARK)
finish = f"New record: {new_record()} \n"
record.add.label(finish, max_char=-1, font_size=20)
record.add.image('../assets/record.jpg', angle=0, scale=(0.15, 0.15))
record.add.button('Menu', go_to_menu)
record.add.button('Restart', restart)
record.mainloop(surface)