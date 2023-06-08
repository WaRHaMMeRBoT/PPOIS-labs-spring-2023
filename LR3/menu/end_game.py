import pygame_menu
import pygame
from pygame_menu import themes
import os

score = 0
record = 0

pygame.init()
surface = pygame.display.set_mode((600, 400))

def end_game():
    global score, record
    file = open('score.txt', 'r')
    score = file.readline()
    record = file.readline()
    file.close()
    if int(score) > int(record):
        record = score
        os.system("py new_record.py")
        quit()
    file1 = open('score.txt', 'w')
    file1.write(f'{score}{record}')
    file1.close()
    return score

def go_to_menu():
    os.system('py menu.py')
    quit()

def restart():
    os.chdir('..')
    os.system('py pacman.py')
    quit()


end = pygame_menu.Menu('End game', 600, 400, theme=themes.THEME_DARK)
finish = f"Title: {end_game()} \n"
end.add.label(finish, max_char=-1, font_size=20)
end.add.button('Menu', go_to_menu)
end.add.button('Restart', restart)
end.mainloop(surface)