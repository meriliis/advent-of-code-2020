from typing import List, Dict, Tuple
import numpy as np
from collections import Counter


def get_adapters(data: str) -> List:
    return [int(x) for x in data.split('\n')]


def get_part_a_answer(data: str) -> int:
    adapters = get_adapters(data)

    charging_outlet = 0
    device_adapter_diff = 3
    adapters = [charging_outlet] + adapters + [max(adapters) + device_adapter_diff]

    diffs = np.diff(sorted(adapters))
    diffs_count = Counter(diffs)

    return diffs_count[1] * diffs_count[3]


def get_part_b_answer(data: str) -> int:
    adapters = get_adapters(data)

    charging_outlet = 0
    device_adapter_diff = 3
    adapters = [charging_outlet] + adapters + [max(adapters) + device_adapter_diff]

    max_diff = 3

    cache = {}

    def count_arrangements(remaining_adapters: List[int]) -> int:
        if len(remaining_adapters) == 1:
            return 1

        current_adapter = remaining_adapters[0]
        next_adapters = remaining_adapters[1:]
        next_arrangements_counts = []

        for i, potential_next_adapter in enumerate(next_adapters[:max_diff]):
            if potential_next_adapter - current_adapter <= max_diff:
                if potential_next_adapter in cache:
                    next_arrangement_count = cache[potential_next_adapter]
                else:
                    next_arrangement_count = count_arrangements(next_adapters[i:])
                    cache[potential_next_adapter] = next_arrangement_count

                next_arrangements_counts.append(next_arrangement_count)

        return sum(next_arrangements_counts)

    return count_arrangements(sorted(adapters))
