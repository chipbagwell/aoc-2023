from aocd import get_data

data = get_data(day=15, year=2023).splitlines()
data = ''.join(data)

data2 = "rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7"
def part_1():
    d = data.split(',')
    retval = 0
    for s in d:
        r = 0
        for c in s:
            r = ((r + ord(c)) * 17) % 256
        retval += r        
    return retval


def part_2():
    d = data.split(',')
    retval = 0
    boxes = [{} for i in range(256)]
    for s in d:
        box_id = 0
        for j,c in enumerate(s):
            if c == '=':
                label = s[0:j]
                boxes[box_id][label] = int(s[j+1])
                break
            if c == '-':
                label = s[0:j]
                if label in boxes[box_id].keys():
                    del boxes[box_id][label]
                break
            box_id = ((box_id + ord(c)) * 17) % 256
    lens = sum([(i+1) * (j+1) * v for i,box in enumerate(boxes) for j, (k,v) in enumerate(box.items())])
    return lens


print(f"Part 1: {part_1()}, Part 2: {part_2()}")
