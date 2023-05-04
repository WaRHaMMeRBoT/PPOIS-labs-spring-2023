import sys

import manage
from help import commands_help

def main():
    args = sys.argv
    if args[1] == 'gui':
        from gui.app import App
        App().run()
    elif args[1] == '--help':
        print(f'Справка:\n{commands_help}')
    elif args[1] == 'cli':
        garden_manage: manage.ManageGarden = manage.ManageGarden()
        garden_manage.command_hadler(args)
        

if __name__ == '__main__':
    main()
