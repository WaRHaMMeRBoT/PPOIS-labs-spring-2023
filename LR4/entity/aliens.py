import random
import pygame
from pygame import Surface
from entity.abstract import Entity
from entity.player import Player
from entity.projectiles import Projectile, SuperProjectile
from utils.utils import overlay_fill

from main import\
ALIEN_ATTACK_DELAY,\
DELTA,\
ENTITY_SIZE,\
KILL,\
PROJECTILE_SPEED,\
TPS


class Alien(Entity):
    def __init__(self, player: Player, allies, pos: tuple[int, int], level: int, texture: Surface) -> None:
        self.level = level
        self.pos = pos
        self.texture = overlay_fill(texture, pygame.Color(255, int(255 / level), int(255 / level)))
        self.texture = pygame.transform.scale(texture, (ENTITY_SIZE, ENTITY_SIZE))
        self.aabb = texture.get_rect(topleft = pos).scale_by(4, 4)
        self.health = level
        self.attack_timer = ALIEN_ATTACK_DELAY + random.random() * TPS
        self.player = player
        self.projectiles = []
        self.horizontal_vector = 1
        self.allies = allies

    def update(self):
        self.projectiles = list(filter(lambda proj: proj.health > 0, self.projectiles))

        self.attack_timer -= 1

        if self.attack_timer <= 0:
            can_shoot = True
            for ally in self.allies:
                if (ally.aabb.x == self.aabb.x) and (ally.aabb.y > self.aabb.y):
                    can_shoot = False
                    break
            if(can_shoot):
                self.shoot([self.player])
            self.attack_timer = ALIEN_ATTACK_DELAY + random.random() * TPS

        for projectile in self.projectiles:
            projectile.update()

    def shoot(self, enemies):
        pass

    def draw(self, surface: Surface):
        for projectile in self.projectiles:
            projectile.draw(surface)
        surface.blit(self.texture, self.aabb)


class RegularAlien(Alien):
    def __init__(self, player: Player, allies, pos: tuple[int, int], level: int) -> None:
        super().__init__(player, allies, pos, level, pygame.image.load('assets/regular.png').convert_alpha())

    def die(self):
        pygame.mixer.Sound.play(KILL)
        self.player.score += 100 * self.level

    def shoot(self, enemies):
        new_projectile = Projectile(self.aabb.midbottom, (0, PROJECTILE_SPEED / DELTA), enemies)
        self.projectiles.append(new_projectile)


class ShotgunAlien(Alien):
    def __init__(self, player: Player, allies, pos: tuple[int, int], level: int) -> None:
        super().__init__(player, allies, pos, level, pygame.image.load('assets/shotgun.png').convert_alpha())

    def die(self):
        pygame.mixer.Sound.play(KILL)
        self.player.score += 150 * self.level

    def shoot(self, enemies):
        new_projectile1 = Projectile(self.aabb.midbottom, (0, PROJECTILE_SPEED / DELTA), enemies)
        new_projectile2 = Projectile(self.aabb.midbottom, (PROJECTILE_SPEED / 10 / DELTA, PROJECTILE_SPEED / DELTA), enemies)
        new_projectile3 = Projectile(self.aabb.midbottom, (-PROJECTILE_SPEED / 10 / DELTA, PROJECTILE_SPEED / DELTA), enemies)
        self.projectiles.append(new_projectile1)
        self.projectiles.append(new_projectile2)
        self.projectiles.append(new_projectile3)

class BurstAlien(Alien):
    def __init__(self, player: Player, allies, pos: tuple[int, int], level: int) -> None:
        super().__init__(player, allies, pos, level, pygame.image.load('assets/burst.png').convert_alpha())

    def die(self):
        pygame.mixer.Sound.play(KILL)
        self.player.score += 200 * self.level

    def shoot(self, enemies):
        new_projectile1 = Projectile(self.aabb.midbottom, (0, PROJECTILE_SPEED / DELTA), enemies)
        new_projectile2 = Projectile(self.aabb.midbottom, (0, PROJECTILE_SPEED * 0.9 / DELTA), enemies)
        new_projectile3 = Projectile(self.aabb.midbottom, (0, PROJECTILE_SPEED * 0.8 / DELTA), enemies)
        self.projectiles.append(new_projectile1)
        self.projectiles.append(new_projectile2)
        self.projectiles.append(new_projectile3)

class SuperAlien(Alien):
    def __init__(self, player: Player, allies, pos: tuple[int, int], level: int) -> None:
        super().__init__(player, allies, pos, level, pygame.image.load('assets/super.png').convert_alpha())

    def die(self):
        pygame.mixer.Sound.play(KILL)
        self.player.score += 250 * self.level

    def shoot(self, enemies):
        new_projectile = SuperProjectile(self.aabb.midbottom, (0, PROJECTILE_SPEED * 0.5 / DELTA), enemies)
        self.projectiles.append(new_projectile)