import pygame
import math

import src.game as game

sound_library = {}


def print_text(message, x, y, font_clr=(0, 0, 0), font_type='fonts/RequestPersonalUse.otf', font_size=30, align='left'):
    font_type = pygame.font.Font(font_type, font_size)
    text = font_type.render(message, True, font_clr)
    if align == 'center':
        text_rect = text.get_rect(center=(x, y))
        game.screen.blit(text, text_rect)
    elif align == 'left':
        game.screen.blit(text, (x, y))


def play_sfx(name):
    if game.SFX:
        global sound_library
        sound = sound_library.get(name)
        if sound is None:
            canonicalized_path = get_sound(name)
            sound = pygame.mixer.Sound(canonicalized_path)
            sound_library[name] = sound
        sound.play()


def get_rotated_image(image, rect, angle):
    new_image = pygame.transform.rotate(image, angle)
    new_rect = new_image.get_rect(center=rect.center)
    return new_image, new_rect


def angle_between_points(x1, y1, x2, y2):
    return math.degrees(math.atan2(y1 - y2, x2 - x1))


def get_image(file_name):
    return f'img/{file_name}'


def get_sound(file_name):
    return f'snd/{file_name}'
