import random
import pygame
from Player import Player
from Weapons import Pistol
from Weapons import Uzi
from Weapons import Double_Barrel
from Weapons import M16
from Weapons import Heavy_Pistol
from Wave import Wave
from Utility import HelperFunctions
from Environment import Popup
from Leaderboard_Record import Leaderboard_Record

class Game_State():
    pygame.init()
    pygame.mixer.init()
    window_width = 800
    window_height = 600
    screen = pygame.display.set_mode((window_width, window_height))
    pygame.display.set_caption("Crimson Miami")
    

    player = Player(window_width // 2, window_height // 2)
    player_alive = True

    mouse_x, mouse_y = pygame.mouse.get_pos()

    # Sounds
    main_game_music = pygame.mixer.Sound("Assets\Sounds\Le_Perv.mp3")
    menu_music = pygame.mixer.Sound("Assets\Sounds\Dust.mp3")
    currently_playing_music = menu_music
    player_hit_sound = pygame.mixer.Sound("Assets\Sounds\Player_hit.mp3")
    shot_sound = pygame.mixer.Sound(player.current_weapon.sound)
    # Sounds

    clock = pygame.time.Clock()
    target_fps = 60
    running = True

    menu_open = True
    leaderboard_open = False
    help_open = False

    leaderboard = Leaderboard_Record.read_records_from_json("leaderboard.json")

    hue = 0
    frames_per_cycle = 3000

    # Events

    time_increment_event = pygame.USEREVENT + 1
    wave_change_event = pygame.USEREVENT + 2
    weapon_spawn_event = pygame.USEREVENT + 3

    close_slow_enemy_spawn_event = pygame.USEREVENT + 4
    close_slow_upgraded_enemy_spawn_event = pygame.USEREVENT + 5
    close_slow_superior_enemy_spawn_event = pygame.USEREVENT + 6
    close_chunky_enemy_spawn_event = pygame.USEREVENT + 7
    close_fast_enemy_spawn_event = pygame.USEREVENT + 8
    inspector_chunky_enemy_spawn_event = pygame.USEREVENT + 9
    inspector_chunky_upgraded_enemy_spawn_event = pygame.USEREVENT + 10
    waiter_average_enemy_spawn_event = pygame.USEREVENT + 11
    close_fast_knife_enemy_spawn_event = pygame.USEREVENT + 12
    police_average_enemy_spawn_event = pygame.USEREVENT + 13

    pygame.time.set_timer(time_increment_event, 1000)
    pygame.time.set_timer(weapon_spawn_event, 30000)
    pygame.time.set_timer(wave_change_event, 30000)

    available_weapon_list = [Uzi(), Double_Barrel(), M16(), Heavy_Pistol()]

    wave_list = Wave.read_waves_from_json("wave.json")
    current_wave = wave_list[0]
    current_wave_number = 0

    projectiles = []
    enemies = []
    corpses = []
    laying_weapons = []
    max_corpses = 45
    seconds_survived = 0
    special_weapon_hold_time = 0

    score = 0
    max_player_score = 0
    
    background_color = pygame.Color(255, 255, 255)
    popup_color = pygame.Color(0, 0, 0)
    popup_font = pygame.font.Font('Assets\FIGHTT3_.ttf', 25)
    popups = []

    @staticmethod
    def reset_game():
        Game_State.player = Player(Game_State.window_width // 2, Game_State.window_height // 2)
        Game_State.player_alive = True
        Game_State.projectiles.clear()
        Game_State.enemies.clear()
        Game_State.corpses.clear()
        Game_State.popups.clear()
        Game_State.laying_weapons.clear()
        Game_State.player.change_weapon(Pistol())
        Game_State.seconds_survived = 0
        Game_State.special_weapon_hold_time = 0
        Game_State.score = 0
        Game_State.previous_score = 0
        Game_State.wave_list = Wave.read_waves_from_json("wave.json")
        Game_State.current_wave = Game_State.wave_list[0]
        Game_State.change_enemy_spawn_rates(Game_State.current_wave)
        Game_State.current_wave_number = 1

    @staticmethod
    def change_enemy_spawn_rates(wave):
        pygame.time.set_timer(Game_State.close_slow_enemy_spawn_event, wave.close_slow_enemy_spawn_time)
        pygame.time.set_timer(Game_State.close_slow_upgraded_enemy_spawn_event, wave.close_slow_upgraded_enemy_spawn_time)
        pygame.time.set_timer(Game_State.close_slow_superior_enemy_spawn_event, wave.close_slow_superior_enemy_spawn_time)
        pygame.time.set_timer(Game_State.close_fast_enemy_spawn_event, wave.close_fast_enemy_spawn_time)
        pygame.time.set_timer(Game_State.close_chunky_enemy_spawn_event, wave.close_chunky_enemy_spawn_time)
        pygame.time.set_timer(Game_State.inspector_chunky_enemy_spawn_event, wave.inspector_chunky_enemy_spawn_time)
        pygame.time.set_timer(Game_State.inspector_chunky_upgraded_enemy_spawn_event, wave.inspector_chunky_upgraded_enemy_spawn_time)
        pygame.time.set_timer(Game_State.waiter_average_enemy_spawn_event, wave.waiter_average_enemy_spawn_time)
        pygame.time.set_timer(Game_State.close_fast_knife_enemy_spawn_event, wave.close_fast_knife_enemy_spawn_time)
        pygame.time.set_timer(Game_State.police_average_enemy_spawn_event, wave.police_average_enemy_spawn_time)

    @staticmethod
    def update_colors():
        Game_State.hue = (Game_State.hue + 1) % Game_State.frames_per_cycle
        Game_State.popup_color.hsva = (((Game_State.hue + 500) * 360 / Game_State.frames_per_cycle) % 360, 100, 100, 100)
        Game_State.background_color.hsva = (Game_State.hue * 360 / Game_State.frames_per_cycle, 65, 65, 65)

    @staticmethod
    def update_wave():
        if Game_State.current_wave_number < 20:
            Game_State.current_wave : Wave = Game_State.wave_list[Game_State.current_wave_number]
            Game_State.change_enemy_spawn_rates(Game_State.current_wave)
            Game_State.current_wave_number += 1
            Game_State.add_popup(Popup(f"Wave:{Game_State.current_wave_number}", 300, 40, 80))

    @staticmethod
    def update_shot_sound(new_sound):
        Game_State.shot_sound = pygame.mixer.Sound(new_sound)

    @staticmethod
    def update_survived_time(new_time):
        Game_State.seconds_survived = new_time

    @staticmethod
    def update_score(new_score):
        Game_State.score = new_score

    @staticmethod
    def add_enemy(enemy):
        Game_State.enemies.append(enemy)

    @staticmethod
    def remove_enemy(enemy):
        Game_State.enemies.remove(enemy)

    @staticmethod
    def clear_laying_weapons():
        Game_State.laying_weapons.clear()

    @staticmethod
    def spawn_random_laying_weapon(x, y, angle):
        random_number = random.randrange(0, len(Game_State.available_weapon_list), 1)
        Game_State.laying_weapons.append(Game_State.available_weapon_list[random_number].get_laying_entity(x, y, angle))

    @staticmethod
    def add_projectile(projectile):
        Game_State.projectiles.append(projectile)

    @staticmethod
    def update_entity_coords(entity, x, y):
        entity.x = x
        entity.y = y

    @staticmethod
    def remove_projectile(projectile):
        Game_State.projectiles.remove(projectile)

    @staticmethod
    def update_popup_scale(popup, new_scale):
        popup.scale = new_scale

    @staticmethod
    def remove_popup(popup):
        Game_State.popups.remove(popup)

    @staticmethod
    def add_popup(popup):
        Game_State.popups.append(popup)

    @staticmethod
    def remove_corpse(corpse):
        Game_State.corpses.remove(corpse)

    @staticmethod
    def add_corpse(corpse):
        Game_State.corpses.append(corpse)

    @staticmethod
    def set_special_weapon_hold_time(ticks):
        Game_State.special_weapon_hold_time = ticks