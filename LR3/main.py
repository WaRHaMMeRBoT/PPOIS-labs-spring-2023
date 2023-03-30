import sys
from src import *


def add_target(group, env_x, scale, number, dt):
    count = len(group)
    if count < number:
        position = start_position_generation()
        position.x += env_x
        velocity = start_velocity_generation(scale)
        ran_num = random.randint(0, len(Balloon_idle_Set) - 1)
        target = Balloon(ran_num, position, velocity, scale, dt)
        group.add(target)


def start_position_generation():
    position = Vector2(random.randint(0, 3000), screen_height + random.randint(0, 100))
    return position


def start_velocity_generation(scale):
    vel_x = random.uniform(-0.15, 0.15)
    vel_y = random.uniform(-0.2, -0.1) * scale
    velocity = Vector2(vel_x, vel_y)
    return velocity


def bullet_clear(group):
    group.empty()
    return False


def bullet_reload(group, delta_time, img_list):
    group.empty()
    ammo_number = 10
    position = Vector2(screen_width - 20 * ammo_number, screen_height - 40)
    for bullet_count in range(ammo_number):
        bullet_icon = BulletIcon(position, delta_time, img_list)
        position.x += 20
        group.add(bullet_icon)
    channel2.play(reload_sound)
    return True


def bullet_reduction(group):
    bullet_list = group.sprites()
    bullet_index = len(bullet_list) - 1
    if bullet_list:
        while bullet_list[bullet_index].is_quit_trigger():
            bullet_index -= 1
            if bullet_index < 0:
                channel2.play(no_ammo_sound)
                return False
        bullet_list[bullet_index].set_quit_trigger()
        channel2.play(shoot_sound)
        return True
    else:
        channel2.play(no_ammo_sound)
        return False


def set_cursor(path):  # set a customized cursor
    image = pygame.image.load(path).convert_alpha()
    img_width, img_height = image.get_rect().size
    defined_cursor = pygame.cursors.Cursor((int(img_width / 2), int(img_height / 2)), image)
    pygame.mouse.set_cursor(defined_cursor)


def check_shooting(group, score_amplifier, d_t):
    global score
    mouse_pos = pygame.mouse.get_pos()
    real_shot_list = []

    for collide_sprite in group:
        if collide_sprite.rect.collidepoint(mouse_pos):
            pos_in_mask = mouse_pos[0] - collide_sprite.rect.x, mouse_pos[1] - collide_sprite.rect.y
            if collide_sprite.mask.get_at(pos_in_mask):
                real_shot_list.append(collide_sprite)

    if real_shot_list:
        if not real_shot_list[-1].is_quit_trigger():
            real_shot_list[-1].set_quit_trigger()

            score += 1 * score_amplifier  # score accumulation

            position, height, color_index = real_shot_list[-1].require_parameters()
            scoring_ani_group.add(ScoringAnimation(position, height / 2, color_index, score_amplifier, d_t))

            real_shot_list[-1].remove()
        return True
    return False


def update_fps():
    fps = str(int(clock.get_fps()))
    fps_text = FPS_font.render(f'FPS: {fps}', True, pygame.Color('white'))
    return fps_text


def update_time(seconds):
    is_end = False
    time_limit = 30
    countdown = int((time_limit - seconds) * 10) / 10  # 1 decimal remained
    time_text_renderer = RenderText(Board_font)
    time_text = time_text_renderer.render(f'TIME LEFT: {countdown} s', pygame.Color('white'))

    if countdown < 10 and (int(countdown) + 1) % 2 == 0:  # flash effect on the text when <10s
        time_text = time_text_renderer.render(f'TIME LEFT: {countdown} s', pygame.Color(DARK_RED))

    if countdown <= 0:
        is_end = True

    return time_text, is_end


def update_score():
    score_text_renderer = RenderText(Board_font)
    score_text = score_text_renderer.render(f'SCORE: {score}', pygame.Color('white'))
    return score_text


def require_state(prepare_trigger, start_trigger, end_trigger):
    if not prepare_trigger and not start_trigger and not end_trigger:
        state = 0
    elif prepare_trigger and not start_trigger and not end_trigger:
        state = 1
    elif not prepare_trigger and start_trigger and not end_trigger:
        state = 2
    elif not prepare_trigger and not start_trigger and end_trigger:
        state = 3
    else:
        state = 4
        print("Error")
    return state


def draw_start_menu():
    screen.blit(bg_sky, (0, 0))
    screen.blit(bg_mountain, (x * 2, 150))
    screen.blit(mg_hill, (x * 3.6, 350))
    screen.blit(mg_bush, (x * 4.5, 350))
    screen.blit(fg_grass, (x * 6.8, screen_height - H_fg_grass))
    font = pygame.font.SysFont('arial', 40)
    start = font.render('Space - Играть', True, (255, 255, 255))
    reference = font.render('I - Справка', True, (255, 255, 255))
    record = font.render('R - Рекорд', True, (255, 255, 255))
    start_button = font.render('Esc - Выход', True, (255, 255, 255))
    screen.blit(start, (screen_width/2 - start.get_width()/2, screen_height/2 - start.get_height()/2 - 50))
    screen.blit(reference, (screen_width/2 - reference.get_width()/2, screen_height/2 + reference.get_height()/2))
    screen.blit(record, (screen_width/2 - record.get_width()/2, screen_height/2 - record.get_height()/2))
    screen.blit(start_button, (screen_width/2 - start_button.get_width()/2, screen_height/2 + start_button.get_height()/2 + 50))
    pygame.display.update()


def draw_reference_menu():
    screen.blit(bg_sky, (0, 0))
    screen.blit(bg_mountain, (x * 2, 150))
    screen.blit(mg_hill, (x * 3.6, 350))
    screen.blit(mg_bush, (x * 4.5, 350))
    screen.blit(fg_grass, (x * 6.8, screen_height - H_fg_grass))
    screen.blit(text_initial_control1, (180, 300))
    screen.blit(text_initial_control2, (180, 340))
    pygame.display.update()


def draw_record_menu():
    screen.blit(bg_sky, (0, 0))
    screen.blit(bg_mountain, (x * 2, 150))
    screen.blit(mg_hill, (x * 3.6, 350))
    screen.blit(mg_bush, (x * 4.5, 350))
    screen.blit(fg_grass, (x * 6.8, screen_height - H_fg_grass))
    font = pygame.font.SysFont('arial', 40)
    record = font.render(str(FileUtils.read_from_json("./record.json")["record"]), True, (255, 255, 255))
    screen.blit(record, (screen_width/2 - record.get_width()/2, screen_height/2 - record.get_height()/2))
    pygame.display.update()


set_cursor("res/crosshair.png")


announce_sound = mixer.Sound('res/audio/announce.mp3')

shoot_sound = mixer.Sound('res/audio/LaserGun.ogg')
no_ammo_sound = mixer.Sound('res/audio/NoAmmo.ogg')
reload_sound = mixer.Sound('res/audio/GunCocking.ogg')

MUSICSTOP = pygame.event.custom_type()

channel1 = mixer.Channel(0)
channel1.set_volume(0.3)
channel1.set_endevent(MUSICSTOP)
channel2 = mixer.Channel(1)
channel2.set_volume(0.5)

Bullet_List = [pygame.image.load("res/bullet_icon.png").convert_alpha(),
               pygame.image.load("res/bullet_shell_icon.png").convert_alpha()]

bg_sky = pygame.image.load("res/background/BG_sky.png").convert()
bg_mountain = pygame.image.load("res/background/BG_mountain.png").convert_alpha()
mg_hill = pygame.image.load("res/background/MG_hill.png").convert_alpha()
mg_bush = pygame.image.load("res/background/MG_bush.png").convert_alpha()
fg_grass = pygame.image.load("res/background/FG_grass.png").convert_alpha()

bg_sky = pygame.transform.smoothscale(bg_sky, (screen_width, screen_height))
W_fg_grass, H_fg_grass = fg_grass.get_rect().size

scoring_ani_group = pygame.sprite.Group()

target_group1 = pygame.sprite.Group()
target_group2 = pygame.sprite.Group()
target_group3 = pygame.sprite.Group()
target_group4 = pygame.sprite.Group()

bullet_group = pygame.sprite.Group()

FPS_font = pygame.font.SysFont("Arial", 18)
Info_font = pygame.font.SysFont("Showcard Gothic", 30)

text_Ammo_Unavailable = Info_font.render(f'Out Of Ammo!!', True, pygame.Color('white'))
text_initial = Info_font.render(f'=== Click To Start ===', True, pygame.Color(DARK_RED))
text_initial_control1 = Info_font.render(f'Left: A                 Right: D', True, pygame.Color('white'))
text_initial_control2 = Info_font.render(f'Fire: L Click   Reload: R Click', True, pygame.Color('white'))
text_ready = Info_font.render(f'Ready?', True, pygame.Color('white'))
text_go = Info_font.render(f'GO!!', True, pygame.Color(DARK_RED))
text_end = Info_font.render(f'=== Game Over ===', True, pygame.Color(DARK_RED))
text_restart = Info_font.render(f'Press SPACE To Restart', True, pygame.Color('white'))

x = -300
v = 0
scrolling_speed = 0.1

score = 0

delta_t = 0
Start_Time = 0
Current_Time = 0
Previous_Time = 0

ammo_available = False

mixer.music.load("res/audio/EndMusic.mp3")
mixer.music.set_volume(0.5)
mixer.music.play(-1)

edge_trigger = False

Prepare_trigger = False
StartPlay_trigger = False
EndPlay_trigger = False
MoveLeft_Flag = False
MoveRight_Flag = False


Loop_State = require_state(Prepare_trigger, StartPlay_trigger, EndPlay_trigger)

game_state = "start_menu"

while True:
    clock.tick(FPS_value)
    Current_Time = pygame.time.get_ticks()
    delta_t = Current_Time - Previous_Time
    Previous_Time = Current_Time

    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if Loop_State == 0:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    Prepare_trigger = True
                    ammo_available = bullet_reload(bullet_group, delta_t, Bullet_List)
                    channel1.play(announce_sound)
                    mixer.music.fadeout(4000)

        elif Loop_State == 1:
            if event.type == MUSICSTOP:
                Prepare_trigger = False
                StartPlay_trigger = True
                Start_Time = pygame.time.get_ticks()
                mixer.music.load("res/audio/PlayMusic.mp3")
                mixer.music.set_volume(0.5)
                mixer.music.play(-1)

        elif Loop_State == 2:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    ammo_available = bullet_reduction(bullet_group)
                    if ammo_available:
                        if not check_shooting(target_group1, 1, delta_t):
                            if not check_shooting(target_group2, 2, delta_t):
                                if not check_shooting(target_group3, 5, delta_t):
                                    check_shooting(target_group4, 10, delta_t)
                elif event.button == 3:
                    ammo_available = bullet_reload(bullet_group, delta_t, Bullet_List)

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    MoveLeft_Flag = True
                if event.key == pygame.K_d:
                    MoveRight_Flag = True
                v = -scrolling_speed * (MoveRight_Flag - MoveLeft_Flag)
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_a:
                    MoveLeft_Flag = False
                if event.key == pygame.K_d:
                    MoveRight_Flag = False
                v = -scrolling_speed * (MoveRight_Flag - MoveLeft_Flag)

        elif Loop_State == 3:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    EndPlay_trigger = False
                    x = -300
                    v = 0
                    score = 0
                    Start_Time = 0
                    Current_Time = 0
                    Previous_Time = 0
                    ammo_available = bullet_clear(bullet_group)
                    sound_count = 0

    Loop_State = require_state(Prepare_trigger, StartPlay_trigger, EndPlay_trigger)

    if game_state == "start_menu":
        draw_start_menu()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            game_state = "game"
        if keys[pygame.K_ESCAPE]:
            game_state = "quit"
        if keys[pygame.K_i]:
            game_state = "reference"
        if keys[pygame.K_r]:
            game_state = "record"

    if game_state == "reference":
        keys = pygame.key.get_pressed()
        if keys[pygame.K_q]:
            game_state = "start_menu"

    if game_state == "record":
        keys = pygame.key.get_pressed()
        if keys[pygame.K_q]:
            game_state = "start_menu"

    if game_state == "game":
        keys = pygame.key.get_pressed()
        if keys[pygame.K_q]:
            game_state = "start_menu"

    if game_state == "game":
        if channel2.get_busy() or channel3.get_busy():
            mixer.music.set_volume(0.3)
        else:
            mixer.music.set_volume(0.5)

        movement_step = v * delta_t
        x += movement_step
        if x < -600:
            x = -600
            edge_trigger = True
        elif x > 0:
            x = 0
            edge_trigger = True
        else:
            edge_trigger = False

        screen.blit(bg_sky, (0, 0))
        if Loop_State != 2:
            screen.blit(bg_mountain, (x * 2, 150))
            screen.blit(mg_hill, (x * 3.6, 350))
            screen.blit(mg_bush, (x * 4.5, 350))
            screen.blit(fg_grass, (x * 6.8, screen_height - H_fg_grass))

        if Loop_State == 0:
            screen.blit(text_initial, (250, 150))
            screen.blit(text_initial_control1, (180, 300))
            screen.blit(text_initial_control2, (180, 340))

        if Loop_State == 1:
            screen.blit(text_ready, (350, 150))

            bullet_group.draw(screen)
            bullet_group.update()

        if Loop_State == 2:
            if edge_trigger:
                target_group1.update((0, 0))
                target_group2.update((0, 0))
                target_group3.update((0, 0))
                target_group4.update((0, 0))
            else:
                target_group1.update((movement_step * 6.8, 0))
                target_group2.update((movement_step * 4.5, 0))
                target_group3.update((movement_step * 3.6, 0))
                target_group4.update((movement_step * 2, 0))

            add_target(target_group4, x, 0.2, 10, delta_t)
            target_group4.draw(screen)

            screen.blit(bg_mountain, (x * 2, 150))
            add_target(target_group3, x * 2, 0.4, 5, delta_t)
            target_group3.draw(screen)

            screen.blit(mg_hill, (x * 3.6, 350))
            add_target(target_group2, x * 3.6, 0.6, 5, delta_t)
            target_group2.draw(screen)

            screen.blit(mg_bush, (x * 4.5, 350))
            add_target(target_group1, x * 4.5, 1, 10, delta_t)
            target_group1.draw(screen)

            screen.blit(fg_grass, (x * 6.8, screen_height - H_fg_grass))

            scoring_ani_group.draw(screen)
            scoring_ani_group.update()

            bullet_group.draw(screen)
            bullet_group.update()

            screen.blit(update_score(), (20, 20))

            if Current_Time - Start_Time <= 500:
                screen.blit(text_go, (380, 150))

            if not ammo_available:
                screen.blit(text_Ammo_Unavailable, (screen_width - 230, screen_height - 40))

            Time_text, EndPlay_trigger = update_time((Current_Time - Start_Time) / 1000)
            screen.blit(Time_text, (screen_width - 220, 20))

            if EndPlay_trigger and StartPlay_trigger:
                MoveLeft_Flag = False
                MoveRight_Flag = False
                StartPlay_trigger = False
                v = -0.05
                target_group1.empty()
                target_group2.empty()
                target_group3.empty()
                target_group4.empty()
                mixer.music.load("res/audio/EndMusic.mp3")
                mixer.music.set_volume(0.5)
                mixer.music.play(-1)

        if Loop_State == 3:
            screen.blit(text_end, (290, 150))
            screen.blit(text_restart, (220, 280))
            screen.blit(update_score(), (350, 220))
            if edge_trigger:
                v *= -1
            if score > FileUtils.read_from_json("./record.json")["record"]:
                data = {"record": score}
                FileUtils.save_in_json(data, "./record.json")
        screen.blit(update_fps(), (20, screen_height - 30))
        pygame.display.flip()

    if game_state == "reference":
        draw_reference_menu()

    if game_state == "record":
        draw_record_menu()

    if game_state == "quit":
        pygame.quit()
        sys.exit()
