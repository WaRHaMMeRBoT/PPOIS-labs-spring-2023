class Stats:
    def __init__(self, health: int, speed: int, damage: int, sight: int):
        self.health = health
        self.currentHealth = health / 2
        self.speed = speed
        self.damage = damage
        self.sight = sight
