import pygame
import pygame_menu

from lr3.constants import FPS, BLACK, WIDTH, HEIGHT
from lr3.game import Game

pygame.init()


class Menu:

    def __init__(self):
        self.engine = None

        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.menu_screen = pygame_menu.Menu('Пакман', WIDTH, HEIGHT, theme=pygame_menu.themes.THEME_BLUE)

        self.score_screen = pygame_menu.Menu('Пакман', WIDTH, HEIGHT, theme=pygame_menu.themes.THEME_BLUE)

        self.menu_screen.add.button('Начать игру', self.start_game)

        self.menu_screen.add.button('Выход', pygame_menu.events.EXIT)

        self.menu_screen.mainloop(self.screen)

    def run(self):
        running = True
        self.engine = Game(self.menu_screen)
        self.score_screen.clear()
        while running:
            self.engine.clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            if self.engine.player_dead:
                running = False

            self.engine.player_collision()
            self.engine.ghost_collision(self.engine.red)
            self.engine.ghost_collision(self.engine.pink)
            self.engine.ghost_collision(self.engine.blue)
            self.engine.ghost_collision(self.engine.orange)

            self.engine.pink.find_pacman(self.engine.player)
            self.engine.blue.find_pacman(self.engine.player)
            self.engine.orange.find_pacman(self.engine.player)
            self.engine.red.find_pacman(self.engine.player)

            self.engine.screen.fill(BLACK)

            self.engine.pacman.update()
            self.engine.pacman.draw(self.engine.screen)
            pygame.display.flip()

        self.score_screen.add.label("Ваш счет: " + str(self.engine.score), font_size=100, font_color=(0, 0, 204))
        self.score_screen.add.button("Перезапустить игру", self.run)
        self.score_screen.add.button("Выход", pygame_menu.events.EXIT)
        self.score_screen.mainloop(self.screen)

        pygame.quit()

    def start_game(self):
        self.run()

def run():
    menu = Menu()

if __name__ == "__main__":
    run()

