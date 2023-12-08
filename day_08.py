from aocd import get_data
from aoc_utils import lcm

data = get_data(day=8, year=2023).splitlines()

DIRECTION = {'L':0,'R':1}


def part_1():
    steps = [DIRECTION[c] for c in data[0]]
    nodes = dict([(a[0],(a[2][1:-1],a[3][0:-1]))for a in [d.split() for d in data[2:]]])
    count = 0
    pos = 'AAA'
    i = 0
    while pos != 'ZZZ':
      pos = nodes[pos][steps[i]]
      i = (i + 1)%len(steps)
      count += 1
    return count


def part_2():
    steps = [DIRECTION[c] for c in data[0]]
    nodes = dict([(a[0],(a[2][1:-1],a[3][0:-1]))for a in [d.split() for d in data[2:]]])
    pos = [n for n in nodes.keys() if n[2] == 'A']
    vals = []
    for p in pos:
      count = 0
      i = 0
      while p[2] != 'Z':
        p = nodes[p][steps[i]]
        i = (i + 1)%len(steps)
        count += 1
      vals.append(count)
    return lcm(vals)


print(f"Part 1: {part_1()}, Part 2: {part_2()}")
