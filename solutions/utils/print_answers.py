from typing import Optional
import importlib
from aocd import get_data

from .timing import timeit


def print_answers(day: int, year: int, part: Optional[str]) -> None:
    def print_part_answers(data: str, module: str, part: str) -> None:
        part_fun = getattr(module, f'get_part_{part}_answer', None)
        if part_fun:
            answer, time = timeit(part_fun)(data)
            print(f'Part {part} answer: {answer}\n'
                  f'⏱️  {time:.3f} ms\n')
        else:
            print(f'Part {part} is not solved yet... ⏳️')

    data = get_data(day=day, year=year)

    print(f'-- 📅 {year} day {day} --')

    module = importlib.import_module(f'solutions.day_{day}.solution')

    if part is not None:
        print_part_answers(data, module, part)

    else:
        print_part_answers(data, module, 'a')
        print_part_answers(data, module, 'b')
