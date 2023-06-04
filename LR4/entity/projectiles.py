import pygame
from entity.abstract import Entity
from main import \
PROJECTILE_SIZE,\
SCREEN_HEIGHT,\
SCREEN_WIDTH


class Projectile(Entity):
    def __init__(self, pos: tuple[int, int], vector: tuple[int, int], entities: list[Entity]) -> None:
        self.texture = pygame.image.load('assets/projectile.png').convert_alpha()
        self.texture = pygame.transform.scale(self.texture, (PROJECTILE_SIZE, PROJECTILE_SIZE))
        self.aabb = self.texture.get_rect(midbottom = pos)
        self.vector = vector
        self.health = 1
        self.damage = 1
        self.scene_entities = entities

    def update(self):
        if (self.aabb.right > SCREEN_WIDTH - 48) or \
           (self.aabb.left < 48) or \
           (self.aabb.bottom < 48) or \
           (self.aabb.top > SCREEN_HEIGHT - 48):
            self.health = 0

        self.aabb.x += self.vector[0]
        self.aabb.y += self.vector[1]

        for entity in self.scene_entities:
            e_aabb = entity.aabb
            if self.aabb.colliderect(e_aabb):
                entity.health -= self.damage
                self.health = 0

    def draw(self, surface: pygame.Surface):
        surface.blit(self.texture, self.aabb)


class SuperProjectile(Projectile):
    def __init__(self, pos: tuple[int, int], vector: tuple[int, int], entities: list[Entity]) -> None:
        super().__init__(pos, vector, entities)
        self.damage = 2
        self.texture = pygame.image.load('assets/super_projectile.png').convert_alpha()
        self.texture = pygame.transform.scale(self.texture, (PROJECTILE_SIZE, PROJECTILE_SIZE))
        self.aabb = self.texture.get_rect(midbottom = pos)    