from game import *
from projectile import Bullet
import random
import toolbox
import  menu

class Weapon:
    def __init__(self, type: str, shoot_cooldown_max: int,  ammo_count_max: int, reload_cooldown_max: int, damage:int, speed:int, image:str, shoot_sound:str):
        self.type = type

        self.shoot_cooldown = 0
        self.shoot_cooldown_max = shoot_cooldown_max
        self.start_shoot_cd = self.shoot_cooldown_max

        self.ammo_count_max = ammo_count_max
        self.ammo_count = self.ammo_count_max

        self.reload_cooldown = 0
        self.reload_cooldown_max = reload_cooldown_max
        self.start_reload_cd = self.reload_cooldown_max

        self.ammo_speed = speed
        self.damage = damage

        self.image = image
        self.shoot_sound = shoot_sound
        self.reload_sound = 'reload.mp3'

    def shoot(self, player):
        if self.ammo_count > 0:
            if self.type == 'gun':
                Bullet(player.screen, player.x, player.y, player.angle, self.damage, self.ammo_speed)

            if self.type == 'shotgun':
                Bullet(player.screen, player.x, player.y, player.angle, self.damage, self.ammo_speed)
                Bullet(player.screen, player.x, player.y, player.angle + 3, self.damage, self.ammo_speed)
                Bullet(player.screen, player.x, player.y, player.angle - 3, self.damage, self.ammo_speed)
                Bullet(player.screen, player.x, player.y, player.angle + 6, self.damage, self.ammo_speed)
                Bullet(player.screen, player.x, player.y, player.angle - 6, self.damage, self.ammo_speed)
                self.ammo_count -= 1

            if self.type == 'snipe':
                Bullet(player.screen, player.x, player.y, player.angle,  self.damage, self.ammo_speed)
                self.ammo_count -=1

            if self.type == 'machine':
                angle = random.uniform(player.angle - 10, player.angle + 10)
                Bullet(player.screen, player.x, player.y, angle, self.damage, self.ammo_speed)
                self.ammo_count -=1

            toolbox.playSound(self.shoot_sound)

    def reload(self):
        self.ammo_count = self.ammo_count_max


    def draw_reload(self, screen, x, y):
        reload_percentage = int(self.reload_cooldown / self.reload_cooldown_max* 359)

        pygame.gfxdraw.arc(screen, int(x), int(y), 22, -90, reload_percentage - 90, (255, 255, 255))
        pygame.gfxdraw.arc(screen, int(x), int(y), 23, -90, reload_percentage - 90, (255, 255, 255))

    def draw_ammo(self, x, y):
        if self.type != 'gun':
            menu.print_text(f'{self.ammo_count}/{self.ammo_count_max}', x+18, y+18, font_type="Qore.otf", font_clr=(255,255,255), font_size=15)