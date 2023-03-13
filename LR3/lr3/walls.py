import pygame

from lr3.constants import WIDTH, BLUE


class PartOfWall(pygame.sprite.Sprite):
    def __init__(self, wight, height, pos: tuple):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((wight, height))
        self.image.fill(BLUE)
        self.image = pygame.transform.scale(self.image, (wight, height))
        self.rect = self.image.get_rect()
        self.rect.center = pos

    def update(self):
        self.rect.x += 0
        if self.rect.left > WIDTH:
            self.rect.right = 0


class Wall:
    def __init__(self, wight, height, pos: tuple):
        self.wall = pygame.sprite.Group()
        self.left = PartOfWall(wight=wight / 2, height=height - height * 0.1, pos=(pos[0] - wight/302, pos[1]))
        self.right = PartOfWall(wight=wight / 2, height=height - height * 0.1, pos=(pos[0] - wight / 2, pos[1]))
        self.top = PartOfWall(wight=wight, height=height * 0.1, pos=(self.left.rect.left, self.right.rect.top))
        self.bottom = PartOfWall(wight=wight, height=height * 0.1, pos=(self.left.rect.left, self.right.rect.bottom))
        self.wall.add(self.left, self.right, self.top, self.bottom)

    def getWall(self) -> pygame.sprite.Group:
        return self.wall


class GorizontalWall(Wall):
    def __init__(self, wight, height, pos: tuple):
        super().__init__(wight, height, pos)
        self.tempWall = self.top
        self.top = self.left
        self.left = self.tempWall
        self.tempWall = self.bottom
        self.bottom = self.right
        self.right = self.tempWall
        self.wall.empty()
        self.wall = pygame.sprite.Group()
        self.wall.add(self.left, self.right, self.top, self.bottom)


class CrossWall:
    def __init__(self, wight, height, pos: tuple):
        self.wall = pygame.sprite.Group()
        self.firstWall = Wall(wight, height, pos)
        self.secondWall = GorizontalWall(height, wight, pos)

    def getWall(self) -> pygame.sprite.Group:
        return self.wall
