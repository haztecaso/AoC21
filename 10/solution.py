#!/usr/bin/env python3

chars = { "(": ")", "{": "}", "[": "]", "<": ">" }
points = {")": 3, "]": 57, "}": 1197, ">": 25137}
scores = {")": 1, "]": 2, "}": 3, ">": 4}
        
def parse_input(filename):
    with open(filename, "r") as f:
        lines = f.readlines()
    return [line.strip() for line in lines]

def check_line(line):
    stack = []
    for char in line:
        if char in chars.values():
            last = stack.pop()
            if not chars[last] == char:
                raise ValueError(char)
        elif char in chars.keys():
            stack.append(char)
    return stack

def autocomplete_score(line):
    stack = []
    for char in line:
        if char in chars.values():
            last = stack.pop()
            if not chars[last] == char:
                raise ValueError(":(")
        elif char in chars.keys():
            stack.append(char)
    stack.reverse()
    score = 0
    for char in map(lambda c: chars[c], stack):
        score *= 5
        score += scores[char]
    return score

def part1(lines):
    score = 0
    incomplete_segments = []
    for line in lines:
        try:
            incomplete_segments.append(check_line(line))
        except ValueError as e:
            error_char = e.args[0]
            score += points[error_char]
    print("Result part 1:", score)
    return incomplete_segments

def part2(incomplete_segments):
    scores = []
    for line in incomplete_segments:
        scores.append(autocomplete_score(line))
    scores.sort()
    assert len(scores) % 2 == 1
    print("Result part 2:", scores[len(scores) // 2])

lines = parse_input("input")
incomplete_segments = part1(lines)
part2(incomplete_segments)
