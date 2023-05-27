import pygame
import sys
from collections import defaultdict

class GameKernel:

    def __init__(self, caption, width, height, background_image_file, frame_rate):
        self._background_image = pygame.image.load(background_image_file)
        self._frame_rate = frame_rate
        self._game_over = False
        self._objects = []
        pygame.mixer.pre_init(44100, 16, 2, 4096)
        pygame.init()
        pygame.font.init()
        self._surface = pygame.display.set_mode((width, height))
        pygame.display.set_caption(caption)
        self._clock = pygame.time.Clock()
        self._keydown_handlers = defaultdict(list)
        self._keyup_handlers = defaultdict(list)
        self._mouse_handlers = []

    def update(self):
        for object in self._objects:
            object.update()

    def draw(self):
        for object in self._objects:
            object.draw(self._surface)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                for handler in self._keydown_handlers[event.key]:
                    handler(event.key)
            elif event.type == pygame.KEYUP:
                for handler in self._keyup_handlers[event.key]:
                    handler(event.key)
            elif event.type in (pygame.MOUSEBUTTONDOWN, pygame.MOUSEBUTTONUP, pygame.MOUSEMOTION):
                for handler in self._mouse_handlers:
                    handler(event.type, event.pos)

    def run(self):
        while not self._game_over:
            self._surface.blit(self._background_image, (0, 0))
            self.handle_events()
            self.update()
            self.draw()
            pygame.display.update()
            self._clock.tick(self._frame_rate)

    @property
    def keydown_handlers(self):
        return self._keydown_handlers

    @property
    def keyup_handlers(self):
        return self._keyup_handlers

    @property
    def mouse_handlers(self):
        return self._mouse_handlers

    @property
    def objects(self):
        return self._objects
