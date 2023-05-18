import copy

import pygame
import math
import pygame_menu
from random import randrange

WIDTH, HEIGHT = 1920, 1080
paddle_width_current = 300
paddle_width_constant = 300
paddle_speed_current = 50
paddle_speed_constant = 50
pygame.mixer.init()
back_ground_music = pygame.mixer.Sound('02 Space Riddle.mp3')
back_ground_music.set_volume(0.6)
block_broken = pygame.mixer.Sound('mixkit-arcade-game-explosion-2759.wav')
block_broken.set_volume(0.6)
ball_touch_paddle = pygame.mixer.Sound('mixkit-arcade-game-explosion-1699.wav')
ball_touch_paddle.set_volume(0.6)
level_win_sound = pygame.mixer.Sound('success_bell-6776.mp3')
level_win_sound.set_volume(2.0)
game_win_sound = pygame.mixer.Sound('goodresult-82807.mp3')
game_win_sound.set_volume(2.0)
game_lost_sound = pygame.mixer.Sound('mixkit-retro-arcade-game-over-470.wav')
game_lost_sound.set_volume(2.0)
live_lost_Sound = pygame.mixer.Sound('mixkit-losing-bleeps-2026.wav')


class Paddle:
    paddle_width = paddle_width_current
    paddle_height = 60
    paddle_speed = paddle_speed_constant
    paddle = pygame.Rect(WIDTH // 2 - paddle_width // 2, HEIGHT - paddle_height - 10,
                         paddle_width, paddle_height)


class Ball:
    ball_radius = 30
    ball_speed = 10
    inscribed_square = int(math.sqrt(2)*ball_radius)
    ball = pygame.Rect(randrange(inscribed_square, WIDTH - inscribed_square), HEIGHT // 2,
                       inscribed_square, inscribed_square)
    direction_x, direction_y = 1, -1


def press_processor(key, ball, lives):
    if key[pygame.K_LEFT] and Paddle.paddle.left > 0:
        Paddle.paddle.left -= Paddle.paddle_speed
    if key[pygame.K_RIGHT] and Paddle.paddle.right < WIDTH:
        Paddle.paddle.right += Paddle.paddle_speed
    if key[pygame.K_h] and ball.centery > HEIGHT:
        ball.centerx = WIDTH//2
        ball.centery = HEIGHT//2
        lives-=1
        live_lost_Sound.play()
    return lives


def ball_movement():
    Ball.ball.x += Ball.ball_speed * Ball.direction_x
    Ball.ball.y += Ball.ball_speed * Ball.direction_y
    if Ball.ball.centerx < Ball.ball_radius or Ball.ball.centerx > WIDTH - Ball.ball_radius:
        Ball.direction_x = -Ball.direction_x
    if Ball.ball.centery < Ball.ball_radius:
        Ball.direction_y = -Ball.direction_y
    if Ball.ball.colliderect(Paddle.paddle) and Ball.direction_y > 0:
        Ball.direction_x, Ball.direction_y = ball_and_block_collision_check(Ball.direction_x, Ball.direction_y,
                                                                            Ball.ball, Paddle.paddle)
        block_broken.play(fade_ms=50)


def ball_and_block_collision_check(direction_x, direction_y, ball, rect):
    if direction_x > 0:
        delta_x = ball.right - rect.left
    else:
        delta_x = rect.right - ball.left
    if direction_y > 0:
        delta_y = ball.bottom - rect.top
    else:
        delta_y = rect.bottom - ball.top
    if abs(delta_x - delta_y) < 25:
        direction_x, direction_y = -direction_x, -direction_y
    elif delta_x > delta_y:
        direction_y = -direction_y
    elif delta_y > delta_x:
        direction_x = -direction_x
    return direction_x, direction_y


def hit_output(hit_index, level_block, direction_x, direction_y, ball, score, broken_blocks):
    if hit_index != -1:
        hit_rect = level_block.pop(hit_index)
        broken_blocks.append([hit_rect, 0])
        direction_x, direction_y = ball_and_block_collision_check(direction_x, direction_y, ball, hit_rect)
        ball_touch_paddle.play(fade_ms=50)
        return direction_x, direction_y, level_block, score+1, broken_blocks
    else:
        return direction_x, direction_y, level_block, score, broken_blocks


def game_end_conditions(score, ball, lives, level_blocks):
    if score >= len(level_blocks):
        return score, ball, lives
    elif ball.centery > HEIGHT or ball.centerx > WIDTH or ball.centerx < 0:
        if lives > 0:
            ball: pygame.Rect
            ball.centerx = WIDTH//2
            ball.centery = HEIGHT//2
            lives-=1
            live_lost_Sound.play()
            return score, ball, lives
        else:
            print("Game Over!")
            return score, ball, 0
    else:
        return score, ball, lives


def buff_processor(score, buff, timer, level_blocks, fps, lives):
    global paddle_width_current
    global paddle_speed_current

    if buff == 'Longer paddle' and timer==0:
        paddle_width_current += 200
        timer = 3600
        return score, timer, level_blocks, fps, lives
    elif buff == 'Faster paddle' and timer==0:
        if paddle_speed_current>0:
            paddle_speed_current+= 50
        else:
            paddle_speed_current-=50
        timer = 3600
        return score, timer, level_blocks, fps, lives
    elif buff == 'Slower game' and timer==0:
        fps = 30
        timer = 3600
        return score, timer, level_blocks, fps, lives
    elif buff == 'Additional lives':
        if lives < 4:
            lives += 1
        return score+1, timer, level_blocks, fps, lives
    elif buff =='Bricks broken':
        for iteration in range(int(len(level_blocks)/10)):
            level_blocks.pop(0)
            score+=1
        return score, timer, level_blocks, fps, lives
    else:
        if timer != 0:
            timer-=60
            return score, timer, level_blocks, fps, lives
        else:
            fps = 60
            paddle_speed_current = copy.deepcopy(paddle_speed_constant)
            paddle_width_current = copy.deepcopy(paddle_width_constant)
            return score, timer, level_blocks, fps, lives


def ball_direction_processor(direction_x, direction_y, ball_north_east, ball_north_west, ball_straight,
                             ball_south_west, ball_south_east, screen):
    if direction_x == -1 and direction_y == -1:
        screen.blit(ball_north_west, (Ball.ball.centerx - 30, Ball.ball.centery - 30))
    elif direction_x == -1 and direction_y == 1:
        screen.blit(ball_south_west, (Ball.ball.centerx - 30, Ball.ball.centery - 30))
    elif direction_x == 1 and direction_y == -1:
        screen.blit(ball_north_east, (Ball.ball.centerx - 30, Ball.ball.centery - 30))
    elif direction_x == 1 and direction_y == 1:
        screen.blit(ball_south_east, (Ball.ball.centerx - 30, Ball.ball.centery - 30))
    else:
        screen.blit(ball_straight, (Ball.ball.centerx, Ball.ball.centery))


def blocks_image_processor(level_blocks, screen, block_untouched):
    for block in level_blocks:
        screen.blit(block_untouched, (block.centerx - 64, block.centery - 64))


def explousion_constructor():
    explousion_frame_1 = pygame.image.load('star_tiny.png').convert_alpha()
    explousion_frame_2 = pygame.image.load('star_small.png').convert_alpha()
    explousion_frame_3 = pygame.image.load('star_medium.png').convert_alpha()
    explousion_frame_4 = pygame.image.load('star_large.png').convert_alpha()
    explousion_frame_5 = pygame.image.load('meteor_large.png').convert_alpha()
    explousion = [explousion_frame_1, explousion_frame_2, explousion_frame_3, explousion_frame_4, explousion_frame_5]
    return explousion


def explousion_animation(rect, screen, explousion):
    for broken in rect:
        if broken[1] <15:
            screen.blit(explousion[0], (broken[0].centerx-64, broken[0].centery-64))
        elif 30 > broken[1] > 15:
            screen.blit(explousion[1], (broken[0].centerx - 64, broken[0].centery - 64))
        elif 30 < broken[1] <40:
            screen.blit(explousion[2], (broken[0].centerx - 64, broken[0].centery - 64))
        elif 40 < broken[1] <60:
            screen.blit(explousion[3], (broken[0].centerx - 64, broken[0].centery - 64))
        elif 60 < broken[1] <80:
            screen.blit(explousion[0], (broken[0].centerx - 64, broken[0].centery - 64))
        broken[1]+=1
    rect = [broken for broken in rect if broken[1]<80]
    return rect


def draw_lives(lives, live_pict, screen):
    for live in range(lives):
        screen.blit(live_pict, (128*live, 10))


def main(level_blocks, screen, fps, current: pygame_menu.Menu, table_of_buffs, lives):
    startind_blocks = len(level_blocks)

    live_pict = pygame.image.load('ship_B.png').convert_alpha()
    background = pygame.image.load('background.jpg').convert_alpha()
    ball_north_east = pygame.image.load('plate_north_east.png').convert_alpha()
    ball_north_west = pygame.image.load('plate_north_west.png').convert_alpha()
    ball_straight = pygame.image.load('plate_straight.png').convert_alpha()
    ball_south_east = pygame.image.load('plate_south_east.png').convert_alpha()
    ball_south_west = pygame.image.load('plate_south_west.png').convert_alpha()
    block_before_touch = pygame.image.load('table_with_customers.png').convert_alpha()
    paddle_picture = pygame.image.load('paddle.png').convert_alpha()
    broken_blocks = []
    explousion = explousion_constructor()

    back_ground_music.play()
    clock = pygame.time.Clock()
    score = 0
    running = True
    timer = 0
    while running:

        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                break
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_ESCAPE:
                    current.enable()
        if current.is_enabled():
            current.update(events)

        screen.blit(background, (0, 0))

        blocks_image_processor(level_blocks, screen, block_before_touch)
        screen.blit(paddle_picture, (Paddle.paddle.centerx-paddle_width_constant//2, Paddle.paddle.centery-30))
        draw_lives(lives, live_pict, screen)
        ball_direction_processor(Ball.direction_x, Ball.direction_y, ball_north_east,
                                 ball_north_west, ball_straight, ball_south_west, ball_south_east, screen)

        hit_index = Ball.ball.collidelist(level_blocks)
        Ball.direction_x, Ball.direction_y, level_blocks, score, broken_blocks= hit_output(hit_index, level_blocks,
                                                                                           Ball.direction_x,
                                                                                           Ball.direction_y, Ball.ball,
                                                                                           score, broken_blocks)
        broken_blocks = explousion_animation(broken_blocks, screen, explousion)
        ball_movement()
        key_pressed = pygame.key.get_pressed()
        lives = press_processor(key_pressed, Ball.ball, lives)

        score, timer, level_blocks, fps, lives = buff_processor(score, table_of_buffs.get(score),
                                                                timer, level_blocks, fps, lives)

        score, Ball.ball, lives = game_end_conditions(score, Ball.ball, lives, level_blocks)
        if lives == 0:
            back_ground_music.stop()
            game_lost_sound.play()
            return score, 0
        elif lives != 0 and len(level_blocks) == 0:
            back_ground_music.stop()
            if startind_blocks == 34:
                game_win_sound.play()
            else:
                level_win_sound.play()
            return score, lives
        pygame.display.flip()
        clock.tick(fps)

