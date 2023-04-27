import os

SCREEN_WIDTH = 1600
SCREEN_HEIGHT = 900
FPS = 60
BASE_GAME_TIME = 120

ROOT_DIR = os.path.realpath(os.path.join(os.path.dirname(__file__), '..'))

ICON_DIR = os.path.realpath(os.path.join(ROOT_DIR, 'assets/ready_assets/miscellaneous/icon.png'))

MAIN_MENU_BG_DIR = os.path.realpath(os.path.join(ROOT_DIR, 'assets/ready_assets/miscellaneous/main_menu_bg.png'))
MAIN_MENU_BTN = {'play': os.path.realpath(os.path.join(ROOT_DIR, 'assets/ready_assets/miscellaneous/buttons'
                                                                 '/main_menu_btn_play.png')),
                 'quit': os.path.realpath(os.path.join(ROOT_DIR, 'assets/ready_assets/miscellaneous/buttons'
                                                                 '/main_menu_btn_quit.png')),
                 'tutorial': os.path.realpath(os.path.join(ROOT_DIR, 'assets/ready_assets/miscellaneous/buttons'
                                                                     '/main_menu_btn_tutorial.png'))}


class MapSize:
    STANDARD = (SCREEN_WIDTH * 3, SCREEN_HEIGHT)


BACKGROUND_DIR = {'bg_day': os.path.realpath(os.path.join(ROOT_DIR, 'assets/ready_assets/bg/bg_day.png'))}
UI_SPRITES_IMG = {'cursor': os.path.realpath(os.path.join(ROOT_DIR, 'assets/ready_assets/miscellaneous'
                                                                    '/cursor_cross.png')),
                  'sight': os.path.realpath(os.path.join(ROOT_DIR, 'assets/ready_assets/miscellaneous'
                                                                   '/tank_sight.png')),
                  'ammo_icon': os.path.realpath(os.path.join(ROOT_DIR, 'assets/ready_assets/miscellaneous'
                                                                       '/ammo_icon.png'))}
SIGHT_SPEED = SCREEN_HEIGHT // 100
CLIP_SIZE = 10
IN_GAME_FONT = os.path.realpath(os.path.join(ROOT_DIR, 'assets/fonts/joystix_monospace.otf'))

ALL_ENEMIES = ['enemy_tank_1', 'enemy_tank_2', 'enemy_tank_3']
ENEMY_SPRITES_IMG = {'enemy_tank_1': [os.path.realpath(os.path.join(ROOT_DIR, f'assets/ready_assets/enemies/'
                                                                              f'enemy_tank_1/enemy_tank_1_{i}.png'))
                                      for i in range(1, 11)],
                     'enemy_tank_2': [os.path.realpath(os.path.join(ROOT_DIR, f'assets/ready_assets/enemies/'
                                                                              f'enemy_tank_2/enemy_tank_2_{i}.png'))
                                      for i in range(1, 13)],
                     'enemy_tank_3': [os.path.realpath(os.path.join(ROOT_DIR, f'assets/ready_assets/enemies/'
                                                                              f'enemy_tank_3/enemy_tank_3_{i}.png'))
                                      for i in range(1, 17)]

                     }
ENEMY_BASIC_REL_SIZE = {'enemy_tank_1': (30, 10),
                        'enemy_tank_2': (18, 6.7),
                        'enemy_tank_3': (12, 4)}
ENEMY_BASIC_SPEED = {'enemy_tank_1': 55,
                     'enemy_tank_2': 65,
                     'enemy_tank_3': 68}

EFFECTS_IMG = {'explosion': [os.path.realpath(os.path.join(ROOT_DIR, f'assets/ready_assets/miscellaneous/effects/'
                                                                     f'explosion/explosion_{i}.png'))
                             for i in range(1, 17)]}

# PLAY SCORE
play_score = 0

SCORE_LEADERBOARD_PATH = os.path.realpath(os.path.join(ROOT_DIR, 'score_leaders.json'))

AFTER_GAME_BG = os.path.realpath(os.path.join(ROOT_DIR, 'assets/ready_assets/miscellaneous/after_game_bg.png'))
