from argparse import ArgumentParser

from src import *


def main():
    parser = ArgumentParser(prog='Lab_1', usage='%(prog)s [options]')
    parser.add_argument(
        '--play',
        help='Show game iteration',
        action='store_true'
    )
    parser.add_argument(
        '--create',
        help="Create new simulation field",
        action='store_true'
    )
    parser.add_argument(
        '--add',
        help="Create new simulation's entity instance",
    )
    args = parser.parse_args()

    if args.create:
        try:
            print("Введите размеры поля")
            n = int(input())
            game = GameBoard(n)
            game()
            FileUtils.save_in_json(game.to_dict(), "./state.json")
        except Exception as exc:
            print(f"Внутренняя ошибка: {exc}")

    if args.add and args.add == "w":
        print("Введите координты расположение волка")
        try:
            x, y = map(int, input().split())
            data = FileUtils.read_from_json("./state.json")
            game = State.get_game_board(data)
            game[x - 1][y - 1].put_entity(Wolf())
            game()
            FileUtils.save_in_json(game.to_dict(), "./state.json")
        except Exception as exc:
            print(f"Внутренняя ошибка: {exc}")

    if args.add and args.add == "f":
        try:
            print("Введите координты расположение лисы")
            x, y = map(int, input().split())
            data = FileUtils.read_from_json("./state.json")
            game = State.get_game_board(data)
            game[x - 1][y - 1].put_entity(Fox())
            game()
            FileUtils.save_in_json(game.to_dict(), "./state.json")
        except Exception as exc:
            print(f"Внутренняя ошибка: {exc}")

    if args.add and args.add == "b":
        try:
            print("Введите координты расположение медведя")
            x, y = map(int, input().split())
            data = FileUtils.read_from_json("./state.json")
            game = State.get_game_board(data)
            game[x - 1][y - 1].put_entity(Bear())
            game()
            FileUtils.save_in_json(game.to_dict(), "./state.json")
        except Exception as exc:
            print(f"Внутренняя ошибка: {exc}")

    if args.add and args.add == "r":
        try:
            print("Введите координты расположение кролика")
            x, y = map(int, input().split())
            data = FileUtils.read_from_json("./state.json")
            game = State.get_game_board(data)
            game[x - 1][y - 1].put_entity(Rabbit())
            game()
            FileUtils.save_in_json(game.to_dict(), "./state.json")
        except Exception as exc:
            print(f"Внутренняя ошибка: {exc}")

    if args.add and args.add == "d":
        try:
            print("Введите координты расположение лося")
            x, y = map(int, input().split())
            data = FileUtils.read_from_json("./state.json")
            game = State.get_game_board(data)
            game[x - 1][y - 1].put_entity(Deer())
            game()
            FileUtils.save_in_json(game.to_dict(), "./state.json")
        except Exception as exc:
            print(f"Внутренняя ошибка: {exc}")

    if args.add and args.add == "p":
        try:
            print("Введите координты расположение растения")
            x, y = map(int, input().split())
            data = FileUtils.read_from_json("./state.json")
            game = State.get_game_board(data)
            game[x - 1][y - 1].put_entity(Plant())
            game()
            FileUtils.save_in_json(game.to_dict(), "./state.json")
        except Exception as exc:
            print(f"Внутренняя ошибка: {exc}")

    if args.play:
        while True:
            try:
                print("continue - сделать итерацию", "end - завершить итерации", sep="\n")
                temp = input()
                data = FileUtils.read_from_json("./state.json")
                game = State.get_game_board(data)
                if temp == 'continue':
                    game.iteration()
                    FileUtils.save_in_json(game.to_dict(), "./state.json")
                    game()
                if temp == 'end':
                    break
            except Exception as exc:
                print(f"Внутренняя ошибка: {exc}")
                break


if __name__ == "__main__":
    main()
