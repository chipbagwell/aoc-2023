from aocd import get_data
from collections import Counter
from functools import reduce
from math import pow
from operator import add

data = get_data(day=4, year=2023).splitlines()


def gen_cards():
    return [
        len(c[1].intersection(c[0]))
        for c in [
            tuple(map(lambda x: set(x.split()), l.split(":")[1].split("|"))) for l in data
        ]
    ]


def part_1():
    return int(reduce(add, list(map(lambda x: pow(2, x - 1) if x else 0, gen_cards()))))


def part_2():
    count = Counter()
    for i, c in enumerate(gen_cards()):
        count.update([i])
        for n in range(count[i]):
            count.update(range(i + 1, i + c + 1))
    return count.total()


print(f"Part 1: {part_1()}, Part 2: {part_2()}")
