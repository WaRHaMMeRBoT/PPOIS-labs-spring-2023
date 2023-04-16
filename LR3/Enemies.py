from Entity import Entity
from Environment import Corpse
import math
import random

class Enemy(Entity):
    def __init__(self, x, y, speed, max_health, size, sprite, dead_sprite):
        self.x = x
        self.y = y
        self.speed = speed
        self.max_health = max_health
        self.current_health = max_health
        self.size = size
        self.cooldown = 0
        self.turn_angle = 0
        self.dead_sprite = dead_sprite
        Entity.__init__(self, sprite)
    def update_angle(self, target_x, target_y):
        dx = target_x - self.x
        dy = target_y - self.y
        self.turn_angle = math.atan2(dy, dx)
    def take_damage(self, damage):
        self.current_health -= damage
    def get_corpse(self):
        return Corpse(self.x, self.y, self.dead_sprite, self.turn_angle)

class Close_Slow_Enemy(Enemy):
    def __init__(self, x, y):
        Enemy.__init__(self, x, y, 1, 2, 24, "Assets\Sprites\EnemyCloseSlow.png", "Assets\Sprites\CloseSlowDead.png")
    def get_move_result(self):
        y = self.speed * math.sin(self.turn_angle)
        x = self.speed * math.cos(self.turn_angle)
        return x, y

class Close_Slow_Upgraded_Enemy(Enemy):
    def __init__(self, x, y):
        Enemy.__init__(self, x, y, 1.1, 2, 24, "Assets\Sprites\EnemyCloseSlow2.png", "Assets\Sprites\CloseSlowDead2.png")
    def get_move_result(self):
        y = self.speed * math.sin(self.turn_angle)
        x = self.speed * math.cos(self.turn_angle)
        return x, y

class Close_Slow_Superior_Enemy(Enemy):
    def __init__(self, x, y):
        Enemy.__init__(self, x, y, 1.2, 3, 24, "Assets\Sprites\EnemyCloseSlow3.png", "Assets\Sprites\CloseSlowDead3.png")
    def get_move_result(self):
        y = self.speed * math.sin(self.turn_angle)
        x = self.speed * math.cos(self.turn_angle)
        return x, y

class Close_Chunky_Enemy(Enemy):
    def __init__(self, x, y):
        Enemy.__init__(self, x, y, 0.9, 7, 24, "Assets\Sprites\EnemyCloseChunky.png", "Assets\Sprites\CloseChunkyDead.png")
    def get_move_result(self):
        y = self.speed * math.sin(self.turn_angle)
        x = self.speed * math.cos(self.turn_angle)
        return x, y

class Close_Fast_Enemy(Enemy):
    def __init__(self, x, y):
        Enemy.__init__(self, x, y, 2.2, 2, 22, "Assets\Sprites\EnemyCloseFast.png", "Assets\Sprites\CloseFastDead.png")
    def get_move_result(self):
        y = self.speed * math.sin(self.turn_angle)
        x = self.speed * math.cos(self.turn_angle)
        return x, y

class Inspector_Chunky_Enemy(Enemy):
    def __init__(self, x, y):
        Enemy.__init__(self, x, y, 1, 9, 26, "Assets\Sprites\ChunkyInspector.png", "Assets\Sprites\InspectorDead.png")
    def get_move_result(self):
        y = self.speed * math.sin(self.turn_angle)
        x = self.speed * math.cos(self.turn_angle)
        if random.randint(0,3) == 3:
            y += self.speed * math.sin(self.turn_angle)
            x += self.speed * math.cos(self.turn_angle)
        return x, y

class Inspector_Chunky_Upgraded_Enemy(Enemy):
    def __init__(self, x, y):
        Enemy.__init__(self, x, y, 1, 11, 26, "Assets\Sprites\ChunkyInspector2.png", "Assets\Sprites\InspectorDead2.png")
    def get_move_result(self):
        y = self.speed * math.sin(self.turn_angle)
        x = self.speed * math.cos(self.turn_angle)
        if random.randint(0,3) == 3:
            y += self.speed * math.sin(self.turn_angle)
            x += self.speed * math.cos(self.turn_angle)
        return x, y

class Waiter_Average_Enemy(Enemy):
    def __init__(self, x, y):
        Enemy.__init__(self, x, y, 1.7, 4, 24, "Assets\Sprites\EnemyCloseAveragWBottle.png", "Assets\Sprites\WaiterDead.png")
    def get_move_result(self):
        y = self.speed * math.sin(self.turn_angle)
        x = self.speed * math.cos(self.turn_angle)
        rand = random.randint(0,3)
        if rand == 3:
            y = 0
            x += self.speed * math.cos(self.turn_angle)
        elif rand == 2:
            x = 0
            y += self.speed * math.cos(self.turn_angle)
        return x, y

class Close_Fast_Knife_Enemy(Enemy):
    def __init__(self, x, y):
        Enemy.__init__(self, x, y, 2.8, 1, 22, "Assets\Sprites\EnemyCloseFastWknife.png", "Assets\Sprites\CloseFastDead.png")
    def get_move_result(self):
        y = self.speed * math.sin(self.turn_angle)
        x = self.speed * math.cos(self.turn_angle)
        if random.randint(0,2) == 2:
            x = 0
            y = 0
        return x, y
class Police_Average_Enemy(Enemy):
    def __init__(self, x, y):
        Enemy.__init__(self, x, y, 1.9, 3, 22, "Assets\Sprites\EnemyClosePoliceWStick.png", "Assets\Sprites\PoliceDead.png")
    def get_move_result(self):
        temp_speed = self.speed
        if random.randint(0,2) == 2:
            temp_speed = temp_speed * 2
        y = temp_speed * math.sin(self.turn_angle)
        x = temp_speed * math.cos(self.turn_angle)
        return x, y