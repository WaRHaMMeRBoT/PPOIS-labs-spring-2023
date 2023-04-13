import pygame
import pygame_menu
import json

import game
import timer_game


def set_difficulty(value, difficulty):
    with open('difficulty.json', 'w+') as file:
        data_json = json.dumps(difficulty)
        file.write(data_json)
        file.close()


def start_the_game():

    with open("difficulty.json") as file:
        mode = json.load(file)
        file.close()
    if mode != 4:
        game.main()
    else:
        timer_game.main()


pygame.init()
surface = pygame.display.set_mode((630, 630))
pygame.display.set_icon(pygame.image.load('images/fire_transparent.png'))
pygame.display.set_caption("Element Crush")

menu = pygame_menu.Menu('Welcome', 630, 630, theme=pygame_menu.themes.THEME_BLUE)

menu.add.selector('Mode :', [('Easy', 1), ('Medium', 2), ('Hard', 3), ('Time', 4)],
                  onchange=set_difficulty)

menu.add.button('Play', start_the_game)
menu.add.button('Quit', pygame_menu.events.EXIT)

with open('difficulty.json', 'w+') as file:
    data_json = json.dumps(1)
    file.write(data_json)
    file.close()

menu.mainloop(surface)


