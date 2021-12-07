#!/usr/bin/env python3

from functools import reduce

def align_to_position(reference, positions):
    return reduce(lambda x, y: x+y,
            map(lambda position: abs(reference-position), positions)
           )


def parse_input(filename):
    with open(filename, "r") as f:
        line = f.readline()
    positions = [int(n) for n in line.split(",")]
    return positions


def part1(positions):
    all = map(lambda position: align_to_position(position, positions), positions)
    print(min(*all))

positions = parse_input("input")
part1(positions)
