from typing import List, Tuple


def get_instructions(data: str) -> List[Tuple[str, int]]:
    return [(row[0], int(row[1:])) for row in data.split('\n')]


def get_part_a_answer(data: str) -> int:
    def handle_instruction(instruction: Tuple[str, int],
                           current_status: Tuple[Tuple[int, int], str]) -> Tuple[Tuple[int, int], str]:
        action, value = instruction
        (x, y), direction = current_status

        if action == 'N':
            return (x, y + value), direction
        elif action == 'S':
            return (x, y - value), direction
        elif action == 'E':
            return (x + value, y), direction
        elif action == 'W':
            return (x - value, y), direction
        elif action == 'R':
            new_direction_index = int(directions.index(direction) + value / 90) % 4
            return (x, y), directions[new_direction_index]
        elif action == 'L':
            return handle_instruction(('R', 360 - value % 360), current_status)
        elif action == 'F':
            return handle_instruction((direction, value), current_status)

    directions = 'NESW'
    instructions = get_instructions(data)
    status = ((0, 0), 'E')

    for i in instructions:
        status = handle_instruction(i, status)

    final_location = status[0]
    distance_from_start = abs(final_location[0]) + abs(final_location[1])

    return distance_from_start


def get_part_b_answer(data: str) -> int:
    def move(direction: Tuple[int, int], location: Tuple[int, int], value):
        x, y = location
        return x + value * direction[0], y + value * direction[1]

    def turn_right(waypoint: Tuple[int, int], n: int) -> Tuple[int, int]:
        wp_x, wp_y = waypoint
        for _ in range(n):
            wp_x, wp_y = wp_y, -wp_x

        return wp_x, wp_y

    def handle_instruction(instruction: Tuple[str, int],
                           current_location: Tuple[int, int],
                           current_waypoint: Tuple[int, int]) -> Tuple[Tuple[int, int], Tuple[int, int]]:
        action, value = instruction
        x, y = current_location
        wp_x, wp_y = current_waypoint

        if action in 'NESW':
            wp_x, wp_y = move(directions[action], current_waypoint, value)
        elif action == 'R':
            n_turns = int(value / 90) % 4
            wp_x, wp_y = turn_right((wp_x, wp_y), n_turns)
        elif action == 'L':
            n_turns = 4 - int(value / 90) % 4
            wp_x, wp_y = turn_right((wp_x, wp_y), n_turns)
        elif action == 'F':
            x, y = move(current_waypoint, current_location, value)

        return (x, y), (wp_x, wp_y)

    instructions = get_instructions(data)
    directions = {
        'N': (0, 1),
        'E': (1, 0),
        'S': (0, -1),
        'W': (-1, 0)
    }
    location = (0, 0)
    waypoint = (10, 1)

    for i in instructions:
        location, waypoint = handle_instruction(i, location, waypoint)

    distance_from_start = abs(location[0]) + abs(location[1])

    return distance_from_start
