import pygame
from entity.abstract import Entity
from entity.projectiles import Projectile, SuperProjectile
from main import\
DELTA,\
ENTITY_SIZE,\
PLAYER_HEALTH,\
PLAYER_SPEED,\
PROJECTILE_SPEED,\
SCREEN_HEIGHT,\
SCREEN_WIDTH,\
SHOOT, \
TPS

MOVE_LEFT = pygame.K_LEFT
MOVE_RIGHT = pygame.K_RIGHT

class Player(Entity):
    def __init__(self) -> None:
        self.texture = pygame.image.load('assets/player.png').convert_alpha()
        self.texture = pygame.transform.scale(self.texture, (ENTITY_SIZE, ENTITY_SIZE))
        self.aabb = self.texture.get_rect(midbottom = (SCREEN_WIDTH / 2, SCREEN_HEIGHT - 24))
        self.health = PLAYER_HEALTH
        self.last_movement = None
        self.movement = {
                MOVE_LEFT: False,
                MOVE_RIGHT: False
        }
        self.projectiles = []
        self.score = 0
        self.shotgun_timer = 0
        self.super_timer = 0

    def update(self):
        self.projectiles = list(filter(lambda proj: proj.health > 0, self.projectiles))
        
        for projectile in self.projectiles:
            projectile.update()

        if self.shotgun_timer > 0:
            self.shotgun_timer -= 1
        if self.super_timer > 0:
            self.super_timer -= 1

        if self.movement[MOVE_LEFT] and ((self.last_movement == MOVE_LEFT) or (self.last_movement is None)):
            self.aabb.x -= PLAYER_SPEED / DELTA
        if self.movement[MOVE_RIGHT] and ((self.last_movement == MOVE_RIGHT) or (self.last_movement is None)):
            self.aabb.x += PLAYER_SPEED / DELTA

        if self.aabb.right > SCREEN_WIDTH: self.aabb.right = SCREEN_WIDTH
        if self.aabb.left < 0: self.aabb.left = 0

    def shoot(self, enemies):
        pygame.mixer.Sound.play(SHOOT)
        new_projectile = Projectile(self.aabb.midtop, (0, -PROJECTILE_SPEED / DELTA), enemies)
        self.projectiles.append(new_projectile)
    
    def shoot_shotgun(self, enemies):
        if self.shotgun_timer > 0:
            return
        pygame.mixer.Sound.play(SHOOT)
        new_projectile1 = Projectile(self.aabb.midtop, (0, -PROJECTILE_SPEED / DELTA), enemies)
        new_projectile2 = Projectile(self.aabb.midtop, (0.25 * -PROJECTILE_SPEED / DELTA, -PROJECTILE_SPEED / DELTA), enemies)
        new_projectile3 = Projectile(self.aabb.midtop, (0.25 * PROJECTILE_SPEED / DELTA, -PROJECTILE_SPEED / DELTA), enemies)
        self.projectiles.append(new_projectile1)
        self.projectiles.append(new_projectile2)
        self.projectiles.append(new_projectile3)
        self.shotgun_timer = 3 * TPS
   
    def shoot_super(self, enemies):
        if self.super_timer > 0:
            return
        pygame.mixer.Sound.play(SHOOT)
        new_projectile = SuperProjectile(self.aabb.midtop, (0, 0.5 * -PROJECTILE_SPEED / DELTA), enemies)
        self.projectiles.append(new_projectile)
        self.super_timer = 3 * TPS

    def draw(self, surface: pygame.Surface):
        for projectile in self.projectiles:
            projectile.draw(surface)
        surface.blit(self.texture, self.aabb)