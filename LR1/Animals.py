import random
import LABAp1
import click


@click.group()
def cli():
    pass


@cli.command()
def simulation():
    snakes = LABAp1.Animal('snake', 0, 3, 0)
    apples = LABAp1.Plant('apple', 0, 0)
    lions = LABAp1.Animal('lion',0,2,3)
    list1 = [1, 2, 3, 4]
    list2 = [1, 2, 3, 4]
    LABAp1.boardgame()
    while LABAp1.count != 2:
        k = random.choice(list1)
        m = random.choice(list2)
        if k == 1:
            snakes.moveup()
            list1 = [1,3,4]

        elif k == 2:
            snakes.movedown()
            list1 = [2,3,4]

        elif k == 3:
            snakes.moveright()
            list1 = [1,2,3]

        else:
            snakes.moveleft()
            list1 = [1,2,4]

        if m == 1:
            lions.moveup()
            list2 = [1, 3, 4]
            if LABAp1.check == 1:
                snakes.death()

        elif m == 2:
            lions.movedown()
            list2 = [2, 3, 4]
            if LABAp1.check == 1:
                snakes.death()

        elif m == 3:
            lions.moveright()
            list2 = [1, 2, 3]
            if LABAp1.check == 1:
                snakes.death()

        else:
            lions.moveleft()
            list2 = [1, 2, 4]
            if LABAp1.check == 1:
                snakes.death()

        LABAp1.boardgame()
        print('-----------------------')



if __name__ == '__main__':
    cli()

