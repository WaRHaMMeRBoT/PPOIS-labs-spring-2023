import json


def read_from_file():
    with open("res.json") as f:
        data = f.read()
    return json.loads(data)


def write_to_file(data):
    with open("res.json", "w") as file:
        file.write(json.dumps(data))


class Rating:
    def __init__(self, table):
        self.r_table: int = table
        self.data: dict = read_from_file()

    def update(self, name, value):
        self.data[name] = value
        write_to_file(self.data)


