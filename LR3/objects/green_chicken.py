import time

import pygame
import random


class ChickenGreen(pygame.sprite.Sprite):
    def __init__(self, screen, pos_y):
        pygame.sprite.Sprite.__init__(self)
        self.screen = screen
        self.chickens = []

        # if CHICKEN is still alive
        self.alive = 2

        # POSITION and TIMER  of chicken's DEATH
        self.dead_index = 0
        self.max_dead_time = 2
        self.dead_time = 0

        # TIMER of chicken's FLIGHT
        self.fly_index = 0
        self.max_fly_time = 2
        self.fly_time = 0

        # CHICKEN size
        self.size = (60, 60)
        self.speed = 0.1

        # direction of CHICKEN flight
        self.direction = 0
        self.img_path = 'img/green_chicken_flight/chicken1.png'
        r = random.choice([0, 800])
        if r == 0:
            self.direction = 1
        else:
            self.direction = -1

        self.image = pygame.transform.scale(pygame.image.load(self.img_path).convert_alpha(), self.size)
        self.rect = self.image.get_rect(center=(r, pos_y))

    # logic of flight
    def update(self, dt, move):

        # if CHICKEN is alive
        if self.alive:
            self.fly_time += 1
            # self.chickens.append(self.rect)
            self.screen.blit(self.image, self.rect)

            # flight to the RIGHT
            if self.direction == 1:
                if move == 'move_r':
                    self.rect.x -= (40 + float(self.speed * dt))
                elif move == 'move_l':
                    self.rect.x += (40 + float(self.speed * dt))
                else:
                    self.rect.x += float(self.speed * dt)

                if self.fly_time == self.max_fly_time:
                    self.fly_time = 0
                    self.fly_index += 1
                    if self.fly_index == 13:
                        self.fly_index = 0
                    elif self.fly_index <= 12:
                        path = 'img/green_chicken_flight/chicken' + str(self.fly_index) + '.png'
                        self.image = pygame.transform.flip(
                            pygame.transform.scale(pygame.image.load(path).convert_alpha(), self.size), True, False)

            # flight to the LEFT
            else:
                if move == 'move_r':
                    self.rect.x -= (40 + float(self.speed * dt))
                elif move == 'move_l':
                    self.rect.x += (40 + float(self.speed * dt))
                else:
                    self.rect.x -= float(self.speed * dt)

                if self.fly_time == self.max_fly_time:
                    self.fly_time = 0
                    self.fly_index += 1
                    if self.fly_index == 13:
                        self.fly_index = 0
                    elif self.fly_index <= 12:
                        path = 'img/green_chicken_flight/chicken' + str(self.fly_index) + '.png'
                        self.image = pygame.transform.scale(pygame.image.load(path).convert_alpha(), self.size)

            # if the chicken is out of the screen
            if self.rect.y >= 540:
                self.kill()
            elif self.rect.x >= 4000:
                self.kill()
            if self.rect.x == -4000:
                self.kill()

        # if we have shot one of them
        if self.alive == 0:
            self.dead_time += 1
            self.rect.y += float(self.speed * dt)

            if self.dead_time == self.max_dead_time:
                self.dead_time = 0
                self.dead_index += 1
                if self.dead_index == 9:
                    self.kill()
                elif self.dead_index <= 8:
                    path = 'img/green_chicken_flight_death/chickendead' + str(self.dead_index) + '.png'
                    self.image = pygame.transform.scale(pygame.image.load(path).convert_alpha(), self.size)
                    # self.rect.y += 2
