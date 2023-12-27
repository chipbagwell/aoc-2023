from aocd import get_data

data = get_data(day=18, year=2023).splitlines()

OUTSIDE_PAIRS = [('U','R'), ('R','D'), ('D','L'), ('L','U')]
NUM_2_DIR = {
    '0':'R',
    '1':'D',
    '2':'L',
    '3':'U'
}

def segments(p):
    return zip(p, p[1:] + [p[0]])

def area(p):
    return 0.5 * abs(sum(x0*y1 - x1*y0
                         for ((x0, y0), (x1, y1)) in segments(p)))

def parts(part_1):
    input = data
    x = 0
    y = 0
    points = [(y,x)]
    directions = []
    counts = []
    if part_1:
        for d in input:
            tokens = d.split()
            directions.append(tokens[0])
            counts.append(int(tokens[1]))
    else:
        for d in input:
            tokens = d.split()
            directions.append(NUM_2_DIR[tokens[2][7]])
            counts.append(int(tokens[2][2:7], base=16))

    d_pairs = [(directions[i],directions[(i+1)%len(directions)])for i,_ in enumerate(directions)]
    d_pairs = [d_pairs[-1]] + d_pairs
    corners = [1 if step in OUTSIDE_PAIRS else 0 for step in d_pairs]
    for i,(d,c) in enumerate(zip(directions,counts)):
        match d:
            case 'U':
                y -= (c - 1 + corners[i] + corners[i+1])
            case 'D':
                y += (c - 1 + corners[i] + corners[i+1])
            case 'L':
                x -= (c - 1 + corners[i] + corners[i+1])
            case 'R':
                x += (c - 1 + corners[i] + corners[i+1])
        points.append((y,x))
    return int(area(points))

print(f"Part 1: {parts(True)}, Part 2: {parts(False)}")
