from Entity import Entity
from Weapons import Pistol
from Environment import Corpse
import math

class Player(Entity):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed = 2
        self.max_health = 5
        self.current_health = self.max_health
        self.size = 24
        self.cooldown = 0
        self.current_weapon = Pistol()
        self.turn_angle = 0
        Entity.__init__(self, self.current_weapon.sprite)
    def use_weapon(self):
        if (self.cooldown <= 0):
            self.cooldown = self.current_weapon.cooldown
            return self.current_weapon.shoot(self.x, self.y, self.turn_angle)
    def change_weapon(self, weapon):
        self.current_weapon = weapon
        self.sprite = weapon.sprite
    def decrement_cooldown(self):
        self.cooldown -= 1
    def move_right(self):
        self.x += self.speed
    def move_left(self):
        self.x -= self.speed
    def move_up(self):
        self.y -= self.speed
    def move_down(self):
        self.y += self.speed
    def fix_player_coords(self, width, height):
        self.x = max(0, min(self.x, width))
        self.y = max(0, min(self.y, height))
    def reduce_cooldown(self):
        self.cooldown -= 1
    def update_angle(self, mouse_x, mouse_y):
        dx = mouse_x - self.x
        dy = mouse_y - self.y
        self.turn_angle = math.atan2(dy, dx)
    def get_corpse(self):
        return Corpse(self.x, self.y, "Assets\Sprites\Dead.png", self.turn_angle)