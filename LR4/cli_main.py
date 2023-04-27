
from argparse import ArgumentParser
from src.simulation import Simulation



def main() -> None:
    parser = ArgumentParser(prog='laba4', usage="%(prog)s [options]")
    parser.add_argument(
        "--init",
        type=int,
        help="How many plants simulation need to have",
        default=-1,
    )
    parser.add_argument(
        '--run',
        choices=['r', 'd', 'w', 'f', 'e', 'i'],
    )
    args = parser.parse_args()
    if args.init != -1:
        Simulation.init(args.init)
    if args.run:
        Simulation.run(args.run)


if __name__ == "__main__":
    main()