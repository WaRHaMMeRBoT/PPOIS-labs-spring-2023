import argparse
import random

from tabulate import tabulate

from LR1.garden.garden import load, init
from LR1.garden.plants import whatThePlant, whatTheSeed


def args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-s', '--square', nargs='+')
    parser.add_argument('--init', action='store_const', const=True)
    parser.add_argument('--view', action='store_const', const=True)
    parser.add_argument('--add', nargs='*')
    parser.add_argument('--remove', nargs='*')
    parser.add_argument('--weather', nargs='*')
    parser.add_argument('--warp', nargs='+')
    parser.add_argument('--add_seed', nargs='*')
    arguments = parser.parse_args()

    if arguments.init and arguments.square:
        init(int(arguments.square[0]), int(arguments.square[1]))
    else:
        if arguments.init:
            init(random.randint(1, 100), random.randint(1, 100))
    if arguments.view:
        garden = load()
        print(tabulate(garden.print()))
    if arguments.add:
        garden = load()
        plant = whatThePlant(arguments.add[0])
        garden.addEntity(plant, int(arguments.add[1]), int(arguments.add[2]))
        garden.garbageCollector()
        garden.warp(1)
        garden.save()
    if arguments.add_seed:
        garden = load()
        seed = whatTheSeed(arguments.add_seed[0])
        garden.addEntity(seed, int(arguments.add_seed[1]), int(arguments.add_seed[2]))
        garden.garbageCollector()
        garden.warp(1)
        garden.save()
    if arguments.remove:
        garden = load()
        garden.removeEntity(int(arguments.add[0]), int(arguments.add[1]))
        garden.garbageCollector()
        garden.warp(1)
        garden.save()
    if arguments.weather:
        garden = load()
        garden.weather.type = arguments.weather[0]
        garden.weather.time = int(arguments.weather[1])
        garden.garbageCollector()
        garden.warp(1)
        garden.save()
    if arguments.warp:
        garden = load()
        garden.warp(int(arguments.warp[0]))
        garden.garbageCollector()
        garden.save()


def start():
    args()


if __name__ == '__main__':
    start()
