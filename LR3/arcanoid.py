# Author Vodohleb04
import random
from datetime import datetime, timedelta
import time
from typing import NoReturn, Tuple, List
import pygame
from pygame.rect import Rect
from config_controller import ConfigController, Levels
from bowl import Bowl
from brick import Brick
from menu_button import Button
from game_kernel import GameKernel
from player_break import Paddle
from text_controller import TextObject
import colors
from records_dialog import make_record_dialog
from help_dialog import  make_help_dialog


class Arcanoid(GameKernel):
    def __init__(self):
        self.config = ConfigController()
        GameKernel.__init__(self, 'Arcanoid04', self.config.screen_width, self.config.screen_height,
                            self.config.background_image, self.config.frame_rate)
        self._sound_effects = {name: pygame.mixer.Sound(sound) for name, sound in self.config.sounds_effects.items()}
        self._reset_effect = None
        self._effect_start_time = None
        self._current_level = None
        self._lives = self.config.initial_lives
        self._score = 5 * self._lives
        self._start_level = False
        self._paddle = None
        self._bricks = None
        self._bowl = None
        self._menu_buttons = []
        self._stats_button = None
        self._play_button = None
        self._is_game_running = False
        self._accelerate_paddle_flag = False
        self._make_special_effects()
        self._create_menu()
        self._points_per_brick = 1
        self._sound_effects["background_music"].play()
        self._background_music_start = datetime.now()
        self._broken_bricks_amount = 0

    def _make_special_effects(self) -> NoReturn:
        self.special_effects = dict(
            long_paddle=(
                colors.ORANGE, lambda g: g._paddle.bounds.inflate_ip(self.config.paddle_width // 2, 0),
                lambda g: g._paddle.bounds.inflate_ip(-self.config.paddle_width // 2, 0)),
            slow_bowl=(
                colors.AQUAMARINE2, lambda g: g.change_bowl_speed(-1), lambda g: g.change_bowl_speed(1)),
            tripple_points=(
                colors.DARKSEAGREEN4, lambda g: g.set_points_per_brick(5), lambda g: g.set_points_per_brick(1)),
            extra_life=(
                colors.GOLD1, lambda g: g.add_life(), lambda g: None))

    def add_life(self) -> NoReturn:
        self._lives += 1
        self._score += 5

    def set_points_per_brick(self, points) -> NoReturn:
        self._points_per_brick = points

    def change_bowl_speed(self, dy) -> NoReturn:
        self._bowl.speed = (self._bowl.speed[0], self._bowl.speed[1] + dy)

    def _on_play(self, button: List[Button]) -> NoReturn:
        for b in self._menu_buttons:
            self._objects.remove(b)
        self._is_game_running = True
        self._start_level = True
        self._sound_effects["start"].play()

    def _on_quit(self, button) -> NoReturn:
        self._game_over = True
        self._is_game_running = False

    def _on_show_stats(self, button) -> NoReturn:
        make_record_dialog(self.config)

    def _on_show_help(self, button) -> NoReturn:
        make_help_dialog(self.config)

    def _make_stats_button(self) -> NoReturn:
        if self._stats_button:
            self._objects.remove(self._stats_button)
            self._menu_buttons.remove(self._stats_button)
            self._mouse_handlers.remove(self._stats_button.handle_mouse_event)
        b = Button(self.config, self.config.menu_offset_x, self.config.font_size + self.config.status_offset_y +
                   (self.config.menu_button_h + 5) * 7, self.config.menu_button_w,
                   self.config.menu_button_h, "STATS", self._on_show_stats, padding=5)
        self._objects.append(b)
        self._menu_buttons.append(b)
        self._mouse_handlers.append(b.handle_mouse_event)
        self._stats_button = b

    def _make_play_button(self) -> NoReturn:
        if self._play_button:
            self._objects.remove(self._play_button)
            self._menu_buttons.remove(self._play_button)
            self._mouse_handlers.remove(self._play_button.handle_mouse_event)
        b = Button(self.config, self.config.menu_offset_x, self.config.screen_height // 2 + self.config.font_size,
                   self.config.menu_button_w, self.config.menu_button_h, "PLAY", self._on_play, padding=5)
        self._objects.append(b)
        self._menu_buttons.insert(0, b)
        self._mouse_handlers.append(b.handle_mouse_event)
        self._play_button = b

    def _make_help_button(self) -> NoReturn:
        help_button = Button(
            self.config, self.config.menu_offset_x + self.config.menu_button_w + self.config.menu_button_interval,
                         self.config.font_size + self.config.status_offset_y + (self.config.menu_button_h + 5) * 7,
            self.config.menu_button_w, self.config.menu_button_h, text='HELP', on_click=self._on_show_help, padding=5)
        self._objects.append(help_button)
        self._menu_buttons.append(help_button)
        self._mouse_handlers.append(help_button.handle_mouse_event)

    @staticmethod
    def _define_level_number(button) -> Levels:
        if button.text.text_string == "LEVEL 1":
            return Levels.LEVEL1
        elif button.text.text_string == "LEVEL 2":
            return Levels.LEVEL2
        elif button.text.text_string == "LEVEL 3":
            return Levels.LEVEL3
        elif button.text.text_string == "LEVEL 4":
            return Levels.LEVEL4
        elif button.text.text_string == "LEVEL 5":
            return Levels.LEVEL5
        else:
            raise ValueError("Unknown button")

    def _on_load_level(self, button) -> NoReturn:
        if self._define_level_number(button) != self._current_level:
            if self._current_level:
                self._new_game()
            self._make_play_button()
            self._make_stats_button()
            self.config.load_level_info(self._define_level_number(button))
            self._current_level = self._define_level_number(button)
            self._create_objects()

    def _make_buttons(self) -> List:
        res_buttons = [('QUIT', self._on_quit)]
        if self.config.level_open_flags["LEVEL 1"]:
            res_buttons.append(('LEVEL 1', self._on_load_level))
        if self.config.level_open_flags["LEVEL 2"]:
            res_buttons.append(('LEVEL 2', self._on_load_level))
        if self.config.level_open_flags["LEVEL 3"]:
            res_buttons.append(('LEVEL 3', self._on_load_level))
        if self.config.level_open_flags["LEVEL 4"]:
            res_buttons.append(('LEVEL 4', self._on_load_level))
        if self.config.level_open_flags["LEVEL 5"]:
            res_buttons.append(('LEVEL 5', self._on_load_level))
        return res_buttons

    def create_menu_buttons(self) -> NoReturn:
        for i, (text, click_handler) in enumerate(self._make_buttons()):
            b = Button(self.config, self.config.menu_offset_x +
                       (self.config.menu_button_w + self.config.menu_button_interval) * (i + 1),
                       self.config.screen_height // 2 + self.config.font_size, self.config.menu_button_w,
                       self.config.menu_button_h, text, click_handler, padding=5)
            self._objects.append(b)
            self._menu_buttons.append(b)
            self._mouse_handlers.append(b.handle_mouse_event)
        self._make_help_button()

    def _create_menu(self) -> NoReturn:
        self.create_labels()
        self.create_menu_buttons()

    def _create_objects(self) -> NoReturn:
        self.create_bricks()
        self.create_paddle()
        self.create_bowl()

    def create_labels(self) -> NoReturn:
        self.score_label = TextObject(
            self.config.score_offset, self.config.status_offset_y, lambda: f'SCORE: {self._score}',
            self.config.text_color, self.config.font_name, self.config.font_size)
        self.objects.append(self.score_label)
        self.lives_label = TextObject(
            self.config.lives_offset, self.config.status_offset_y, lambda: f'LIVES: {self._lives}',
            self.config.text_color, self.config.font_name, self.config.font_size)
        self.objects.append(self.lives_label)

    def create_bowl(self) -> NoReturn:
        speed = (random.randint(-2, 2), self.config.bowl_speed)
        self._bowl = Bowl(self.config.screen_width // 2, self.config.screen_height // 2, self.config.bowl_radius,
                          self.config.bowl_color, speed, self.config.bowl_acceleration)
        self.objects.append(self._bowl)

    def create_paddle(self) -> NoReturn:
        paddle = Paddle(
            self.config, (self.config.screen_width - self.config.paddle_width) // 2,
            self.config.screen_height - self.config.paddle_height * 2, self.config.paddle_width,
            self.config.paddle_height, self.config.paddle_color, self.config.paddle_speed)
        self.keydown_handlers[pygame.K_LEFT].append(paddle.handle)
        self.keydown_handlers[pygame.K_RIGHT].append(paddle.handle)
        self.keyup_handlers[pygame.K_LEFT].append(paddle.handle)
        self.keyup_handlers[pygame.K_RIGHT].append(paddle.handle)
        self._paddle = paddle
        self.objects.append(self._paddle)

    def create_bricks(self) -> NoReturn:
        def make_brick(self: Arcanoid, w, h, offset_x, row, col) -> Brick:
            effect = None
            brick_color = self.config.brick_color
            index = random.randint(0, 10)
            nonlocal bricks_with_effect_amount
            if bricks_with_effect_amount < self.config.max_effects_amount and index < len(self.special_effects):
                brick_color, start_effect_func, reset_effect_func = list(self.special_effects.values())[index]
                effect = start_effect_func, reset_effect_func
                bricks_with_effect_amount += 1

            return Brick(offset_x + col * (w + 1), self.config.offset_y + row * (h + 1), w, h, brick_color, effect)

        bricks_with_effect_amount = 0
        w = self.config.brick_width
        h = self.config.brick_height
        brick_count = self.config.screen_width // (w + 1)
        offset_x = (self.config.screen_width - brick_count * (w + 1)) // 2
        bricks = []
        for row in range(self.config.row_count):
            for col in range(brick_count):
                brick = make_brick(self, w, h, offset_x, row, col)
                bricks.append(brick)
                self.objects.append(brick)
        self._bricks = bricks

    @staticmethod
    def _intersect(obj, bowl) -> [str, None]:
        edges = dict(left=Rect(obj.left, obj.top, 1, obj.height), right=Rect(obj.right, obj.top, 1, obj.height),
                     top=Rect(obj.left, obj.top, obj.width, 1), bottom=Rect(obj.left, obj.bottom, obj.width, 1))
        collisions = set(edge for edge, rect in edges.items() if bowl.bounds.colliderect(rect))
        if not collisions:
            return None
        if len(collisions) == 1:
            return list(collisions)[0]
        if 'top' in collisions:
            if bowl.centery <= obj.top:
                return 'top'
            if bowl.centerx - bowl.radius <= obj.left:
                return 'left'
            else:
                return 'right'
        if 'bottom' in collisions:
            if bowl.centery >= obj.bottom:
                return 'bottom'
            elif bowl.centerx + bowl.radius <= obj.left:
                return 'left'
            else:
                return 'right'

    def _hit_paddle(self) -> NoReturn:
        speed = self._bowl.speed
        edge = self._intersect(self._paddle, self._bowl)
        if edge is not None:
            self._sound_effects['paddle_hit'].play()
        if edge == 'top':
            self._top_hit_paddle(speed)
        if edge == 'left':
            self._left_hit_paddle(speed)
        if edge == 'right':
            self._right_hit_paddle(speed)

    def _top_hit_paddle(self, speed: Tuple[int, int]) -> NoReturn:
        speed_x = speed[0]
        speed_y = -speed[1]
        if self._paddle.moving_left:
            speed_x -= 1
        elif self._paddle.moving_right:
            speed_x += 1
        if self._paddle.top >= self._bowl.centery + self._bowl.radius:
            shift = self._bowl.radius - (self._paddle.top - self._bowl.centery)
        else:
            shift = self._bowl.radius + (self._bowl.centery - self._paddle.top)
        self._bowl.move(0, -shift)
        self._bowl.speed = speed_x, speed_y

    def _left_hit_paddle(self, speed: Tuple[int, int]) -> NoReturn:
        self._bowl.speed = (-speed[0], speed[1]) if speed[0] > 0 else (speed[0], speed[1])
        if self._bowl.centerx < self._paddle.left:
            shift = self._bowl.radius - (self._paddle.left - self._bowl.centerx)
        else:
            shift = self._bowl.radius + self._bowl.centerx - self._paddle.left
        if self._paddle.moving_left:
            shift += self._paddle.speed[0]
            self._bowl.speed = self._bowl.speed[0] + self._paddle.speed[0], self._bowl.speed[1]
        self._bowl.move(-shift, 0)

    def _right_hit_paddle(self, speed: Tuple[int, int]) -> NoReturn:
        self._bowl.speed = (-speed[0], speed[1]) if speed[0] < 0 else (speed[0], speed[1])
        if self._bowl.centerx > self._paddle.right:
            shift = self._bowl.radius - (self._bowl.centerx - self._paddle.right)
        else:
            shift = self._bowl.radius + self._paddle.right - self._bowl.centerx
        if self._paddle.moving_right:
            shift += self._paddle.speed[0]
            self._bowl.speed = self._bowl.speed[0] + self._paddle.speed[0], self._bowl.speed[1]
        self._bowl.move(shift, 0)

    def _hit_screen_bounds(self) -> NoReturn:
        speed = self._bowl.speed
        if self._bowl.top > self.config.screen_height:
            self._lives -= 1
            self._score -= 5
            if self._lives == 0:
                self._sound_effects["death"].play()
                self.show_message('GAME OVER!', self.config.death_message_duration, centralized=True)
                self._new_game()
                return
            else:
                self._lose_hp()
        if self._bowl.top < 0:
            self._bowl.speed = (speed[0], -speed[1])
            self._sound_effects["wall_hit"].play()
        if self._bowl.left < 0 or self._bowl.right > self.config.screen_width:
            self._bowl.speed = (-speed[0], speed[1])
            self._sound_effects["wall_hit"].play()

    def _break_brick(self, brick: Brick) -> NoReturn:
        self._broken_bricks_amount += 1
        self._sound_effects['brick_hit'].play()
        self._bricks.remove(brick)
        self.objects.remove(brick)
        self._score += self._points_per_brick

    def _hit_brick(self) -> NoReturn:
        speed = self._bowl.speed
        for brick in self._bricks:
            edge = self._intersect(brick, self._bowl)
            if not edge:
                continue
            self._break_brick(brick)
            if edge in ('top', 'bottom'):
                self._bowl.speed = (speed[0], -speed[1])
            else:
                self._bowl.speed = (-speed[0], speed[1])
            if brick.special_effect is not None:
                if self._reset_effect is not None:
                    self._reset_effect(self)
                self._effect_start_time = datetime.now()
                brick.special_effect[0](self)
                self._reset_effect = brick.special_effect[1]
                if not len(self._bricks) == 0:
                    self._sound_effects["bonus_taken"].play()

    def handle_bowl_collisions(self) -> NoReturn:
        self._hit_paddle()
        self._hit_brick()
        self._hit_screen_bounds()

    def update(self) -> NoReturn:
        self._update_background_music()
        if not self._is_game_running:
            return
        if self._start_level:
            self._start_level = False
            self.show_message('GET READY!', self.config.start_message_duration, centralized=True)
        if not self._bricks:
            self._win()
            return
        if self._reset_effect:
            self._update_effect_duration()
        if self._broken_bricks_amount >= self.config.bowl_acceleration_interval:
            self._bowl_acceleration()
            self._paddle_acceleration()
        self.handle_bowl_collisions()
        super().update()

    def _update_effect_duration(self) -> NoReturn:
        if datetime.now() - self._effect_start_time >= timedelta(seconds=self.config.effect_duration):
            self._reset_effect(self)
            self._reset_effect = None

    def _update_background_music(self) -> NoReturn:
        if datetime.now() - self._background_music_start >= timedelta(seconds=self.config.background_music_duration):
            self._sound_effects["background_music"].play()
            self._background_music_start = datetime.now()

    def _is_record(self) -> bool:
        if len(self.config.level_records.values()) < 5:
            return True
        for score in self.config.level_records.values():
            if self._score >= score:
                return True
        return False

    def _unlock_new_level(self) -> NoReturn:
        if self._current_level == Levels.LEVEL1 and not self.config.level_open_flags["LEVEL 2"]:
            self.config.level_open_flags["LEVEL 2"] = True
        elif self._current_level == Levels.LEVEL2 and not self.config.level_open_flags["LEVEL 3"]:
            self.config.level_open_flags["LEVEL 3"] = True
        elif self._current_level == Levels.LEVEL3 and not self.config.level_open_flags["LEVEL 4"]:
            self.config.level_open_flags["LEVEL 4"] = True
        elif self._current_level == Levels.LEVEL4 and not self.config.level_open_flags["LEVEL 5"]:
            self.config.level_open_flags["LEVEL 5"] = True

    def _new_game(self) -> NoReturn:
        self._reset_effect = None
        self._effect_start_time = None
        self._current_level = None
        self._lives = self.config.initial_lives
        self._score = 5 * self._lives
        self._start_level = False
        self._paddle = None
        self._bricks = None
        self._bowl = None
        self.objects.clear()
        self._menu_buttons.clear()
        self.mouse_handlers.clear()
        self._stats_button = None
        self._play_button = None
        self._is_game_running = False
        self._accelerate_paddle_flag = False
        self._create_menu()
        self._broken_bricks_amount = 0

    def _win(self) -> NoReturn:
        self._unlock_new_level()
        self.config.update_general_config()
        if not self._is_record():
            win_msg = f'win{random.randint(1, 2)}'
            self._sound_effects[win_msg].play()
            self.show_message('YOU WIN!!!', self.config.win_message_duration, centralized=True)
            self._is_game_running = False
            self._new_game()
        else:
            self._sound_effects["new_record"].play()
            self.show_message('NEW RECORD!!!', self.config.win_message_duration, centralized=True)
            make_record_dialog(self.config, self._score)
            self._is_game_running = False
            self._new_game()

    def _lose_hp(self) -> NoReturn:
        self._broken_bricks_amount = 0
        self._sound_effects['minus_hp'].play()
        self.create_bowl()
        self._paddle.base_speed()
        self._accelerate_paddle_flag = False
        if self._reset_effect:
            self._reset_effect(self)
            self._reset_effect = None
        self._paddle.move(-self._paddle.left, 0)
        self._paddle.move((self.config.screen_width - self.config.paddle_width) // 2, 0)
        self.show_message("BE READY!", self.config.start_message_duration, centralized=True)

    def _bowl_acceleration(self) -> NoReturn:
        self._bowl.accelerate()
        self._broken_bricks_amount = 0

    def _paddle_acceleration(self) -> NoReturn:
        if self._accelerate_paddle_flag:
            self._paddle.accelerate()
            self._accelerate_paddle_flag = False
        else:
            self._accelerate_paddle_flag = True

    def show_message(self, text, duration, color=colors.WHITE, font_name='Arial', font_size=20, centralized=False)\
            -> NoReturn:
        message = TextObject(self.config.screen_width // 2, self.config.screen_height // 2, lambda: text, color,
                             font_name, font_size)
        self.draw()
        message.draw(self._surface, centralized)
        pygame.display.update()
        time.sleep(duration)


def main() -> NoReturn:
    Arcanoid().run()


if __name__ == '__main__':
    main()

