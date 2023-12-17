from aocd import get_data
from aoc_utils import pivot_2d_y_to_x
from collections import Counter
import copy
import sys

from pprint import PrettyPrinter

data = get_data(day=13, year=2023).splitlines()
data2 = [
    "#.##..##.",
    "..#.##.#.",
    "##......#",
    "##......#",
    "..#.##.#.",
    "..##..##.",
    "#.#.##.#.",
    "",
    "#...##..#",
    "#....#..#",
    "..##..###",
    "#####.##.",
    "#####.##.",
    "..##..###",
    "#....#..#",
]


def gen_boards(d):
    last_index = 0
    indices = [i for i, x in enumerate(d) if x == ""]
    for i in indices:
        yield d[last_index:i]
        last_index = i + 1
    yield d[last_index:]

def find_reflection_index(b):
    line = 0
    len_diff = sys.maxsize
    for i in range(0,len(b)-1):
        x = ''.join(b[i::-1])
        y = ''.join(b[i+1:])
        a = len(x)-len(y)
        c = len(y)-len(x)
        if x.find(y) == 0:
            if len_diff > a:
                line = i
                len_diff = a
        if y.find(x) == 0:
            if len_diff > c:
                line = i
                len_diff = c
    return line if len_diff != sys.maxsize else -1

def find_reflection_index2(b):
    line = []
    len_diff = sys.maxsize
    for i in range(0,len(b)-1):
        x = ''.join(b[i::-1])
        y = ''.join(b[i+1:])
        a = len(x)-len(y)
        c = len(y)-len(x)
        if x.find(y) == 0 or y.find(x) == 0:
            line.append(i)
    return line

def part_1():
    sum = 0
    for b in gen_boards(data):
        line = find_reflection_index(b)
        if line == -1:
            line = find_reflection_index(pivot_2d_y_to_x(b))
            sum += (line+1)
        else:
            sum += 100*(line+1)
    return sum
    


def part_2():
    pp = PrettyPrinter()
    sum = 0
    vals = dict()
    for i,b in enumerate(gen_boards(data)):
        line = find_reflection_index(b)
        if line == -1:
            line = find_reflection_index(pivot_2d_y_to_x(b))+1
        else:
            line = (line + 1) * 100
        vals[i] = line
    print(vals)
    print("start second part")

    for i,b in enumerate(gen_boards(data)):
        print(f"processing {i}")
        y_max = len(b)
        x_max = len(b[0])
        coords = [(y,x) for y in range(y_max) for x in range(x_max)]
        for c in coords:
            b_prime = copy.deepcopy(b)
            new_c = '.' if b_prime[c[0]][c[1]] == '#' else '#'
            b_prime[c[0]] = b_prime[c[0]][:c[1]] + new_c + b_prime[c[0]][c[1]+1:]
            # check for vertical reflection
            line = find_reflection_index2(b_prime)
            line = [l for l in line if (l+1) * 100 != vals[i]]
            if not line:
                # no vertical reflection, check for horizontal
                line = find_reflection_index2(pivot_2d_y_to_x(b_prime))
                line = [l for l in line if l+1 != vals[i]]
                if line:
                    # found horizontal and a different row
                    print(i, c, "col: ", line)
                    if(len(line) != 1):
                        print("found multiple reflections")
                    sum += (line[0]+1)
                    break
            elif line * 100 != vals[i]:
                # found vertical and a different row
                print(i, c, "row: ", line)
                if(len(line) != 1):
                    print("found multiple reflections")
                sum += 100*(line[0]+1)
                break
    return sum



print(f"Part 1: {part_1()}, Part 2: {part_2()}")
"""
pp = PrettyPrinter()
for i,b in enumerate(gen_boards(data)):
    print(f"board {i} normal")
    pp.pprint(b)
    print(f"board {i} transpose")
    pp.pprint(pivot_2d_y_to_x(b))
"""