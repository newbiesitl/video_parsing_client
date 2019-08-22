import argparse

from src import cache

parser = argparse.ArgumentParser()
parser.add_argument("detect", help="detect car of a given time stamp",
                    type=int)


args = parser.parse_args()
ts = args.detect