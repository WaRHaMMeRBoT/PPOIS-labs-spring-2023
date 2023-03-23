from .items import Item
from .function import Func
from .constans import Flag
from .utils import FileUtils

class Simulation:
    def __int__(self):
        self.n = 0
        self.items = []

    @staticmethod
    def run(arg: str):
        s = Simulation.from_dict(FileUtils.read_from_json('./state.json'))
        s.dispatch(arg)
        FileUtils.save_in_json(s.to_dict(), './state.json')
        s.get_info()


    @staticmethod
    def from_dict(d: dict) -> 'Simulation':
        s = Simulation()
        s.n = d['n']
        s.items = [Item.from_dict(v) for v in d['items']]
        return s

    def dispatch(self, arg: str) -> None:
        if arg == 'r':
            self.after_rain()
        elif arg == 'd':
            self.on_drought()
        elif arg == 'w':
            self.after_watering()
        elif arg == 'f':
            self.after_fertiliser()
        elif arg == 'e':
            self.after_weeding()
        elif arg == 'i':
            self.after_disease()

    def to_dict(self) -> dict:
        d = dict()
        d['n'] = self.n
        d['items'] = [item.to_dict() for item in self.items]
        return d

    @staticmethod
    def init(n: int) -> None:
        s = Simulation()
        s.n = n
        i = Item()
        s.items = [Item() for _ in range(s.n)]
        FileUtils.save_in_json(s.to_dict(), './state.json')

    def on_drought(self) -> None:
        for item in self.items:
            flag = Func.drought(item)
            if flag == Flag.NEED_TO_CLONE:
                self.items += [Item(), Item()]
                self.n += 2
            elif flag == Flag.NEED_TO_DELETE:
                del item

    def after_rain(self) -> None:
        for item in self.items:
            flag = Func.rain(item)
            if flag == Flag.NEED_TO_CLONE:
                self.items += [Item(), Item()]
                self.n += 2
            elif flag == Flag.NEED_TO_DELETE:
                del item


    def after_watering(self) -> None:
        for item in self.items:
            flag = Func.watering(item)
            if flag == Flag.NEED_TO_CLONE:
                self.items += [Item(), Item()]
                self.n += 2
            elif flag == Flag.NEED_TO_DELETE:
                del item

    def after_fertiliser(self) -> None:
        for item in self.items:
            flag = Func.fertiliser(item)
            if flag == Flag.NEED_TO_CLONE:
                self.items += [Item(), Item()]
                self.n += 2
            elif flag == Flag.NEED_TO_DELETE:
                del item

    def after_weeding(self) -> None:
        for item in self.items:
            flag = Func.weeding(item)
            if flag == Flag.NEED_TO_CLONE:
                self.items += [Item(), Item()]
                self.n += 2
            elif flag == Flag.NEED_TO_DELETE:
                del item

    def after_disease(self) -> None:
        for item in self.items:
            flag = Func.disease(item)
            if flag == Flag.NEED_TO_CLONE:
                self.items += [Item(), Item()]
                self.n += 2
            elif flag == Flag.NEED_TO_DELETE:
                del item

    def get_info(self) -> None:
        n = 1
        for item in self.items:
            print('plant', n, '{' , '\n',
                  'name: ', item.name, '\n',
                  'state: ', item.state, '\n',
                  'health: ', item.health, '\n',
                  '}', '\n'
                  )
            n += 1
