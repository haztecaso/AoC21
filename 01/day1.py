#!/usr/bin/env python3

with open("input", "r") as f:
    lines = f.readlines()

measures = [int(line.strip()) for line in lines]

last = measures[0]

result_part_1 = 0

for measure in measures[1:-1]:
    if measure > last:
        result_part_1 += 1
    last = measure

print(f"{result_part_1 = }")

i = 0

last = 10000000000000000000000000000000000000
result_part_2 = 0

while i+3 <= len(measures):
    ssum = sum(measures[i: i+3])
    if ssum > last:
        result_part_2 += 1
    last = ssum
    i += 1

print(f"{result_part_2 = }")
