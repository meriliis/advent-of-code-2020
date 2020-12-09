from typing import Tuple
import collections


def extract_data(row: str) -> Tuple[str, Tuple[int, int, str]]:
    # pylint: disable=invalid-name
    policy, password = row.split(': ')
    min_max, c = policy.split(' ')
    min_c, max_c = min_max.split('-')

    return password, (int(min_c), int(max_c), c)


def get_part_a_answer(data: str) -> int:
    def verify_password(password: str, policy: Tuple[int, int, str]) -> bool:
        # pylint: disable=invalid-name
        min_c, max_c, c = policy
        character_counts = collections.Counter(password)
        is_valid = max_c >= character_counts.get(c, 0) >= min_c

        return is_valid

    passwords = [extract_data(row) for row in data.split('\n')]
    return sum([verify_password(password, policy) for password, policy in passwords])


def get_part_b_answer(data: str) -> int:
    def verify_password(password: str, policy: Tuple[int, int, str]) -> bool:
        # pylint: disable=invalid-name
        idx1, idx2, c = policy
        c1, c2 = password[idx1 - 1], password[idx2 - 1]
        is_valid = (c1 == c and c2 != c) or (c1 != c and c2 == c)

        return is_valid

    passwords = [extract_data(row) for row in data.split('\n')]
    return sum([verify_password(password, policy) for password, policy in passwords])
