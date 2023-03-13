from another_operations import Another_operations
from constants import Constants
from sets_and_operations import Sets_and_operations
import argparse


class Read_a_Line:

    @staticmethod
    def validate_line(raw_line):
        if raw_line.count('(') != raw_line.count(')') or raw_line.count('{') != raw_line.count('}'):
            raise ValueError('Invalid expression: The number of brackets is not the same')

    @staticmethod
    def read_raw_line(raw_line: str):
        raw_line = raw_line.replace(' ', '')
        try:
            Read_a_Line.validate_line(raw_line)

            if raw_line.find('size') != -1 or raw_line.find('psp') != -1 or raw_line.find('[') != -1:
                print(Another_operations().read_the_line_with_another_operatios(raw_line))

            elif not raw_line.islower() and (raw_line[0].isalpha() or raw_line[0] == '{' or raw_line[0] == '('):
                Constants().read_line(raw_line)

            elif raw_line[0] == '(' or raw_line[0] == '{':
                Sets_and_operations.check(raw_line)

            else:
                raise ValueError('Invalid expression')
        except Exception as e:
            if str(e) == 'list index out of range':
                print('Unknown error! The expression is incorrect!')
            else:
                print(e)


parser = argparse.ArgumentParser()
parser.add_argument('--set', type=str, help='combinations of sets')
args = parser.parse_args()
Read_a_Line.read_raw_line(args.set)

# Read_a_line.read_raw_line('A = {a, b}')
