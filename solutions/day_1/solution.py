from typing import List, Callable, Tuple, Optional
import itertools
import functools
import numpy as np


def find_two_matching(a: List[int], fun: Callable, required_result: float) -> Tuple:
    # pylint: disable=invalid-name
    results = fun(a, np.reshape(a, newshape=(-1, 1)))
    idx = np.where(results == required_result)[0]
    idx1 = idx[0]
    idx2 = idx[1]

    return a[idx1], a[idx2]


def find_n_matching(a: List[int], n: int, fun: Callable, required_result: float) -> Optional[Tuple[int, ...]]:
    # pylint: disable=invalid-name
    combinations = itertools.combinations(a, n)

    for c in combinations:
        result = fun(c)
        if result == required_result:
            return c

    return None


def get_part_a_answer(data: str) -> int:
    arr = [int(x) for x in data.split('\n')]
    pair = find_two_matching(arr, fun=np.add, required_result=2020)

    return pair[0] * pair[1]


def get_part_b_answer(data: str) -> int:
    arr = [int(x) for x in data.split('\n')]
    trio = find_n_matching(arr, n=3, fun=sum, required_result=2020)

    return functools.reduce(lambda x, y: x * y, trio)
