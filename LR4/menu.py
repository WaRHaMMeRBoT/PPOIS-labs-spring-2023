from model import*
from view import*
from controller import*
import sys
import click
from click_shell import shell


@click.option(
    '--use-save',
    default=True,
    help="Set this parameter as 'True' to upload previous session, otherwise 'False'."
)
@click.option(
    '--gui',
    default=True,
    help="Set this parameter as 'True' to run GUI, set 'False to run CLI."
)
@shell(prompt='>> ', intro='Launching cli application...')
def main(use_save, gui):
    global garden
    garden = Model()

    if use_save:
        garden.get_data_from_file()

    if gui:
        model = Model()
        controller = Controller(model)
        Garden(model, controller).run()
        sys.exit()


@main.command(help='To the next day.', name='next_day')
def next_day():
    click.echo(garden.next_day())
    garden.set_data_in_file()


@main.command(help='Show information about garden.', name='show')
def show():
    click.echo(garden.show())
    garden.set_data_in_file()


@main.command(help='Add garden bed.', name='add_bed')
def add_bed():
    click.echo(garden.add_garden_bed())
    garden.set_data_in_file()


@main.command(help='Plant a tree.', name='plant_tree')
@click.argument('name', type=str)
def plant_tree(name):
    click.echo(garden.plant_tree(name))
    garden.set_data_in_file()


@main.command(help='Plant a cultivated plant.', name='plant_cult')
@click.argument('name')
@click.argument('bed', type=int)
def plant_cult(name, bed):
    click.echo(garden.plant_cultivated_plant(name, bed-1))
    garden.set_data_in_file()


@main.command(help='Weed a garden bed.', name='weed')
@click.argument('bed', type=int)
def weeding(bed):
    click.echo(garden.weeding(bed-1))
    garden.set_data_in_file()


@main.command(help='Water a garden bed.', name='water')
@click.argument('bed', type=int)
def watering(bed):
    click.echo(garden.watering(bed-1))
    garden.set_data_in_file()


@main.command(help='Fertilize a plant.', name='fertilize')
@click.argument('bed', type=int)
def fertilizing(bed):
    click.echo(garden.fertilize(bed-1))
    garden.set_data_in_file()


@main.command(help='Kill pests on a plant.', name='kill_pest')
@click.argument('type_name')
@click.argument('bed', type=int)
def kill_pest(type_name, bed):
    click.echo(garden.kill_pest(type_name, bed-1))
    garden.set_data_in_file()


@main.command(help='Take harvest from a plant.', name='harvest')
@click.argument('type_name')
@click.argument('bed', type=int)
def harvesting(type_name, bed):
    click.echo(garden.harvesting(type_name, bed-1))
    garden.set_data_in_file()


@main.command(help='Treat a plant.', name='treat')
@click.argument('type_name')
@click.argument('bed', type=int)
def treatment(type_name, bed):
    click.echo(garden.treatment(type_name, bed-1))
    garden.set_data_in_file()


if __name__ == '__main__':
    main()
