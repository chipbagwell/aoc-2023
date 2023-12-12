from aocd import get_data
from aoc_utils import manhatten_distance, pivot_2d_y_to_x
from itertools import combinations

data = get_data(day=11, year=2023).splitlines()
data2 = ["...#......",
".......#..",
"#.........",
"..........",
"......#...",
".#........",
".........#",
"..........",
".......#..",
"#...#....."]

def part_1():
    t = [[d,d] if d.count('.') == len(d) else [d] for d in data]
    t = [a for d in t for a in d]
    t = pivot_2d_y_to_x(t)
    t = [[d,d] if d.count('.') == len(d) else [d] for d in t]
    t = [a for d in t for a in d]
    t = pivot_2d_y_to_x(t)
    
    g_pairs = list(combinations([(y,x) for y,d in enumerate(t) for x,c in enumerate(d) if c == '#'],2))
    dist = [manhatten_distance(g[0],g[1]) for g in g_pairs]

    return sum(dist)

def part_2(count):
    t = [[d]*count if d.count('.') == len(d) else [d] for d in data]
    t = [a for d in t for a in d]
    t = pivot_2d_y_to_x(t)
    t = [[d]*count if d.count('.') == len(d) else [d] for d in t]
    t = [a for d in t for a in d]
    t = pivot_2d_y_to_x(t)
    
    g_pairs = list(combinations([(y,x) for y,d in enumerate(t) for x,c in enumerate(d) if c == '#'],2))
    dist = [manhatten_distance(g[0],g[1]) for g in g_pairs]

    return sum(dist)
    

#for i in range(1,101):
#  print(f"count = {i} Part 2: {part_2(i)} calc: {7849428 + (i*857979)}")
print(f"part1: {part_1()}, part2: {7849428 + (1000000*857979)}")
