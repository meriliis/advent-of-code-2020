from typing import List, Tuple, Generator, Iterator
import math
from functools import reduce


def get_schedule(data: str) -> Tuple[int, List[int]]:
    arrival_time, bus_numbers = data.split('\n')
    arrival_time = int(arrival_time)
    bus_numbers = bus_numbers.split(',')

    return arrival_time, bus_numbers


def get_part_a_answer(data: str) -> int:
    arrival_time, bus_numbers_str = get_schedule(data)
    bus_numbers = [int(bus_number) for bus_number in bus_numbers_str if bus_number != 'x']
    next_departures = [math.ceil(arrival_time / bus) * bus for bus in bus_numbers]
    waiting_times = [departure - arrival_time for departure in next_departures]
    min_waiting_time = min(waiting_times)
    earliest_bus = bus_numbers[waiting_times.index(min_waiting_time)]

    return min_waiting_time * earliest_bus


def get_part_b_answer(data: str) -> int:
    _, bus_numbers_str = get_schedule(data)
    bus_numbers = [1 if bus_number == 'x' else int(bus_number) for bus_number in bus_numbers_str]

    def lcm(a, b):
        return abs(a * b) // math.gcd(a, b)

    step = 1
    ts = 0
    for offset, bus_number in enumerate(bus_numbers):
        while (ts + offset) % bus_number != 0:
            ts += step

        step = reduce(lambda x, y: lcm(x, y), bus_numbers[:(offset + 1)])

        if offset == len(bus_numbers) - 1:
            return ts


# Initial solution for part B that would've taken forever
# -------------------------------------------------------
# def get_part_b_answer(data: str) -> int:
#     _, bus_numbers_str = get_schedule(data)
#    bus_numbers = [1 if bus_number == 'x' else int(bus_number) for bus_number in bus_numbers_str]

#     def positive_numbers():
#         n = 0
#         while True:
#             yield n
#             n += 1
#
#     def keep_valid(timestamps: Generator[int, None, None], bus: Tuple[int, int]) -> Iterator[int]:
#         i, bus_number = bus
#         return filter(lambda ts: (ts + i) % bus_number == 0, timestamps)
#
#     candidate_timestamps = positive_numbers()
#     for i, bus_number in enumerate(bus_numbers):
#         if bus_number == 1:
#             continue
#         candidate_timestamps = keep_valid(candidate_timestamps, (i, bus_number))
#
#     return next(candidate_timestamps)
