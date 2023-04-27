import random
import enemy
from manager import Background


class Wave:
    def __init__(self, enemies, screen, amount, posX, maxY, *groups):
        self.enemies = enemies
        self.amount = amount
        self.groups = groups
        self.screen = screen
        self.posX = posX
        self.maxY = maxY

    def start_wave(self, target):
        for i in range(self.amount):
            a = random.randint(0, 1)
            b = random.randint(0, 1)
            if a and b:
                x = random.randint(-100 - int(Background.display_scroll[0]), 0 - int(Background.display_scroll[0]))
                y = random.randint(-100 - int(Background.display_scroll[1]),
                                   self.maxY + 100 - int(Background.display_scroll[1]))
            if a and not b:
                x = random.randint(self.posX - int(Background.display_scroll[0]),
                                   self.posX + 100 - int(Background.display_scroll[0]))
                y = random.randint(-100 - int(Background.display_scroll[1]),
                                   self.maxY + 100 - int(Background.display_scroll[1]))
            if b and not a:
                x = random.randint(-100 - int(Background.display_scroll[0]),
                                   self.posX + 100 - int(Background.display_scroll[0]))
                y = random.randint(-100 - int(Background.display_scroll[1]), 0 - int(Background.display_scroll[1]))
            if not a and not b:
                x = random.randint(-100 - int(Background.display_scroll[0]),
                                   self.posX + 100 - int(Background.display_scroll[0]))
                y = random.randint(self.maxY - int(Background.display_scroll[1]),
                                   self.maxY + 100 - int(Background.display_scroll[1]))

            index = random.randint(0, len(self.enemies) - 1)
            type = self.enemies[index]
            if type == "walker":
                enemy.Enemy(self.screen, x, y, target)
            elif type == "crawler":
                enemy.Crawler(self.screen, x, y, target)
            elif type == "brute":
                enemy.Brute(self.screen, x, y, target)
            elif type == "spider":
                enemy.Spider(self.screen, x, y, target)
            elif type == "runner":
                enemy.Runner(self.screen, x, y, target)
            elif type == "motorcycle":
                enemy.Motorcycle(self.screen, x, y, target)
            elif type == "helicopter":
                enemy.Helicopter(self.screen, x, y, target)
