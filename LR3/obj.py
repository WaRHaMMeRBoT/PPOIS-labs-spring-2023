from pygame.rect import Rect

class Obj:
    def __init__(self, x, y, width, height, speed=(0, 0)):
        self._bounds = Rect(x, y, width, height)
        self._speed = speed

    @property
    def speed(self):
        return self._speed

    @speed.setter
    def speed(self, new_speed):
        self._speed = new_speed

    @property
    def bounds(self):
        return self._bounds

    @property
    def left(self):
        return self._bounds.left

    @property
    def right(self):
        return self._bounds.right

    @property
    def top(self):
        return self._bounds.top

    @property
    def bottom(self):
        return self._bounds.bottom

    @property
    def width(self):
        return self._bounds.width

    @property
    def height(self):
        return self._bounds.height

    @property
    def center(self):
        return self._bounds.center

    @property
    def centerx(self):
        return self._bounds.centerx

    @property
    def centery(self):
        return self._bounds.centery

    def draw(self, surface):
        raise NotImplementedError

    def move(self, new_x, new_y):
        self._bounds = self._bounds.move(new_x, new_y)

    def update(self):
        if self.speed == [0, 0]:
            return
        self.move(*self.speed)

