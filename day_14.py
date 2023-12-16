from aocd import get_data
from aoc_utils import pivot_2d_y_to_x
from pprint import PrettyPrinter

data = get_data(day=14, year=2023).splitlines()
data2 = ["O....#....",
"O.OO#....#",
".....##...",
"OO.#O....O",
".O.....O#.",
"O.#..O.#.#",
"..O..#O..O",
".......O..",
"#....###..",
"#OO..#...."]


def part_1():
    pdata = pivot_2d_y_to_x(data2)
    pdata =pivot_2d_y_to_x(['#'.join([''.join(sorted(list(s),reverse=True)) for s in d.split('#')]) for d in pdata])
    weight = sum([(i+1) * d.count('O') for i,d in enumerate(pdata[::-1])])
    return weight
    pass

def part_2():
    pp = PrettyPrinter()
    weight = 0
    pdata = data
    for i in range(1000):
        print(i, weight)
        # tilt north
        pdata = pivot_2d_y_to_x(pdata)
        pdata = pivot_2d_y_to_x(['#'.join([''.join(sorted(list(s),reverse=True)) for s in d.split('#')]) for d in pdata])

        # tilt west
        pdata = ['#'.join([''.join(sorted(list(s),reverse=True)) for s in d.split('#')]) for d in pdata]

        # tilt south
        pdata = pivot_2d_y_to_x(pdata)
        pdata = pivot_2d_y_to_x(['#'.join([''.join(sorted(list(s))) for s in d.split('#')]) for d in pdata])

        # tilt east
        pdata = ['#'.join([''.join(sorted(list(s))) for s in d.split('#')]) for d in pdata]
        pp.pprint(pdata)
        weight = sum([(i+1) * d.count('O') for i,d in enumerate(pdata[::-1])])
    return weight
    
print(f"Part 1: {part_1()}, Part 2: {part_2()}")
