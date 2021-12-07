#!/usr/bin/env python3

from dataclasses import dataclass

@dataclass
class LanternFish():
    clock:int = 8
    
    def pass_time(self, school):
        if self.clock == 0:
            self.clock = 6
            school.append(LanternFish())
        else:
            self.clock -= 1

    def __repr__(self):
        return str(self.clock)

def parse_input(filename):
    with open(filename, "r") as f:
        line = f.readline()
    clocks = [int(n) for n in line.split(",")]
    return clocks


def part1(clocks, days):
    school = []
    for clock in clocks:
        school.append(LanternFish(clock))
    for i in range(days):
        for k in range(len(school)):
            school[k].pass_time(school)
        print(f"{i}:",len(school))
    print("final len:", len(school))


clocks = parse_input("input")
part1(clocks, 80)
