import argparse

from src import cache
from src.utils import detect_car_give_ts

parser = argparse.ArgumentParser()
parser.add_argument("args", nargs='*', default=None, )

# parser.add_argument('')
args = parser.parse_args()
args_len = len(args.args)

if args_len < 2:
    print('''
Usage:
1. detect [int]timestamp 
    - detect if given time stamp is a car
usage:
python cars.py detect 1538076003
2. compare [int]timestamp1, [int]timestamp2
    - check if two cars are the same
usage:
python cars.py compare 1538076003 1538079781
3. analyze [int]timestamp1, [int]timestamp2
    - produce report between two timestamps
usage:
python cars.py analyze 1538076003 1538079781
''')
    exit()


commend = args.args[0]
if commend.lower() == 'detect':
    ts = args.args[1]
    ts = int(ts)
    print(detect_car_give_ts(ts))
    pass
elif commend.lower() == 'compare':
    pass
elif commend.lower() == 'analyze':
    pass
else:
    print('unknown commend %s' % (commend))
    exit()

