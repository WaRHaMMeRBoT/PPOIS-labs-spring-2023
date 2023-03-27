from classes import Garden, Commander
import sys


def main():
    garden = Garden()
    commander = Commander(garden)
    if len(sys.argv) > 1:
        commander.start(sys.argv[1:])


if __name__ == "__main__":
        main()







