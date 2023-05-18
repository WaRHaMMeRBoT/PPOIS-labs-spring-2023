import pygame
import gui.utils as utils
import gui.config as config
import time


class InfoBox:
    def __init__(self, text='', background_color=(255, 255, 255), text_color=(0, 0, 0), font_size=30,
                 border_color=(0, 0, 0), border_radius=0, border=1, font_style=None):
        self.background_color = background_color
        self.border_color = border_color
        self.border = border
        self.border_radius = border_radius
        self.text_color = text_color
        self.text = text
        self.font = pygame.font.Font(font_style, font_size)
        self.txt_surface = self.font.render(self.text, True, self.text_color)

        self.surface = pygame.Surface((self.txt_surface.get_width() + 10, self.txt_surface.get_height() + 10))

        self.surface.fill(background_color)
        self.surface.set_alpha(200)

        self.timer = 0.
        self.clock = time.time()
        self.active = False

    def update(self):
        curr_time = time.time()
        self.timer += (curr_time - self.clock)
        self.clock = curr_time

        if self.timer > 1.5:
            self.timer = 0
            self.active = False

    def draw(self, screen):
        self.surface.set_alpha(300 - int(pow(self.timer, 1.5) * 100))
        size = self.surface.get_size()
        rect_image = pygame.Surface(size, pygame.SRCALPHA)
        pygame.draw.rect(rect_image, (255, 255, 255), (0, 0, *size), border_radius=self.border_radius)

        image = self.surface.copy().convert_alpha()
        image.blit(rect_image, (0, 0), None, pygame.BLEND_RGBA_MIN)

        styled_text = self.font.render(self.text, True, self.text_color)
        text_rect = styled_text.get_rect(
            center=((self.txt_surface.get_width() + 10) // 2, (self.txt_surface.get_height() + 10) // 2)
        )
        image.blit(styled_text, text_rect)

        screen.blit(image, ((config.WIDTH - (self.txt_surface.get_width() + 10)) // 2,
                            config.HEIGHT // 6 * 5))
        pygame.display.update(
            ((config.WIDTH - self.surface.get_width()) // 2, config.HEIGHT // 6 * 5,
             *self.surface.get_size())
        )

    def trigger(self):
        self.active = True
        self.surface.set_alpha(200)
        self.timer = 0.
        self.clock = time.time()
