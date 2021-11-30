from typing import Tuple, Callable
import numpy as np
import copy
from itertools import product


def get_seat_layout(data: str) -> np.array:
    return np.array([list(map(lambda seat: 0 if seat == 'L' else 1 if seat == '#' else np.nan, row))
                     for row in data.split('\n')])


def apply_rules(padded_layout: np.array, get_new_seat_value: Callable) -> np.array:
    new_layout = np.zeros_like(padded_layout)
    n_rows, n_cols = padded_layout.shape
    for i in range(1, n_rows - 1):
        for j in range(1, n_cols - 1):
            # print(get_new_seat_value(padded_layout, (i, j)))
            new_layout[i, j] = get_new_seat_value(padded_layout, (i, j))

    return new_layout


def get_part_a_answer(data: str) -> int:
    def get_new_seat_value(padded_layout: np.array, seat_location: Tuple[int, int]) -> np.array:
        is_occupied = padded_layout[seat_location]
        if np.isnan(is_occupied):
            return is_occupied

        i, j = seat_location
        local_layout = padded_layout[i - 1:i + 2, j - 1:j + 2]
        n_neighbors = np.nansum(local_layout) - is_occupied
        if is_occupied == 0 and n_neighbors == 0:
            return 1
        elif is_occupied == 1 and n_neighbors >= 4:
            return 0

        return is_occupied

    seat_layout = get_seat_layout(data)
    n_rows, n_cols = seat_layout.shape
    padded_layout = np.zeros((n_rows + 2, n_cols + 2))
    padded_layout[1:-1, 1:-1] = seat_layout

    current_layout = copy.deepcopy(padded_layout)
    while True:
        new_layout = apply_rules(current_layout, get_new_seat_value)
        if np.array_equal(new_layout, current_layout, equal_nan=True):
            return np.nansum(current_layout)

        current_layout = new_layout


def get_part_b_answer(data: str) -> int:
    def get_visible_seats(padded_layout: np.array, seat_location: Tuple[int, int]):
        x, y = seat_location
        n_rows, n_cols = padded_layout.shape
        visible_seats = 0
        directions = product([-1, 0, 1], repeat=2)
        for i, (d_x, d_y) in enumerate(directions):
            if (d_x, d_y) == (0, 0):
                continue

            step = 1
            while True:
                x1, y1 = x + step * d_x, y + step * d_y
                if x1 < 1 or x1 > n_cols - 1 or y1 < 1 or y1 > n_rows - 1:
                   break

                v = padded_layout[x1, y1]
                if not np.isnan(v):
                    visible_seats += v
                    break

                step += 1

        return visible_seats

    def get_new_seat_value(padded_layout: np.array, seat_location: Tuple[int, int]) -> np.array:
        is_occupied = padded_layout[seat_location]
        n_neighbors = get_visible_seats(padded_layout, seat_location)
        if is_occupied == 0 and n_neighbors == 0:
            return 1
        elif is_occupied == 1 and n_neighbors >= 5:
            return 0

        return is_occupied

    seat_layout = get_seat_layout(data)
    n_rows, n_cols = seat_layout.shape
    padded_layout = np.zeros((n_rows + 2, n_cols + 2))
    padded_layout[1:-1, 1:-1] = seat_layout

    current_layout = copy.deepcopy(padded_layout)
    while True:
        new_layout = apply_rules(current_layout, get_new_seat_value)
        if np.array_equal(new_layout, current_layout, equal_nan=True):
            return np.nansum(current_layout)

        current_layout = new_layout
