import pygame
import pygame_menu
from pygame_menu import themes
import os


pygame.init()
surface = pygame.display.set_mode((600, 400))
score = 0
records = ''


def start_the_game():
    os.system("py pacman.py")
    quit()

def now_record():
    global score, records
    if os.path.exists('menu/score.txt'):
        file = open('menu/score.txt', 'r')
        score = file.readline()
        records = file.readline()
        file.close()
        return records
    else:
        file = open('score.txt', 'r')
        score = file.readline()
        records = file.readline()
        file.close()
        return records

def manual():
    mainmenu._open(level)

def record_menu():
    mainmenu._open(record)


mainmenu = pygame_menu.Menu('Welcome', 600, 400, theme=themes.THEME_DARK)
mainmenu.add.button('Play', start_the_game)
mainmenu.add.button('Records', record_menu)
mainmenu.add.button('Manual', manual)
mainmenu.add.button('Quit', pygame_menu.events.EXIT)

level = pygame_menu.Menu('Manual', 600, 400, theme=themes.THEME_DARK)
HELP = "Нажмите PgUp чтобы идти вперёд \n"\
       "Нажмите -> чтобы пойти на право \n"\
       "Нажмите <- чтобы пойти на лево \n"\
       "Нажмите PgDn чтобы пойти назад.\n"\
       "Цель: съесть всю еду, пока тебя не съели призраки\n"
level.add.label(HELP, max_char=-1, font_size=20)
record = pygame_menu.Menu('Record', 600, 400, theme=themes.THEME_DARK)
message = f"Рекокд на данный момент: {now_record()}"
record.add.label(message, max_char=-1, font_size=20)

mainmenu.mainloop(surface)