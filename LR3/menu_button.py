# Author Vodohleb04
from typing import NoReturn, Tuple

import pygame

from my_sprite import MySprite
from text_controller import TextObject
from config_controller import ConfigController


class Button(MySprite):

    def __init__(self, config_controller: ConfigController, x, y, w, h, text, on_click=lambda x: None, padding=0):
        super().__init__(x, y, w, h)
        self.state = 'normal'
        self.on_click = on_click

        self.text = TextObject(x + padding, y + padding, lambda: text, config_controller.button_text_color,
                               config_controller.font_name, config_controller.font_size)
        self._back_colors = dict(
            normal=config_controller.button_normal_back_color, hover=config_controller.button_hover_back_color,
            pressed=config_controller.button_pressed_back_color)

    def draw(self, surface) -> NoReturn:
        pygame.draw.rect(surface,  self.back_color, self.bounds)
        self.text.draw(surface)

    def handle_mouse_event(self, type, pos) -> NoReturn:
        if type == pygame.MOUSEMOTION:
            self.handle_mouse_move(pos)
        elif type == pygame.MOUSEBUTTONDOWN:
            self.handle_mouse_down(pos)
        elif type == pygame.MOUSEBUTTONUP:
            self.handle_mouse_up(pos)

    def handle_mouse_move(self, pos) -> NoReturn:
        if self._bounds.collidepoint(pos):
            if self.state != 'pressed':
                self.state = 'hover'
        else:
            self.state = 'normal'

    def handle_mouse_down(self, pos) -> NoReturn:
        if self._bounds.collidepoint(pos):
            self.state = 'pressed'

    def handle_mouse_up(self, pos) -> NoReturn:
        if self.state == 'pressed':
            self.on_click(self)
            self.state = 'hover'

    @property
    def back_color(self) -> Tuple[int, int, int]:
        return self._back_colors[self.state]
