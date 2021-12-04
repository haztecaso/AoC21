#!/usr/bin/env python3

from copy import copy

with open("input", "r") as f:
    lines = f.readlines()

data = [[int(digit) for digit in line.strip()] for line in lines]

def most_common_bit(data, index):
    count = 0
    for value in data:
        count += 1 if value[index] == 0 else -1
    return 0 if count > 0 else 1

def least_common_bit(data, index):
    return int(not(bool(most_common_bit(data,index))))

def data2bin(string):
    result = 0
    for i, d in enumerate(reversed(string)):
        v = int(d)
        result += v*2**i
    return result

gamma = []
epsilon = []
for i in range(len(data[0])):
    gamma.append(most_common_bit(data, i))
    epsilon.append(least_common_bit(data, i))

print("Result part 1:", data2bin(gamma)*data2bin(epsilon))

o2 = copy(data)
for i in range(len(data[0])):
    x = most_common_bit(o2, i)
    o2 = list(filter(lambda value: value[i] == x, o2))
    if len(o2) == 1:
        o2 = o2[0]
        break

co2 = copy(data)
for i in range(len(data[0])):
    x = least_common_bit(co2, i)
    co2 = list(filter(lambda value: value[i] == x, co2))
    if len(co2) == 1:
        co2 = co2[0]
        break

print("Result part 2:", data2bin(o2)*data2bin(co2))
