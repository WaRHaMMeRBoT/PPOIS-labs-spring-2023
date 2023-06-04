from src.map.game_map import Map
from src.util.coordinates2d import Coord2d


class Game:
    def __init__(self, height=35, width=35):
        self.game_map = Map(height, width)

    def test(self):
        print('tesst')

    def next(self):

        self.game_map.reset_turn_sequence()

        for entity in self.game_map.entity_list:
            entity.action(self.game_map)

        self.game_map.update()

    def render(self):
        self.game_map.print_map()

    def add_entity(self, idf, count=1):
        count = int(count)
        [self.game_map.add_entity(idf) for _ in range(count)]

    def save(self, filename):
        f = open(filename, 'w')
        for entity in self.game_map.entity_list:
            out = entity.get_idf() + ' ' + str(entity.get_coords().x) + ' ' + str(entity.get_coords().y) + '\n'
            f.write(out)
        f.close()

    def load(self, filename):
        self.game_map.clear_state()
        f = open(filename, 'r')
        entities = f.readlines()
        for entity in entities:
            params = entity.split()
            x, y = int(params[1]), int(params[2])
            self.game_map.add_entity(params[0], Coord2d(x, y))
        self.game_map.update()
        f.close()


if __name__ == '__main__':
    game = Game(35, 50)


    game.render()

    a = '''
    radius = 3
    rlist = [(x, radius) for x in [*range(-radius, radius + 1)]] + \
            [(radius, x) for x in [*range(-radius, radius + 1)]] + \
            [(x, -radius) for x in [*range(-radius, radius + 1)]] + \
            [(-radius, x) for x in [*range(-radius, radius + 1)]]

    print(rlist)
    '''
