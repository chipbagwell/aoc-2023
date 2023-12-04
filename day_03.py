from aocd import get_data

data = get_data(day=3, year=2023).splitlines()

NUM_COLUMNS = len(data[0])
NUM_ROWS = len(data)
SYMBOLS = list(set([c for c in "".join(data) if c not in "0123456789."]))


def find_numbers():
    numbers = []
    for row, l in enumerate(data):
        num = 0
        coords = []
        for col, c in enumerate(l):
            if c.isnumeric():
                num = (num * 10) + int(c)
                coords.append((row, col))
            else:
                if coords:
                    numbers.append((num, coords))
                    num = 0
                    coords = []
        if coords:
            numbers.append((num, coords))
            num = 0
            coords = []
    return numbers


def make_neighbors(x):
    return [
        (r, c)
        for r in range(max(0, x[0] - 1), min(NUM_ROWS, x[0] + 2))
        for c in range(max(0, x[1] - 1), min(NUM_COLUMNS, x[1] + 2))
        if (r, c) != x
    ]


def part_1():
    return sum(
        n[0]
        for n in find_numbers()
        if any([data[a[0]][a[1]] in SYMBOLS for d in n[1] for a in make_neighbors(d)])
    )


def find_gear_loc():
    return [
        ((row, col), make_neighbors((row, col)))
        for row, l in enumerate(data)
        for col, c in enumerate(l)
        if c == "*"
    ]


def part_2():
    sum = 0
    for g in find_gear_loc():
        x = [n[0] for n in find_numbers() if set(n[1]).intersection(g[1])]
        sum += x[0] * x[1] if len(x) == 2 else 0
    return sum


print(f"Part 1: {part_1()}, Part 2: {part_2()}")
