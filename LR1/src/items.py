
class Item:

    def __init__(self, name='apple', state='seed', health=5):
        self.name = name
        self.state = state
        self.health = health

        # name: apple
        # state: seed, tree, fruit
        # health: 0 - dead, 5 - start, 20 - tree, 30 - tree with fruits

    def get_name(self):
        return self.name

    def get_state(self):
        return self.state

    def get_health(self):
        return self.health

    def to_dict(self) -> dict:
        d = dict()
        d['name'] = self.name
        d['state'] = self.state
        d['health'] = self.health
        return d

    @staticmethod
    def from_dict(d: dict) -> 'Item':
        i = Item()
        i.name = d['name']
        i.state = d['state']
        i.health = d['health']
        return i