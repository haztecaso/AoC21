#!/usr/bin/env python3

from dataclasses import dataclass

@dataclass
class Number():
    value:int
    marked:bool = False

    def mark(self):
        self.marked = True

    def __repr__(self):
        return f"{self.value}!" if self.marked else f"{self.value}."

class Board():
    def __init__(self, board):
        self.board = board
        self.nrows, self.ncols = (len(board[0]), len(board))

    def mark(self, number):
        for row in self.board:
            for n in row:
                if n.value == number:
                    n.mark()

    @property
    def win(self):
        result = False
        for row in self.board:
            if all([n.marked for n in row]):
                result = True
                break
        for col in map(lambda *a: list(a), *self.board):
            if all([n.marked for n in col]):
                result = True
                break
        return result

    @property
    def score(self):
        result = 0
        for row in self.board:
            for n in row:
                if not n.marked:
                    result += n.value
        return result

    def __repr__(self):
        result = ""
        for row in self.board:
            for n in row:
                result += f"{n}\t"
            result += "\n"
        return result.strip()

with open("input", "r") as f:
    number_list = [int(n) for n in f.readline().strip().split(",")]
    f.readline()
    boards = "".join(f.readlines()).split("\n\n")
    boards = [Board([[ Number(int(num)) for num in row.split()] for row in board.strip().split("\n")]) for board in boards]

def main(number_list, boards):
    for number in number_list:
        for board in boards:
            board.mark(number)
            if board.win:
                print("Result part 1:", board.score*number)
                return

main(number_list, boards)
