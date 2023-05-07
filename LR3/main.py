import pygame
import sys

from menu import Menu
from level import Level
from settings import *
from menu import Records
import time


def main():
    pygame.init()
    pygame.mixer.init()
    screen_width = 1520
    screen_height = len(creating_level_map()) * tile_size
    screen = pygame.display.set_mode((screen_width, screen_height))
    clock = pygame.time.Clock()
    level = Level(creating_level_map(), screen)
    level.increment_time = time.time() + 1
    menu = Menu(screen)
    records = Records(screen)
    # death_screen = Death_Screen(screen)
    level_called = False
    records_called = False

    # Setting up music
    pygame.mixer.music.load("C:\\PPOIS_3sem\\lab3\\music.mp3")
    pygame.mixer.music.set_volume(0.3)
    pygame.mixer.music.play(-1)

    while True:
        screen.fill((173, 216, 230))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if menu.start_button.collidepoint(event.pos) and not(records_called or level_called):
                    screen.fill((173, 216, 230))
                    level_called = True
                elif menu.record_button.collidepoint(event.pos) and not(records_called or level_called):
                    screen.fill((173, 216, 230))
                    records_called = True
                elif menu.quit_button.collidepoint(event.pos) and not(records_called or level_called):
                    pygame.quit()
                    quit()
                elif records.menu_button.collidepoint(event.pos) and records_called is True:
                    screen.fill((173, 216, 230))
                    records_called = False
        if level_called is True:
            level.run()
        elif records_called is True:
            records.print_top_10_positions()
        else:
            menu.run()
        pygame.display.update()
        clock.tick(60)


if __name__ == '__main__':
    main()
