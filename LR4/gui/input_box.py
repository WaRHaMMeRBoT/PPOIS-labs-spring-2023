import pygame
import gui.utils as utils


class InputBox:
    def __init__(self, x, y, width, height, text='', background_color=(255, 255, 255), text_color=(0, 0, 0),
                 inactive_border_color=(0, 0, 0), active_border_color=(255, 0, 0), border_radius=0, border=1,
                 font_style=None):
        self.rect = pygame.Rect(x, y, width, height)
        self.background_color = background_color
        self.border_color = inactive_border_color
        self.inactive_border_color = inactive_border_color
        self.active_border_color = active_border_color
        self.border = border
        self.border_radius = border_radius
        self.text_color = text_color
        self.text = text
        self.font = pygame.font.Font(font_style, height)
        self.txt_surface = self.font.render(self.text, True, self.text_color)
        self.active = False

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.active = not self.active
            else:
                self.active = False
            self.border_color = self.active_border_color if self.active else self.inactive_border_color

        elif event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_RETURN:
                    self.active, self.border_color = False, self.inactive_border_color
                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
                self.txt_surface = self.font.render(self.text, True, self.text_color)

    def update(self):
        width = max(self.rect.w, self.txt_surface.get_width()+10)
        self.rect.w = width

    def draw(self, screen):
        utils.draw_react_with_border(screen, self.rect, self.background_color,
                                     self.border_radius, self.border, self.border_color)
        screen.blit(self.txt_surface,
                    self.txt_surface.get_rect(center=(self.rect.x + self.rect.w // 2, self.rect.y + self.rect.h // 2)))
