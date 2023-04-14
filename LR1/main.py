import field
import argparse

parser = argparse.ArgumentParser(prog='game of life')

parser.add_argument('filename')
parser.add_argument('-c', '--count', type=int, required=True, help='count of steps to produce')
parser.add_argument('-v', '--verbose', action='store_true', help='print field on each step')
parser.add_argument('-o', '--output', action='store', help='output file')

args = parser.parse_args()

f = field.field(args.filename, args.output)
for _ in range(args.count):
    f.process()
    if args.verbose:
        print(f, end='\n\n')
f.dump()