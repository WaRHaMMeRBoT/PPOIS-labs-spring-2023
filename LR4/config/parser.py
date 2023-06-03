from configparser import ConfigParser
import json
import entity.aliens


def update_leaderboard(config: ConfigParser, value: tuple):
    scores = get_leaderboard(config)
    scores[str(value[0])] = int(value[1])

    config['Leaderboard']['scores'] = json.dumps(scores)
    with open('config.ini', 'w') as configfile:
        config.write(configfile)


def get_max_score(config: ConfigParser) -> int:
    return int(list(get_sorted_leaderboard(config).values())[0])


def get_leaderboard(config: ConfigParser) -> dict[str, int]:
    config.read('config.ini')
    
    if not config.has_section('Leaderboard'):
        config.add_section('Leaderboard')
        with open('config.ini', 'w') as configfile:
            config.write(configfile)

    return json.loads(config.get('Leaderboard', 'scores'))

def get_sorted_leaderboard(config: ConfigParser) -> dict[str, int]:
    return dict(sorted(get_leaderboard(config).items(), key=lambda e: e[1], reverse=True))


def default_wave(player, aliens, area_start, entity_size, aliens_in_wave, wave) -> list: #отрисовывается в начале
    result = []
    for i in range(aliens_in_wave):

        result.append(entity.aliens.RegularAlien(player, aliens, ((area_start + 1 + ((entity_size + 4) * i), -(entity_size + 4) * wave)), 1))
    return result


def read_waves(player, config: ConfigParser, area_start, entity_size, aliens_in_wave, waves) -> list:
    config.read('config.ini')
    result = []

    if not config.has_section('Waves'):

        config.add_section('waves')
        with open('config.ini', 'w') as configfile:
            config.write(configfile)
            return result

    for w in range(waves):

        try:
            wave: dict[str, int] = json.loads(config.get('Waves', f'wave_{w}'))

            for a in range(aliens_in_wave):
                wave_list = list(wave.items())
                alien = wave_list[a] if a < len(wave_list) else ('regular', 1)


                if alien[0] == 'regular':
                    result.append(entity.aliens.RegularAlien(player, result, (
                    (area_start + 1 + ((entity_size + 4) * a), -(entity_size + 4) * w)), alien[1]))
                elif alien[0] == 'shotgun':
                    result.append(entity.aliens.ShotgunAlien(player, result, (
                    (area_start + 1 + ((entity_size + 4) * a), -(entity_size + 4) * w)), alien[1]))
                elif alien[0] == 'burst':
                    result.append(entity.aliens.BurstAlien(player, result, (
                    (area_start + 1 + ((entity_size + 4) * a), -(entity_size + 4) * w)), alien[1]))
                elif alien[0] == 'super':
                    result.append(entity.aliens.SuperAlien(player, result, (
                    (area_start + 1 + ((entity_size + 4) * a), -(entity_size + 4) * w)), alien[1]))
        except:
            result.extend(default_wave(player, result, area_start, entity_size, aliens_in_wave, w))
    return result