import sys
import pygame
import random
from scripts import configs as cf
from scripts.game_states import GameStates as gs
from scripts.ui_elements.scopes import Cross, Sight
from scripts.ui_elements.camera import CameraGroup
from scripts.sprites.enemies import Enemy, MovementDirection
from scripts.ui_elements.text import draw_text

screen = pygame.display.set_mode((cf.SCREEN_WIDTH, cf.SCREEN_HEIGHT))
icon_image = pygame.image.load(cf.ICON_DIR)
pygame.display.set_icon(icon_image)
clock = pygame.time.Clock()
pygame.event.set_grab(True)


def draw_static_ui():
    ammo_icon_img = pygame.image.load(cf.UI_SPRITES_IMG['ammo_icon'])
    ammo_icon_img = pygame.transform.smoothscale(ammo_icon_img, (int(ammo_icon_img.get_width() *
                                                                     cf.SCREEN_WIDTH / 1000),
                                                                 int(ammo_icon_img.get_height() *
                                                                     cf.SCREEN_HEIGHT / 500)))
    pygame.display.get_surface().blit(ammo_icon_img, (int(cf.SCREEN_WIDTH * 0.75),
                                                      int(cf.SCREEN_HEIGHT * 0.85)))


def spawn_enemy(camera_group):
    enemy_type = random.choice(cf.ALL_ENEMIES)
    enemy_layer = random.choice(['1', '2', '3'])
    enemy_size_coef = {'1': 1, '2': 0.75, '3': 0.55}[enemy_layer]
    enemy_size = tuple(map(lambda size: size * enemy_size_coef, cf.ENEMY_BASIC_REL_SIZE[enemy_type]))
    move_direction = random.choice([MovementDirection.RIGHT, MovementDirection.LEFT])
    spawn_x, spawn_y = 0, 0
    if move_direction == MovementDirection.RIGHT:
        spawn_x = random.randint(int(camera_group.offset.x - cf.SCREEN_WIDTH // 3.5),
                                 int(camera_group.offset.x - cf.SCREEN_WIDTH // 4.5))
    elif move_direction == MovementDirection.LEFT:
        spawn_x = random.randint(int(camera_group.offset.x + cf.SCREEN_WIDTH * 1.2),
                                 int(camera_group.offset.x + cf.SCREEN_WIDTH * 1.5))
    spawn_y_coefs = {'1': round(random.uniform(0.8, 0.85), 2),
                     '2': round(random.uniform(0.71, 0.76), 2),
                     '3': round(random.uniform(0.65, 0.68), 2)}
    spawn_y = cf.SCREEN_HEIGHT * spawn_y_coefs[enemy_layer]
    Enemy(camera_group, spawn_x, spawn_y, cf.ENEMY_SPRITES_IMG[enemy_type], enemy_size,
          cf.ENEMY_BASIC_SPEED[enemy_type], move_direction, cf.MapSize.STANDARD)


def limit_time_mode():
    pygame.display.set_caption('TankHuhn limit time mode')
    pygame.display.set_icon(icon_image)

    remain_time = cf.BASE_GAME_TIME
    time_ticks = 0
    cf.play_score = 0
    spawn_counter = 0

    ammo_count = cf.CLIP_SIZE

    ui_group = pygame.sprite.Group()
    Cross(ui_group)
    sight = Sight(ui_group, cf.SIGHT_SPEED)
    camera_group = CameraGroup(cf.BACKGROUND_DIR['bg_day'])

    running = True
    forced_escape = False

    while running:
        current_ticks = pygame.time.get_ticks()
        if current_ticks - spawn_counter >= 4000:
            spawn_counter = current_ticks
            spawn_enemy(camera_group)
        if current_ticks - time_ticks >= 1000:
            time_ticks = current_ticks
            remain_time -= 1
        screen.fill('black')
        sight_pos = None
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                    forced_escape = True
                if event.key == pygame.K_SPACE:
                    ammo_count = cf.CLIP_SIZE
            if event.type == pygame.MOUSEBUTTONDOWN:
                if ammo_count > 0:
                    sight_pos = sight.rect.center
                    ammo_count -= 1
            if event.type == pygame.MOUSEBUTTONUP:
                sight_pos = None
        if remain_time <= 0:
            forced_escape = False
            running = False
        camera_group.custom_draw()
        camera_group.update(sight_pos=sight_pos)
        ui_group.draw(screen)
        ui_group.update(mouse_pos=pygame.mouse.get_pos())
        score = cf.play_score
        draw_text(f'TIME: {remain_time}', cf.SCREEN_HEIGHT // 15, 'white', (int(cf.SCREEN_WIDTH * 0.03),
                                                                            int(cf.SCREEN_HEIGHT * 0.03)))
        draw_text(f'SCORE: {score}', cf.SCREEN_HEIGHT // 15, 'white', (int(cf.SCREEN_WIDTH * 0.65),
                                                                       int(cf.SCREEN_HEIGHT * 0.03)))
        draw_text(f'X {ammo_count}', cf.SCREEN_HEIGHT // 15, 'white', (int(cf.SCREEN_WIDTH * 0.8),
                                                                       int(cf.SCREEN_HEIGHT * 0.87)))
        draw_static_ui()
        pygame.display.flip()
        clock.tick(cf.FPS)
    if not running:
        if not forced_escape:
            return gs.AFTER_GAME
        return gs.MAIN_MENU
