from functools import reduce, wraps
import time

import pygame
import gui.config as config


class StopFunc(Exception):
    pass


def stop_func():
    raise StopFunc


class Screen:
    def __init__(self, keys: list = None, handle_events: list = None):
        self.keys = [] if keys is None else keys
        self.handle_events = [] if handle_events is None else handle_events

    def __call__(self, func):
        @wraps(func)
        def wrapper(*args, **kwargs):

            result = None

            config.BOOL_SWITCH = False
            config.timer = 0.0

            for _ in iter(int, 1):

                if config.timer > 0.25:
                    config.BOOL_SWITCH = True
                    config.timer = 0.0
                else:
                    curr = time.time()
                    config.timer += (curr - config.clock)
                    config.clock = curr

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        quit()
                    for handle_event in self.handle_events:
                        handle_event(event)
                try:
                    result = func(*args, **kwargs)
                except StopFunc:
                    break

                if result is not None:
                    kwargs = result

                keys = pygame.key.get_pressed()

                if len(self.keys) and reduce(lambda x, y: x or y, [keys[ind] for ind in self.keys]):
                    break

                pygame.display.update()

            config.BOOL_SWITCH = False
            config.timer = 0.0

            return result

        return wrapper
