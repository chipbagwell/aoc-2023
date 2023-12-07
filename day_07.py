from aocd import get_data
from collections import Counter
import itertools
from functools import cmp_to_key
from pprint import PrettyPrinter

pp = PrettyPrinter()

data = get_data(day=7, year=2023).splitlines()

data2 = ["32T3K 765", "T55J5 684", "KK677 28", "KTJJT 220", "QQQJA 483"]

RANK_COUNTS = [[1, 1, 1, 1, 1], [2, 1, 1, 1], [2, 2, 1], [3, 1, 1], [3, 2], [4, 1], [5]]
CARD_VALUES = {
    "2": 0,
    "3": 1,
    "4": 2,
    "5": 3,
    "6": 4,
    "7": 5,
    "8": 6,
    "9": 7,
    "T": 8,
    "J": 9,
    "Q": 10,
    "K": 11,
    "A": 12,
}
CARD_VALUES_WILD = {
    "J": 0,
    "2": 1,
    "3": 2,
    "4": 3,
    "5": 4,
    "6": 5,
    "7": 6,
    "8": 7,
    "9": 8,
    "T": 9,
    "Q": 10,
    "K": 11,
    "A": 12,
}


def hand_cmp(x, y):
    if x[1] == y[1]:
        return 0
    x_val = 0
    y_val = 0
    for a, b in zip(x[1], y[1]):
        x_val += (x_val * 13) + CARD_VALUES[a]
        y_val += (y_val * 13) + CARD_VALUES[b]
    return -1 if x_val < y_val else 1

def hand_cmp_wild(x, y):
    if x[1] == y[1]:
        return 0
    x_val = 0
    y_val = 0
    for a, b in zip(x[1], y[1]):
        x_val += (x_val * 13) + CARD_VALUES_WILD[a]
        y_val += (y_val * 13) + CARD_VALUES_WILD[b]
    return -1 if x_val < y_val else 1


def part_1():
    hands = [tuple(l.split()) for l in data]
    freqs = [
        (sorted(list(Counter(h[0]).values()), reverse=True), h[0], h[1])
        for h in hands
    ]
    hand_ranks = [[c for c in freqs if c[0] == rank] for rank in RANK_COUNTS]
    sorted_hand_ranks = list(
        itertools.chain.from_iterable(
            [sorted(rank, key=cmp_to_key(hand_cmp)) for rank in hand_ranks]
        )
    )
    return sum([(i + 1) * int(c[2]) for i, c in enumerate(sorted_hand_ranks)])


def convert_wilds(h):
    if h == "JJJJJ":
      return h
    c = Counter(h)
    if c['J']:
      del c['J']
      h = h.replace('J', c.most_common(1)[0][0])
    return h
    

def part_2():
    hands = [tuple(l.split()) for l in data]
    freqs = [
        (sorted(list(Counter(convert_wilds(h[0])).values()), reverse=True), h[0], h[1])
        for h in hands
    ]
    hand_ranks = [[c for c in freqs if c[0] == rank] for rank in RANK_COUNTS]
    sorted_hand_ranks = list(
        itertools.chain.from_iterable(
            [sorted(rank, key=cmp_to_key(hand_cmp_wild)) for rank in hand_ranks]
        )
    )
    pp.pprint(sorted_hand_ranks)
    return sum([(i + 1) * int(c[2]) for i, c in enumerate(sorted_hand_ranks)])

print(f"Part 1: {part_1()}, Part 2: {part_2()}")
