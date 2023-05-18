import pygame

from gui import config


class ScrollBox:

    def __init__(self, x, y, width, height, real_width, real_height, content):

        self.pos = (x, y)

        self.content_pos = (0, 0)
        self.scroll = [0, 0]

        self.surface = pygame.Surface((real_width, real_height))
        self.visible_surface = pygame.Surface((width, height))

        self.slider_x = pygame.Rect(0, height - 15, int((width / real_width) * width), 15)
        self.slider_y = pygame.Rect(width - 15, 0, 15, int((height / real_height) * height))
        self.slider_x_active = False
        self.slider_x_activate_point = None
        self.slider_y_active = False
        self.slider_y_activate_point = None

        self.content = content

    def handle_event(self, event):

        if event.type == pygame.MOUSEBUTTONDOWN and config.BOOL_SWITCH:

            start_event_pos = event.pos

            event.pos = tuple(a - b for a, b in zip(event.pos, self.pos))
            if self.slider_x.collidepoint(event.pos) and self.surface.get_width() != self.visible_surface.get_width():
                self.slider_x_active = True
                self.slider_x_activate_point = event.pos[0] - self.slider_x.x
            if self.slider_y.collidepoint(event.pos) and self.surface.get_height() != self.visible_surface.get_height():
                self.slider_y_active = True
                self.slider_y_activate_point = event.pos[1] - self.slider_y.y

            event.pos = start_event_pos
            event.pos = tuple(a - b - c for a, b, c in zip(event.pos, self.pos, self.content_pos))
            for element in self.content:
                element.handle_event(event)

        elif event.type == pygame.MOUSEBUTTONUP:
            if self.slider_x_active:
                self.slider_x_active = False
            if self.slider_y_active:
                self.slider_y_active = False
                self.slider_y_activate_point = None

    def update(self):

        if self.slider_y_active and 0 <= self.slider_y.y <= self.visible_surface.get_height() - self.slider_y.h:
            self.scroll[1] = self.slider_y.y / self.visible_surface.get_height()
            self.slider_y.y = pygame.mouse.get_pos()[1] - self.pos[1] - self.slider_y_activate_point
        if 0 > self.slider_y.y:
            self.slider_y.y = 0
        elif self.slider_y.y > self.visible_surface.get_height() - self.slider_y.h:
            self.slider_y.y = self.visible_surface.get_height() - self.slider_y.h

        if self.slider_x_active and 0 <= self.slider_x.x <= self.visible_surface.get_width() - self.slider_x.w:
            self.scroll[0] = self.slider_x.x / self.visible_surface.get_width()
            self.slider_x.x = pygame.mouse.get_pos()[0] - self.pos[0] - self.slider_x_activate_point
        if 0 > self.slider_x.x:
            self.slider_x.x = 0
        elif self.slider_x.x > self.visible_surface.get_width() - self.slider_x.w:
            self.slider_x.x = self.visible_surface.get_width() - self.slider_x.w

        self.content_pos = (- self.scroll[0] * self.surface.get_size()[0],
                            - self.scroll[1] * self.surface.get_size()[1])

    def draw(self, screen):
        self.surface.fill((211, 211, 211))
        for element in self.content:
            element.draw(self.surface)

        self.visible_surface.blit(self.surface, self.content_pos)

        if self.surface.get_width() != self.visible_surface.get_width():
            pygame.draw.rect(self.visible_surface, (255, 255, 255), self.slider_x, border_radius=5)
        if self.surface.get_height() != self.visible_surface.get_height():
            pygame.draw.rect(self.visible_surface, (255, 255, 255), self.slider_y, border_radius=5)

        screen.blit(self.visible_surface, self.pos)
