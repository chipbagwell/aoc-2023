from aocd import get_data
from collections import deque
from pprint import PrettyPrinter

data = get_data(day=18, year=2023).splitlines()

data2 = ["R 6 (#70c710)",
"D 5 (#0dc571)",
"L 2 (#5713f0)",
"D 2 (#d2c081)",
"R 2 (#59c680)",
"D 2 (#411b91)",
"L 5 (#8ceee2)",
"U 2 (#caa173)",
"L 1 (#1b58a2)",
"U 2 (#caa171)",
"R 2 (#7807d2)",
"U 3 (#a77fa3)",
"L 2 (#015232)",
"U 2 (#7a21e3)"]

data3 = ["R 2",
         "D 2",
         "L 2",
         "U 2"]

def segments(p):
    return zip(p, p[1:] + [p[0]])

def flood_fill(start, grid):
    d = deque()
    d.append(start)
    while d:
        p = d.pop()
        grid[p[0]][p[1]] = '#'
        if grid[p[0]][p[1]+1] == ' ':
            d.append((p[0],p[1]+1))
        if grid[p[0]][p[1]-1] == ' ':
            d.append((p[0],p[1]-1))
        if grid[p[0]+1][p[1]] == ' ':
            d.append((p[0]+1,p[1]))
        if grid[p[0]-1][p[1]] == ' ':
            d.append((p[0]-1,p[1]))
    return grid

def part_1():
    input = data
    x = 0
    y = 0
    points = [(y,x)]
    for d in input:
        tokens = d.split()
        match tokens[0]:
            case 'D':
                y += int(tokens[1])
            case 'U':
                y -= int(tokens[1])
            case 'L':
                x -= int(tokens[1])
            case 'R':
                x += int(tokens[1])
        points.append((y,x))
    points.pop()
    
    xs = [p[1] for p in points]
    min_x = min(xs)
    max_x = max(xs)
    ys = [p[0] for p in points]
    min_y = min(ys)
    max_y = max(ys)
    print(min_y, max_y, min_x, max_x)
    print(points)
    # move points into lower right quadrant
    p2 = [(p[0] + (abs(min_y)+1), p[1] + (abs(min_x) + 1)) for p in points]
    print(p2)
    max_x += abs(min_x) +3
    max_y += abs(min_y) +3
  
    s = list(segments(p2))
    grid = [[' ' for x in range(max_x)] for y in range(max_y)]
    print(grid)
    for l in s:
        l = sorted(l)
        for y in range(l[0][0],l[1][0]+1):
            for x in range(l[0][1],l[1][1]+1):
                grid[y][x] = '#'
    
    pp = PrettyPrinter()
    pp.pprint(grid)
    grid = flood_fill((8,194),grid)
    pp.pprint(grid)
    return sum([l.count('#') for l in grid])    
        

def part_2():
    pass

print(f"Part 1: {part_1()}, Part 2: {part_2()}")
