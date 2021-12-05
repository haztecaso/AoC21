#!/usr/bin/env python3

from dataclasses import dataclass
from itertools import chain

@dataclass
class Pt():
    x:int
    y:int

    def __repr__(self):
        return f"({self.x},{self.y})"

def line_range(a,b):
    return range(min(a,b), max(a,b)+1)

@dataclass
class Ln():
    a:Pt
    b:Pt

    def __repr__(self):
        return f"{self.a}-{self.b}"

    @property
    def is_horizontal(self):
        return self.a.y == self.b.y

    @property
    def is_vertical(self):
        return self.a.x == self.b.x

    @property
    def points(self):
        result = []
        if self.is_horizontal:
            for x in line_range(self.a.x, self.b.x):
                result.append(Pt(x, self.a.y))
        elif self.is_vertical:
            for y in line_range(self.a.y, self.b.y):
                result.append(Pt(self.a.x, y))
        return result


@dataclass
class Table():
    def __init__(self, size):
        self.table = [[0 for _ in range(size[0])] for _ in range(size[1])]

    def mark_point(self, point):
        self.table[point.y][point.x] += 1

    def mark_line(self, line):
        for point in line.points:
            self.mark_point(point)

    def mark_lines(self, lines):
        for line in lines:
            self.mark_line(line)

    @property
    def overlaps(self):
        result = 0
        for row in self.table:
            result += len(list(filter(lambda v: v >= 2, row)))
        return result

    def __repr__(self):
        result = ""
        for row in self.table:
            result += "".join([str(v) if not v==0 else "." for v in row]) + "\n"
        return result.strip()
        

def parse_pt(point_str):
    x, y = map(int, point_str.split(","))
    return Pt(x,y)

def parse_ln(line_str):
    a, b = map(parse_pt, line_str.split("->"))
    return Ln(a,b)

def parse_input(filename):
    with open(filename, "r") as f:
        lines = f.readlines()
    lines = [parse_ln(line.strip()) for line in lines]
    return lines

def lines_corner(lines):
    max_x = max(chain.from_iterable([[line.a.x, line.b.x] for line in lines]))
    max_y = max(chain.from_iterable([[line.a.y, line.b.y] for line in lines]))
    return (max_x, max_y)

def part1(lines):
    table_size = list(map(lambda x: x+1, lines_corner(lines)))
    table = Table(table_size)
    table.mark_lines(lines)
    print("Result part 1:", table.overlaps)

lines = parse_input("example")
part1(lines)
