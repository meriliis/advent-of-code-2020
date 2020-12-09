from typing import List, Dict, Set
import re


def get_passports(data: str) -> List[Dict]:
    passports_data = [passport.replace('\n', ' ').split(' ') for passport in data.split('\n\n')]
    passports = [dict([field.split(':') for field in passport]) for passport in passports_data]

    return passports


def get_part_a_answer(data: str) -> int:
    def is_valid_passport(passport: Dict, required_fields: Set[str]) -> bool:
        if required_fields - set(passport.keys()):
            return False

        return True

    passports = get_passports(data)
    required_fields = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}
    valid_passports = [is_valid_passport(passport, required_fields=required_fields) for passport in passports]

    return sum(valid_passports)


def get_part_b_answer(data: str) -> int:
    def is_valid_passport(passport: Dict, valid_patterns: Dict[str, str]) -> bool:
        for field, pattern in valid_patterns.items():
            value = passport.get(field, '')
            if not re.match(pattern, value):
                return False

        return True

    passports = get_passports(data)

    valid_patterns = {
        'byr': r'^(19[2-9]\d|200[0-2])$',
        'iyr': r'^(201\d|2020)$',
        'eyr': r'^(202\d|2030)$',
        'hgt': r'^(1[5-8]\dcm|19[0-3]cm|59in|6[0-9]in|7[0-6]in)$',
        'hcl': r'^\#[0-9a-f]{6}$',
        'ecl': r'^(amb|blu|brn|gry|grn|hzl|oth)$',
        'pid': r'^[0-9]{9}$'
    }

    valid_passports = [is_valid_passport(passport, valid_patterns=valid_patterns) for passport in passports]

    return sum(valid_passports)
