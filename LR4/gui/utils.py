import pygame
import math

import gui.config as config

sound_library = {}


def print_text(text, x, y, font_color=(0, 0, 0), font_style=None, font_size=30, align='left', screen=config.screen):
    font_type = pygame.font.Font(font_style, font_size)
    styled_text = font_type.render(text, True, font_color)
    if align == 'center':
        text_rect = styled_text.get_rect(center=(x, y))
        screen.blit(styled_text, text_rect)
    elif align == 'right':
        text_rect = styled_text.get_rect(bottomright=(x, y))
        screen.blit(styled_text, text_rect)
    elif align == 'left':
        text_rect = styled_text.get_rect(bottomleft=(x, y))
        screen.blit(styled_text, text_rect)


def draw_react_with_border(surface, rect, background_color,
                           border_radius, border, border_color):
    pygame.draw.rect(surface, border_color,
                     (rect.x - border, rect.y - border,
                      rect.w + 2 * border, rect.h + 2 * border), border_radius=border_radius)

    pygame.draw.rect(surface, background_color,
                     rect, border_radius=border_radius)


def draw_background(screen: pygame.surface, text: str = ''):
    screen.fill((128, 128, 128))
    pygame.draw.rect(screen, (211, 211, 211), (50, 50, config.WIDTH - 100, config.HEIGHT - 100),
                     border_radius=10)

    print_text(text, config.WIDTH / 2, 80, align='center')


def get_image(file_name):
    return f'img/{file_name}'


def get_sound(file_name):
    return f'snd/{file_name}'
