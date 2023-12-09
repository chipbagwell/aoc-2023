from aocd import get_data
from collections import deque
from functools import reduce

data = get_data(day=9, year=2023).splitlines()


def part_1():
    num = [list(map(int, d.split())) for d in data]
    end_vals = []
    begin_vals = []
    for n in num:
        d = deque()
        d.appendleft(n)
        while not all(d[0][0] == i for i in d[0]):
            d.appendleft([d[0][i + 1] - d[0][i] for i in range(len(d[0]) - 1)])
        end_vals.append(sum([r[-1] for r in d]))
        begin_vals.append(reduce(lambda x, y: y - x, [r[0] for r in d]))
    return sum(end_vals), sum(begin_vals)


print(f"Part 1 and Part 2: {part_1()}")
