import json
from tkinter import *

from enemies import *
from player import Player

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 576

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)


class Game(object):
    def __init__(self):
        self.font = pygame.font.Font(None, 40)
        self.about = False
        self.game_over = True
        self.leaderboard = False
        self.score = 0
        self.font = pygame.font.Font(None, 35)
        self.menu = Menu(("Start", "Leaderboard", "About", "Exit"), font_color=WHITE, font_size=60)
        self.player = Player(32, 128, "player.png")
        self.horizontal_blocks = pygame.sprite.Group()
        self.vertical_blocks = pygame.sprite.Group()
        self.dots_group = pygame.sprite.Group()
        for i, row in enumerate(enviroment()):
            for j, item in enumerate(row):
                if item == 1:
                    self.horizontal_blocks.add(Block(j * 32 + 8, i * 32 + 8, BLACK, 16, 16))
                elif item == 2:
                    self.vertical_blocks.add(Block(j * 32 + 8, i * 32 + 8, BLACK, 16, 16))
        self.enemies = pygame.sprite.Group()
        self.enemies.add(Slime(288, 96, 0, 2))
        self.enemies.add(Slime(288, 320, 0, -2))
        self.enemies.add(Slime(544, 128, 0, 2))
        self.enemies.add(Slime(32, 224, 0, 2))
        self.enemies.add(Slime(160, 64, 2, 0))
        self.enemies.add(Slime(448, 64, -2, 0))
        self.enemies.add(Slime(640, 448, 2, 0))
        self.enemies.add(Slime(448, 320, 2, 0))
        for i, row in enumerate(enviroment()):
            for j, item in enumerate(row):
                if item != 0:
                    self.dots_group.add(Ellipse(j * 32 + 12, i * 32 + 12, WHITE, 8, 8))

        self.pacman_sound = pygame.mixer.Sound("pacman_sound.ogg")
        self.game_over_sound = pygame.mixer.Sound("game_over_sound.ogg")
        self.names = []
        self.scores = []
        with open('leaderboard.json') as f:
            templates = json.load(f)
            names_1 = templates['name']
            scores_1 = templates['score']

        for ind in range(len(names_1)):
            self.names.append(names_1[ind])
            self.scores.append(scores_1[ind])
        allleaders = ""
        for amount in range(len(names_1)):
            nummax = max(scores_1)
            ind = scores_1.index(nummax)
            stroka = names_1[ind]
            stroka += " score - "
            stroka += str(scores_1[ind]) + " "
            allleaders += stroka
            names_1.pop(ind)
            scores_1.pop(ind)
        self.leaders = allleaders

    def save_in_game(self):
        scores_1 = []
        names_1 = []
        allleaders = ""
        for ind in range(3):
            scores_1.append(self.scores[ind])
            names_1.append(self.names[ind])
        for amount in range(len(self.names)):
            nummax = max(scores_1)
            ind = scores_1.index(nummax)
            stroka = names_1[ind]
            stroka += " score - "
            stroka += str(scores_1[ind]) + " "
            allleaders += stroka
            names_1.pop(ind)
            scores_1.pop(ind)
        self.leaders = allleaders

    def process_events(self, screen):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True
            self.menu.event_handler(event)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if self.game_over and not self.about:
                        if self.menu.state == 0:
                            #  START
                            self.__init__()
                            self.game_over = False
                        elif self.menu.state == 1:
                            self.leaderboard = True
                        elif self.menu.state == 2:
                            self.about = True
                        elif self.menu.state == 3:
                            # EXIT
                            self.save_leaders()
                            return True

                elif event.key == pygame.K_RIGHT:
                    self.player.move_right()

                elif event.key == pygame.K_LEFT:
                    self.player.move_left()

                elif event.key == pygame.K_UP:
                    self.player.move_up()

                elif event.key == pygame.K_DOWN:
                    self.player.move_down()

                elif event.key == pygame.K_ESCAPE:
                    self.game_over = True
                    self.about = False
                    self.leaderboard = False

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    self.player.stop_move_right()
                elif event.key == pygame.K_LEFT:
                    self.player.stop_move_left()
                elif event.key == pygame.K_UP:
                    self.player.stop_move_up()
                elif event.key == pygame.K_DOWN:
                    self.player.stop_move_down()

            elif event.type == pygame.MOUSEBUTTONDOWN:
                self.player.explosion = True
                self.check_record(screen)
                self.save_in_game()

        return False

    def run_logic(self, screen):
        if not self.game_over:
            self.player.update(self.horizontal_blocks, self.vertical_blocks)
            block_hit_list = pygame.sprite.spritecollide(self.player, self.dots_group, True)
            if len(block_hit_list) > 0:
                self.pacman_sound.play()
                self.score += 1
            block_hit_list = pygame.sprite.spritecollide(self.player, self.enemies, True)
            if len(block_hit_list) > 0:
                self.player.explosion = True
                self.game_over_sound.play()
                self.display_frame(screen)
                self.check_record(screen)
                self.save_in_game()
            self.game_over = self.player.game_over
            self.enemies.update(self.horizontal_blocks, self.vertical_blocks)

    def record_box(self, screen):
        font = pygame.font.Font(None, 32)
        clock = pygame.time.Clock()
        x = SCREEN_WIDTH / 2
        y = SCREEN_HEIGHT / 2
        input_box = pygame.Rect(x - 80, y + 30, 140, 32)
        color_inactive = pygame.Color('lightskyblue3')
        color_active = pygame.Color('dodgerblue2')
        color = color_inactive
        active = False
        text = ''
        done = False
        pygame.display.update()

        while not done:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if input_box.collidepoint(event.pos):
                        active = not active
                    else:
                        active = False
                    color = color_active if active else color_inactive
                if event.type == pygame.KEYDOWN:
                    if active:
                        if event.key == pygame.K_RETURN:
                            name = text
                            screen.fill(BLACK)
                            self.add_new_leader(name, self.score)
                            done = True
                        elif event.key == pygame.K_BACKSPACE:
                            text = text[:-1]
                        else:
                            text += event.unicode
            screen.fill((30, 30, 30))
            self.display_message(screen, "Congrats! You gain top-3 score! Enter you name!")
            txt_surface = font.render(text, True, color)
            width = max(200, txt_surface.get_width() + 10)
            input_box.w = width
            screen.blit(txt_surface, (input_box.x + 5, input_box.y + 5))
            pygame.draw.rect(screen, color, input_box, 2)
            pygame.display.flip()
            clock.tick(30)

    def check_record(self, screen):
        our_bool = False
        list_score = []
        for ind in range(3):
            list_score.append(self.scores[ind])
        for i in range(3):
            if max(list_score) < self.score:
                screen.fill(BLACK)
                x = SCREEN_WIDTH / 2
                y = SCREEN_HEIGHT / 4
                self.display_message(screen, "Congrats! You gain top-3 score! Enter you name!")
                self.record_box(screen)
                break
            else:
                list_score.pop(list_score.index(max(list_score)))

    def display_frame(self, screen):
        screen.fill(BLACK)
        if self.game_over:
            if self.about:
                self.display_message(screen, "This is arcade game Pacman")
                self.display_messagepos(screen,"Controls: Leftkey, rightkey, upkey, downkey", x=SCREEN_WIDTH/2,y=SCREEN_HEIGHT/2 + 30)
                self.display_messagepos(screen, "You need to avoid enemies and collect all the dots", x=SCREEN_WIDTH / 2,
                                        y=SCREEN_HEIGHT / 2 + 60)
            elif self.leaderboard:
                self.display_message(screen, self.leaders)
            else:
                self.menu.display_frame(screen)
        else:
            self.horizontal_blocks.draw(screen)
            self.vertical_blocks.draw(screen)
            draw_enviroment(screen)
            self.dots_group.draw(screen)
            self.enemies.draw(screen)
            screen.blit(self.player.image, self.player.rect)
            text = self.font.render("Score: " + str(self.score), True, GREEN)
            screen.blit(text, [120, 20])

        pygame.display.flip()

    def display_message(self, screen, message, color=(255, 0, 0)):
        label = self.font.render(message, True, color)
        width = label.get_width()
        height = label.get_height()
        posX = (SCREEN_WIDTH / 2) - (width / 2)
        posY = (SCREEN_HEIGHT / 2) - (height / 2)
        screen.blit(label, (posX, posY))

    def display_messagepos(self, screen, message, color=(255, 0, 0), x=int, y=int):
        label = self.font.render(message, True, color)
        width = label.get_width()
        height = label.get_height()
        posX = x - (width / 2)
        posY = y - (height / 2)
        screen.blit(label, (posX, posY))

    def add_new_leader(self, name=str, score=int):
        nickname = self.names
        our_scores = []
        for j in range(3):
            our_scores.append(self.scores[j])
        if len(self.names) < 3 and len(self.scores) < 3:
            self.names.append(name)
            self.scores.append(score)
            return True
        else:
            for i in range(3):
                if score > max(our_scores):
                    ind = self.scores.index(max(our_scores))
                    self.scores[ind] = score
                    self.names[ind] = name
                    break

                our_scores.pop(our_scores.index(max(our_scores)))
        self.save_leaders()
        return True

    def save_leaders(self):
        data = {}
        data['name'] = []
        data['score'] = []

        for num in range(len(self.names)):
            data['name'].append(self.names[num])
            data['score'].append(self.scores[num])
        with open("leaderboard.json", 'w') as outfile:
            json.dump(data, outfile)


class Menu(object):
    state = 0

    def __init__(self, items, font_color=(0, 0, 0), select_color=(255, 0, 0), ttf_font=None, font_size=25):
        self.font_color = font_color
        self.select_color = select_color
        self.items = items
        self.font = pygame.font.Font(ttf_font, font_size)

    def display_frame(self, screen):
        for index, item in enumerate(self.items):
            if self.state == index:
                label = self.font.render(item, True, self.select_color)
            else:
                label = self.font.render(item, True, self.font_color)

            width = label.get_width()
            height = label.get_height()

            posX = (SCREEN_WIDTH / 2) - (width / 2)
            t_h = len(self.items) * height
            posY = (SCREEN_HEIGHT / 2) - (t_h / 2) + (index * height)

            screen.blit(label, (posX, posY))

    def event_handler(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if self.state > 0:
                    self.state -= 1
            elif event.key == pygame.K_DOWN:
                if self.state < len(self.items) - 1:
                    self.state += 1
