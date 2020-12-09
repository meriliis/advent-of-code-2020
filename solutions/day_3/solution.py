from typing import List, Tuple
from collections import Counter
from functools import reduce
import numpy as np


def traverse_map(hill_map: List[List[str]], slope: Tuple[int, int], start_coordinates: Tuple[int, int]) -> List[str]:
    hill_length, map_width = np.shape(hill_map)
    dx, dy = slope
    x, y = start_coordinates

    slope_map = []

    while y < hill_length - dy:
        y += dy
        x += dx
        if x >= map_width:
            x -= map_width

        slope_map.append(hill_map[y][x])

    return slope_map


def count_trees(slope_map: List[str]) -> int:
    return Counter(''.join(slope_map))['#']


def get_part_a_answer(data: str) -> int:
    hill_map = [list(row) for row in data.split('\n')]
    slope_map = traverse_map(hill_map, slope=(3, 1), start_coordinates=(0, 0))
    return count_trees(slope_map)


def get_part_b_answer(data: str) -> int:
    hill_map = [list(row) for row in data.split('\n')]
    slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    return reduce(lambda x, y: x * y, [count_trees(traverse_map(hill_map, slope, (0, 0))) for slope in slopes])
