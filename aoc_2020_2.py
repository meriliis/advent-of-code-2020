from dotenv import load_dotenv
load_dotenv()

from typing import Tuple
import collections

from aocd import get_data, submit


def extract_data(row: str) -> Tuple[str, Tuple[int, int, str]]:
    policy, password = row.split(': ')
    min_max, c = policy.split(' ')
    min_c, max_c = min_max.split('-')

    return password, (int(min_c), int(max_c), c)


def verify_password_part_a(password: str, policy: Tuple[int, int, str]) -> bool:
    min_c, max_c, c = policy
    character_counts = collections.Counter(password)
    is_valid = max_c >= character_counts.get(c, 0) >= min_c

    return is_valid


def verify_password_part_b(password: str, policy: Tuple[int, int, str]) -> bool:
    idx1, idx2, c = policy
    c1, c2 = password[idx1 - 1], password[idx2 - 1]
    is_valid = (c1 == c and c2 != c) or (c1 != c and c2 == c)

    return is_valid


if __name__ == '__main__':
    day, year = 2, 2020
    data = get_data(day=day, year=year)

    passwords = [extract_data(row) for row in data.split('\n')]

    is_valid_part_a = [verify_password_part_a(password, policy) for password, policy in passwords]
    part_a_answer = sum(is_valid_part_a)
    submit(part_a_answer, part='a', day=day, year=year)

    is_valid_part_b = [verify_password_part_b(password, policy) for password, policy in passwords]
    part_b_answer = sum(is_valid_part_b)
    submit(part_b_answer, part='b', day=day, year=year)

