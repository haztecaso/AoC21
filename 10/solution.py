#!/usr/bin/env python3

chars = { "(": ")", "{": "}", "[": "]", "<": ">" }
points = {")": 3, "]": 57, "}": 1197, ">": 25137}
        
def parse_input(filename):
    with open(filename, "r") as f:
        lines = f.readlines()
    return [line.strip() for line in lines]

def check_line(line):
    stack = []
    result = None
    for char in line:
        if char in chars.values():
            last = stack.pop()
            if not chars[last] == char:
                result = char
        elif char in chars.keys():
            stack.append(char)
    return result

def part1(lines):
    score = 0
    for line in lines:
        error_char = check_line(line)
        if error_char:
            score += points[error_char]
    print("Result part 1:", score)

def part2():
    raise NotImplementedError

lines = parse_input("input")
part1(lines)
# part2()
