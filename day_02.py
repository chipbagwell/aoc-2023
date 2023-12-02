from aocd import get_data, submit
from aoc_utils import find_all
from functools import reduce

CUBE_MAX = {"red": 12, "green": 13, "blue": 14}
too_big = lambda g: int(g[0]) > CUBE_MAX[g[1]]


def part_1():
    sum = 0
    for game in data:
        game_id, tries = game.split(":")
        id = int(game_id.split()[1])
        cubes = [a.strip().split() for a in tries.replace(";", ",").split(",")]
        sum += id if not any([too_big(c) for c in cubes]) else 0
    return sum


def part_2():
    sum = 0
    for game in data:
        _, tries = game.split(":")
        m = {"red": 0, "green": 0, "blue": 0}
        cubes = [a.strip().split() for a in tries.replace(";", ",").split(",")]
        for c in cubes:
            m[c[1]] = max(m[c[1]], int(c[0]))
        sum += reduce((lambda x, y: x * y), m.values())
    return sum


data = get_data(day=2, year=2023).splitlines()
print(f"Part 1: {part_1()}, Part 2: {part_2()}")
