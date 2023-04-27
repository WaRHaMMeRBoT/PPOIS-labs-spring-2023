import pygame
import scripts.configs as cf
from typing import Any, Union
from scripts.sprites.effects import Explosion


class MovementDirection:
    RIGHT = (False, False)
    LEFT = (True, False)


class Enemy(pygame.sprite.Sprite):
    def __init__(self, group, spawn_x: Union[int, float], spawn_y: Union[int, float], animation_frames_path: list[str],
                 rel_size: tuple, movement_speed: int, movement_direction: MovementDirection, map_size: cf.MapSize):
        super(Enemy, self).__init__()
        self.__group = group
        self.add(group)
        self.display = pygame.display.get_surface()
        self.frames = []
        for frame in animation_frames_path:
            image = pygame.image.load(frame)
            image = pygame.transform.smoothscale(image, (int(self.display.get_width() * rel_size[0] / 100),
                                                         int(self.display.get_width() * rel_size[1] / 100)))
            image = pygame.transform.flip(image, movement_direction[0], movement_direction[1])
            self.frames.append(image)
        self.index = 0
        self.image = self.frames[self.index % len(self.frames)]
        self.rect = self.image.get_rect(center=(spawn_x, spawn_y))
        self.counter = 0
        self.map_size = map_size
        self.movement_speed = round(movement_speed / (self.display.get_width() // 100), 2)
        if movement_direction == MovementDirection.LEFT:
            self.movement_speed *= -1

    def update(self, *args: Any, **kwargs: Any) -> None:
        animation_speed = 4

        # movement
        self.rect.centerx += self.movement_speed

        # update animation
        self.counter += 1
        if self.counter >= animation_speed:
            self.counter = 0
            self.index += 1
            self.image = self.frames[self.index % len(self.frames)]

        if self.rect.centerx > self.map_size[0] + self.rect.w or self.rect.centerx < -self.rect.w:
            self.kill()

        if kwargs.get('sight_pos'):
            self.check_collision_with_touch(self.__group.offset + kwargs["sight_pos"])

    def check_collision_with_touch(self, sight_pos):
        if self.rect.collidepoint(sight_pos):
            self.kill()
            cf.play_score += 10
            Explosion(self.__group, sight_pos[0], sight_pos[1], self.rect)
            return True
