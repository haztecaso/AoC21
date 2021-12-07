#!/usr/bin/env python3

from functools import reduce

def align_to_position_v1(reference, positions):
    return reduce(lambda x, y: x+y,
            map(lambda position: abs(reference-position), positions)
           )

def fuel_distance(a,b): # (triangular sum)
    n = abs(a-b)
    return n*(n+1)/2

def align_to_position_v2(reference, positions):
    return reduce(lambda x, y: x+y,
            map(lambda position: fuel_distance(reference, position), positions)
           )

def parse_input(filename):
    with open(filename, "r") as f:
        line = f.readline()
    positions = [int(n) for n in line.split(",")]
    return positions


def part1(positions):
    all = map(lambda position: align_to_position_v1(position, positions), positions)
    print("Result part 1:", min(*all))

def part2(positions):
    references = range(min(positions), max(positions)+1)
    all = map(lambda ref: align_to_position_v2(ref, positions), references)
    print("Result part 2:", int(min(*all)))

positions = parse_input("input")
part1(positions)
part2(positions)
