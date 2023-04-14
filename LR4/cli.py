import argparse

import models.ocean as ocean
from controller.utils import add_instance, next

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="This is a program for life simulation"
    )
    parser.add_argument(
        "-s", "--skip", type=int, metavar="<steps>", help="Pass some simulation steps"
    )
    parser.add_argument(
        "--animal",
        choices=["shark", "parrotfish", "barracuda"],
        help="Create new animal",
    )
    parser.add_argument(
        "--plant", action="store_true", help="Create new plant"
    )  # nargs = 2, type = int, metavar = ('<lifespan>', '<energy_value>'), help = 'Create new plant')

    args = parser.parse_args()

    field = ocean.Ocean((20, 20))
    try:
        with open("./state.json", "r") as area:
            field = ocean.parse_json(area.read())
            area.close()
    except FileNotFoundError:
        pass

    if args.skip:
        next(field, args.skip)
    if args.animal:
        add_instance(field, args.animal)
    if args.plant:
        add_instance(field, "plant")

    text = ocean.convert_to_json(field)

    with open("./state.json", "w") as area:
        area.write(text)
        area.close()
