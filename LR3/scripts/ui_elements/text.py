import pygame
import scripts.configs as cf
from typing import Union


def draw_text(text: str, font_size: Union[int, float], text_color: str, text_coord: tuple):
    font = pygame.font.Font(cf.IN_GAME_FONT, font_size)
    text_img = font.render(text, True, text_color)
    pygame.display.get_surface().blit(text_img, text_coord)
