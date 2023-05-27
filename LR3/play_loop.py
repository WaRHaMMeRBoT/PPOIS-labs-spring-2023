import pygame.gfxdraw
import math

from datetime import datetime

from manager import Background, ScoreManager
from menu import *
import toolbox as toolbox
from game import *


class Button:
    def __init__(self, width, height, in_act_clr=(15, 15, 15)):
        self.width = width
        self.height = height
        self.in_act_clr = in_act_clr

    def draw(self, x, y, message, action=None, start='', font_size=30, b_font_clr=(255, 255, 255)):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        print_text(message=message, x=x + 5, y=y + 5,
                   font_clr=b_font_clr, font_size=font_size)
        if x < mouse[0] < x + self.width:
            if y < mouse[1] < y + self.height:
                pygame.draw.rect(game.screen, self.in_act_clr,
                                 (x, y, self.width, self.height))
                print_text(message=message, x=x + 5, y=y + 5,
                           font_clr=(123, 22, 12), font_size=font_size)
                if click[0] == 1:
                    toolbox.play_sound('button.wav')
                    pygame.time.delay(300)
                    if start == 'start':
                        play_loop(game.screen, game.clock, FPS, mr_player, projectilesGroup, enemiesGroup, powerGroup,
                                  bloodGroup,
                                  wave_controller, font, background_image, True)
                    if start == 'rating':
                        print_rate_table(165, 155)
                    if start == 'rules':
                        rules()
                    if action is not None:
                        if action == quit():
                            pygame.quit()
                            quit()
                        else:
                            action()

        else:
            pygame.draw.rect(game.screen, self.in_act_clr,
                             (x, y, self.width, self.height))
            print_text(message=message, x=x + 5, y=y + 5,
                       font_clr=b_font_clr, font_size=font_size)


def show_menu():
    menu_bg = pygame.image.load(image_util.get_image('crimsonland_menu.jpg'))

    menu = True

    start_btn = Button(125, 25)
    rating_btn = Button(125, 25)
    info_btn = Button(125, 25)
    opt_btn = Button(125, 25)
    quit_btn = Button(125, 25)

    pygame.mouse.set_visible(False)
    cursor_img = pygame.image.load(image_util.get_image('cursor.png'))
    cursor_rect = cursor_img.get_rect()

    pygame.mixer.music.load(image_util.get_image('menu.mp3'))
    pygame.mixer.music.play(-1)

    print(save_data.get('rating'))

    while menu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        cursor_rect.topleft = pygame.mouse.get_pos()
        screen.blit(menu_bg, (0, 0))
        start_btn.draw(220, 213, 'Start game', start='start', font_size=10)
        rating_btn.draw(203, 274, 'Rating', start='rating', font_size=10)
        info_btn.draw(182, 333, 'About game', start='rules', font_size=10)
        opt_btn.draw(161, 394, 'Options', action=None, font_size=10)
        quit_btn.draw(140, 453, 'Quit', action=quit, font_size=10)
        screen.blit(cursor_img, cursor_rect)
        pygame.display.update()
        clock.tick(60)


def congratulations():
    paused = True
    cong_bg = pygame.image.load(image_util.get_image('congratulations.jpg'))
    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        game.screen.blit(cong_bg, (0, 0))
        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            paused = False
        pygame.display.update()


def rules():
    paused = True
    rule_bg = pygame.image.load(image_util.get_image('rules.jpg'))
    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        game.screen.blit(rule_bg, (0, 0))
        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            paused = False

        pygame.display.update()


def print_rate_table(x, y):
    step_x = 380
    step_y = 40
    paused = True
    pause_bg = pygame.image.load(image_util.get_image('table.jpg'))
    # # sorted_tuples = sorted(r_table.r_table, key=lambda item: item[1])
    # sorted_tuples = sorted(r_table.r_table)
    # r_table.r_table = {k: v for k, v in sorted_tuples}
    game.screen.blit(pause_bg, (0, 0))
    count = 0
    for name, value in r_table.data.items():
        if count == 0:
            print_text(' ' + str(count + 1) + '     ' + name, x, y,
                       font_clr=(255, 255, 255),
                       font_size=15)
            x += step_x
        else:
            print_text(str(count + 1) + '     ' + name, x, y,
                       font_clr=(255, 255, 255),
                       font_size=15)
            x += step_x
        print_text(str(value), x, y, font_clr=(255, 255, 255), font_size=15)
        x -= step_x
        y += step_y
        count += 1
        if count == 10:
            break

    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            paused = False

        pygame.display.update()
        clock.tick(FPS)


def game_over():
    got_name = False
    paused = True
    pause_bg = pygame.image.load(image_util.get_image('enter.jpg'))
    cursor_img = pygame.image.load(image_util.get_image('cursor.png'))
    cursor_rect = cursor_img.get_rect()
    quit_btn = Button(200, 40, in_act_clr=(28, 10, 8))
    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        cursor_rect.topleft = pygame.mouse.get_pos()
        game.screen.blit(pause_bg, (0, 0))
        date = datetime.now()
        strDate = str(date.year) + "-" + str(date.month) + "-" + str(date.day) + \
            " " + str(date.hour) + ":" + str(date.minute) + \
            ":" + str(date.second)
        if not got_name:
            print_text('Enter your name: ', 274, 300, font_clr=(255, 255, 255), font_size=20,
                       )
            # name = get_input(274, 335)

            got_name = True

            game.r_table.update(strDate, ScoreManager.score)
            if max(r_table.data.values()) == r_table.data[strDate]:
                congratulations()
        else:
            print_text('R.I.P.', 280, 280, font_clr=(255, 255, 255),
                       font_size=50)
            print_text(strDate, 280, 330, font_clr=(255, 255, 255),
                       font_size=50)
        save_data.save()
        save_data.add('rating', game.r_table.r_table)
        quit_btn.draw(300, 480, '           Quit', action=quit, font_size=15)
        game.screen.blit(cursor_img, cursor_rect)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            paused = False

        pygame.display.update()


def play_loop(screen, clock, FPS, mr_player, projectilesGroup, enemiesGroup, powerGroup, bloodGroup, wave_controller,
              font, background_image, flag):
    pygame.mouse.set_visible(False)
    cursor_img = pygame.image.load(image_util.get_image('curs_white.png'))
    cursor_rect = cursor_img.get_rect()

    rw_flag = False

    running = flag

    while running:

        clock.tick(FPS)

        screen.blit(background_image, (-500 -
                    Background.display_scroll[0], -350 - Background.display_scroll[1]))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pause()
        keys = pygame.key.get_pressed()
        cursor_rect.center = pygame.mouse.get_pos()

        if (keys[pygame.K_d] and keys[pygame.K_s]) or (keys[pygame.K_a] and keys[pygame.K_s]) or (
                keys[pygame.K_w] and keys[pygame.K_a]) or (keys[pygame.K_d] and keys[pygame.K_w]):
            buff_speed = 1 / 1.4
        else:
            buff_speed = 1

        if 250 > Background.display_scroll[0] > - 250:

            if keys[pygame.K_d]:
                mr_player.animate()
                Background.display_scroll[0] += buff_speed * mr_player.speed
                for projectile in projectilesGroup:
                    projectile.x -= buff_speed * mr_player.speed

            elif keys[pygame.K_a]:
                mr_player.animate()
                Background.display_scroll[0] -= buff_speed * mr_player.speed
                for projectile in projectilesGroup:
                    projectile.x += buff_speed * mr_player.speed
        elif Background.display_scroll[0] >= 250:
            if keys[pygame.K_d]:
                mr_player.animate()
                mr_player.move(buff_speed, 0)
            elif keys[pygame.K_a]:
                mr_player.animate()
                mr_player.move(-buff_speed, 0)
                if mr_player.x <= 401 and Background.display_scroll[0] > 250:
                    Background.display_scroll[0] = 249
        elif Background.display_scroll[0] <= -250:
            if keys[pygame.K_d]:
                mr_player.animate()
                mr_player.move(buff_speed, 0)
                if mr_player.x >= 399 and Background.display_scroll[0] < -250:
                    Background.display_scroll[0] = -249
            elif keys[pygame.K_a]:
                mr_player.animate()
                mr_player.move(-buff_speed, 0)
        if 200 > Background.display_scroll[1] > - 200:
            if keys[pygame.K_w]:
                mr_player.animate()
                Background.display_scroll[1] -= buff_speed * mr_player.speed
                for projectile in projectilesGroup:
                    projectile.y += buff_speed * mr_player.speed
            elif keys[pygame.K_s]:
                mr_player.animate()
                Background.display_scroll[1] += buff_speed * mr_player.speed
                for projectile in projectilesGroup:
                    projectile.y -= buff_speed * mr_player.speed
        elif Background.display_scroll[1] >= 200:
            if keys[pygame.K_w]:
                mr_player.animate()
                mr_player.move(0, -buff_speed)
                if mr_player.y <= 301 and Background.display_scroll[1] >= 200:
                    Background.display_scroll[1] = 199
            elif keys[pygame.K_s]:
                mr_player.animate()
                mr_player.move(0, buff_speed)
        elif Background.display_scroll[1] <= - 200:
            if keys[pygame.K_w]:
                mr_player.animate()
                mr_player.move(0, -buff_speed)
            elif keys[pygame.K_s]:
                mr_player.animate()
                mr_player.move(0, buff_speed)
                if mr_player.y >= 299 and Background.display_scroll[1] <= -200:
                    Background.display_scroll[1] = -199
        if pygame.mouse.get_pressed()[0]:
            mr_player.shoot()
        if keys[pygame.K_1]:
            mr_player.change_weapon(0)
        if keys[pygame.K_2]:
            if wave_controller.wave_number >= 5:
                mr_player.change_weapon(1)
        if keys[pygame.K_3]:
            if wave_controller.wave_number >= 10:
                mr_player.change_weapon(2)
        if (keys[
                pygame.K_r] and mr_player.player_weapon.ammo_count_max > mr_player.player_weapon.ammo_count > 0) or mr_player.player_weapon.ammo_count == 0:
            mr_player.reload_weapon(cursor_rect.centerx, cursor_rect.centery)
        else:
            mr_player.player_weapon.reload_cooldown = 0
        if wave_controller.wave_number == 0:
            if keys[pygame.K_SPACE]:
                wave_controller.new_wave(mr_player)
        elif len(enemiesGroup.sprites()) <= 5:
            print_text(f"New Wave coming in", 280, 50, font_clr=(255, 255, 255),
                       font_size=17)
            wave_controller.draw_timer(screen, 400, 110)
            wave_controller.wave_cd += 1
            if keys[pygame.K_SPACE] or wave_controller.wave_cd == wave_controller.wave_cd_max or (
                    wave_controller.wave_cd < wave_controller.wave_cd_max and len(enemiesGroup.sprites()) == 0):
                if wave_controller.wave_cd < wave_controller.wave_cd_max:
                    ScoreManager.score += math.ceil(
                        (wave_controller.wave_cd_max - wave_controller.wave_cd) / 30)

                wave_controller.new_wave(mr_player)
        mr_player.update(enemiesGroup, powerGroup)
        for blood in bloodGroup:
            blood.update()
        for power in powerGroup:
            power.update(mr_player)
        for projectile in projectilesGroup:
            projectile.update()
        for enemy in enemiesGroup:
            enemy.update(projectilesGroup, powerGroup)
        if not mr_player.alive:
            running = False
            game_over()
        print_text("Score: " + str(ScoreManager.score),
                   10, 10, font_clr=(255, 255, 255))
        print_text("Wave: " + str(wave_controller.wave_number),
                   615, 10, font_clr=(255, 255, 255))
        screen.blit(cursor_img, cursor_rect)
        pygame.display.flip()
