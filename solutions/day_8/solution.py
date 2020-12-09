from typing import List, Tuple


def get_instructions(data: str) -> List[Tuple[str, int]]:
    lines = data.split('\n')
    instructions = [tuple(line.split(' ')) for line in lines]
    instructions = [(op, int(arg)) for op, arg in instructions]

    return instructions


def run_program(instructions: List[Tuple[str, int]]) -> Tuple[int, bool]:
    acc = 0
    seen_idx = set()
    terminates = False

    idx = 0
    while idx not in seen_idx:
        if idx >= len(instructions):
            terminates = True
            return acc, terminates

        seen_idx.add(idx)
        op, arg = instructions[idx]

        if op == 'nop':
            idx += 1
        elif op == 'acc':
            acc += arg
            idx += 1
        elif op == 'jmp':
            idx += arg

    return acc, terminates


def get_part_a_answer(data: str) -> int:
    instructions = get_instructions(data)
    acc, _ = run_program(instructions)

    return acc


def get_part_b_answer(data: str) -> int:
    def switch_instruction(instructions: List[Tuple[str, int]], idx: int) -> List[Tuple[str, int]]:
        op, arg = instructions[idx]
        if op == 'nop':
            instructions[idx] = ('jmp', arg)
        elif op == 'jmp':
            instructions[idx] = ('nop', arg)

        return instructions

    instructions = get_instructions(data)
    possible_programs = (switch_instruction(instructions.copy(), idx)
                         for idx in range(len(instructions)) if instructions[idx][0] in ['jmp', 'nop'])

    while True:
        program = next(possible_programs)
        acc, got_terminated_program = run_program(program)
        if got_terminated_program:
            return acc
