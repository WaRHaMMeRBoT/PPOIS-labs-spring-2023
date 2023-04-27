import shelve
import game


class Save:
    def __init__(self):
        self.file = shelve.open('data')

    def save(self):
        self.file['name'] = game.mr_player.name

    def add(self, name, value):
        self.file[name] = value

    def get(self, name):
        try:
            return self.file[name]
        except:
            return 0

    def __del__(self):
        self.file.close()
