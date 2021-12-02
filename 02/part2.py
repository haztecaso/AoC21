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

def runCommand(submarine, command):
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

submarine = Submarine()
for command in commands:
    runCommand(submarine, command)

print(submarine.position.horizontal * submarine.position.depth)
