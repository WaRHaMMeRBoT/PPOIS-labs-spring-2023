import pygame
import math
import toolbox
from manager import ScoreManager, Background
import image_util
import random, power
from blood import Blood

class Enemy(pygame.sprite.Sprite):
    def __init__(self, screen, x, y, target):
        super().__init__(self.containers)
        self.screen = screen
        self.target = target
        self.x = x
        self.y = y

        self.hit = False
        self.alive = True

        self.normalImage = pygame.image.load(image_util.getImage("Walker.png")).convert_alpha()
        self.hurtImage = pygame.image.load(image_util.getImage("Walker_hurt.png")).convert_alpha()
        self.image = self.normalImage
        self.rect = self.image.get_rect()
        self.rect.center = [self.x, self.y]

        self.angle = 180
        self.speed = 3
        self.max_health = 50
        self.health = self.max_health
        self.damage = 10
        self.hurtTimer = 0

        self.max_attackTimer = 250
        self.attackTimer = 0

        self.reset_offset = 0
        self.offset_x = random.randrange(-350, 350)
        self.offset_y = random.randrange(-350, 350)

    def update(self, projectiles, powers):

        if self.alive:
            self.angle = toolbox.angleBetweenPoints(self.x, self.y, self.target.x, self.target.y)
            angle_rads = math.radians(self.angle)

            self.x_move = (math.cos(angle_rads))
            self.y_move = (math.sin(angle_rads))

            self.rect.center = [self.x - Background.display_scroll[0], self.y - Background.display_scroll[1]]
            self.image = self.normalImage

            if self.reset_offset == 0:
                self.offset_x = random.randrange(-300, 300)
                self.offset_y = random.randrange(-300, 300)
                self.reset_offset = random.randrange(130, 150)
            else:
                self.reset_offset -= 1

            if self.target.x + self.offset_x > self.x - Background.display_scroll[0]:
                if self.attackTimer != 0:
                    self.x += 1
                else:
                    self.x += 2
            elif self.target.x + self.offset_x< self.x - Background.display_scroll[0]:
                if self.attackTimer != 0:
                    self.x -= 1
                else:
                    self.x -= 2

            if self.target.y + self.offset_y > self.y - Background.display_scroll[1]:
                if self.attackTimer != 0:
                    self.y += 1
                else:
                    self.y += 2
            elif self.target.y + self.offset_y < self.y - Background.display_scroll[1]:
                if self.attackTimer != 0:
                    self.y -= 1
                else:
                    self.y -= 2

            if self.hurtTimer <= 0:
                imageToRotate = self.image
            else:
                imageToRotate = self.hurtImage
                self.hurtTimer -= 1

            if self.attackTimer == 0:
                if self.rect.colliderect(self.target.rect):
                    self.target.get_hit(self.damage)
                    self.get_hit(0)
                    self.attackTimer = self.max_attackTimer
            else:
                self.attackTimer -= 1

            for projectile in projectiles:
                if self.target.player_weapon.type == 'snipe':
                    if not self.hit:
                        if self.rect.colliderect(projectile.rect):
                            self.get_hit(projectile.damage)
                            self.hit = True
                    if self.hit:
                        if not self.rect.colliderect(projectile.rect):
                            self.hit = False

                if self.target.player_weapon.type != 'snipe':
                    if self.rect.colliderect(projectile.rect):
                        self.get_hit(projectile.damage)
                        projectile.explode()

            image_to_draw, image_rect = toolbox.getRotatedImage(imageToRotate, self.rect, -self.angle)
            self.screen.blit(image_to_draw, image_rect)


    def get_hit(self, damage):
        if damage:
            toolbox.playSound('hit.wav')
            self.hurtTimer = 5

        if 180 >= self.angle >= 0:
            self.y -= self.y_move * self.speed
        else:
            self.y += self.y_move * self.speed
        if 90 >= self.angle >= -90:
            self.x += self.x_move * self.speed
        else:
            self.x -= self.x_move * self.speed

        self.health -= damage
        if self.health <= 0:
            self.alive = False
            Blood(self.screen,self.x, self.y)
            self.kill()

            if random.random() > .85:
                power.PowerUp(self.screen, [self.x, self.y])

            toolbox.playSound('point.wav')
            ScoreManager.score += int(self.max_health/5)


class Brute(Enemy):
    def __init__(self, screen, x, y, target):
        super().__init__(screen, x, y, target)
        self.normalImage = pygame.image.load(image_util.getImage("Brute.png")).convert_alpha()
        self.hurtImage = pygame.image.load(image_util.getImage("Brute_hurt.png")).convert_alpha()
        self.image = self.normalImage
        self.speed = 2
        self.max_health = 100
        self.health = self.max_health
        self.damage = 15
        self.max_attackTimer = 300
        self.attackTimer = 0


class Crawler(Enemy):
    def __init__(self, screen, x, y, target):
        super().__init__(screen, x, y, target)
        self.hurtImage = pygame.image.load(image_util.getImage("Crawler_hurt.png")).convert_alpha()
        self.normalImage = self.normalImage
        self.normalImage = pygame.image.load(image_util.getImage("Crawler.png")).convert_alpha()
        self.speed = 1.5
        self.max_health = 75
        self.health = self.max_health
        self.angle = 90
        self.damage = 20
        self.max_attackTimer = 350
        self.attackTimer = 0


class Helicopter(Enemy):
    def __init__(self, screen, x, y, target):
        super().__init__(screen, x, y, target)
        self.hurtImage = pygame.image.load(image_util.getImage("helicopter_hurt.png")).convert_alpha()
        self.normalImage = pygame.image.load(image_util.getImage("helicopter.png")).convert_alpha()
        self.normalImage = pygame.transform.scale(self.normalImage, (40, 40))
        self.normalImage = self.normalImage
        self.speed = 3
        self.max_health = 80
        self.health = self.max_health
        self.damage = 17
        self.max_attackTimer = 250
        self.attackTimer = 0

class Spider(Enemy):
    def __init__(self, screen, x, y, target):
        super().__init__(screen, x, y, target)
        self.hurtImage = pygame.image.load(image_util.getImage("Spider_hurt.png")).convert_alpha()
        self.image = pygame.image.load(image_util.getImage("Spider.png")).convert_alpha()
        self.speed = 10
        self.max_health = 45
        self.health = self.max_health
        self.damage = 20
        self.max_attackTimer = 220
        self.attackTimer = 0


class Runner(Enemy):
    def __init__(self, screen, x, y, target):
        super().__init__(screen, x, y, target)
        self.hurtImage = pygame.image.load(image_util.getImage("Runner_hurt.png"))
        self.image = pygame.image.load(image_util.getImage("Runner.png"))
        self.speed = 100
        self.max_health = 15
        self.health = self.max_health
        self.damage = 50
        self.max_attackTimer = 380
        self.attackTimer = 0


class Motorcycle(Enemy):
    def __init__(self, screen, x, y, target):
        super().__init__(screen, x, y, target)
        self.hurtImage = pygame.image.load(image_util.getImage("Motorcycle_hurt.png"))
        self.image = pygame.image.load(image_util.getImage("Motorcycle.png"))
        self.speed = 5
        self.max_health = 30
        self.health = self.max_health
        self.damage = 20
        self.max_attackTimer = 250
        self.attackTimer = 0