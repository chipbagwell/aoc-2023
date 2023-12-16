from aocd import get_data
from collections import deque
import cmath
from pprint import PrettyPrinter

data = get_data(day=16, year=2023).splitlines()

data2 = [".|...\\....",
"|.-.\\.....",
".....|-...",
"........|.",
"..........",
".........\\",
"..../.\\\\..",
".-.-/..|..",
".|....-|.\\",
"..//.|...."]

# directions are based on the direction the ray is trying to move through the space
# 'L' - the ray is coming from the right, moving to the left
# 'R' - the ray is coming from the left, moving to the right
# 'U' - the ray is coming from down, moving up
# 'D' - the ray is coming from up, moving own.
#
# The starting direction for the puzzle is defined as 'R'

# tuples are (complex(y, x), direction)
def step(loc):
    d = data
    c = loc[0]
    y = int(loc[0].real)
    x = int(loc[0].imag)
    match loc[1]:
        case 'L':
            match d[y][x]:
                case '.' | '-':
                    return [(c + complex(0,-1),'L')]
                case '|':
                    return [(c + complex(-1,0),'U'),(c + complex(1,0),'D')]
                case '\\':
                    return [(c + complex(-1,0),'U')]
                case '/':
                    return [(c + complex(1,0),'D')]
        case 'R':
            match d[y][x]:
                case '.' | '-':
                    return [(c + complex(0,1),'R')]
                case '|':
                    return [(c + complex(-1,0),'U'),(c + complex(1,0),'D')]
                case '\\':
                    return [(c + complex(1,0),'D')]
                case '/':
                    return [(c + complex(-1,0),'U')]
        case 'U':
            match d[y][x]:
                case '.' | '|':
                    return [(c + complex(-1,0),'U')]
                case '-':
                    return [(c + complex(0,1),'R'),(c + complex(0,-1),'L')]
                case '\\':
                    return [(c + complex(0,-1),'L')]
                case '/':
                    return [(c + complex(0,1),'R')]
        case 'D':
            match d[y][x]:
                case '.' | '|':
                    return [(c + complex(1,0),'D')]
                case '-':
                    return [(c + complex(0,1),'R'),(c + complex(0,-1),'L')]
                case '\\':
                    return [(c + complex(0,1),'R')]
                case '/':
                    return [(c + complex(0,-1),'L')]

def do_work(inits):
    shape = complex(110,110)
    vals = []
    for i in inits:
        visited = dict()
        choices = deque()
        choices.append(i)
        visited[i] = True
        while choices:
            c = choices.pop()
            for next in step(c):
                if next not in visited.keys():
                    if 0 <= next[0].real < shape.real and 0 <= next[0].imag < shape.imag:
                        choices.append(next)
                        visited[next] = True
        vals.append(len(set([v[0] for v in visited.keys()])))
    return max(vals)
            
def part_1():
    inits = [(complex(0,0),'R')]
    return do_work(inits)
    

def part_2():
    shape = complex(110,110)
    # preseed the first location as the first choice to explore
    inits = [(complex(0,x),'D') for x in range(int(shape.imag))]
    inits += [(complex(y,0),'R') for y in range(int(shape.real))]
    inits += [(complex(y,int(shape.imag)-1),'L') for y in range(int(shape.real))]
    inits += [(complex(int(shape.real)-1,x),'U') for x in range(int(shape.imag))]
    
    return do_work(inits)
    
print(f"Part 1: {part_1()}, Part 2: {part_2()}")
