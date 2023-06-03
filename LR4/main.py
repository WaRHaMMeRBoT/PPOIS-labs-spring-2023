import configparser
from time import sleep
import pygame
from config import parser
from entity import player
from utils import utils

############################################CONSTANTS###################################################################
TPS = 60
SCREEN_WIDTH = 960
SCREEN_HEIGHT = 540
ENTITY_SIZE = 48
PROJECTILE_SIZE = 8
HEALTH_SIZE = 24

DELTA = int(1000 / TPS)

PLAYER_HEALTH = 3
PLAYER_SPEED = 96 * 3 #
PROJECTILE_SPEED = 54 * 3 #
ALIEN_ATTACK_DELAY = 2 * TPS #s
ALIENS_IN_WAVE = 10
WAVES = 20
ALIEN_AREA_END = (ALIENS_IN_WAVE + 4) * 48 
ALIEN_AREA_START = 48 * 2
ALIEN_HORIZONTAL_SPEED = 4 #

pygame.mixer.init()
SHOOT = pygame.mixer.Sound('assets/shoot.wav')
SHOOT.set_volume(0.20)
DEATH = pygame.mixer.Sound('assets/explosion.wav')
DEATH.set_volume(0.75)
KILL = pygame.mixer.Sound('assets/invaderkilled.wav')
KILL.set_volume(0.15)
MUSIC = pygame.mixer.music.load('assets/music.mp3')
MUSIC = pygame.mixer.music.play(-1)

#######################################################################

def read_config(config: configparser.ConfigParser):
    config.read('config.ini')
    
    if not config.has_section('Common'):
        config.add_section('Common')
        config['Common']['HEALTH'] = f'{3}'
        config['Common']['PLAYER_SPEED'] = f'{96 * 3}'
        config['Common']['ALIEN_ATTACK_DELAY'] = f'{2}'
        config['Common']['WAVES'] = f'{20}'
        config['Common']['ALIENS_IN_WAVE'] = f'{10}'
        config['Common']['ALIENS_SPEED'] = f'{4}'
        with open('config.ini', 'w') as configfile:
            config.write(configfile)

    try:
        return \
        int(config['Common']['HEALTH']),\
        int(config['Common']['PLAYER_SPEED']),\
        int(config['Common']['ALIEN_ATTACK_DELAY']) * TPS,\
        int(config['Common']['WAVES']),\
        int(config['Common']['ALIENS_IN_WAVE']),\
        int(config['Common']['ALIENS_SPEED'])
    except:
        config.remove_section('Common')
        read_config(config)


if __name__ == '__main__':
    pygame.init()

    surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    background_texture = pygame.image.load('assets/background.png').convert_alpha()
    health_texture = pygame.image.load('assets/health.png').convert_alpha()
    health_texture = pygame.transform.scale(health_texture, (HEALTH_SIZE, HEALTH_SIZE))

    font = pygame.font.Font('assets/font.ttf', 54)
    score_font = pygame.font.Font('assets/font.ttf', HEALTH_SIZE)

    game_active = 1

    config_instance = configparser.ConfigParser()

    PLAYER_HEALTH,\
    PLAYER_SPEED,\
    ALIEN_ATTACK_DELAY,\
    WAVES,\
    ALIENS_IN_WAVE,\
    ALIEN_HORIZONTAL_SPEED = read_config(config_instance)

    scroll = 0
    username = ''
    max_score = 0
    while True:
        player_instance = player.Player()
        aliens = []
        alien_x = ALIEN_AREA_START + 1
        alien_y = 0
        alien_vector = 1
        entities = [
            player_instance
        ]
        entities.extend(parser.read_waves(player_instance, config_instance, ALIEN_AREA_START, ENTITY_SIZE, ALIENS_IN_WAVE, WAVES))

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if game_active == 0:                                                                                    #кнопочки
                    if event.type == pygame.KEYDOWN:
                        if event.key in list(player_instance.movement.keys()):
                            player_instance.last_movement = event.key
                            player_instance.movement[event.key] = True
                        if event.key == pygame.K_f:
                            enemies = list(filter(lambda entity: entity is not player_instance, entities))
                            player_instance.shoot(enemies)
                        if event.key == pygame.K_g:
                            enemies = list(filter(lambda entity: entity is not player_instance, entities))
                            player_instance.shoot_shotgun(enemies)
                        if event.key == pygame.K_h:
                            enemies = list(filter(lambda entity: entity is not player_instance, entities))
                            player_instance.shoot_super(enemies)
                    if event.type == pygame.KEYUP:
                        if event.key in list(player_instance.movement.keys()):
                            player_instance.last_movement = None
                            player_instance.movement[event.key] = False

            if game_active == 4:                                                                                        #рекорд
                if event.type == pygame.TEXTINPUT:
                    username += event.text
                    sleep(0.1)
                if pygame.key.get_pressed()[pygame.K_RETURN]:                                    
                    game_active = 1
                    parser.update_leaderboard(config_instance, (username, str(max_score)))
                    username = ''
                if pygame.key.get_pressed()[pygame.K_BACKSPACE]:
                    username = username[:-1]
                    sleep(0.1)            

            if pygame.key.get_pressed()[pygame.K_ESCAPE]:
                pygame.quit()
                exit()
            if pygame.key.get_pressed()[pygame.K_r]:
                break

            if pygame.key.get_pressed()[pygame.K_SPACE] and game_active == 1:
                game_active = 0 #начало

            if pygame.key.get_pressed()[pygame.K_i] and game_active == 1:
                game_active = 2 #инфо

            if pygame.key.get_pressed()[pygame.K_l] and game_active == 1:
                game_active = 3 #лидеры

            if pygame.key.get_pressed()[pygame.K_BACKSPACE] and (game_active == 2 or game_active == 3):
                game_active = 1 #назад из инфо и лидеров

            if game_active == 0:                                                                                        #игра началась
                scroll += 27 / DELTA
                surface.blit(background_texture, (0, scroll % 540))
                surface.blit(background_texture, (0, -540 + scroll % 540))

                if (player_instance.health <= 0) or (len(entities) <= 1) or (alien_y > (540 - ENTITY_SIZE * 2)):        #причины умереть
                    pygame.mixer.Sound.play(DEATH)
                    game_active = 1
                    break

                alien_x += ALIEN_HORIZONTAL_SPEED / DELTA * alien_vector

                if alien_x + ((ENTITY_SIZE + 4) * ALIENS_IN_WAVE) >= ALIEN_AREA_END:                                    #движение пришельцев
                    alien_vector = -1
                    alien_y += ENTITY_SIZE + 4
                elif alien_x <= ALIEN_AREA_START:
                    alien_vector = 1
                    alien_y += ENTITY_SIZE + 4

                for entity in entities:
                    if entity is not player_instance:
                        entity.aabb.x = entity.pos[0] + alien_x
                        entity.aabb.y = entity.pos[1] + alien_y
                    entity.update()                                                                                     #обновление всех
                    if entity.health <= 0:
                        entity.die()                                                                                    #дохлики
                    entity.draw(surface)

                entities = list(filter(lambda entity: entity.health > 0, entities))

                max_score = max(max_score, player_instance.score)

                for hp in range(1, player_instance.health + 1):
                    surface.blit(health_texture, (SCREEN_WIDTH - (HEALTH_SIZE * hp) - ((HEALTH_SIZE / PLAYER_HEALTH) * (hp - 1)), SCREEN_HEIGHT - HEALTH_SIZE))

                score_text = score_font.render(f'Score: {player_instance.score}', False, 'White')
                score_text_aabb = score_text.get_rect(bottomleft = (0, SCREEN_HEIGHT))
                surface.blit(score_text, score_text_aabb)

            elif game_active == 1 or game_active == 4:                                                                  #отрисовка меню
                surface.fill(pygame.Color(0, 0, 0))
                last_score_text = font.render(f'Last score: {max_score}', False, 'White')
                last_score_text_aabb = last_score_text.get_rect(center = (SCREEN_WIDTH / 2, 27))
                start_text = font.render('Press Space to Start', False, 'White')
                help_text = font.render('Press I for Help', False, 'White')
                lb_text = font.render('Press L for Leaderboard', False, 'White')
                exit_text = font.render('Press ESC to exit', False, 'White')
                start_text_aabb = start_text.get_rect(center = (SCREEN_WIDTH / 2, 27 * 3))
                help_text_aabb = help_text.get_rect(center = (SCREEN_WIDTH / 2, 27 * 5))
                lb_text_aabb = lb_text.get_rect(center = (SCREEN_WIDTH / 2, 27 * 7))
                exit_text_aabb = exit_text.get_rect(center = (SCREEN_WIDTH / 2, 27 * 9))
                surface.blit(last_score_text, last_score_text_aabb)
                surface.blit(start_text, start_text_aabb)
                surface.blit(help_text, help_text_aabb)
                surface.blit(lb_text, lb_text_aabb)
                surface.blit(exit_text, exit_text_aabb)

                if parser.get_max_score(config_instance) < max_score:                                                   #новый лучший результат
                    enter_text = score_font.render('New best! Enter your name:', False, 'Green')
                    enter_text_aabb = enter_text.get_rect(center = (SCREEN_WIDTH / 2, 27 * 12))
                    surface.blit(enter_text, enter_text_aabb)
                    
                    username_box = score_font.render(username, False, 'White')
                    username_aabb = username_box.get_rect(center = (SCREEN_WIDTH / 2, 27 * 13))
                    surface.blit(username_box, username_aabb)                   
                    game_active = 4

            elif game_active == 2:                                                                                      #инфо
                surface.fill(pygame.Color(0, 0, 0))
                utils.grender_multiline(surface, score_font, 'Space Invaders is a fixed shooter in which the player moves\na laser cannon horizontally across the bottom of the screen\nand fires at aliens overhead. The aliens move left and right\nas a group, shifting downward each time they reach a screen\nedge. The goal is to eliminate all of the aliens by shooting\nthem. While the player has three lives, the game ends\nimmediately if the invaders reach the bottom of the screen.\n\nPress F to fire\nUse arrows to navigate', 0, 0, HEALTH_SIZE)
                back_text = score_font.render('Press Backspace to go back', False, 'White')
                back_text_aabb = back_text.get_rect(bottomleft = (0, SCREEN_HEIGHT))
                surface.blit(back_text, back_text_aabb)

            elif game_active == 3:                                                                                      #лидеры
                surface.fill(pygame.Color(0, 0, 0))
                string = ''
                for val in parser.get_sorted_leaderboard(config_instance).items():
                    string += str(val[0]) + '    ' + str(val[1]) + '\n'

                utils.render_multiline(surface, score_font, string, 0, 0, HEALTH_SIZE)
                back_text = score_font.render('Press Backspace to go back', False, 'White')
                back_text_aabb = back_text.get_rect(bottomleft = (0, SCREEN_HEIGHT))
                surface.blit(back_text, back_text_aabb)

            DELTA = clock.tick(TPS)                                                                                     #задержка
            pygame.display.flip()        