import pygame
import json
import scripts.configs as cf
from typing import Optional
from scripts.game_states import GameStates as gs
from scripts.ui_elements.text import draw_text


screen = pygame.display.set_mode((cf.SCREEN_WIDTH, cf.SCREEN_HEIGHT))
icon_image = pygame.image.load(cf.ICON_DIR)
pygame.display.set_icon(icon_image)


def game_result():
    pygame.display.set_caption('TankHuhn After game result')
    pygame.display.set_icon(icon_image)
    after_game_bg = pygame.image.load(cf.AFTER_GAME_BG)
    after_game_bg = pygame.transform.smoothscale(after_game_bg, (cf.SCREEN_WIDTH, cf.SCREEN_HEIGHT))
    with open(cf.SCORE_LEADERBOARD_PATH, "r") as leaderboard_file:
        score_leaderboard = json.load(leaderboard_file)
        score_leaderboard = sorted(score_leaderboard, key=lambda record: record[1], reverse=True)
    new_record: Optional[list] = None
    for record in score_leaderboard:
        if cf.play_score > record[1]:
            new_record = record
    running = True
    while running:
        screen.fill('black')
        screen.blit(after_game_bg, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
        if new_record:
            draw_text('NEW RECORD!', cf.SCREEN_HEIGHT // 10, 'green', (int(cf.SCREEN_WIDTH * 0.25),
                                                                       int(cf.SCREEN_HEIGHT * 0.3)))
        pygame.display.flip()
    if not running:
        return gs.MAIN_MENU

