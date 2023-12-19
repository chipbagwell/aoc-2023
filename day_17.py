from aocd import get_data
import networkx as nx
from pprint import PrettyPrinter

real_data = get_data(day=17, year=2023).splitlines()
data2 = [
    "2413432311323",
    "3215453535623",
    "3255245654254",
    "3446585845452",
    "4546657867536",
    "1438598798454",
    "4457876987766",
    "3637877979653",
    "4654967986887",
    "4564679986453",
    "1224686865563",
    "2546548887735",
    "4322674655533",
]
data3 = [
    "24114",
    "32111",
    "32571",
    "23432",
    "12321",
]

data = [list(map(int, list(d))) for d in real_data]
END_POS = (len(data) - 1, len(data[0]) - 1)
# directions are based on the direction the ray is trying to move through the space
# 'L' - the ray is coming from the right, moving to the left
# 'R' - the ray is coming from the left, moving to the right
# 'U' - the ray is coming from down, moving up
# 'D' - the ray is coming from up, moving down.
# 'N' - no direction, starting position has no direction
#
# The starting direction for the puzzle is defined as loc complex(0,0)
#
# tuple(0,loc: complex, 1,dir: char, 2,step_count: 3,int, sum: int, c4,oord_path: tuple of tuples)


def part_1():
    pp = PrettyPrinter()
    G = nx.DiGraph()
    for y in range(len(data)):
        for x in range(len(data[0])):
            if y == 0 and x == 0:
                G.add_edge((0, 0), (0, 1, 1, "Right"), weight=0)
                G.add_edge((0, 0), (1, 0, 1, "Down"), weight=0)
                continue

            if y > 0:  # D
                if y != END_POS[0]:
                    G.add_edge((y, x, 1, "Down"), (y + 1, x, 2, "Down"), weight=data[y][x])
                if x != 0:
                    G.add_edge((y, x, 1, "Down"), (y, x - 1, 1, "Left"), weight=data[y][x])
                if x != END_POS[1]:
                    G.add_edge((y, x, 1, "Down"), (y, x + 1, 1, "Right"), weight=data[y][x])
            if y > 1:
                if y != END_POS[0]:
                    G.add_edge((y, x, 2, "Down"), (y + 1, x, 3, "Down"), weight=data[y][x])
                if x != 0:
                    G.add_edge((y, x, 2, "Down"), (y, x - 1, 1, "Left"), weight=data[y][x])
                if x != END_POS[1]:
                    G.add_edge((y, x, 2, "Down"), (y, x + 1, 1, "Right"), weight=data[y][x])
            if y > 2:
                if x != 0:
                    G.add_edge((y, x, 3, "Down"), (y, x - 1, 1, "Left"), weight=data[y][x])
                if x != END_POS[1]:
                    G.add_edge((y, x, 3, "Down"), (y, x + 1, 1, "Right"), weight=data[y][x])

            if y < END_POS[0]:  # U
                if y != 0:
                    G.add_edge((y, x, 1, "Up"), (y - 1, x, 2, "Up"), weight=data[y][x])
                if x != 0:
                    G.add_edge((y, x, 1, "Up"), (y, x - 1, 1, "Left"), weight=data[y][x])
                if x != END_POS[1]:
                    G.add_edge((y, x, 1, "Up"), (y, x + 1, 1, "Right"), weight=data[y][x])
            if y < END_POS[0] - 1:
                if y != 0:
                    G.add_edge((y, x, 2, "Up"), (y - 1, x, 3, "Up"), weight=data[y][x])
                if x != 0:
                    G.add_edge((y, x, 2, "Up"), (y, x - 1, 1, "Left"), weight=data[y][x])
                if x != END_POS[1]:
                    G.add_edge((y, x, 2, "Up"), (y, x + 1, 1, "Right"), weight=data[y][x])
            if y < END_POS[0] - 2:
                if x != 0:
                    G.add_edge((y, x, 3, "Up"), (y, x - 1, 1, "Left"), weight=data[y][x])
                if x != END_POS[1]:
                    G.add_edge((y, x, 3, "Up"), (y, x + 1, 1, "Right"), weight=data[y][x])

            if x > 0:  # R
                if x != END_POS[1]:
                    G.add_edge(
                        (y, x, 1, "Right"), (y, x + 1, 2, "Right"), weight=data[y][x]
                    )
                if y != END_POS[0]:
                    G.add_edge((y, x, 1, "Right"), (y + 1, x, 1, "Down"), weight=data[y][x])
                if y != 0:
                    G.add_edge((y, x, 1, "Right"), (y - 1, x, 1, "Up"), weight=data[y][x])
            if x > 1:
                if x != END_POS[1]:
                    G.add_edge(
                        (y, x, 2, "Right"), (y, x + 1, 3, "Right"), weight=data[y][x]
                    )
                if y != END_POS[0]:
                    G.add_edge((y, x, 2, "Right"), (y + 1, x, 1, "Down"), weight=data[y][x])
                if y != 0:
                    G.add_edge((y, x, 2, "Right"), (y - 1, x, 1, "Up"), weight=data[y][x])
            if x > 2:
                if y != END_POS[0]:
                    G.add_edge((y, x, 3, "Right"), (y + 1, x, 1, "Down"), weight=data[y][x])
                if y != 0:
                    G.add_edge((y, x, 3, "Right"), (y - 1, x, 1, "Up"), weight=data[y][x])

            if x < END_POS[1]:  # L
                if x != 0:
                    G.add_edge((y, x, 1, "Left"), (y, x - 1, 2, "Left"), weight=data[y][x])
                if y != END_POS[0]:
                    G.add_edge((y, x, 1, "Left"), (y + 1, x, 1, "Down"), weight=data[y][x])
                if y != 0:
                    G.add_edge((y, x, 1, "Left"), (y - 1, x, 1, "Up"), weight=data[y][x])
            if x < END_POS[1] - 1:
                if x != 0:
                    G.add_edge((y, x, 2, "Left"), (y, x - 1, 3, "Left"), weight=data[y][x])
                if y != END_POS[0]:
                    G.add_edge((y, x, 2, "Left"), (y + 1, x, 1, "Down"), weight=data[y][x])
                if y != 0:
                    G.add_edge((y, x, 2, "Left"), (y - 1, x, 1, "Up"), weight=data[y][x])

            if x < END_POS[1] - 2:
                if y != END_POS[0]:
                    G.add_edge((y, x, 3, "Left"), (y + 1, x, 1, "Down"), weight=data[y][x])
                if y != 0:
                    G.add_edge((y, x, 3, "Left"), (y - 1, x, 1, "Up"), weight=data[y][x])
    # Graph edges and nodes have been populated
    ends = [
        k
        for k, v in G.nodes.items()
        if k[0] == END_POS[0] and k[1] == END_POS[1] and k[2] != 3
    ]
    for n in ends:
        G.add_edge(n, (2000, 2000), weight=data[END_POS[0]][END_POS[1]])

    val = nx.dijkstra_path_length(G, (0, 0), (2000, 2000))
    return val


def part_2():
    pass


print(f"Part 1: {part_1()}, Part 2: {part_2()}")
