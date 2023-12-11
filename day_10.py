from aocd import get_data
from aoc_utils import pivot_2d_y_to_x
import cmath
from collections import Counter, deque
from pprint import PrettyPrinter
pp = PrettyPrinter()

"""
| is a vertical pipe connecting north and south.
- is a horizontal pipe connecting east and west.
L is a 90-degree bend connecting north and east.
J is a 90-degree bend connecting north and west.
7 is a 90-degree bend connecting south and west.
F is a 90-degree bend connecting south and east.
. is ground; there is no pipe in this tile.
S is the starting position of the animal;
 there is a pipe on this tile,
 but your sketch doesn't show what shape the pipe has.
"""
data = get_data(day=10, year=2023).splitlines()
data2 = ["-L|F7",
         "7S-7|",
         "L|7||",
         "-L-J|",
         "L|-JF"]

UP = complex(1, 0)
DOWN = complex(-1, 0)
LEFT = complex(0, -1)
RIGHT = complex(0, 1)

def check_left_right(s):
    count = 0
    found_f = False
    found_l = False
    found_j = False
    found_7 = False
    for c in s:
        match c:
            case ' ' | '-':
                continue
            case '|'| 'S':
                count += 1
                continue
            case 'F':
                found_f = True
            case '7':
                found_7 = True
            case 'L':
                found_l = True
            case 'J': 
                found_j = True
        if found_f and found_7:
            count += 2
            found_f = False
            found_7 = False
            continue
        if found_l and found_j:
            count += 2
            found_l = False
            found_j = False
            continue
        if found_f and found_j:
            count += 1
            found_f = False
            found_j = False
            continue
        if found_l and found_7:
            count += 1
            found_l = False
            found_7 = False
            continue
    return count

def check_up_down(s):
    count = 0
    found_f = False
    found_l = False
    found_j = False
    found_7 = False
    for c in s:
        match c:
            case ' ' | '|' | 'S':
                continue
            case '-':
                count += 1
                continue
            case 'F':
                found_f = True
            case '7':
                found_7 = True
            case 'L':
                found_l = True
            case 'J': 
                found_j = True
        if found_f and found_l:
            count += 2
            found_f = False
            found_l = False
            continue
        if found_7 and found_j:
            count += 2
            found_7 = False
            found_j = False
            continue
        if found_f and found_j:
            count += 1
            found_f = False
            found_j = False
            continue
        if found_l and found_7:
            count += 1
            found_l = False
            found_7 = False
            continue
    return count

        
def find_s(data):
    for i, d in enumerate(data):
        if "S" in d:
            return (i, d.index("S"))


def step(d, prev, curr):
    retval = None
    p = complex(prev[0], prev[1])
    c = complex(curr[0], curr[1])
    match d[curr[0]][curr[1]]:
        case "|":
            retval = (curr[0] + 1, curr[1]) if c - p == UP else (curr[0] - 1, curr[1])
        case "-":
            retval = (curr[0], curr[1] + 1) if c - p == RIGHT else (curr[0], curr[1] - 1)
        case "L":
            retval = (curr[0], curr[1] + 1) if c - p == UP else (curr[0] - 1, curr[1])
        case "J":
            retval = (curr[0], curr[1] - 1) if c - p == UP else (curr[0] - 1, curr[1])
        case "7":
            retval = (curr[0], curr[1] - 1) if c - p == DOWN else (curr[0] + 1, curr[1])
        case "F":
            retval = (curr[0], curr[1] + 1) if c - p == DOWN else (curr[0] + 1, curr[1])
    return retval


def part_1():
    s_loc = find_s(data)
    prev = s_loc
    next = s_loc[0]-1,s_loc[1] # found manually
    count = 1
    while next != s_loc:
        next2 = step(data, prev, next)
        prev = next
        next = next2
        count += 1

    return count/2


def part_2():
    contour = deque()
    src = data
    
    s_loc = find_s(src)
    contour.append(s_loc)
    prev = s_loc
    next = s_loc[0]-1,s_loc[1] # found manually
    contour.append(next)
    count = 0
    while next != s_loc:
        next2 = step(src, prev, next)
        contour.append(next2)
        prev = next
        next = next2

    new_src = [list(' '*len(src[0])) for s in src ]
    for c in contour:
        new_src[c[0]][c[1]] = src[c[0]][c[1]]
    src = [''.join(l) for l in new_src]

    pivot_src = pivot_2d_y_to_x(src)
    
    for y in range(len(src)):
        for x in range(len(src[0])):
            if (y,x) not in contour:
              a1 = check_left_right(src[y][x:])
              a2 = check_left_right(src[y][:x])
              a3 = check_up_down(pivot_src[x][:y])
              a4 = check_up_down(pivot_src[x][y:])
              if True in (a == 0 for a in [a1,a2,a3,a4]):
                  continue
              if a1%2 or a2%2 or a3%2 or a4%2:
                  count += 1
    return count


print(f"Part 1 {part_1()}, Part 2: {part_2()}")
