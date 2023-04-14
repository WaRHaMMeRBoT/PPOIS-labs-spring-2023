import math
import random

class HelperFunctions:
    def build_angled_rectangle(pygame, width, height, angle):
        rect_surface = pygame.Surface((width, height))
        rect_surface.fill((255, 0, 0))
        return pygame.transform.rotate(rect_surface, angle*180/math.pi - 90)
    def get_random_border_point(window_width, window_height):
        border = random.randint(0, 3)
    
        if border == 0:
            x = random.randint(0, window_width)
            y = 0
        elif border == 1:
            x = window_width
            y = random.randint(0, window_height)
        elif border == 2:
            x = random.randint(0, window_width)
            y = window_height
        else:
            x = 0
            y = random.randint(0, window_height)
        return (x, y)

    def collide(x, y, entity):
        return (x <= entity.x + entity.size / 2) and (x >= entity.x - entity.size / 2) and (y <= entity.y + entity.size / 2) and (y >= entity.y - entity.size / 2)
    
    def intersect (entity_1, entity_2):
        return HelperFunctions.collide(entity_1.x - entity_1.size / 3, entity_1.y - entity_1.size / 3, entity_2) or HelperFunctions.collide(entity_1.x + entity_1.size / 3, entity_1.y - entity_1.size / 3, entity_2) or HelperFunctions.collide(entity_1.x - entity_1.size / 3, entity_1.y + entity_1.size / 3, entity_2) or HelperFunctions.collide(entity_1.x + entity_1.size / 3, entity_1.y + entity_1.size / 3, entity_2)