from typing import List, Set


def get_answers_by_group(data: str) -> List[List[str]]:
    return [group.split('\n') for group in data.split('\n\n')]


def get_unique_answers_by_group(data: str) -> List[Set[str]]:
    answers_by_group = get_answers_by_group(data)
    unique_answers_by_group = [set(''.join(group)) for group in answers_by_group]

    return unique_answers_by_group


def get_all_yes_answers_by_group(data: str) -> List[Set[str]]:
    answers_by_group = get_answers_by_group(data)
    all_yes_answers_by_group = [set.intersection(*map(set, g)) for g in answers_by_group]

    return all_yes_answers_by_group


def get_part_a_answer(data: str) -> int:
    n_unique_answers_by_group = [len(answers) for answers in get_unique_answers_by_group(data)]
    return sum(n_unique_answers_by_group)


def get_part_b_answer(data: str) -> int:
    n_all_yes_answers_by_group = [len(answers) for answers in get_all_yes_answers_by_group(data)]
    return sum(n_all_yes_answers_by_group)
