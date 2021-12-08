#!/usr/bin/env python3
from dataclasses import dataclass

BOLD = '\033[1m'
END = '\033[0m'

def bold(string):
    return f"{BOLD}{string}{END}"

class Pattern():
    def __init__(self, str_pattern):
        self.letters = str_pattern.strip()
        self.marked = False

    @property
    def len(self):
        return len(self.letters)

    def __repr__(self):
        return bold(self.letters) if self.marked else self.letters


def parse_patterns(raw_str):
    return [Pattern(p) for p in raw_str.split()]

class Entry():
    def __init__(self, raw_str):
        self.signals = parse_patterns(raw_str.split("|")[0])
        self.digits  = parse_patterns(raw_str.split("|")[1])

    def __repr__(self):
        return f"{' '.join(map(str, self.signals))} | {' '.join(map(str, self.digits))}"

def count_easy_digits(pattern_list):
    result = 0
    for pattern in pattern_list:
        if pattern.len in [2, 3, 4, 7]:
            pattern.marked = True
            result += 1
    return result

def parse_input(filename):
    with open(filename, "r") as f:
        lines = f.readlines()
    entries = [Entry(line) for line in lines]
    return entries


def part1(entries):
    count = sum(map(lambda entry: count_easy_digits(entry.digits), entries))
    for entry in entries:
        print(entry)
    print(count)

entries = parse_input("input")
part1(entries)
