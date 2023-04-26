import argparse
from services.base_controller import BaseController
from gameboard import *


class CLIController:
    def __init__(self):
        parser = argparse.ArgumentParser()
        parser.add_argument('--play', action='store_true')
        parser.add_argument('--size', nargs='+')
        parser.add_argument('--add', nargs='*')
        parser.add_argument('--view', action='store_true')
        parser.add_argument('--create', action='store_true')
        self.arguments = parser.parse_args()
        self.controller = BaseController()

        if self.arguments.create and self.arguments.size:
            self.controller.create_new_game_board(int(self.arguments.size[0]))

        if self.arguments.view:
            self.controller.view()

        if self.arguments.add and self.arguments.add[0] == 'w':
            self.controller.add(entity=Wolf(), x=int(self.arguments.add[1]), y=int(self.arguments.add[2]))
        if self.arguments.add and self.arguments.add[0] == 'f':
            self.controller.add(entity=Fox(), x=int(self.arguments.add[1]), y=int(self.arguments.add[2]))
        if self.arguments.add and self.arguments.add[0] == 'b':
            self.controller.add(entity=Bear(), x=int(self.arguments.add[1]), y=int(self.arguments.add[2]))
        if self.arguments.add and self.arguments.add[0] == 'r':
            self.controller.add(entity=Rabbit(), x=int(self.arguments.add[1]), y=int(self.arguments.add[2]))
        if self.arguments.add and self.arguments.add[0] == 'd':
            self.controller.add(entity=Deer(), x=int(self.arguments.add[1]), y=int(self.arguments.add[2]))
        if self.arguments.add and self.arguments.add[0] == 'p':
            self.controller.add(entity=Plant(), x=int(self.arguments.add[1]), y=int(self.arguments.add[2]))

        if self.arguments.play:
            self.controller.play()
