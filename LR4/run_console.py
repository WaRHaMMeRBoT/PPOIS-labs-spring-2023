from wild_forest import Game
import sys
import os


class ConsoleHandler:
    def __init__(self, height=35, width=35):
        self.game = Game(height, width)
        self.command_dict = dict()
        self.info_dict = dict()
        self.is_running = True

        def game_exit():
            self.is_running = False

        self.add_command(['--exit'], 'breaks the game loop', game_exit)
        self.add_command(['--save'], 'save simulation in file: --save [filename]', self.game.save)
        self.add_command(['--load'], 'loads saved simulation, format: --load [filename]', self.game.load)
        self.add_command(['--help', '--info'], 'prints all available commands', self.print_info)
        self.add_command(['--next', '-n', 'n'], 'renders next iteration', self.game.next)
        self.add_command(['--add', '-a'], 'spawns creature(s) by identifier in random position, format: --add [identifier] [count]', self.game.add_entity)

    def print_info(self):
        for key, value in self.info_dict.items():
            print(key, '\t -- ', value)

    def add_command(self, command_list, info, _lambda):
        for command in command_list:
            self.command_dict[command] = _lambda
            self.info_dict[command] = info

    def handle(self, command):
        argv = command.split()
        argc = len(argv)
        if argv[0] not in self.command_dict.keys():
            print('Invalid option, type --help for more info.')
        else:
            os.system('clear')
            if argc == 3:
                self.command_dict[argv[0]](argv[1], argv[2])
            elif argc == 2:
                self.command_dict[argv[0]](argv[1])
            else:
                self.command_dict[argv[0]]()

            self.game.render()


if __name__ == '__main__':

    if len(sys.argv) == 3:
        h, w = int(sys.argv[1]), int(sys.argv[2])
        game = ConsoleHandler(h, w)
    else:
        game = ConsoleHandler()

    os.system('clear')
    game.game.render()

    while game.is_running:
        user_input = input()
        game.handle(user_input)

    os.system('clear')