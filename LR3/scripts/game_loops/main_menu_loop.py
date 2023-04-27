import pygame
import sys
from scripts import configs as cf
from scripts.game_states import GameStates as gs
from scripts.ui_elements.buttons import Button, Action


screen = pygame.display.set_mode((cf.SCREEN_WIDTH, cf.SCREEN_HEIGHT))
icon_image = pygame.image.load(cf.ICON_DIR)
pygame.display.set_icon(icon_image)
clock = pygame.time.Clock()
pygame.init()


def main_menu():
    pygame.display.set_caption('TankHuhn')
    pygame.display.set_icon(icon_image)
    menu_bg = pygame.image.load(cf.MAIN_MENU_BG_DIR)
    menu_bg = pygame.transform.smoothscale(menu_bg, (cf.SCREEN_WIDTH, cf.SCREEN_HEIGHT))
    font_holder = pygame.font.SysFont('arial', 10)
    buttons = [Button(cf.MAIN_MENU_BTN['play'], (50, 40), (20, 15), '', font_holder, 'black', Action.PLAY),
               Button(cf.MAIN_MENU_BTN['tutorial'], (50, 60), (20, 15), '', font_holder, 'black', Action.TUTORIAL),
               Button(cf.MAIN_MENU_BTN['quit'], (50, 80), (20, 15), '', font_holder, 'black', Action.QUIT)]
    running = True
    while running:
        screen.fill('black')
        screen.blit(menu_bg, (0, 0))
        button_action = None
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                for button in buttons:
                    if button.action(pygame.mouse.get_pos()):
                        button_action = button.action(pygame.mouse.get_pos())
        if button_action == Action.QUIT:
            pygame.quit()
            sys.exit()
        elif button_action == Action.PLAY:
            return gs.LIMIT_TIME_MODE
        for button in buttons:
            button.update(pygame.mouse.get_pos())
        pygame.display.flip()
