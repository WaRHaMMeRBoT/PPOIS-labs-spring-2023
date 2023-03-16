import pygame

from lr3.constants import WIDTH, BLUE


class PartOfWall(pygame.sprite.Sprite):
    def __init__(self, width, height, pos: tuple):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((width, height))
        self.image.fill(BLUE)
        self.image = pygame.transform.scale(self.image, (width, height))
        self.rect = self.image.get_rect()
        self.rect.center = pos

    def update(self):
        self.rect.x += 0
        if self.rect.left > WIDTH:
            self.rect.right = 0


class Wall:
    def __init__(self, width, height, pos: tuple):
        self.wall = pygame.sprite.Group()

        self.left = PartOfWall(width=width / 2, height=height - 40, pos=(pos[0], pos[1]))
        self.right = PartOfWall(width=width / 2, height=height - 40, pos=(pos[0] - width / 2, pos[1]))
        self.top = PartOfWall(width=width, height=40, pos=(self.left.rect.left, self.right.rect.top))
        self.bottom = PartOfWall(width=width, height=40,
                                 pos=(self.left.rect.left, self.right.rect.bottom))
        self.wall.add(self.left, self.right, self.top, self.bottom)


class HorizontalWall:
    def __init__(self, width, height, pos: tuple):
        self.bottom = PartOfWall(width=width, height=height / 2, pos=(pos[0], pos[1]))
        self.top = PartOfWall(width=width, height=height / 2, pos=(pos[0], pos[1] - height / 2))
        self.right = PartOfWall(width=1, height=height * 0.4, pos=(self.bottom.rect.left + 1, self.bottom.rect.top))
        self.left = PartOfWall(width=1, height=height * 0.4, pos=(self.bottom.rect.right - 1, self.bottom.rect.top))
        self.wall = pygame.sprite.Group()
        self.wall.add(self.left, self.right, self.top, self.bottom)


class CrossWall:
    def __init__(self, wight, height, pos: tuple):
        self.firstWall = Wall(wight, height, pos)
        self.secondWall = HorizontalWall(height, wight, pos)


class LWall:
    def __init__(self, width, height, pos: tuple):
        self.firstWall = Wall(width, height, pos)
        print(self.firstWall.right.rect.right)
        self.secondWall = HorizontalWall(height, width,
                                         pos=(
                                             self.firstWall.right.rect.bottom,
                                             self.firstWall.bottom.rect.bottom))


class RectangleWall:
    def __init__(self, width, height_left, height_top, pos: tuple):
        self.wall = pygame.sprite.Group()
        self.bottom = PartOfWall(width=height_top, height=width * 1.5, pos=(pos[0], pos[1] + width))
        self.left = PartOfWall(width=width * 2, height=height_left * 0.5, pos=(self.bottom.rect.right - width, pos[1]))
        self.right = PartOfWall(width=width * 2, height=height_left * 0.5, pos=(self.bottom.rect.left + width, pos[1]))
        self.top = PartOfWall(width=height_top, height=width * 1.5, pos=(pos[0], pos[1] - width))
        self.wall.add(self.left, self.right, self.bottom, self.top)


class BoardWall:
    def __init__(self):
        self.wall = pygame.sprite.Group()
        self.bottom = PartOfWall(width=1650, height=40, pos=(850, 15))
        self.left = PartOfWall(width=40, height=1050, pos=(15, 525))
        self.right = PartOfWall(width=40, height=1050, pos=(1665, 525))
        self.top = PartOfWall(width=1650, height=40, pos=(850, 1035))
        self.wall.add(self.left, self.right, self.bottom, self.top)
