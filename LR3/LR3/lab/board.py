import json

import pygame

from constants import WIDTH
from walls import Wall, CrossWall, LWall, HorizontalWall, BoardWall, RectangleWall
from constants import config_folder


class Board:
    
    types = {
        'Wall': Wall,
        'HorizontalWall': HorizontalWall,
    }

    def add(self, wall: Wall | CrossWall | LWall | BoardWall | HorizontalWall | RectangleWall):

        if isinstance(wall, Wall | BoardWall | HorizontalWall | RectangleWall):
            self.right_walls_group.add(wall.right)
            self.left_walls_group.add(wall.left)
            self.up_walls_group.add(wall.top)
            self.down_walls_group.add(wall.bottom)
        elif isinstance(wall, CrossWall | LWall):
            self.add(wall.firstWall)
            self.add(wall.secondWall)

    def __init__(self):
        self.right_walls_group = pygame.sprite.Group()
        self.left_walls_group = pygame.sprite.Group()
        self.down_walls_group = pygame.sprite.Group()
        self.up_walls_group = pygame.sprite.Group()

        self.walls = pygame.sprite.Group()

        self.Board = BoardWall()
        self.add(self.Board)

        self.top_peek = Wall(height=115, width=2560, pos=(1500, self.Board.bottom.rect.bottom))
        self.add(self.top_peek)

        self.wall = HorizontalWall(height=50, width=350, pos=(WIDTH / 2, self.top_peek.bottom.rect.bottom + 90))
        self.add(self.wall)
        
        board_config_data = []
        with open(config_folder, 'r+') as f:
            data = json.load(f)
            board_config_data = data.get('WALLS')
            
        for wall_data in board_config_data:
            wall = self.types[wall_data['type']](
                height=wall_data.get('height'),
                width=wall_data.get('width'),
                pos=(
                    wall_data.get('posx'),
                    wall_data.get('posy')
                ))

        self.wall = Wall(height=503, width=50, pos=(WIDTH / 2 + 15, 848))
        self.add(self.wall)

        self.wall = HorizontalWall(height=50, width=300, pos=(90, 850))
        self.add(self.wall)

        self.wall = HorizontalWall(height=50, width=180, pos=(180, 740))
        self.add(self.wall)

        self.wall = HorizontalWall(height=50, width=350, pos=(90, 635))
        self.add(self.wall)

        self.wall = HorizontalWall(height=50, width=350, pos=(1550, 850))
        self.add(self.wall)

        self.wall = HorizontalWall(height=50, width=350, pos=(1550, 635))
        self.add(self.wall)

        self.wall = HorizontalWall(height=50, width=220, pos=(1480, 740))
        self.add(self.wall)

        self.wall = HorizontalWall(height=50, width=425, pos=(535, 850))
        self.add(self.wall)
        self.wall = HorizontalWall(height=40, width=660, pos=(420, 950))
        self.add(self.wall)
        self.wall = HorizontalWall(height=40, width=685, pos=(1250, 950))
        self.add(self.wall)

        self.wall = HorizontalWall(height=50, width=410, pos=(1115, 850))
        self.add(self.wall)

        self.wall = HorizontalWall(height=158, width=410, pos=(1115, 715))
        self.add(self.wall)

        self.wall = HorizontalWall(height=158, width=425, pos=(535, 715))
        self.add(self.wall)

        self.wall = Wall(height=150, width=350, pos=(WIDTH / 2 + 87, 245))
        self.add(self.wall)

        self.wall = Wall(height=400, width=50, pos=(WIDTH / 3 + 35, 345))
        self.add(self.wall)
        self.wall = Wall(height=400, width=120, pos=(WIDTH / 3 - 90, 345))
        self.add(self.wall)
        self.wall = Wall(height=400, width=50, pos=(WIDTH - WIDTH / 3 - 10, 345))
        self.add(self.wall)
        self.wall = Wall(height=400, width=162, pos=(WIDTH - WIDTH / 3 + 180, 345))
        self.add(self.wall)
        self.wall = RectangleWall(height_top=225, height_left=150, width=30,
                                  pos=(self.Board.left.rect.right + 165, 490))
        self.add(self.wall)

        self.wall = Wall(height=240, width=210, pos=(self.Board.right.rect.left - 110, 265))
        self.add(self.wall)

        self.wall = Wall(height=240, width=226, pos=(self.Board.left.rect.right + 220, 265))
        self.add(self.wall)

        self.wall = RectangleWall(height_top=215, height_left=125, width=30, pos=(
            self.Board.right.rect.left - 160, 490))
        self.add(self.wall)

        self.bottom_wall_of_box = HorizontalWall(height=40, width=350, pos=(WIDTH / 2, 534))
        self.add(self.bottom_wall_of_box)
        self.right_wall_of_box = Wall(height=150, width=30, pos=(self.bottom_wall_of_box.right.rect.right + 20, 450))
        self.add(self.right_wall_of_box)
        self.left_wall_of_box = Wall(height=150, width=30, pos=(self.bottom_wall_of_box.left.rect.left - 7, 450))
        self.add(self.left_wall_of_box)

        self.top_left_of_box = HorizontalWall(height=30, width=150, pos=((WIDTH / 2) - 15, 395))
        self.add(self.top_left_of_box)
        self.top_right_of_box = HorizontalWall(height=30, width=150, pos=((WIDTH / 2) + 15, 395))
        self.add(self.top_right_of_box)
        self.walls.add(self.left_walls_group, self.right_walls_group, self.up_walls_group, self.down_walls_group)
