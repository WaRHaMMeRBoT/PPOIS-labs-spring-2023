from enum import Enum
import json

class Levels(Enum):
    LEVEL1 = "./configs/levels/level1.json"
    LEVEL2 = "./configs/levels/level2.json"
    LEVEL3 = "./configs/levels/level3.json"
    LEVEL4 = "./configs/levels/level4.json"
    LEVEL5 = "./configs/levels/level5.json"
    LEVEL6 = "./configs/levels/level6.json"
    LEVEL7 = "./configs/levels/level7.json"
    LEVEL8 = "./configs/levels/level8.json"
    LEVEL9 = "./configs/levels/level9.json"
    LEVEL10 = "./configs/levels/level10.json"

class ConfigController:

    def __init__(self):
        unpacked_data = self._load_json_config("./configs/general_configs.json")
        self._unpack_general_params(unpacked_data["general_params"])
        self._unpack_objects_params(unpacked_data["objects_params"])
        self._unpack_info_panels_params(unpacked_data["info_panels_params"])
        self._unpack_text_message_params(unpacked_data["text_message_params"])

    @staticmethod
    def _load_json_config(filename):
        with open(filename, 'r') as config_file:
            if config_file:
                return json.load(config_file)
            raise ValueError(f"No such file {filename}")

    def _unpack_general_params(self, unpacked_data):
        self.background_image = unpacked_data["background_image"]
        self.screen_width = unpacked_data["screen_width"]
        self.screen_height = unpacked_data["screen_height"]
        self.frame_rate = unpacked_data["frame_rate"]
        self.effect_duration = unpacked_data["effect_duration"]
        self.initial_lives = unpacked_data["initial_lives"]
        self.background_music_duration = unpacked_data["background_music_duration"]
        self.sounds_effects = unpacked_data["sounds_effects"]
        self.level_open_flags = unpacked_data["level_open_flags"]
        self.help_messages = unpacked_data["help_messages"]

    def _unpack_objects_params(self, unpacked_data):
        self.menu_offset_x = unpacked_data["menu_offset_x"]
        self.menu_offset_y = unpacked_data["menu_offset_y"]
        self.menu_button_w = unpacked_data["menu_button_w"]
        self.menu_button_h = unpacked_data["menu_button_h"]
        self.menu_button_interval = unpacked_data["menu_button_interval"]
        self.button_text_color = unpacked_data["button_text_color"]
        self.button_normal_back_color = unpacked_data["button_normal_back_color"]
        self.button_hover_back_color = unpacked_data["button_hover_back_color"]
        self.button_pressed_back_color = unpacked_data["button_pressed_back_color"]

        self.brick_width = unpacked_data["brick_width"]
        self.brick_height = unpacked_data["brick_height"]
        self.brick_color = unpacked_data["brick_color"]

        self.ball_speed = unpacked_data["ball_speed"]
        self.ball_radius = unpacked_data["ball_radius"]
        self.ball_color = unpacked_data["ball_color"]
        self.ball_acceleration = unpacked_data["ball_acceleration"]

        self.paddle_width = unpacked_data["paddle_width"]
        self.paddle_height = unpacked_data["paddle_height"]
        self.paddle_color = unpacked_data["paddle_color"]
        self.paddle_speed = unpacked_data["paddle_speed"]

    def _unpack_bricks_location_params(self, unpacked_data):
        self.row_count = unpacked_data["row_count"]
        self.brick_width = unpacked_data["brick_width"]
        self.offset_y = unpacked_data["offset_y"]

    def _unpack_info_panels_params(self, unpacked_data):
        self.status_offset_y = unpacked_data["status_offset_y"]
        self.text_color = unpacked_data["text_color"]
        self.lives_right_offset = unpacked_data["lives_right_offset"]
        self.lives_offset = unpacked_data["lives_offset"]
        self.score_offset = unpacked_data["score_offset"]

    def _unpack_text_message_params(self, unpacked_data):
        self.font_name = unpacked_data["font_name"]
        self.font_size = unpacked_data["font_size"]
        self.death_message_duration = unpacked_data["death_message_duration"]
        self.start_message_duration = unpacked_data["start_message_duration"]
        self.win_message_duration = unpacked_data["win_message_duration"]

    def load_level_info(self, level_number):
        if isinstance(level_number, Levels):
            unpacked_data = self._load_json_config(level_number.value)
            self._unpack_bricks_location_params(unpacked_data["bricks_location_params"])
            self.ball_acceleration_interval = unpacked_data["ball_acceleration_interval"]
            self.level_records = unpacked_data["level_records"]
            self.level_records = dict(sorted(self.level_records.items(), key=lambda item: item[1], reverse=True))
            self.level_config_file = level_number.value
            self.max_effects_amount = unpacked_data["max_effects_amount"]
        else:
            raise ValueError(f"Unknown level {level_number}")

    def update_level_config(self):
        if not self.level_config_file.endswith('.json'):
            raise ValueError(f"Excepted .json file, got {self.level_config_file} instead")
        with open(self.level_config_file, 'w') as config_file:
            if config_file:
                new_config_data = {
                    "ball_acceleration_interval": self.ball_acceleration_interval,
                    "level_records": self.level_records,
                    "bricks_location_params": {
                        "row_count": self.row_count,
                        "brick_width": self.brick_width,
                        "offset_y": self.offset_y
                    },
                    "max_effects_amount": self.max_effects_amount
                }
                return json.dump(new_config_data, config_file, indent='\t')
            raise ValueError(f"No such file {self.level_config_file}")

    def _pack_general_params(self):
        return {
            "background_image": self.background_image,
            "screen_width": self.screen_width,
            "screen_height": self.screen_height,
            "frame_rate": self.frame_rate,
            "effect_duration": self.effect_duration,
            "initial_lives": self.initial_lives,
            "background_music_duration": self.background_music_duration,
            "sounds_effects": self.sounds_effects,
            "level_open_flags": self.level_open_flags,
            "help_messages": self.help_messages
        }

    def _pack_object_params(self):
        return {
            "menu_offset_x": self.menu_offset_x,
            "menu_offset_y": self.menu_offset_y,
            "menu_button_w": self.menu_button_w,
            "menu_button_h": self.menu_button_h,
            "menu_button_interval": self.menu_button_interval,
            "button_text_color": self.button_text_color,
            "button_normal_back_color": self.button_normal_back_color,
            "button_hover_back_color": self.button_hover_back_color,
            "button_pressed_back_color": self.button_pressed_back_color,
            "brick_width": self.brick_width,
            "brick_height": self.brick_height,
            "brick_color": self.brick_color,
            "ball_speed": self.ball_speed,
            "ball_radius": self.ball_radius,
            "ball_color": self.ball_color,
            "ball_acceleration": self.ball_acceleration,
            "paddle_width": self.paddle_width,
            "paddle_height": self.paddle_height,
            "paddle_color": self.paddle_color,
            "paddle_speed": self.paddle_speed
        }

    def _pack_info_panels_params(self):
        return {
            "status_offset_y": self.status_offset_y,
            "text_color": self.text_color,
            "lives_right_offset": self.lives_right_offset,
            "lives_offset": self.lives_offset,
            "score_offset": self.score_offset
        }

    def _pack_text_message_params(self):
        return {
            "font_name": self.font_name,
            "font_size": self.font_size,
            "death_message_duration": self.death_message_duration,
            "start_message_duration": self.start_message_duration,
            "win_message_duration": self.win_message_duration
        }

    def update_general_config(self):
        new_config_data = {
            "general_params": self._pack_general_params(),
            "objects_params": self._pack_object_params(),
            "info_panels_params": self._pack_info_panels_params(),
            "text_message_params": self._pack_text_message_params(),
        }
        with open("./configs/general_configs.json", 'w') as config_file:
            json.dump(new_config_data, config_file, indent='\t')
