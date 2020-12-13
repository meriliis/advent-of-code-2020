import argparse
from datetime import datetime

from solutions.utils.print_answers import print_answers

from dotenv import load_dotenv
load_dotenv()

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('day', type=int)
    parser.add_argument('-p', '--part', default=None, type=str)
    args = parser.parse_args()

    if args.day:
        print_answers(day=args.day, year=2020, part=args.part)
    else:
        current_time = datetime.now()
        for time in [datetime(2020, 12, i, 7) for i in range(1, 32)]:
            if current_time >= time:
                print_answers(day=time.day, year=2020)
