import pygame
import gui.utils as utils


class TextBox:
    def __init__(self, x, y, width, height, text='', background_color=(255, 255, 255), text_color=(0, 0, 0),
                 border_color=(0, 0, 0), border_radius=0, border=1, font_style=None, font_size=None):
        self.rect = pygame.Rect(x, y, width, height)
        self.background_color = background_color
        self.border_color = border_color
        self.border = border
        self.border_radius = border_radius
        self.text_color = text_color
        self.text = text
        self.font = pygame.font.Font(font_style, (height if font_size is None else font_size))
        self.txt_surface = self.font.render(self.text, True, self.text_color)

    def draw(self, screen):
        if self.background_color is not None:
            utils.draw_react_with_border(screen, self.rect, self.background_color,
                                         self.border_radius, self.border, self.border_color)
        screen.blit(self.txt_surface,
                    self.txt_surface.get_rect(center=(self.rect.x + self.rect.w // 2, self.rect.y + self.rect.h // 2)))
