import argparse

from src import cache

parser = argparse.ArgumentParser()
parser.add_argument("detect", nargs='*', default=None, )

# parser.add_argument('')
args = parser.parse_args()
args_len = len(args.detect)

if args_len < 1:
    print('''
    Usage:
    1.
    detect [int]timestamp , detect if given time stamp is a car
    usage:
    python cars.py detect 1538076003
    2.
    compare [int]timestamp1, [int]timestamp2
    ''')


commend, others = args.detect

print(commend, others)