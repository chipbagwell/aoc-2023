from aocd import get_data
import networkx as nx
from pprint import PrettyPrinter

real_data = get_data(day=17, year=2023).splitlines()

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
# Must move a minimum of 4 blocks before you can turn and a max of 10 then must turn.
# 4,5,6,7,8,9,10 are now all valid counts before a turn.
def part_2():
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
            if y > 1:
                if y != END_POS[0]:
                    G.add_edge((y, x, 2, "Down"), (y + 1, x, 3, "Down"), weight=data[y][x])
            if y > 2:
                if y != END_POS[0]:
                    G.add_edge((y, x, 3, "Down"), (y + 1, x, 4, "Down"), weight=data[y][x])
            if y > 3:
                if y != END_POS[0]:
                    G.add_edge((y, x, 4, "Down"), (y + 1, x, 5, "Down"), weight=data[y][x])
                if x != 0:
                    G.add_edge((y, x, 4, "Down"), (y, x - 1, 1, "Left"), weight=data[y][x])
                if x != END_POS[1]:
                    G.add_edge((y, x, 4, "Down"), (y, x + 1, 1, "Right"), weight=data[y][x])
            if y > 4:
                if y != END_POS[0]:
                    G.add_edge((y, x, 5, "Down"), (y + 1, x, 6, "Down"), weight=data[y][x])
                if x != 0:
                    G.add_edge((y, x, 5, "Down"), (y, x - 1, 1, "Left"), weight=data[y][x])
                if x != END_POS[1]:
                    G.add_edge((y, x, 5, "Down"), (y, x + 1, 1, "Right"), weight=data[y][x])
            if y > 5:
                if y != END_POS[0]:
                    G.add_edge((y, x, 6, "Down"), (y + 1, x, 7, "Down"), weight=data[y][x])
                if x != 0:
                    G.add_edge((y, x, 6, "Down"), (y, x - 1, 1, "Left"), weight=data[y][x])
                if x != END_POS[1]:
                    G.add_edge((y, x, 6, "Down"), (y, x + 1, 1, "Right"), weight=data[y][x])
            if y > 6:
                if y != END_POS[0]:
                    G.add_edge((y, x, 7, "Down"), (y + 1, x, 8, "Down"), weight=data[y][x])
                if x != 0:
                    G.add_edge((y, x, 7, "Down"), (y, x - 1, 1, "Left"), weight=data[y][x])
                if x != END_POS[1]:
                    G.add_edge((y, x, 7, "Down"), (y, x + 1, 1, "Right"), weight=data[y][x])
            if y > 7:
                if y != END_POS[0]:
                    G.add_edge((y, x, 8, "Down"), (y + 1, x, 9, "Down"), weight=data[y][x])
                if x != 0:
                    G.add_edge((y, x, 8, "Down"), (y, x - 1, 1, "Left"), weight=data[y][x])
                if x != END_POS[1]:
                    G.add_edge((y, x, 8, "Down"), (y, x + 1, 1, "Right"), weight=data[y][x])
            if y > 8:
                if y != END_POS[0]:
                    G.add_edge((y, x, 9, "Down"), (y + 1, x, 10, "Down"), weight=data[y][x])
                if x != 0:
                    G.add_edge((y, x, 9, "Down"), (y, x - 1, 1, "Left"), weight=data[y][x])
                if x != END_POS[1]:
                    G.add_edge((y, x, 9, "Down"), (y, x + 1, 1, "Right"), weight=data[y][x])
            if y > 9:
                if x != 0:
                    G.add_edge((y, x, 10, "Down"), (y, x - 1, 1, "Left"), weight=data[y][x])
                if x != END_POS[1]:
                    G.add_edge((y, x, 10, "Down"), (y, x + 1, 1, "Right"), weight=data[y][x])

            if y < END_POS[0]:  # U
                if y != 0:
                    G.add_edge((y, x, 1, "Up"), (y - 1, x, 2, "Up"), weight=data[y][x])
            if y < END_POS[0] - 1:
                if y != 0:
                    G.add_edge((y, x, 2, "Up"), (y - 1, x, 3, "Up"), weight=data[y][x])
            if y < END_POS[0] - 2:
                if y != 0:
                    G.add_edge((y, x, 3, "Up"), (y - 1, x, 4, "Up"), weight=data[y][x])
            if y < END_POS[0] - 3:
                if y != 0:
                    G.add_edge((y, x, 4, "Up"), (y - 1, x, 5, "Up"), weight=data[y][x])
                if x != 0:
                    G.add_edge((y, x, 4, "Up"), (y, x - 1, 1, "Left"), weight=data[y][x])
                if x != END_POS[1]:
                    G.add_edge((y, x, 4, "Up"), (y, x + 1, 1, "Right"), weight=data[y][x])
            if y < END_POS[0] - 4:
                if y != 0:
                    G.add_edge((y, x, 5, "Up"), (y - 1, x, 6, "Up"), weight=data[y][x])
                if x != 0:
                    G.add_edge((y, x, 5, "Up"), (y, x - 1, 1, "Left"), weight=data[y][x])
                if x != END_POS[1]:
                    G.add_edge((y, x, 5, "Up"), (y, x + 1, 1, "Right"), weight=data[y][x])
            if y < END_POS[0] - 5:
                if y != 0:
                    G.add_edge((y, x, 6, "Up"), (y - 1, x, 7, "Up"), weight=data[y][x])
                if x != 0:
                    G.add_edge((y, x, 6, "Up"), (y, x - 1, 1, "Left"), weight=data[y][x])
                if x != END_POS[1]:
                    G.add_edge((y, x, 6, "Up"), (y, x + 1, 1, "Right"), weight=data[y][x])
            if y < END_POS[0] - 6:
                if y != 0:
                    G.add_edge((y, x, 7, "Up"), (y - 1, x, 8, "Up"), weight=data[y][x])
                if x != 0:
                    G.add_edge((y, x, 7, "Up"), (y, x - 1, 1, "Left"), weight=data[y][x])
                if x != END_POS[1]:
                    G.add_edge((y, x, 7, "Up"), (y, x + 1, 1, "Right"), weight=data[y][x])
            if y < END_POS[0] - 7:
                if y != 0:
                    G.add_edge((y, x, 8, "Up"), (y - 1, x, 9, "Up"), weight=data[y][x])
                if x != 0:
                    G.add_edge((y, x, 8, "Up"), (y, x - 1, 1, "Left"), weight=data[y][x])
                if x != END_POS[1]:
                    G.add_edge((y, x, 8, "Up"), (y, x + 1, 1, "Right"), weight=data[y][x])
            if y < END_POS[0] - 8:
                if y != 0:
                    G.add_edge((y, x, 9, "Up"), (y - 1, x, 10, "Up"), weight=data[y][x])
                if x != 0:
                    G.add_edge((y, x, 9, "Up"), (y, x - 1, 1, "Left"), weight=data[y][x])
                if x != END_POS[1]:
                    G.add_edge((y, x, 9, "Up"), (y, x + 1, 1, "Right"), weight=data[y][x])
            if y < END_POS[0] - 9:
                if x != 0:
                    G.add_edge((y, x, 10, "Up"), (y, x - 1, 1, "Left"), weight=data[y][x])
                if x != END_POS[1]:
                    G.add_edge((y, x, 10, "Up"), (y, x + 1, 1, "Right"), weight=data[y][x])


            if x > 0:  # R
                if x != END_POS[1]:
                    G.add_edge((y, x, 1, "Right"), (y, x + 1, 2, "Right"), weight=data[y][x])
            if x > 1:  # R
                if x != END_POS[1]:
                    G.add_edge((y, x, 2, "Right"), (y, x + 1, 3, "Right"), weight=data[y][x])
            if x > 2:  # R
                if x != END_POS[1]:
                    G.add_edge((y, x, 3, "Right"), (y, x + 1, 4, "Right"), weight=data[y][x])
                
            if x > 3:
                if x != END_POS[1]:
                    G.add_edge((y, x, 4, "Right"), (y, x + 1, 5, "Right"), weight=data[y][x])
                if y != END_POS[0]:
                    G.add_edge((y, x, 4, "Right"), (y + 1, x, 1, "Down"), weight=data[y][x])
                if y != 0:
                    G.add_edge((y, x, 4, "Right"), (y - 1, x, 1, "Up"), weight=data[y][x])
            if x > 4:
                if x != END_POS[1]:
                    G.add_edge((y, x, 5, "Right"), (y, x + 1, 6, "Right"), weight=data[y][x])
                if y != END_POS[0]:
                    G.add_edge((y, x, 5, "Right"), (y + 1, x, 1, "Down"), weight=data[y][x])
                if y != 0:
                    G.add_edge((y, x, 5, "Right"), (y - 1, x, 1, "Up"), weight=data[y][x])
            if x > 5:
                if x != END_POS[1]:
                    G.add_edge((y, x, 6, "Right"), (y, x + 1, 7, "Right"), weight=data[y][x])
                if y != END_POS[0]:
                    G.add_edge((y, x, 6, "Right"), (y + 1, x, 1, "Down"), weight=data[y][x])
                if y != 0:
                    G.add_edge((y, x, 6, "Right"), (y - 1, x, 1, "Up"), weight=data[y][x])
            if x > 6:
                if x != END_POS[1]:
                    G.add_edge((y, x, 7, "Right"), (y, x + 1, 8, "Right"), weight=data[y][x])
                if y != END_POS[0]:
                    G.add_edge((y, x, 7, "Right"), (y + 1, x, 1, "Down"), weight=data[y][x])
                if y != 0:
                    G.add_edge((y, x, 7, "Right"), (y - 1, x, 1, "Up"), weight=data[y][x])
            if x > 7:
                if x != END_POS[1]:
                    G.add_edge((y, x, 8, "Right"), (y, x + 1, 9, "Right"), weight=data[y][x])
                if y != END_POS[0]:
                    G.add_edge((y, x, 8, "Right"), (y + 1, x, 1, "Down"), weight=data[y][x])
                if y != 0:
                    G.add_edge((y, x, 8, "Right"), (y - 1, x, 1, "Up"), weight=data[y][x])
            if x > 8:
                if x != END_POS[1]:
                    G.add_edge((y, x, 9, "Right"), (y, x + 1, 10, "Right"), weight=data[y][x])
                if y != END_POS[0]:
                    G.add_edge((y, x, 9, "Right"), (y + 1, x, 1, "Down"), weight=data[y][x])
                if y != 0:
                    G.add_edge((y, x, 9, "Right"), (y - 1, x, 1, "Up"), weight=data[y][x])
            if x > 9:
                if y != END_POS[0]:
                    G.add_edge((y, x, 10, "Right"), (y + 1, x, 1, "Down"), weight=data[y][x])
                if y != 0:
                    G.add_edge((y, x, 10, "Right"), (y - 1, x, 1, "Up"), weight=data[y][x])

            if x < END_POS[1]:  # L
                if x != 0:
                    G.add_edge((y, x, 1, "Left"), (y, x - 1, 2, "Left"), weight=data[y][x])
            if x < END_POS[1] - 1:  # L
                if x != 0:
                    G.add_edge((y, x, 2, "Left"), (y, x - 1, 3, "Left"), weight=data[y][x])
            if x < END_POS[1] - 2:  # L
                if x != 0:
                    G.add_edge((y, x, 3, "Left"), (y, x - 1, 4, "Left"), weight=data[y][x])
                
            if x < END_POS[1] - 3:
                if x != 0:
                    G.add_edge((y, x, 4, "Left"), (y, x - 1, 5, "Left"), weight=data[y][x])
                if y != END_POS[0]:
                    G.add_edge((y, x, 4, "Left"), (y + 1, x, 1, "Down"), weight=data[y][x])
                if y != 0:
                    G.add_edge((y, x, 4, "Left"), (y - 1, x, 1, "Up"), weight=data[y][x])
            if x < END_POS[1] - 4:
                if x != 0:
                    G.add_edge((y, x, 5, "Left"), (y, x - 1, 6, "Left"), weight=data[y][x])
                if y != END_POS[0]:
                    G.add_edge((y, x, 5, "Left"), (y + 1, x, 1, "Down"), weight=data[y][x])
                if y != 0:
                    G.add_edge((y, x, 5, "Left"), (y - 1, x, 1, "Up"), weight=data[y][x])
            if x < END_POS[1] - 5:
                if x != 0:
                    G.add_edge((y, x, 6, "Left"), (y, x - 1, 7, "Left"), weight=data[y][x])
                if y != END_POS[0]:
                    G.add_edge((y, x, 6, "Left"), (y + 1, x, 1, "Down"), weight=data[y][x])
                if y != 0:
                    G.add_edge((y, x, 6, "Left"), (y - 1, x, 1, "Up"), weight=data[y][x])
            if x < END_POS[1] - 6:
                if x != 0:
                    G.add_edge((y, x, 7, "Left"), (y, x - 1, 8, "Left"), weight=data[y][x])
                if y != END_POS[0]:
                    G.add_edge((y, x, 7, "Left"), (y + 1, x, 1, "Down"), weight=data[y][x])
                if y != 0:
                    G.add_edge((y, x, 7, "Left"), (y - 1, x, 1, "Up"), weight=data[y][x])
            if x < END_POS[1] - 7:
                if x != 0:
                    G.add_edge((y, x, 8, "Left"), (y, x - 1, 9, "Left"), weight=data[y][x])
                if y != END_POS[0]:
                    G.add_edge((y, x, 8, "Left"), (y + 1, x, 1, "Down"), weight=data[y][x])
                if y != 0:
                    G.add_edge((y, x, 8, "Left"), (y - 1, x, 1, "Up"), weight=data[y][x])
            if x < END_POS[1] - 8:
                if x != 0:
                    G.add_edge((y, x, 9, "Left"), (y, x - 1, 10, "Left"), weight=data[y][x])
                if y != END_POS[0]:
                    G.add_edge((y, x, 9, "Left"), (y + 1, x, 1, "Down"), weight=data[y][x])
                if y != 0:
                    G.add_edge((y, x, 9, "Left"), (y - 1, x, 1, "Up"), weight=data[y][x])

            if x < END_POS[1] - 9:
                if y != END_POS[0]:
                    G.add_edge((y, x, 10, "Left"), (y + 1, x, 1, "Down"), weight=data[y][x])
                if y != 0:
                    G.add_edge((y, x, 10, "Left"), (y - 1, x, 1, "Up"), weight=data[y][x])
    # Graph edges and nodes have been populated
    ends = [
        k
        for k, v in G.nodes.items()
        if k[0] == END_POS[0] and k[1] == END_POS[1] and 3 < k[2] < 10
    ]
    for n in ends:
        G.add_edge(n, (2000, 2000), weight=data[END_POS[0]][END_POS[1]])

    val = nx.dijkstra_path_length(G, (0, 0), (2000, 2000))
    return val


print(f"Part 1: {part_1()}, Part 2: {part_2()}")
