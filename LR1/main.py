import random
import Randomazer
import Railway
import Train
import click

@click.group()
def cli():
    pass

@click.command()
@click.argument('train-speed')
@click.argument('pass-cars')
@click.argument('freight-cars')
def start(train_speed, pass_cars, freight_cars):
    random.seed()
    train = Train.Train(int(train_speed), int(pass_cars), int(freight_cars))
    randomazerr = Randomazer.Randomazer()
    railway = Railway.Railway(randomazerr.generateRandomStation(), train)
    railway.start_train()

cli.add_command(start)

if __name__ == '__main__':
   cli()



