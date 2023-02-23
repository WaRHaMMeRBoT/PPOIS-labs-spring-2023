import os

import manage
from help import commands_help


def main():
    os.system('clear')
    print('Для начала симуляции введите "начать".\nДля вывода списка по командам введите "справка".\nДля выхода введите "выход".')

    command: str = input('Команда: ')

    while command:
        if command == 'справка':
            print(f'Справка:\n{commands_help}')
        elif command == 'начать':
            print('Симуляция началась!')
            garden_manage: manage.ManageGarden = manage.ManageGarden()
            garden_manage.command_hadler()
            break
        elif command == 'выход':
            break
        else:
            print(f'{command} не найдена, повторите снова: ')
        command = input('Команда: ').lower()


if __name__ == '__main__':
    main()
