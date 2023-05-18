import src.game as game
import json


def data_save():
    with open('data/data.json', 'w') as file:
        json.dump(
            {
                'rating': game.rating,
                'music': game.MUSIC,
                'sfx': game.SFX,
                'sound_volume': game.SOUND_VOLUME
            },
            file
        )


def data_read():
    try:
        with open('data/data.json', 'r') as f:
            data = f.read()
            json_data = json.loads(data)

            game.rating = json_data['rating']
            game.MUSIC = json_data['music']
            game.SFX = json_data['sfx']
            game.SOUND_VOLUME = json_data['sound_volume']
    except (FileExistsError, FileNotFoundError, json.decoder.JSONDecodeError):
        pass
