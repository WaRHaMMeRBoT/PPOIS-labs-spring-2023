 
from garden import*
import argparse


def args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--view', action='store_const', const=True)
    parser.add_argument('--add_plant', nargs='*')
    parser.add_argument('--remove', nargs='*')
    parser.add_argument('--weather', nargs='+')
    parser.add_argument('--fertilize', nargs='+')
    parser.add_argument('--water', nargs='+')
    parser.add_argument('--skip_time', nargs='+')
    parser.add_argument('--plant', nargs='*')
    parser.add_argument('--show', nargs='*')
    parser.add_argument('--enviroment', action='store_const', const=True)
    parser.add_argument('--show_need', nargs='*')
    parser.add_argument('--weed', action='store_const', const=True)
    arguments = parser.parse_args()
    
    if arguments.view:
        garden = loadFile()
        garden.view()
    if arguments.add_plant:
        garden = loadFile()
        garden.area[int(arguments.add_plant[0])][int(arguments.add_plant[1])] = garden.plantConstructorAccess(arguments.add_plant[2])
        garden.grow[int(arguments.add_plant[0])][int(arguments.add_plant[1])] = 10
        garden.save()
    if arguments.plant:
        garden = loadFile()
        garden.planting(int(arguments.plant[0]), int(arguments.plant[1]),int(arguments.plant[2]), int(arguments.plant[3]), arguments.plant[4] )
        garden.save()
    if arguments.show_need:
        garden = loadFile()
        garden.area[int(arguments.show_need[0])][int(arguments.show_need[1])].showNeed()
    if arguments.remove:
        garden = loadFile()
        garden.remove(int(arguments.remove[0]), int(arguments.remove[1]))
        garden.save()
    if arguments.weather:
        garden = loadFile()
        garden.weather.type = arguments.weather[0]
        garden.save()
    if arguments.water:
        garden = loadFile()
        garden.soil.watering(float(arguments.water[0]))
        garden.save()
    if arguments.fertilize:
        garden = loadFile()
        garden.soil.fertilizing(int(arguments.fertilize[0]))
        garden.save()
    if arguments.skip_time:
        garden = loadFile()
        garden.skipTime(int(arguments.skip_time[0]))
        garden.save()
    if arguments.show:
        garden = loadFile()
        garden.__str__(int(arguments.show[0]), int(arguments.show[1]))
        garden.save()
    if arguments.enviroment:
        garden = loadFile()
        garden.enviroment()
    if arguments.weed:
        garden = loadFile()
        garden.weeding()
        garden.save()


def start():
    args()


if __name__ == '__main__':
    start()