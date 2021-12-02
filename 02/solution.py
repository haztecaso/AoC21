#!/usr/bin/env python3

from enum import Enum, unique
from dataclasses import dataclass

@unique
class CommandName(Enum):
    FORWARD = 1
    DOWN = 2
    UP = 3

def parseCommandName(token_name):
    if token_name == "forward":
        return CommandName.FORWARD
    elif token_name == "up":
        return CommandName.UP
    elif token_name == "down":
        return CommandName.DOWN

def parseCommand(line):
    assert len(line.split()) == 2
    token_name, token_value = line.split()
    return parseCommandName(token_name), int(token_value)

@dataclass
class Position():
    horizontal:int = 0
    depth: int = 0

@dataclass
class Submarine():
    position: Position = Position()
    aim: int = 0

def runCommandPart1(position, command):
    command_name, value = command
    if command_name == CommandName.FORWARD:
        position.horizontal += value
    elif command_name == CommandName.UP:
        position.depth -= value
    elif command_name == CommandName.DOWN:
        position.depth += value

def runCommandPart2(submarine, command):
    command_name, value = command
    if command_name == CommandName.FORWARD:
        submarine.position.horizontal += value
        submarine.position.depth += submarine.aim * value
    elif command_name == CommandName.UP:
        submarine.aim -= value
    elif command_name == CommandName.DOWN:
        submarine.aim += value


with open("input", "r") as f:
    lines = f.readlines()

commands = [parseCommand(line) for line in lines]

position = Position()
for command in commands:
    runCommandPart1(position, command)

print("Result part 1:", position.horizontal * position.depth)

submarine = Submarine()
for command in commands:
    runCommandPart2(submarine, command)

print("Result part 2:", submarine.position.horizontal * submarine.position.depth)
