#!/usr/bin/env python3

from itertools import groupby
from functools import reduce
from copy import deepcopy

digitsegments = { 0: "ABCEFG", 1: "CF", 2: "ACDEG", 3: "ACDFG", 4: "BCDF", 5: "ABDFG", 6: "ABDEFG", 7: "ACF", 8: "ABCDEFG", 9: "ABCDFG" }
len2segments = {
        n: reduce(lambda a, b: a.union(b),
            map(lambda a: set(a),
                filter(lambda v: len(v) == n, digitsegments.values())
                )
            )
        if any(len(v) == n for v in  digitsegments.values())
        else set()
        for n in range(8)
        }

def str_intersection(a, b):
    return set(a).intersection(b)

class Inclusion():
    def __init__(self, letter, segments):
        self.letter = letter
        self.segments:set = segments

    @property
    def is_equality(self):
        return len(self.segments)==1
    
    @property
    def possible_eqs(self):
        result = []
        for segment in self.segments:
            return [Inclusion(self.letter, {segment}) for segment in self.segments]

    def __repr__(self):
        if self.is_equality:
            return f"{self.letter} = {self.segments.copy().pop()}"
        else:
            return f"{self.letter} ∈ {self.segments}"

class InclusionSet():
    def __init__(self, inclusions):
        self.inclusions = inclusions

    def simplify(self):
        self.merge_inclusions()
        for _ in range(8):
            self.enforce_equalities()

    def merge_inclusions(self):
        self.inclusions.sort(key=lambda inc: inc.letter)
        new_inclusions = []
        for letter, group in groupby(self.inclusions, lambda inc: inc.letter):
            segment_list = list(map(lambda inc: inc.segments, group))
            segments = reduce(lambda a, b: a.intersection(b), segment_list)
            new_inclusions.append(Inclusion(letter,segments)) 
        self.inclusions = new_inclusions

    def insert_eq(self, eq):
        assert eq.is_equality
        self.inclusions.append(eq)

    @property
    def possible_eqs(self):
        result = []
        for inclusion in filter(lambda i: not i.is_equality, self.inclusions):
            result += inclusion.possible_eqs
        return result

    def enforce_equalities(self):
        for eq in filter(lambda i: i.is_equality, self.inclusions):
            letter = eq.letter
            self.inclusions = list(map(lambda inclusion: inclusion if inclusion.is_equality
                    else Inclusion(inclusion.letter, inclusion.segments.difference(eq.segments))
                        , self.inclusions))

    def __add__(self, other):
        result = InclusionSet(self.inclusions + other.inclusions)
        return result
    
    def __repr__(self):
        return "\n".join([str(inclusion) for inclusion in self.inclusions])


class Pattern():
    def __init__(self, raw_str):
        self.letters = raw_str.strip()
        self._inclusions = None

    @property
    def len(self): return len(self.letters)

    @property
    def inclusions(self):
        if not self._inclusions: 
            self._inclusions = InclusionSet([Inclusion(letter, len2segments[self.len]) for letter in self.letters])
        return self._inclusions

    def __repr__(self):
        return self.letters

class PatternSet():
    def __init__(self, raw_str):
        self.patterns = [Pattern(p) for p in raw_str.split()]

    @property
    def inclusions(self):
        inclusions = reduce(lambda a,b: a+b, map(lambda p: p.inclusions, self.patterns))
        inclusions.simplify()
        return inclusions

    def __repr__(self):
        return f"<PatternSet {' '.join(map(lambda p: str(p), self.patterns))} >"

class Entry():
    def __init__(self, raw_str):
        signals_raw, digits_raw = raw_str.split("|")
        self.signals = PatternSet(signals_raw)
        self.digits  = PatternSet(digits_raw)

def guess_equalities(inclusions):
    print(f"guess_equalities")
    print(f"{inclusions.possible_eqs=}")
    print(inclusions)
    input()
    for eq in inclusions.possible_eqs:
        print(f"Insert eq {eq}")
        inclusions_copy = deepcopy(inclusions)
        inclusions_copy.insert_eq(eq)
        inclusions_copy.simplify()
        print(inclusions_copy)
        guess_equalities(inclusions_copy)
        print("E")

def part2(entries):
    entry = Entry("acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab | cdfeb fcadb cdfeb cdbaf")
    patterns = entry.signals
    inclusions = patterns.inclusions
    guess_equalities(inclusions)
        
def parse_input(filename):
    with open(filename, "r") as f:
        lines = f.readlines()
    entries = [Entry(line) for line in lines]
    return entries


entries = parse_input("sample")
part2(entries)
