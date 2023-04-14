from Entity import Entity
import random

def modifyAngleWithAccuracy(accuracy, turn_angle):
    return turn_angle * random.uniform(accuracy, 2 - accuracy)

class Projectile(Entity):
    def __init__(self, weapon, x, y, turn_angle, damage, width, height, speed, sprite):
        self.weapon = weapon
        self.x = x
        self.y = y
        self.speed = speed
        self.width = width
        self.height = height
        self.turn_angle = turn_angle
        self.damage = damage
        Entity.__init__(self, sprite)

class Weapon(Entity):
    def __init__(self, damage, speed, accuracy, cooldown, sprite, laying_sprite, sound):
        self.damage = damage
        self.speed = speed
        self.accuracy = accuracy
        self.cooldown = cooldown
        self.sound = sound
        self.laying_sprite = laying_sprite
        Entity.__init__(self, sprite)
    def get_laying_entity(self, x, y, turn_angle):
        return Laying_Weapon(self, x, y, turn_angle, self.laying_sprite)

class Laying_Weapon(Entity):
    def __init__(self, weapon, x, y, turn_angle, sprite):
        self.weapon = weapon
        self.x = x
        self.y = y
        self.turn_angle = turn_angle
        Entity.__init__(self, sprite)

class Pistol(Weapon):
    def __init__(self):
        Weapon.__init__(self, 3, 24, 0.97, 15, "Assets\Sprites\Pistol.png", "", "Assets\Sounds\Pistol_Sound.mp3")
    def shoot(self, x, y, turn_angle):
        return [Projectile(self, x, y, modifyAngleWithAccuracy(self.accuracy, turn_angle), self.damage, 5, 10, self.speed, "Assets\Sprites\Bullet.png")]

class Heavy_Pistol(Weapon):
    def __init__(self):
        Weapon.__init__(self, 20, 20, 0.98, 25, "Assets\Sprites\Heavy_Pistol.png", "Assets\Sprites\Heavy_Pistol_Laying.png", "Assets\Sounds\Heavy_Pistol_Sound.mp3")
    def shoot(self, x, y, turn_angle):
        return [Projectile(self, x, y, modifyAngleWithAccuracy(self.accuracy, turn_angle), self.damage, 5, 10, self.speed, "Assets\Sprites\Heavy_Bullet.png")]

class Uzi(Weapon):
    def __init__(self):
        Weapon.__init__(self, 2, 20, 0.75, 6, r"Assets\Sprites\Uzi.png", r"Assets\Sprites\Uzi_Laying.png",  r"Assets\Sounds\Uzi_Sound.mp3")
    def shoot(self, x, y, turn_angle):
        return [Projectile(self, x, y, modifyAngleWithAccuracy(self.accuracy, turn_angle), self.damage, 5, 10, self.speed, "Assets\Sprites\Bullet.png")]

class Double_Barrel(Weapon):
    def __init__(self):
        Weapon.__init__(self, 2, 18, 0.75, 48, "Assets\Sprites\DoubleBarrel.png", "Assets\Sprites\DoubleBarrel_Laying.png", "Assets\Sounds\DoubleBarrel_Sound.mp3")
    def shoot(self, x, y, turn_angle):
        projectiles = []
        for i in range(6):
          projectiles.append(Projectile(self, x, y, modifyAngleWithAccuracy(self.accuracy, turn_angle), self.damage, 5, 10, self.speed, "Assets\Sprites\Bullet.png"))
        return projectiles

class M16(Weapon):
    def __init__(self):
        Weapon.__init__(self, 2, 22, 0.92, 9, "Assets\Sprites\M16.png", "Assets\Sprites\M16_Laying.png", "Assets\Sounds\M16_Sound.mp3")
    def shoot(self, x, y, turn_angle):
        return [Projectile(self, x, y, modifyAngleWithAccuracy(self.accuracy, turn_angle), self.damage, 5, 10, self.speed, "Assets\Sprites\Bullet.png")]