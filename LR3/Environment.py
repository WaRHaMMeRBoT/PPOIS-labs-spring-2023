from Entity import Entity
import math

class Popup():
    def __init__(self, value, x, y, initial_size):
        self.value = value
        self.x = x
        self.y = y
        self.initial_size = initial_size
        self.scale = 1

class Corpse(Entity):
    def __init__(self, x, y, sprite, turn_angle):
        self.x = x
        self.y = y
        self.sprite = sprite
        self.turn_angle = turn_angle - math.pi