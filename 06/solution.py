#!/usr/bin/env python3

from functools import reduce

class School():
    fishes:dict = {key:0 for key in range(9)}

    def pass_time(self):
        new_generation = self.fishes[0]
        for key in range(1,9):
            self.fishes[key - 1] = self.fishes[key]
        self.fishes[6] += new_generation
        self.fishes[8] = new_generation
    
    @property
    def count(self):
        return reduce(lambda a,b: a+b, self.fishes.values())

    def __repr__(self):
        return str(self.fishes)

def parse_input(filename):
    with open(filename, "r") as f:
        line = f.readline()
    clocks = [int(n) for n in line.split(",")]
    return clocks

def solve(clocks, days):
    school = School()
    for clock in clocks:
        school.fishes[clock] += 1
    for _ in range(days):
        school.pass_time()
    return(school.count)

clocks = parse_input("input")
print("Result part 1:", solve(clocks, 80))
print("Result part 2:", solve(clocks, 256))
