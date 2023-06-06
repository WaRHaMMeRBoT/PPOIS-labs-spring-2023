import json


def dump_json(data):
    with open('users.json', 'w+') as file:
        data_json = json.dumps(data, indent=3)
        file.write(data_json)
        file.close()


def dump_cache(data):
    with open('cache.json', 'w+') as file:
        data_json = json.dumps(data, indent=2)
        file.write(data_json)
        file.close()
