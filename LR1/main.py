import logging
import time
import sys

from utility import IO

logging.basicConfig(level=logging.INFO)



if __name__ == '__main__':
    road = IO.create_railroad('test.txt')
    trains = IO.create_trains('test.txt', road)

    days = 0

    while True:

        logging.info('Days passed: {0}'.format(days))
        for train in trains:
            train.tick()
        road.tick()
        days += 1
        print('---------')
        if "--manual" in sys.argv[1:]:
            input()
        else:
            time.sleep(1)
