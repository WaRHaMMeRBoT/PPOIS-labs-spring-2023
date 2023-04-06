# Author: Vodohleb04
from typing import Tuple, NoReturn
from pygame.rect import Rect


class MySprite:

    def __init__(self, x, y, width, height, speed=(0, 0)):
        self._bounds = Rect(x, y, width, height)
        self._speed = speed

    @property
    def speed(self) -> Tuple[int, int]:
        return self._speed

    @speed.setter
    def speed(self, new_speed: Tuple[int, int]) -> NoReturn:
        self._speed = new_speed

    @property
    def bounds(self) -> Rect:
        return self._bounds

    @property
    def left(self) -> int:
        return self._bounds.left

    @property
    def right(self) -> int:
        return self._bounds.right

    @property
    def top(self) -> int:
        return self._bounds.top

    @property
    def bottom(self) -> int:
        return self._bounds.bottom

    @property
    def width(self) -> int:
        return self._bounds.width

    @property
    def height(self) -> int:
        return self._bounds.height

    @property
    def center(self) -> Tuple[int, int]:
        return self._bounds.center

    @property
    def centerx(self) -> int:
        return self._bounds.centerx

    @property
    def centery(self) -> int:
        return self._bounds.centery

    def draw(self, surface):
        raise NotImplementedError

    def move(self, x_shift, y_shift) -> NoReturn:
        self._bounds = self._bounds.move(x_shift, y_shift)

    def update(self) -> NoReturn:
        if self.speed == [0, 0]:
            return
        self.move(*self.speed)

