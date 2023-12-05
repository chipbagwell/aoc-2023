from aocd import get_data
from collections import Counter
from functools import reduce
from math import pow
from operator import add

data2 = get_data(day=5, year=2023).splitlines()
data = [
    "seeds: 79 14 55 13",
    "",
    "seed-to-soil map:",
    "50 98 2",
    "52 50 48",
    "",
    "soil-to-fertilizer map:",
    "0 15 37",
    "37 52 2",
    "39 0 15",
    "",
    "fertilizer-to-water map:",
    "49 53 8",
    "0 11 42",
    "42 0 7",
    "57 7 4",
    "",
    "water-to-light map:",
    "88 18 7",
    "18 25 70",
    "",
    "light-to-temperature map:",
    "45 77 23",
    "81 45 19",
    "68 64 13",
    "",
    "temperature-to-humidity map:",
    "0 69 1",
    "1 0 69",
    "",
    "humidity-to-location map:",
    "60 56 37",
    "56 93 4",
]

def parse_input(data):
    map_inputs = {}
    key = ""
    for s in data:
        match s:
            case "seed-to-soil map:":
                key = "seed-to-soil"
                map_inputs[key] = []

            case "soil-to-fertilizer map:":
                key = "soil-to-fertilizer"
                map_inputs[key] = []

            case "fertilizer-to-water map:":
                key = "fertilizer-to-water"
                map_inputs[key] = []

            case "water-to-light map:":
                key = "water-to-light"
                map_inputs[key] = []

            case "light-to-temperature map:":
                key = "light-to-temperature"
                map_inputs[key] = []

            case "temperature-to-humidity map:":
                key = "temperature-to-humidity"
                map_inputs[key] = []

            case "humidity-to-location map:":
                key = "humidty-to-location"
                map_inputs[key] = []

            case "":
                continue
            
            case x:
                map_inputs[key].append([int(v) for v in x.split()])
    return map_inputs

def apply_map(seeds, mapping):
    """
    mapping = [dest_range_start, source_range_start, range_length]
    """
    retval = []
    for s in seeds:
        for m in mapping:
            if m[1] <= s < (m[1] + m[2]):
                s = m[0] + (s - m[1])
                break
        retval.append(s)
    return retval
    
def apply_maps_to_seed(s, mapping):
    for k,v in mapping.items():
        for m in v:
            if m[1] <= s < (m[1] + m[2]):
                s = m[0] + (s - m[1])
                break
    return s

def part_1():
    seeds = [int(s) for s in data2[0].split()[1:]]
    mapping = parse_input(data2[2:])
    for k, v in mapping.items():
        seeds = apply_map(seeds, v)
    return min(seeds)

def part_2():
    seeds = [int(s) for s in data2[0].split()[1:]]
    mapping = parse_input(data2[2:])
    retval = 999999999999999
    for i in range(0, len(seeds)-1, 2):
        seed_range = seeds[i:i+2]
        for s in range(seed_range[0], seed_range[0]+seed_range[1]):
            retval = min(retval,apply_maps_to_seed(s, mapping))
    return retval

print(f"Part 1: {part_1()}, Part 2: {part_2()}")
