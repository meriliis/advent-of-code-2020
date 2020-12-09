import sys
from datetime import datetime

from solutions.utils.print_answers import print_answers

from dotenv import load_dotenv
load_dotenv()

if __name__ == '__main__':
    if len(sys.argv) > 1:
        print_answers(day=int(sys.argv[1]), year=2020)
    else:
        current_time = datetime.now()
        for time in [datetime(2020, 12, i, 7) for i in range(1, 32)]:
            if current_time >= time:
                print_answers(day=time.day, year=2020)
