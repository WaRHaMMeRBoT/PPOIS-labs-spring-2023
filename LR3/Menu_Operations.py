import pygame
import pygame_menu
import random
import yaml
from main_loop import main

WIDTH, HEIGHT = 1920, 1080
fps = 60
username = 'None'

dict_of_buffs = {0: 'Ghost ball', 1: 'Longer paddle', 2: 'Faster paddle', 3: 'Slower game',
                 4: 'Additional lives'}

background_image = pygame_menu.BaseImage('VuNsTSl-space-hd-wallpapers-1080p.jpg')


def game_plan(screen, current):
    global username
    leader_board = open('Leader_board.yaml', 'r')
    leaders =yaml.load(leader_board, Loader=yaml.Loader)
    levels_from_memory = open('Level_yaml.yaml', 'r')
    levels = yaml.load(levels_from_memory, Loader=yaml.Loader)
    full_score = 0
    current_lives = 3
    current.disable()
    current.full_reset()
    for level in range(1, 11):
        current_build = levels.get(level)
        level_blocks = [pygame.Rect(coordinates[0], coordinates[1], 128, 128) for coordinates in current_build]
        level_table_of_buffs = {int(len(level_blocks)/5): dict_of_buffs.get(random.randrange(5)),
                                int(len(level_blocks)/12): dict_of_buffs.get(random.randrange(5)),
                                int(len(level_blocks)/3): dict_of_buffs.get(random.randrange(5))}
        scores_get, current_lives = main(level_blocks, screen, fps, current, level_table_of_buffs, current_lives)
        full_score += scores_get
    levels_from_memory.close()
    for index in range(len(leaders)-1):
        if leaders[index][1] < full_score:
            leaders.insert(index, [username, full_score])
            break
    leaders.pop(len(leaders)-1)
    leader_board.close()
    leader_board = open('Leader_board.yaml', 'w')
    yaml.dump(leaders, leader_board)
    leader_board.close()
    current.enable()
    current.full_reset()


def menu_reactivation(current_menu, previous_menu):
    current_menu.disable()
    current_menu.full_reset()
    previous_menu.enable()
    previous_menu.full_reset()


def show_leaders(screen, main_menu: pygame_menu.Menu, main_theme):
    main_menu.disable()
    main_menu.full_reset()
    leader_board = open('Leader_board.yaml', 'r')
    leader_list = yaml.load(leader_board, Loader=yaml.Loader)
    leader_list: list
    leader_menu = pygame_menu.Menu('Leader board', WIDTH, HEIGHT, surface=screen, theme=main_theme)
    leader_menu.add.label('Leader board', align=pygame_menu.locals.ALIGN_CENTER, font_size=30,
                          font_background_color=(250, 140, 120))
    for leader in leader_list:
        leader_menu.add.label(leader[0]+' '+str(leader[1]), align=pygame_menu.locals.ALIGN_CENTER,
                              font_size=30,  font_background_color=(250, 140, 120))
    leader_menu.add.button('Вернуться', lambda: menu_reactivation(leader_menu, main_menu),
                           font_background_color=(250, 140, 120))
    leader_menu.mainloop()


def set_username(name):
    global username
    username = name


def menu_help(main_menu, screen, main_menu_theme):
    help_menu = pygame_menu.Menu('Справка', WIDTH, HEIGHT, surface=screen, theme=main_menu_theme)
    help_file = open('Readme.txt', 'r')
    menu_reactivation(main_menu, help_menu)
    for line in help_file:
        help_menu.add.label(line, align=pygame_menu.locals.ALIGN_LEFT, font_size=30,
                            font_background_color=(250, 140, 120))
    help_menu.add.button('Вернуться', lambda: menu_reactivation(help_menu, main_menu),
                         font_background_color=(250, 140, 120))
    help_menu.mainloop()


def menu():
    main_menu_theme = pygame_menu.themes.THEME_ORANGE.copy()
    main_menu_theme.background_color = background_image
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    current = pygame_menu.Menu("Arkanid", WIDTH, HEIGHT, surface=screen, theme=main_menu_theme)
    background_image.draw(screen)
    background_sound = pygame_menu.sound.Sound()
    background_sound.set_sound(pygame_menu.sound.SOUND_TYPE_OPEN_MENU, 'E:\\ppois_lr3_arkanoid\\Winter.mp3')
    current.set_sound(background_sound, recursive=True)
    current.add.button('Играть', lambda: game_plan(screen, current),
                       font_background_color=(250, 140, 120))
    current.add.text_input('Name:', textinput_id='Username', onreturn=set_username, default='None',
                           font_background_color=(250, 140, 120))
    current.add.button('Таблица рекордов', lambda: show_leaders(screen, current, main_menu_theme),
                       font_background_color=(250, 140, 120))
    current.add.button('Справка', lambda: menu_help(current, screen, main_menu_theme),
                       font_background_color=(250, 140, 120))
    current.add.button('Выход', lambda: exit(),  font_background_color=(250, 140, 120))
    current.mainloop(screen)


if __name__ == '__main__':
    menu()
