from dotenv import load_dotenv
load_dotenv()

from typing import List, Callable, Tuple, Optional
import itertools
import functools
import numpy as np

from aocd import get_data, submit


def find_two_matching(a: List[int], fun: Callable, required_result: float) -> Tuple:
    results = fun(a, np.reshape(a, newshape=(-1, 1)))
    idx = np.where(results == required_result)[0]
    idx1 = idx[0]
    idx2 = idx[1]

    return a[idx1], a[idx2]


def find_n_matching(a: List[int], n: int, fun: Callable, required_result: float) -> Optional[Tuple[int, ...]]:
    combinations = itertools.combinations(a, n)

    for c in combinations:
        result = fun(c)
        if result == required_result:
            return c

    return None


if __name__ == '__main__':
    day, year = 1, 2020

    data = get_data(day=day, year=year)
    arr = [int(x) for x in data.split('\n')]

    pair = find_two_matching(arr, np.add, 2020)
    part_one_answer = pair[0] * pair[1]
    submit(part_one_answer, part='a', day=day, year=year)

    trio = find_n_matching(arr, n=3, fun=sum, required_result=2020)
    part_two_answer = functools.reduce(lambda x, y: x * y, trio)
    submit(part_two_answer, part='b', day=day, year=year)
