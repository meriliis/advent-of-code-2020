from typing import Tuple


def get_seat_location(boarding_pass: str) -> Tuple[int, int]:
    n_rows, n_cols = 128, 8
    row_spec, col_spec = boarding_pass[:7], boarding_pass[7:]

    rows, cols = range(n_rows), range(n_cols)
    while len(rows) > 1:
        midpoint = int(len(rows) / 2)
        rows = rows[:midpoint] if row_spec[0] == 'F' else rows[midpoint:]
        row_spec = row_spec[1:]

    while len(cols) > 1:
        midpoint = int(len(cols) / 2)
        cols = cols[:midpoint] if col_spec[0] == 'L' else cols[midpoint:]
        col_spec = col_spec[1:]

    return rows[0], cols[0]


def get_seat_id(location: Tuple[int, int]) -> int:
    row, col = location
    seat_id = row * 8 + col

    return seat_id


def get_part_a_answer(data: str) -> int:
    boarding_passes = data.split('\n')
    seat_ids = [get_seat_id(get_seat_location(boarding_pass)) for boarding_pass in boarding_passes]

    return max(seat_ids)


def get_part_b_answer(data: str) -> int:
    boarding_passes = data.split('\n')
    seat_ids = [get_seat_id(get_seat_location(boarding_pass)) for boarding_pass in boarding_passes]
    sum_of_seat_ids = sum(range(min(seat_ids), max(seat_ids) + 1))

    return sum_of_seat_ids - sum(seat_ids)
