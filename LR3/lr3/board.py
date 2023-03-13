import pygame

from lr3.walls import Wall, CrossWall, GorizontalWall


class Board:

    def add(self, wall: Wall):
        self.right_walls_group.add(wall.right)
        self.left_walls_group.add(wall.left)
        self.up_walls_group.add(wall.top)
        self.down_walls_group.add(wall.bottom)

    def __init__(self):
        self.right_walls_group = pygame.sprite.Group()
        self.left_walls_group = pygame.sprite.Group()
        self.down_walls_group = pygame.sprite.Group()
        self.up_walls_group = pygame.sprite.Group()

        self.walls = pygame.sprite.Group()

        # self.wall = Wall(height=100, wight=7, pos=(0, 570))
        # self.add(self.wall)
        # self.wall = Wall(height=60, wight=100, pos=(0, 0))
        # self.add(self.wall)
        # self.wall = Wall(height=100, wight=7, pos=(100, 570))
        # self.add(self.wall)
        # self.wall = Wall(height=60, wight=100, pos=(0, 1050))
        # self.add(self.wall)

        # self.wall = PartOfWall(height=30, wight=350, pos=(300, 200))
        # self.left_walls_group.add(self.wall)
        # self.wall = PartOfWall(height=350, wight=30, pos=(300, 200))
        # self.down_walls_group.add(self.wall)
        self.wall = GorizontalWall(height=30, wight=350, pos=(300, 200))
        self.add(self.wall)
        #self.add(self.wall.secondWall)
        self.walls.add(self.left_walls_group, self.right_walls_group, self.up_walls_group, self.down_walls_group)

    def getBoard(self) -> pygame.sprite.Group:
        return self.walls
