from typing import Dict, List, Set


def get_rules_map(data: str) -> Dict[str, Dict[str, int]]:
    rules_map = dict()
    lines = data.split('.\n')
    for line in lines:
        color, contents = line.split(' bags contain ')
        contents_list = list(map(lambda x: x.rsplit(' ', 1)[0], contents.split(', ')))
        if contents_list[0] == 'no other':
            contents_dict = dict()
        else:
            contents_dict = {content_str.split(' ', 1)[1]: int(content_str.split(' ', 1)[0])
                             for content_str in contents_list}

        rules_map[color] = contents_dict

    return rules_map


def get_reversed_rules_map(data: str) -> Dict[str, Set[str]]:
    rules_map = dict()
    lines = data.split('.\n')
    for line in lines:
        color, contents = line.split(' bags contain ')
        contents_list = map(lambda x: x.rsplit(' ', 1)[0].split(' ', 1)[1], contents.split(', '))
        for content_color in contents_list:
            if content_color not in rules_map:
                rules_map[content_color] = {color}
            else:
                rules_map[content_color].add(color)

    return rules_map


def get_part_a_answer(data: str) -> int:
    def parse_tree(tree: Dict[str, Set[str]], nodes: Set[str], seen: Set[str]):
        if not set.difference(nodes, seen):
            return seen

        seen.update(nodes)
        next_nodes = set()
        for node in nodes:
            next_nodes.update(tree.get(node, set()))

        return parse_tree(tree, next_nodes, seen)

    reversed_rules_map = get_reversed_rules_map(data)
    traversed_nodes = parse_tree(reversed_rules_map, {'shiny gold'}, set())
    return len(traversed_nodes) - 1


def get_part_b_answer(data: str) -> int:
    def get_number_of_bags_inside(rules_map: Dict[str, Dict[str, int]], bag: str) -> int:
        inner_bags = rules_map[bag]
        if inner_bags == dict():
            return 0
        else:
            return sum(
                [bag_count + bag_count * get_number_of_bags_inside(rules_map, inner_bag)
                 for inner_bag, bag_count in inner_bags.items()])

    rules_map = get_rules_map(data)
    return get_number_of_bags_inside(rules_map, 'shiny gold')
