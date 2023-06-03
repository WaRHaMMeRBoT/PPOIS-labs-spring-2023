from pygame import Surface


class Entity():
    def __init__(self) -> None:
        self.health = 0
        self.texture = None
        self.aabb = None

    def update(self):
        pass

    def draw(self, surface: Surface):
        pass

    def die(self):
        pass