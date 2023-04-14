import math
import random
import pygame
from Weapons import Projectile
from Environment import Popup
from Weapons import Pistol
from Utility import HelperFunctions
from GameState import Game_State
from Enemies import Close_Slow_Enemy
from Enemies import Close_Slow_Upgraded_Enemy
from Enemies import Close_Slow_Superior_Enemy
from Enemies import Close_Chunky_Enemy
from Enemies import Inspector_Chunky_Enemy
from Enemies import Inspector_Chunky_Upgraded_Enemy
from Enemies import Waiter_Average_Enemy
from Enemies import Police_Average_Enemy
from Enemies import Close_Fast_Enemy
from Enemies import Close_Fast_Knife_Enemy

def draw_new_personal_best(new_score):
    congrats_surface = Game_State.popup_font.render("New personal best! - {}".format(new_score), True, Game_State.popup_color)  # update the score surface
    Game_State.screen.blit(congrats_surface, (Game_State.window_width//2 - 130, Game_State.window_height//2 - 200))

def draw_dead_message():
    dead_message_surface = Game_State.popup_font.render("You're dead. R - to restart", True, Game_State.popup_color)  # update the score surface
    Game_State.screen.blit(dead_message_surface, (Game_State.window_width//2 - 130, Game_State.window_height//2 - 100))

def draw_menu():
    start_surface = Game_State.popup_font.render("Press SPACE to start the game", True, Game_State.popup_color)  # update the score surface
    help_surface = Game_State.popup_font.render("Press H for HELP", True, Game_State.popup_color)  # update the score surface
    lb_surface = Game_State.popup_font.render("Press TAB to open the LEADERBOARD", True, Game_State.popup_color)  # update the score surface
    Game_State.screen.blit(start_surface, (Game_State.window_width//2 - 130, Game_State.window_height//2 + 150))
    Game_State.screen.blit(help_surface, (Game_State.window_width//2 - 80, Game_State.window_height//2 + 200))
    Game_State.screen.blit(lb_surface, (Game_State.window_width//2 - 150, Game_State.window_height//2 + 250))

def draw_leaderboard():
    y_offset = 0
    index_offset = 0
    records = Game_State.leaderboard
    for i in range(len(records)):
        if records[i].score < Game_State.max_player_score and index_offset == 0:
            name_surface =  Game_State.popup_font.render("You", True, Game_State.popup_color)
            score_surface = Game_State.popup_font.render("{}".format(Game_State.max_player_score), True, Game_State.popup_color)
            index_offset = 1
        else:
            name_surface =  Game_State.popup_font.render("{}".format(records[i-index_offset].name), True, Game_State.popup_color)
            score_surface = Game_State.popup_font.render("{}".format(records[i-index_offset].score), True, Game_State.popup_color)
        Game_State.screen.blit(name_surface, (100, 30 + y_offset))
        Game_State.screen.blit(score_surface, (600, 30 + y_offset))
        y_offset += 50

def draw_help():
    text_1 = "Welcome to Crimson Miami!"
    text_2 = "The game is set in an alternate version of 1980s Miami"
    text_3 = "You play as an unnamed hitman"
    text_4 = "Fight off numerous amounts of enemies and get the highest score!"
    help_text_1_surface = Game_State.popup_font.render(text_1, True, Game_State.popup_color)
    help_text_2_surface = Game_State.popup_font.render(text_2, True, Game_State.popup_color)
    help_text_3_surface = Game_State.popup_font.render(text_3, True, Game_State.popup_color)
    help_text_4_surface = Game_State.popup_font.render(text_4, True, Game_State.popup_color)
    Game_State.screen.blit(help_text_1_surface, (100, 60))
    Game_State.screen.blit(help_text_2_surface, (100, 120))
    Game_State.screen.blit(help_text_3_surface, (100, 180))
    Game_State.screen.blit(help_text_4_surface, (100, 240))

def rotate_and_draw(entity):
    entity_image = pygame.image.load(entity.sprite)
    rotated_entity_image = pygame.transform.rotate(entity_image, -entity.turn_angle*180/math.pi)
    entity_rect = rotated_entity_image.get_rect(center= entity_image.get_rect(center = (entity.x, entity.y)).center)
    Game_State.screen.blit(rotated_entity_image, entity_rect)

def handle_enemy_spawn_event(event):
    x, y = HelperFunctions.get_random_border_point(Game_State.window_width, Game_State.window_height)
    if event.type == Game_State.close_slow_enemy_spawn_event:
        Game_State.add_enemy(Close_Slow_Enemy(x, y))
    elif event.type == Game_State.close_slow_upgraded_enemy_spawn_event:
        Game_State.add_enemy(Close_Slow_Upgraded_Enemy(x, y))
    elif event.type == Game_State.close_slow_superior_enemy_spawn_event:
        Game_State.add_enemy(Close_Slow_Superior_Enemy(x, y))
    elif event.type == Game_State.close_fast_enemy_spawn_event:
        Game_State.add_enemy(Close_Chunky_Enemy(x, y))
    elif event.type == Game_State.close_chunky_enemy_spawn_event:
        Game_State.add_enemy(Close_Fast_Enemy(x, y))
    elif event.type == Game_State.close_fast_knife_enemy_spawn_event:
        Game_State.add_enemy(Close_Fast_Knife_Enemy(x, y))
    elif event.type == Game_State.waiter_average_enemy_spawn_event:
        Game_State.add_enemy(Waiter_Average_Enemy(x, y))
    elif event.type == Game_State.inspector_chunky_enemy_spawn_event:
        Game_State.add_enemy(Inspector_Chunky_Enemy(x, y))
    elif event.type == Game_State.inspector_chunky_upgraded_enemy_spawn_event:
        Game_State.add_enemy(Inspector_Chunky_Upgraded_Enemy(x, y))
    elif event.type == Game_State.police_average_enemy_spawn_event:
        Game_State.add_enemy(Police_Average_Enemy(x, y))

def resolve_ingame_events():
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            Game_State.menu_open = True
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_r:
            Game_State.reset_game()
            continue
        elif Game_State.player_alive:
            if event.type == Game_State.time_increment_event:
                Game_State.update_survived_time(Game_State.seconds_survived + 1)
            elif event.type == Game_State.wave_change_event:
                Game_State.update_wave()
            elif event.type == Game_State.weapon_spawn_event:
                if len(Game_State.laying_weapons) > 0:
                    Game_State.clear_laying_weapons()
                x = random.randrange(Game_State.window_width)
                y = random.randrange(Game_State.window_height)
                angle = random.randrange(360)
                Game_State.spawn_random_laying_weapon(x, y, angle)
            else:
                handle_enemy_spawn_event(event)

def resolve_menu_events():
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                if Game_State.help_open or Game_State.leaderboard_open:
                    Game_State.leaderboard_open = False
                    Game_State.help_open = False
                else:
                    Game_State.running = False
            elif event.key == pygame.K_SPACE:
                Game_State.menu_open = False
                Game_State.help_open = False
                Game_State.leaderboard_open = False
            elif event.key == pygame.K_h:
                Game_State.help_open = True
            elif event.key == pygame.K_TAB:
                Game_State.leaderboard_open = True

def try_set_music(music):
    if Game_State.currently_playing_music != music:
        Game_State.currently_playing_music.stop()
        music.play()
        Game_State.currently_playing_music = music

def resolve_menu_display():
    Game_State.screen.blit(pygame.image.load("Assets\Sprites\Menu_bg.jpg"), (0,0))
    try_set_music(Game_State.menu_music)
    resolve_menu_events()
    if Game_State.help_open:
        draw_help()
    elif Game_State.leaderboard_open:
        draw_leaderboard()
    else:
        draw_menu()

def resolve_player_actions():
    mouse_buttons = pygame.mouse.get_pressed()
    if mouse_buttons[0]:
        projectile_list: Projectile = Game_State.player.use_weapon()
        if (projectile_list != None):
            for projectile in projectile_list:
                Game_State.add_projectile(projectile)
            Game_State.shot_sound.play()
    keys = pygame.key.get_pressed()
            
    if keys[pygame.K_a]:
        Game_State.player.move_left()
    if keys[pygame.K_d]:
        Game_State.player.move_right()
    if keys[pygame.K_w]:
        Game_State.player.move_up()
    if keys[pygame.K_s]:
        Game_State.player.move_down()

def resolve_projectile_movement():
    for projectile in Game_State.projectiles:
        y = projectile.speed * math.sin(projectile.turn_angle)
        x = projectile.speed * math.cos(projectile.turn_angle)
        Game_State.update_entity_coords(projectile, projectile.x + x, projectile.y + y)
        if projectile.y < 0 or projectile.y > Game_State.window_height or projectile.x < 0 or projectile.x > Game_State.window_width:
            Game_State.remove_projectile(projectile)

def resolve_enemy_movement():
    for enemy in Game_State.enemies:
        enemy.update_angle(Game_State.player.x, Game_State.player.y)
        x, y = enemy.get_move_result()
        Game_State.update_entity_coords(enemy, enemy.x + x, enemy.y + y)

def draw_entities():
    for corpse in Game_State.corpses:
        rotate_and_draw(corpse)
    for enemy in Game_State.enemies:
        rotate_and_draw(enemy)
    for weapon in Game_State.laying_weapons:
        rotate_and_draw(weapon)
    for projectile in Game_State.projectiles:
        rotate_and_draw(projectile)
    if  Game_State.player_alive:
        rotate_and_draw(Game_State.player)

def draw_popups():
    for popup in Game_State.popups:
        if popup.scale < 2:
            new_scale = popup.scale + 0.02
            Game_State.update_popup_scale(popup, new_scale)
        else:
            Game_State.remove_popup(popup)
        popup_surface = Game_State.popup_font.render('{}'.format(popup.value), True, Game_State.popup_color)  # update the score surface
        scaled_popup_surface = pygame.transform.scale(popup_surface,(popup.initial_size * popup.scale, popup.initial_size * popup.scale))
        Game_State.screen.blit(scaled_popup_surface, (popup.x, popup.y))

def resolve_enemy_collisions():
    for enemy in Game_State.enemies:
        for projectile in Game_State.projectiles:
            if (enemy in Game_State.enemies and HelperFunctions.collide(projectile.x, projectile.y, enemy)):
                enemy.take_damage(projectile.damage)
                if enemy.current_health <= 0:
                    if (len(Game_State.corpses) > Game_State.max_corpses):
                        Game_State.remove_corpse(Game_State.corpses[0])
                    Game_State.add_corpse(enemy.get_corpse())
                    Game_State.remove_enemy(enemy)
                    Game_State.update_score(Game_State.score + enemy.max_health * 100)
                    Game_State.add_popup(Popup(Game_State.score, enemy.x, enemy.y, 25))
                    projectile.damage -= (enemy.max_health + enemy.current_health)
                else:
                    Game_State.remove_projectile(projectile)
        if HelperFunctions.intersect(Game_State.player, enemy) and Game_State.player_alive:
            Game_State.player.current_health -= 1
            if Game_State.player.current_health <= 0:
                Game_State.add_corpse(Game_State.player.get_corpse())
                Game_State.player_alive = False
                Game_State.player_hit_sound.play()

def resolve_weapon_interaction():
    if pygame.time.get_ticks() - Game_State.special_weapon_hold_time > 30000:
        Game_State.player.change_weapon(Pistol())
        Game_State.update_shot_sound(Game_State.player.current_weapon.sound)
    for weapon in Game_State.laying_weapons:
        if HelperFunctions.collide(weapon.x, weapon.y, Game_State.player):
            Game_State.player.change_weapon(weapon.weapon)
            Game_State.update_shot_sound(weapon.weapon.sound)
            Game_State.clear_laying_weapons()
            Game_State.set_special_weapon_hold_time(pygame.time.get_ticks())

def resolve_player_death():
    if Game_State.score >= Game_State.max_player_score:
        Game_State.max_player_score = Game_State.score
        draw_new_personal_best(Game_State.score)
    draw_dead_message()

def start_game():
    Game_State.update_wave()
    Game_State.currently_playing_music.play()
    while Game_State.running:
        pygame.display.update()
        Game_State.update_colors()
        Game_State.screen.fill(Game_State.background_color)
        Game_State.clock.tick(Game_State.target_fps)
        if Game_State.menu_open:
            resolve_menu_display()
            continue
        try_set_music(Game_State.main_game_music)
        mouse_x, mouse_y = pygame.mouse.get_pos()
        Game_State.player.update_angle(mouse_x, mouse_y)
        resolve_ingame_events()
        if Game_State.player_alive:
            resolve_player_actions()
        Game_State.player.fix_player_coords(Game_State.window_width, Game_State.window_height)
        Game_State.player.reduce_cooldown()
        resolve_projectile_movement()
        resolve_enemy_movement()
        draw_entities()
        draw_popups()
        resolve_enemy_collisions()
        resolve_weapon_interaction()
        if Game_State.player_alive == False:
            resolve_player_death()
    pygame.quit()