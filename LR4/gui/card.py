import pygame

from gui import utils, config
from src.card import Card


class CardImg:

    def __init__(self, card: Card, x, y, scale=1,
                 background_color=(200, 215, 215), border_radius=10, border=2, border_color=(0, 0, 0)):
        self.card = card
        self.rect = pygame.Rect(x, y, int(250 * scale), int(150 * scale))
        self.background_color = background_color
        self.border_radius = border_radius
        self.border = border
        self.border_color = border_color
        self.font_size = int(27 * scale)

        self.chosen = False

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and self.rect.collidepoint(event.pos) and config.BOOL_SWITCH:
            self.chosen = True

    def draw(self, screen):

        utils.draw_react_with_border(screen, self.rect, self.background_color,
                                     self.border_radius, self.border, self.border_color)

        utils.print_text(text=self.card.number,
                         x=self.rect.x + self.rect.w // 2, y=self.rect.y + self.rect.h // 5,
                         font_color=(0, 0, 0), font_size=self.font_size, align='center', screen=screen)
        utils.print_text(text=self.card.account.login,
                         x=self.rect.x + self.font_size, y=self.rect.y + self.rect.h - self.font_size,
                         font_color=(0, 0, 0), font_size=self.font_size, align='left', screen=screen)
        utils.print_text(text=self.card.date,
                         x=self.rect.x + self.rect.w - self.font_size, y=self.rect.y + self.rect.h - self.font_size,
                         font_color=(0, 0, 0), font_size=self.font_size, align='right', screen=screen)
