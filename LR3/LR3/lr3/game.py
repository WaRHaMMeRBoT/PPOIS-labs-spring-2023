import pygame
import pygame_menu

from board import Board
from constants import red_ghost_img, blue_ghost_img, pink_ghost_img, orange_ghost_img, dead_ghost_img, WIDTH, HEIGHT
from ghosts import StaticGhost
from static_ghosts import StaticGhost
from pills import Pill
from player import Player
from score import Score


class Game:
    def __init__(self, menu: pygame_menu.Menu):
        pygame.display.init()
        pygame.mixer.init()
        self.channel = pygame.mixer.Channel(0)
        self.menu = menu
        self.font = pygame.font.Font(None, 36)

        self.player_dead = False
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.clock = pygame.time.Clock()

        self.score = 0

        self.personalities = pygame.sprite.Group()

        self.player = Player()

        self.iter = 0
        self.board = Board()

        self.walls = self.board.walls

        self.ghosts = pygame.sprite.Group()

        self.red = StaticGhost(red_ghost_img, (WIDTH / 2, HEIGHT / 2.5), self.walls)
        self.blue = StaticGhost(blue_ghost_img, (WIDTH / 2, HEIGHT / 2.5), self.walls)
        self.orange = StaticGhost(orange_ghost_img, (WIDTH / 2, HEIGHT / 2.5), self.walls)
        self.pink = StaticGhost(pink_ghost_img, (WIDTH / 2, HEIGHT / 2.5), self.walls)
        self.static = StaticGhost(dead_ghost_img, (WIDTH / 2, HEIGHT / 2.5), self.walls)

        self.ghosts.add(self.red, self.pink, self.blue, self.orange, self.static)

        self.pills = pygame.sprite.Group()

        self.add_pills()

        self.personalities.add(self.player, self.ghosts)

        self.pacman = pygame.sprite.Group()

        self.score_text = Score(self)
        self.pacman.add(self.walls, self.personalities, self.pills, self.score_text)

    def add_pills(self):
        for i in range(60, 1670, 60):
            self.pill = Pill(pos=(i, 120))
            self.pills.add(self.pill)

        for i in range(100, 340, 60):
            self.pill = Pill(pos=(i, 415))
            self.pills.add(self.pill)

        for i in range(1400, 1600, 60):
            self.pill = Pill(pos=(i, 415))
            self.pills.add(self.pill)

        for i in range(170, 590, 60):
            self.pill = Pill(pos=(60, i))
            self.pills.add(self.pill)

        for i in range(170, 590, 60):
            self.pill = Pill(pos=(340, i))
            self.pills.add(self.pill)

        for i in range(170, 590, 60):
            self.pill = Pill(pos=(520, i))
            self.pills.add(self.pill)

        for i in range(170, 590, 60):
            self.pill = Pill(pos=(625, i))
            self.pills.add(self.pill)

        for i in range(170, 590, 60):
            self.pill = Pill(pos=(1025, i))
            self.pills.add(self.pill)

        for i in range(170, 590, 60):
            self.pill = Pill(pos=(1130, i))
            self.pills.add(self.pill)

        for i in range(170, 590, 60):
            self.pill = Pill(pos=(1350, i))
            self.pills.add(self.pill)

        for i in range(60, 1670, 60):
            self.pill = Pill(pos=(i, 570))
            self.pills.add(self.pill)

        for i in range(170, 590, 60):
            self.pill = Pill(pos=(1620, i))
            self.pills.add(self.pill)

        for i in range(620, 1000, 60):
            self.pill = Pill(pos=(775, i))
            self.pills.add(self.pill)

        for i in range(620, 1000, 60):
            self.pill = Pill(pos=(880, i))
            self.pills.add(self.pill)

        for i in range(60, 780, 60):
            self.pill = Pill(pos=(i, 990))
            self.pills.add(self.pill)

        for i in range(60, 780, 60):
            self.pill = Pill(pos=(i, 900))
            self.pills.add(self.pill)

        for i in range(60, 780, 60):
            self.pill = Pill(pos=(i, 785))
            self.pills.add(self.pill)

        for i in range(920, 1620, 60):
            self.pill = Pill(pos=(i, 990))
            self.pills.add(self.pill)

        for i in range(920, 1620, 60):
            self.pill = Pill(pos=(i, 900))
            self.pills.add(self.pill)

        for i in range(920, 1620, 60):
            self.pill = Pill(pos=(i, 785))
            self.pills.add(self.pill)

    def player_collision(self):
        collide_right = pygame.sprite.spritecollide(self.player, self.board.right_walls_group, dokill=False)
        collide_left = pygame.sprite.spritecollide(self.player, self.board.left_walls_group, dokill=False)
        collide_down = pygame.sprite.spritecollide(self.player, self.board.down_walls_group, dokill=False)
        collide_up = pygame.sprite.spritecollide(self.player, self.board.up_walls_group, dokill=False)

        colide_with_ghost = pygame.sprite.spritecollide(self.player, self.ghosts, dokill=False)

        pill_collide = pygame.sprite.spritecollide(self.player, self.pills, dokill=False)

        if collide_right:
            self.player.speedx = 0
            self.player.speedy = 0
            self.player.rect.right = collide_right[0].rect.left - 1
        elif collide_left:
            self.player.speedx = 0
            self.player.speedy = 0
            self.player.rect.left = collide_left[0].rect.right + 1
        elif collide_down:
            self.player.speedx = 0
            self.player.speedy = 0
            self.player.rect.top = collide_down[0].rect.bottom + 1
        elif collide_up:
            self.player.speedx = 0
            self.player.speedy = 0
            self.player.rect.bottom = collide_up[0].rect.top - 1
        elif colide_with_ghost:
            self.player.kill()
            self.player_dead = True
        elif pill_collide:
            if self.iter < 2:
                self.player.eat_effect.play()
            self.iter += 1
            if self.iter >= 2:
                self.iter = 0
            pill_collide[0].kill()
            self.score += 1

    def ghost_collision(self, ghost: StaticGhost):
        collide_right = pygame.sprite.spritecollide(ghost, self.board.right_walls_group, dokill=False)
        collide_left = pygame.sprite.spritecollide(ghost, self.board.left_walls_group, dokill=False)
        collide_down = pygame.sprite.spritecollide(ghost, self.board.down_walls_group, dokill=False)
        collide_up = pygame.sprite.spritecollide(ghost, self.board.up_walls_group, dokill=False)

        pill_collide = pygame.sprite.spritecollide(ghost, self.pills, dokill=False)

        if collide_right:
            ghost.random_direction()
            ghost.speedx = 0
            ghost.speedy = 0
            ghost.rect.right = collide_right[0].rect.left + 1
        elif collide_left:
            ghost.random_direction()
            ghost.speedx = 0
            ghost.speedy = 0
            ghost.rect.left = collide_left[0].rect.right + 1
        elif collide_down:
            ghost.random_direction()
            ghost.speedx = 0
            ghost.speedy = 0
            ghost.rect.top = collide_down[0].rect.bottom + 1
        elif collide_up:
            ghost.random_direction()
            ghost.speedx = 0
            ghost.speedy = 0
            ghost.rect.bottom = collide_up[0].rect.top - 1
