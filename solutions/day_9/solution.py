from typing import List, Optional


def get_series(data: str) -> List:
    return [int(x) for x in data.split('\n')]


def get_part_a_answer(data: str) -> Optional[int]:
    series = get_series(data)
    preamble_length = 25

    for i, x in enumerate(series[preamble_length:]):
        preamble = set(series[i:i + preamble_length])
        has_sum = sum([(x - y) in preamble for y in preamble]) > 0
        if not has_sum:
            return x

    return None


def get_part_b_answer(data: str) -> int:
    series = get_series(data)
    invalid_number = get_part_a_answer(data)

    for i in range(len(series)):
        contiguous_numbers = []
        contiguous_sum = 0

        j = 0
        while contiguous_sum < invalid_number:
            x = series[i + j]
            contiguous_numbers.append(x)
            contiguous_sum += x
            j += 1

        if contiguous_sum == invalid_number:
            return min(contiguous_numbers) + max(contiguous_numbers)
