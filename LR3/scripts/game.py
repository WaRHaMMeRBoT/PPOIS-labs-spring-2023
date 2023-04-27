import pygame
from scripts import configs as cf
from scripts.game_loops.limit_time_mode_loop import limit_time_mode as ltm
from scripts.game_loops.main_menu_loop import main_menu
from scripts.game_loops.game_result_loop import game_result
from scripts.game_states import GameStates as gs


clock = pygame.time.Clock()

screen = pygame.display.set_mode((cf.SCREEN_WIDTH, cf.SCREEN_HEIGHT))
icon_image = pygame.image.load(cf.ICON_DIR)
pygame.display.set_icon(icon_image)
pygame.init()


class Game:
    def __init__(self):
        self.__main_menu_loop = main_menu
        self.__limit_time_mode_loop = ltm
        self.__after_game = game_result
        self.__game_state = gs.MAIN_MENU

    def game(self):
        while True:
            if self.__game_state == gs.MAIN_MENU:
                self.__game_state = self.__main_menu_loop()
            elif self.__game_state == gs.LIMIT_TIME_MODE:
                self.__game_state = self.__limit_time_mode_loop()
            elif self.__game_state == gs.AFTER_GAME:
                self.__game_state = self.__after_game()
