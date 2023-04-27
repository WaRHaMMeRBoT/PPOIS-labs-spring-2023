import pygame
from scripts import configs as cf


class Action:
    PLAY = 'play'
    QUIT = 'quit'
    TUTORIAL = 'tutorial'


class Button:
    def __init__(self, btn_img_path: str, rel_coordinates: tuple, rel_size: tuple, text: str,
                 text_font: pygame.font.Font, text_color: str, action: Action):
        self.__btn_image_path = btn_img_path
        self.__btn_img = pygame.image.load(self.__btn_image_path)
        self.__btn_img = pygame.transform.scale(self.__btn_img, (int(cf.SCREEN_WIDTH * (rel_size[0] / 100)),
                                                                 int(cf.SCREEN_HEIGHT * (rel_size[1] / 100))))
        self.__coords = (int(cf.SCREEN_WIDTH * (rel_coordinates[0] / 100)),
                         int(cf.SCREEN_HEIGHT * (rel_coordinates[1] / 100)))
        self.__rel_size = rel_size
        self.__rect = self.__btn_img.get_rect(center=self.__coords)
        self.__text = text
        self.__text_surface = text_font.render(self.__text, True, text_color)
        self.__text_rect = self.__text_surface.get_rect(center=self.__coords)
        self.__screen = pygame.display.get_surface()
        self.__action = action

    def update(self, touch_pos):
        if self.__rect.collidepoint(touch_pos):
            btn_width = int(cf.SCREEN_WIDTH * ((self.__rel_size[0] + 1) / 100))
            btn_height = int(cf.SCREEN_HEIGHT * ((self.__rel_size[1] + 1) / 100))
        else:
            btn_width = int(cf.SCREEN_WIDTH * (self.__rel_size[0] / 100))
            btn_height = int(cf.SCREEN_HEIGHT * (self.__rel_size[1] / 100))
        self.__btn_img = pygame.transform.scale(pygame.image.load(self.__btn_image_path), (btn_width, btn_height))
        self.__rect = self.__btn_img.get_rect(center=self.__coords)
        self.__text_rect = self.__text_surface.get_rect(center=self.__coords)
        self.__screen.blit(self.__btn_img, self.__rect)
        self.__screen.blit(self.__text_surface, self.__text_rect)

    def action(self, touch_pos):
        if self.__rect.collidepoint(touch_pos):
            return self.__action
        return None
