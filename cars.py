import argparse
from client_config import CACHE_DIR
from utils import detect_car_give_ts, is_match, analyze

parser = argparse.ArgumentParser()
parser.add_argument("args", nargs='*', default=None, )
parser.add_argument('-v', action="cache_dir", default=None,)
# parser.add_argument('')
args = parser.parse_args()
cache_dir = parser.cache_dir
args_len = len(args.args)
if cache_dir is not None:
    global CACHE_DIR
    CACHE_DIR = cache_dir

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

import json

commend = args.args[0]
if commend.lower() == 'detect':
    ts = args.args[1]
    ts = int(ts)
    ret = detect_car_give_ts(ts)
    # ret = json.loads(ret)
    print(ret['result'])
elif commend.lower() == 'compare':
    if len(args.args) < 3:
        print('need to pass at least 3 argument `python cars.py compare ts1 ts2`')
    ts1, ts2 = args.args[1], args.args[2]
    ret = is_match(ts1, ts2)
    print(ret)
elif commend.lower() == 'analyze':
    if len(args.args) < 3:
        print('need to pass at least 3 argument `python cars.py analyze ts1 ts2`')
    ts1, ts2 = int(args.args[1]), int(args.args[2])
    analyze(ts1, ts2)

else:
    print('unknown commend %s' % (commend))
    exit()

