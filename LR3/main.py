import pygame
from settings.states import Game

# MAIN GAME
game = Game()

if __name__ == '__main__':
    game.start_game()
pygame.quit()
