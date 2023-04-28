from entity import *
from util import clamp, is_clamp
from copy import deepcopy
import yaml


class field:
    def __init__(self, fin, fout) -> None:
        game_state = yaml.safe_load(open(fin, 'r'))
        self.entities = game_state['entities']
        state = game_state['field']
        self.fout = fout

        self.height = state['height']
        self.width = state['width']
        self.state = [[[] for _ in range(self.width)]
                      for _ in range(self.height)]

        cells = state['cells']
        for row, cols in cells.items():
            for col, ents in cols.items():
                for ent in ents:
                    name = next(iter(ent))
                    info = [name] + ent[name]
                    template = game_state['entities'][name]

                    ent_obj = globals()[template['type']](
                        *info, **template)

                    if is_clamp(row, 0, self.height) and\
                       is_clamp(col, 0, self.width):
                        self.state[row][col].append(ent_obj)
                    else:
                        raise ValueError(f"incorrect cell index {row}, {col}")

    def __repr__(self) -> str:
        s = [[str(e) for e in row] for row in self.state]
        lens = [max(map(len, col)) for col in zip(*s)]
        fmt = '\t'.join('{{:{}}}'.format(x) for x in lens)
        table = [fmt.format(*row) for row in s]
        return '\n'.join(table)

    def dump(self):
        file = open(self.fout, 'w')
        data = {
            'entities': {},
            'field': {
                'width': self.width,
                'height': self.height,
                'cells': {}
            }
        }

        for i, row in enumerate(self.state):
            for j, cell in enumerate(row):
                for ent in cell:
                    data['field']['cells']\
                        .setdefault(i, {})\
                        .setdefault(j, [])\
                        .append({ent.name : ent.info()})

                    if ent.name in data['entities']:
                        continue
                    
                    data['entities'].setdefault(ent.name, ent.dump())
        yaml.safe_dump(data, file)

    def process(self):
        for i, row in enumerate(self.state):
            for j, cell in enumerate(row):
                for ent in cell:
                    ent.process()

        self.cleaning()
        self.moving()
        self.eating()
        self.reproduce()

    def reproduce(self):
        def random_sex(): return random() > 0.5
        for i, row in enumerate(self.state):
            for j, cell in enumerate(row):
                for ent in cell:
                    partners = list(filter(lambda x: ent.name == x.name, cell))
                    for i in partners:
                        if ent.is_love(i) and not i.is_dodge():
                            child = deepcopy(ent)
                            child.sex = random_sex()
                            child.health = child.max_health
                            cell.append(child)
                            break
                    else:
                        continue
                    break

    def moving(self):
        for i, row in enumerate(self.state):
            for j, cell in enumerate(row):
                for ent in cell:
                    new_coords = ent.move()
                    new_y = clamp(i + new_coords[0], 0, self.height-1)
                    new_x = clamp(j + new_coords[1], 0, self.width-1)
                    if new_y != i or new_x != j:
                        self.state[new_y][new_x].append(ent)
                        cell.remove(ent)

    def eating(self):
        for i, row in enumerate(self.state):
            for j, cell in enumerate(row):
                for ent in cell:
                    if len(cell) == 1:
                        break

                    for i in ent.eats:
                        food = list(filter(lambda x: i == x.name, cell))
                        if not len(food) or food[0].is_dodge():
                            continue

                        ent.health = ent.max_health
                        food[0].is_die = True
                        break

        self.cleaning()

    def cleaning(self):
        for i, row in enumerate(self.state):
            for j, cell in enumerate(row):
                for ent in cell:
                    if ent.is_die:
                        cell.remove(ent)
