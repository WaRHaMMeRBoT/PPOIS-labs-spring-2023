import pygame
import gui.utils as utils
import gui.config as config


class Button:
    def __init__(self, x, y, width, height, background_color=(255, 255, 255),
                 text='', font_size=30, inactive_font_color=(0, 0, 0), active_font_color=(255, 0, 0), font_style=None,
                 border=0, border_radius=0, border_color=(0, 0, 0),
                 action=(lambda **kwargs: None), kwargs=None):

        self.rect = pygame.Rect(x, y, width, height)
        self.font = pygame.font.Font(font_style, font_size)
        self.active_font_color = active_font_color
        self.inactive_font_color = inactive_font_color

        self.text = text

        self.background_color = background_color
        self.border = border
        self.border_radius = border_radius
        self.border_color = border_color

        self.action = action
        self.kwargs = {} if kwargs is None else kwargs

    def update(self, **kwargs):
        self.kwargs = kwargs

    def draw(self, screen):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        if self.rect.collidepoint(mouse) and config.BOOL_SWITCH and click[0] == 1:
            self.action(**self.kwargs)

        text_surface = self.font.render(self.text, True,
                                        (self.active_font_color if self.rect.collidepoint(mouse)
                                         else self.inactive_font_color))

        utils.draw_react_with_border(screen, self.rect, self.background_color,
                                     self.border_radius, self.border, self.border_color)
        screen.blit(text_surface,
                    text_surface.get_rect(center=(self.rect.x + self.rect.w // 2, self.rect.y + self.rect.h // 2)))
