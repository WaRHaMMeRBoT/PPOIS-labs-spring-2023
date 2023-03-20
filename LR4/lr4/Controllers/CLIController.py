import argparse
import random

from lr4.Controllers.baseController import BaseController
from lr4.garden.model import create_dir


class CLIController:
    def __init__(self):

        parser = argparse.ArgumentParser()
        parser.add_argument('-s', '--square', nargs='+')
        parser.add_argument('--init', action='store_const', const=True)
        parser.add_argument('--view', action='store_const', const=True)
        parser.add_argument('--add', nargs='*')
        parser.add_argument('--remove', nargs='*')
        parser.add_argument('--weather', nargs='*')
        parser.add_argument('--warp', nargs='+')
        parser.add_argument('--add_seed', nargs='*')
        self.arguments = parser.parse_args()

        if self.arguments.init and self.arguments.square:
            create_dir(int(self.arguments.square[0]), int(self.arguments.square[1]))
        else:
            if self.arguments.init:
                create_dir(random.randint(1, 100), random.randint(1, 100))
        self.controller = BaseController()
        if self.arguments.view:
            self.controller.view()
        if self.arguments.add:
            self.controller.add(plant_name=self.arguments.add[0], x=int(self.arguments.add[1]),
                                y=int(self.arguments.add[2]))
        if self.arguments.add_seed:
            self.controller.add_seed(seed_name=self.arguments.add[0], x=int(self.arguments.add[1]),
                                     y=int(self.arguments.add[2]))
        if self.arguments.remove:
            self.controller.remove(int(self.arguments.remove[0]), int(self.arguments.remove[1]))
        if self.arguments.weather:
            self.controller.weather(type=self.arguments.weather[0], time=int(self.arguments.weather[1]))
        if self.arguments.warp:
            self.controller.warp(time=int(self.arguments.warp[0]))
