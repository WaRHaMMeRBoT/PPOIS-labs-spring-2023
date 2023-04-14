import json

class Wave:
    def __init__(self, close_slow_enemy_spawn_time, close_slow_upgraded_enemy_spawn_time,
                 close_slow_superior_enemy_spawn_time, close_chunky_enemy_spawn_time,
                 close_fast_enemy_spawn_time, inspector_chunky_enemy_spawn_time,
                 inspector_chunky_upgraded_enemy_spawn_time, waiter_average_enemy_spawn_time,
                 close_fast_knife_enemy_spawn_time, police_average_enemy_spawn_time):
        self.close_slow_enemy_spawn_time = close_slow_enemy_spawn_time
        self.close_slow_upgraded_enemy_spawn_time = close_slow_upgraded_enemy_spawn_time
        self.close_slow_superior_enemy_spawn_time = close_slow_superior_enemy_spawn_time
        self.close_chunky_enemy_spawn_time = close_chunky_enemy_spawn_time
        self.close_fast_enemy_spawn_time = close_fast_enemy_spawn_time
        self.inspector_chunky_enemy_spawn_time = inspector_chunky_enemy_spawn_time
        self.inspector_chunky_upgraded_enemy_spawn_time = inspector_chunky_upgraded_enemy_spawn_time
        self.waiter_average_enemy_spawn_time = waiter_average_enemy_spawn_time
        self.close_fast_knife_enemy_spawn_time = close_fast_knife_enemy_spawn_time
        self.police_average_enemy_spawn_time = police_average_enemy_spawn_time

    @staticmethod
    def read_waves_from_json(file_path):
        waves = []
        with open(file_path, 'r') as f:
            data = json.load(f)
            for i in range(1, 21):
                wave_data = data.get(f"wave_{i}")
                wave = Wave(**wave_data)
                waves.append(wave)
        return waves



