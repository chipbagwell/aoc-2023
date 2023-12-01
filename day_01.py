from aocd import get_data, submit
from aoc_utils import find_all

data = get_data(day=1, year=2023).splitlines()

DIGITS = "0123456789"
DIGIT_MAP = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}


def sum_digits_part1(l):
    digits = [c for c in l if c in DIGITS]
    return int(digits[0] + digits[-1])


def sum_digits_part2(l):
    text_digits = [
        (i, v) for k, v in DIGIT_MAP.items() for i in list(find_all(l, k, overlap=True))
    ]
    num_digits = [
        (i, v) for _, v in DIGIT_MAP.items() for i in list(find_all(l, v, overlap=True))
    ]
    digits = sorted(text_digits + num_digits, key=lambda x: x[0])
    return int(digits[0][1] + digits[-1][1])


def part_1():
    return sum([sum_digits_part1(l) for l in data])


def part_2():
    return sum([sum_digits_part2(l) for l in data])


print(f"Part 1: {part_1()}, Part 2: {part_2()}")
