from wild_life import Game
import sys
import os


class ConsoleHandler:
    def __init__(self):
        self.game = Game()
        self.command_dict = dict()
        self.info_dict = dict()
        self.is_running = True

        def game_exit():
            self.is_running = False

        self.add_command(['--exit'], 'breaks the game loop', game_exit)
        self.add_command(['--help'], 'prints all available commands', self.print_info)
        self.add_command(['--save'], 'save simulation in file: --save [filename]', self.game.save)
        self.add_command(['--load'], 'loads saved simulation, format: --load [filename]', self.game.load)
        self.add_command(['-n', '--next'], 'renders next iteration', self.game.next)
        self.add_command(['-a', '--add'], 'spawns creature(s) by identifier in random position, format: --add [identifier] [count]', self.game.add_entity)

    def print_info(self):
        for key, value in self.info_dict.items():
            print(key, '\t -- ', value)

    def add_command(self, _command_list, info, _lambda):
        for command in _command_list:
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

    arg_combinations = []
    command_list = []
    config = {'height': 50, 'width': 50}

    handler = ConsoleHandler()

    current_arg_list = []
    current_command = None
    print(handler.command_dict.keys())
    for i, argument in enumerate(sys.argv):
        if argument in handler.command_dict.keys():

            if current_command is None:
                current_arg_list = []
            else:
                arg_combinations.append((current_command, current_arg_list))
                current_arg_list = []

            current_command = argument

        else:
            current_arg_list.append(argument)

        if i == len(sys.argv) - 1 and current_command is not None:
            arg_combinations.append((current_command, current_arg_list))

    print(sys.argv)
    print(arg_combinations)

    for comb in arg_combinations:
        if comb[0] in ['-h', '--height']:
            arg_list = comb[1]
            config['height'] = arg_list[0]
        elif comb[0] in ['-w', '--width']:
            arg_list = comb[1]
            config['width'] = arg_list[0]
        elif comb[0] in ['-a', '--add']:
            arg_list = comb[1]
            command_list.append(('add', [arg_list[0], arg_list[1]]))

    print(command_list)

    for comb in command_list:
        if comb[0] == 'add':
            arg_list = comb[1]
            handler.game.add_entity(arg_list[0], int(arg_list[1]))

    os.system('clear')
    handler.game.render()

    while handler.is_running:
        user_input = input()
        handler.handle(user_input)

    os.system('clear')
