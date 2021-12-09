#!/usr/bin/env python3

from itertools import product
from collections import Counter
from functools import reduce

class HeigtMap():
    def __init__(self, heightmap):
        self.heightmap = heightmap

    @property
    def size(self):
        return (len(self.heightmap[0]), len(self.heightmap))

    def get_value(self, x, y):
        assert self.valid_coord(x, y), "Invalid coordinate"
        return self.heightmap[y][x]

    def valid_coord(self, x, y):
        return (x >= 0 and x < self.size[0])\
           and (y >= 0 and y < self.size[1])

    def adjacent_coords(self, x, y):
        coords = [(x-1, y), (x, y-1), (x+1, y), (x, y+1)]
        return list(filter(lambda coord: self.valid_coord(*coord), coords))

    def is_low(self, x, y):
        adj = self.adjacent_coords(x, y)
        return self.get_value(x,y) < min(map(lambda c: self.get_value(*c), adj))

    def flow_downward(self, x, y):
        if self.is_low(x,y):
            return (x,y)
        else:
            adj_values = map(lambda c: (c, self.get_value(*c)), self.adjacent_coords(x,y))
            next_coord = min(adj_values, key=lambda v: v[1])[0]
            return self.flow_downward(*next_coord)


    def __repr__(self):
        return "\n".join(["".join([str(n) for n in row]) for row in self.heightmap])
        
def parse_input(filename):
    with open(filename, "r") as f:
        lines = f.readlines()
    return HeigtMap([[int(n) for n in line.strip()] for line in lines])

def part1(heightmap):
    size_x, size_y = heightmap.size
    risk = 0
    for y in range(size_y):
        for x in range(size_x):
            if heightmap.is_low(x,y):
                risk += heightmap.get_value(x,y) + 1
    print("Result part 1:", risk)

def part2(heightmap):
    size_x, size_y = heightmap.size
    all_coords = product(range(size_x), range(size_y))
    coords = filter(lambda c: not heightmap.get_value(*c) == 9, all_coords)
    basins = Counter(map(lambda c: heightmap.flow_downward(*c), coords))
    basins_sizes = list(basins.items())
    basins_sizes.sort(key=lambda b: b[1])
    result = reduce(lambda a,b:a*b, map(lambda bs: bs[1], basins_sizes[-3:]))
    print("Result part 2:", result)

heightmap = parse_input("input")
part1(heightmap)
part2(heightmap)
