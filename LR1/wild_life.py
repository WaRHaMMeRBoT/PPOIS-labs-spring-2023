import time
import threading
# import pygame
from SRC.Map.map import Map
from SRC.Utility.coordinates2d import Coord2d

'''pygame.init()
screen = pygame.display.set_mode((959,546))
pygame.display.set_caption("Wild Life")
pygame.display.set_icon(pygame.image.load('image/main_icon.png'))'''

running = True

class Game:
    def __init__(self, height=35, width=35):
        self.map = Map(height, width)

    def next(self):

        self.map.reset_turn_sequence()

        for entity in self.map.entity_list:
            entity.action(self.map)

        self.map.update()

    '''def cicly(self):

        while(True):

            self.map.reset_turn_sequence()

            for entity in self.map.entity_list:
                entity.action(self.map)

            self.map.update()

            time.sleep(4)

    def pause(pause):
        pause=0'''

    def render(self):
        self.map.print_map()

    def add_entity(self, idf, count=1):
        count = int(count)
        [self.map.add_entity(idf) for _ in range(count)]

    def save(self, filename):
        f = open(filename, 'w')
        for entity in self.map.entity_list:
            out = entity.get_idf() + ' ' + str(entity.get_coords().x) + ' ' + str(entity.get_coords().y) + '\n'
            f.write(out)
        f.close()

    def load(self, filename):
        self.map.clear_state()
        f = open(filename, 'r')
        entities = f.readlines()
        for entity in entities:
            params = entity.split()
            x, y = int(params[1]), int(params[2])
            self.map.add_entity(params[0], Coord2d(x, y))
        self.map.update()
        f.close()


if __name__ == '__main__':
    game = Game(35, 50)


    game.render()

    '''while running:

        pygame.display.update()

        screen.blit(pygame.image.load('image/phon.png'),(0,0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()'''
