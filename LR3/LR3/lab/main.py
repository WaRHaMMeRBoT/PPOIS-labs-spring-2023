import pygame
import pygame.locals as pg_locals
import pygame_menu
import pygame_gui
from pygame_gui.elements.ui_text_entry_line import UITextEntryLine

from pygame.rect import Rect
from leaderboard import Leaderboard


from constants import FPS, BLACK, WIDTH, HEIGHT
from game import Game

pygame.init()

class Menu:

    def __init__(self):
        self.engine = None

        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.menu_screen = pygame_menu.Menu('Пакман', WIDTH, HEIGHT, theme=pygame_menu.themes.THEME_BLUE)

        self.score_screen = pygame_menu.Menu('Пакман', WIDTH, HEIGHT, theme=pygame_menu.themes.THEME_BLUE)
        self.leaderboard_screen = pygame_menu.Menu('Лидеры', WIDTH, HEIGHT, theme=pygame_menu.themes.THEME_BLUE)

        #self.info_screen = pygame.display.set_mode((WIDTH, HEIGHT))

        self.menu_screen.add.button('Начать игру', self.start_game)
        self.menu_screen.add.button('Таблица лидеров', self.leaders)
        self.menu_screen.add.button('Справка', self.info)


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
        self.save_score()
        self.score_screen.add.button("Перезапустить игру", self.run)
        self.score_screen.add.button("Вернуться в меню", self.back_to_menu)
        self.score_screen.add.button("Выход", pygame_menu.events.EXIT)
        self.score_screen.mainloop(self.screen)

        pygame.quit()
        
    
    def info(self):
        
        self.menu_screen.clear()
        info = '''
        Задача игрока — управляя Пакманом, съесть все точки в лабиринте,
        избегая встречи с привидениями, которые гоняются за героем.
        Набрав рекордное количество очков Вы попадаете в таблицу лидеров!
        '''
        self.menu_screen.add.label(info, font_size=40, font_color=(0, 0, 204))
        
        self.menu_screen.add.button('Назад', self.back_to_menu)
        pygame.display.flip()
        
        
    def leaders(self):
        import json
        data = {}
        with open('score.json', 'r') as f:
            data = json.load(f)
        
        sorted_scores = sorted(data.items(), key=lambda x:x[1], reverse=True)
        self.menu_screen.clear()
        print('!!!!!!!11')
        for position, item in enumerate(sorted_scores):
            name, score = item
            self.menu_screen.add.label(f'{position + 1}. {name} - {score}', font_size=100, font_color=(0, 0, 204))
        
        self.menu_screen.add.button('Назад', self.back_to_menu)
        pygame.display.flip()

    def back_to_menu(self):
        self.menu_screen.clear()
        self.menu_screen.add.button('Начать игру', self.start_game)
        self.menu_screen.add.button('Таблица лидеров', self.leaders)

        self.menu_screen.add.button('Справка', self.info)


        self.menu_screen.add.button('Выход', pygame_menu.events.EXIT)

        self.menu_screen.mainloop(self.screen)
        

        
    def score_event(self):
        # pygame.init() will initialize all
        # imported module
        clock = pygame.time.Clock()

        # it will display on screen        
        # basic font for user typed
        base_font = pygame.font.Font(None, 32)
        user_text = ''
        
        # create rectangle

        input_rect = pygame.Rect(WIDTH // 2, HEIGHT // 2, 1000, 50)
        
        # color_active stores color(lightskyblue3) which
        # gets active when input box is clicked by user
        color_active = pygame.Color('lightskyblue3')
        
        # color_passive store color(chartreuse4) which is
        # color of input box.
        color_passive = pygame.Color('chartreuse4')
        color = color_passive
        
        active = False

        while True:
            for event in pygame.event.get():
        
            # if user types QUIT then the screen will close
                if event.type == pygame.QUIT:
                    pygame.quit()
        
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if input_rect.collidepoint(event.pos):
                        active = True
                    else:
                        active = False
        
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        self.dump_json(user_text)
                        return user_text
                    # Check for backspace
                    if event.key == pygame.K_BACKSPACE:
        
                        # get text input from 0 to -1 i.e. end.
                        user_text = user_text[:-1]
        
                    # Unicode standard is used for string
                    # formation
                    else:
                        user_text += event.unicode
            
            # it will set background color of screen
            self.screen.fill((255, 255, 255))
        
            if active:
                color = color_active
            else:
                color = color_passive
                
            # draw rectangle and argument passed which should
            # be on screen
            pygame.draw.rect(self.screen, color, input_rect)
        
            text_surface = base_font.render(user_text, True, (255, 255, 255))
            
            # render at position stated in arguments
            self.screen.blit(text_surface, (input_rect.x+5, input_rect.y+5))
            
            # set width of textfield so that text cannot get
            # outside of user's text input
            input_rect.w = max(100, text_surface.get_width()+10)
            
            # display.flip() will update only a portion of the
            # screen to updated, not full area
            pygame.display.flip()
            
            # clock.tick(60) means that for every second at most
            # 60 frames should be passed.
            clock.tick(60)
            
    def dump_json(self, name):
        import json
        with open('score.json', '+r') as f:
            try:
                score = json.load(f)
            except Exception:
                score = {}
        score[name] = self.engine.score
        with open('score.json', 'w') as f:
            json.dump(score, f)
            
    
    def save_score(self):
        import json
        score = {}
        with open('score.json', '+r') as f:
            try:
                score = json.load(f)
            except Exception:
                score = None
        if not score:
            self.score_screen.add.label(" Рекорд!", font_size=100, font_color=(0, 0, 204))
            self.score_screen.add.button("Ввести имя для таблицы рекордов", self.score_event)
        else:
            highest_player = max(score, key=score.get)
            if self.engine.score > score.get(highest_player):
                self.score_screen.add.label("Рекорд!", font_size=100, font_color=(0, 0, 204))
                self.score_screen.add.button("Ввести имя для таблицы рекордов", self.score_event)



    def start_game(self):
        self.run()

def run():
    menu = Menu()

if __name__ == "__main__":
    run()

