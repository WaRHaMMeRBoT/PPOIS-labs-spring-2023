import pygame
from tiles import Tile
from player import Player
from settings import *
from tiles import Clouds
from menu import Records
from death_screen import Death
import time

class Level:
    def __init__(self, level_data, surface):
        self.display_surface = surface
        self.setup_level(level_data)
        self.world_shift = 0
        self.current_x = 0


    def setup_level(self, layout):
        self.tiles = pygame.sprite.Group()
        self.player = pygame.sprite.GroupSingle()
        self.clouds = pygame.sprite.Group()
        self.player_score = 0
        self.font = pygame.font.SysFont('Arial', 24)
        for row_index, row in enumerate(layout):
            for column_index, cell in enumerate(row):
                if cell == "X":
                    tile = Tile((column_index * tile_size, row_index * tile_size), tile_size)
                    self.tiles.add(tile)
                if cell == "P":
                    player = Player((column_index * tile_size, row_index * tile_size))
                    self.player.add(player)
                if cell == "C":
                    cloud = Clouds((column_index * tile_size, row_index * tile_size))
                    self.clouds.add(cloud)

    def scroll_x(self):
        player = self.player.sprite
        player_x = player.rect.centerx
        direction_x = player.direction.x

        if player_x < screen_width - (screen_width / 4) and direction_x < 0:
            self.world_shift = 8
            player.speed = 0
        elif player_x > screen_width - (screen_width / 4) and direction_x > 0:
            self.world_shift = -8
            player.speed = 0
        else:
            self.world_shift = 0
            player.speed = 8

    def horizontal_movement_collision(self):
        player = self.player.sprite
        player.rect.x += player.direction.x * player.speed

        for sprite in self.tiles.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.direction.x < 0:
                    player.rect.left = sprite.rect.right
                    player.on_left = True
                    self.current_x = player.rect.left
                elif player.direction.x > 0:
                    player.rect.right = sprite.rect.left
                    player.on_right = True
                    self.current_x = player.rect.right

        if player.on_left and (player.rect.left < self.current_x or player.direction.x >= 0):
            player.on_left = False
        if player.on_right and (player.rect.right > self.current_x or player.direction.x <= 0):
            player.on_right = False

    def vertical_movement_collision(self):
        player = self.player.sprite
        player.apply_gravity()
        for sprite in self.tiles.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.direction.y > 0:
                    player.rect.bottom = sprite.rect.top
                    player.direction.y = 0
                    player.on_ground = True
                elif player.direction.y < 0:
                    player.rect.top = sprite.rect.bottom
                    player.direction.y = 0
                    player.on_ceiling = True

        if player.on_ground and player.direction.y < 0 or player.direction.y > 1:
            player.on_ground = False
        if player.on_ceiling and player.direction.y > 0:
            player.on_ceiling = False


    def increment_score(self):
        if time.time() >= self.increment_time:
            self.player_score += 1
            self.increment_time = time.time() + 1

    def run(self):
        # actions with level
        record_table = Records(self.display_surface)
        self.clouds.update(self.world_shift)
        self.clouds.draw(self.display_surface)
        self.tiles.update(self.world_shift)
        self.tiles.draw(self.display_surface)
        self.scroll_x()
        # actions with score
        if self.player.sprite.death is True:
            # Death_screen.run()
            print("You're dead!!!")
            record_table.add_score(self.player_score)
            pygame.quit()
            quit()
        else:
            self.increment_score()
        score_surface = self.font.render('Score: {}'.format(self.player_score), True, (255, 255, 255))
        self.display_surface.blit(score_surface, (0, 0))
        # player tile
        self.player.update()
        self.horizontal_movement_collision()
        self.vertical_movement_collision()
        self.player.draw(self.display_surface)
