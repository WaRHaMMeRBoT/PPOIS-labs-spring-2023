import random
import sys
from collections import defaultdict

import pygame

from asteroid import Asteroid
from bullet import Bullet
from spaceship import SpaceShip


class Game:
    @staticmethod
    def __load_image():
        image = pygame.image.load('./images/ships/ship_1.png')
        return pygame.transform.scale(image, (40, 40))

    def __init__(self,
                 caption,
                 width,
                 height,
                 back_image_filename,
                 frame_rate):
        self.background_image = pygame.image.load(back_image_filename)  # задаем картинку
        self.frame_rate = frame_rate  # задаем частоту кадров
        self.game_over = False
        Asteroid.asteroids_amount = 0
        self.sprites = pygame.sprite.Group()  # объекты игры
        self.spaceship = SpaceShip(250, 250, 7, self.sprites)
        self.sprites.add(self.spaceship)
        self.bullets = pygame.sprite.Group()
        self.asteroids = pygame.sprite.Group()
        pygame.init()  # сам модуль
        pygame.font.init()  # работа со шрифтами
        self.surface = pygame.display.set_mode((width, height))  # отображение дисплея
        pygame.display.set_caption(caption)
        self.clock = pygame.time.Clock()
        self.life_image = self.__load_image()
        self.life_rect = self.life_image.get_rect()


    def __draw_lives(self):
        distance_between_lives = 10
        for i in range(self.spaceship.hp):
            self.surface.blit(self.life_image,
                              (distance_between_lives + (distance_between_lives + self.life_rect.width) * i, 50))

    def __set_background_size(self):
        new_window_size = self.surface.get_size()
        self.background_image = pygame.transform.scale(self.background_image, new_window_size)

    def __collision_check(self):
        for asteroid in self.asteroids:
            if asteroid.rect.colliderect(self.spaceship.collision_rect) and not self.spaceship.padded:
                asteroid.kill()
                self.spaceship.hp -= 1
                if self.spaceship.hp <= 0:
                    self.game_over = True

                self.spaceship.start_padded_timer()

    def __generate_asteroids(self):
        if Asteroid.asteroids_amount < 10:
            asteroid = Asteroid(self.surface.get_size(), self.surface)
            self.asteroids.add(asteroid)
            self.sprites.add(asteroid)
            Asteroid.asteroids_amount += 1

    def __smash_an_asteroid(self, smashed: Asteroid):
        if smashed.size > 70:
            if bool(random.randint(0, 1)):
                params = {'image': smashed.image, 'size': smashed.size / 2, 'x': smashed.rect.x, 'y': smashed.rect.y}
                new_ast_1 = Asteroid(self.surface, params=params, first_time=False)
                new_ast_2 = Asteroid(self.surface, params=params, first_time=False)
                Asteroid.asteroids_amount += 2
                self.asteroids.add(new_ast_1)
                self.asteroids.add(new_ast_2)
                self.sprites.add(new_ast_1)
                self.sprites.add(new_ast_2)

    def __check_hits(self):
        hits = pygame.sprite.groupcollide(self.asteroids, self.bullets, True, True)
        if hits:
            Bullet.bullet_amount -= 1
            Asteroid.asteroids_amount -= 1
            smashed_asteroid = None
            for asteroid, bullet in hits.items():
                smashed_asteroid = asteroid
                if asteroid.acceleration:
                    self.spaceship.game_points += 20
                else:
                    self.spaceship.game_points += 10
            self.__smash_an_asteroid(smashed_asteroid)
            pos = smashed_asteroid.rect.center
            smashed_asteroid.kill()

    def __check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game_over = True
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                self.bullet_fired = True
            if event.type == pygame.KEYUP and event.key == pygame.K_SPACE:
                self.bullet_fired = False

    def run(self):

        while not self.game_over:
            self.bullet_fired = False
            self.__check_events()

            list_of_args_for_stripe = {'surface_size': self.surface.get_size(),
                                       'bullet_fired': self.bullet_fired,
                                       'screen': self.surface,
                                       'bullets': self.bullets}
            self.__generate_asteroids()
            self.__check_hits()
            self.__collision_check()

            self.sprites.update(list_of_args_for_stripe)
            self.surface.blit(self.background_image, (0, 0))
            self.__set_background_size()
            self.sprites.draw(self.surface)

            font = pygame.font.Font(None, 36)
            score_text = font.render(f"Score: {self.spaceship.game_points}", True, (255, 0, 0))
            self.surface.blit(score_text, (10, 10))
            self.__draw_lives()
            pygame.display.update()
            self.clock.tick(self.frame_rate)

        pygame.time.delay(1000)  # задержка в 1 секунду
        return self.spaceship.game_points
