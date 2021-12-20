#!/usr/bin/env python3

import sys


class BingoTile:
    def __init__(self, number):
        self.number = int(number, 10)
        self.marked = False

    def mark(self, number):
        if number == self.number:
            self.marked = True


class BingoBoard:
    def __init__(self, lines):
        self._last_number = 0
        self._numbers = []
        self._rows = []
        self._cols = ([], [], [], [], [])
        for line in lines:
            row = [BingoTile(num) for num in line.strip().split()]
            self._rows.append(row)
            for idx in range(5):
                tile = row[idx]
                self._numbers.append(tile.number)
                self._cols[idx].append(tile)

    def __repr__(self):
        return str(self)

    def __str__(self):
        return str(self._rows)

    def __iter__(self):
        return iter(self._rows)

    def mark(self, number):
        if number in self._numbers:
            self._numbers.remove(number)
            self._last_number = number
        for row in self._rows:
            for tile in row:
                tile.mark(number)

    def is_winner(self):
        row = any(all(tile.marked for tile in row) for row in self._rows)
        col = any(all(tile.marked for tile in col) for col in self._cols)
        return row or col

    def score(self):
        return sum(self._numbers) * self._last_number


def parse_numbers(line):
    return [int(num, 10) for num in line.strip().split(',')]

def parse_boards(lines):
    boards = []
    while len(lines) > 0:
        lines.pop(0)
        boards.append(BingoBoard(lines[:5]))
        lines = lines[5:]
    return boards


def part1(lines):
    numbers = parse_numbers(lines.pop(0))
    boards = parse_boards(lines)

    winner = None
    while not winner:
        num = numbers.pop(0)
        for board in boards:
            board.mark(num)
            if board.is_winner():
                winner = board
                break
    return winner.score()


def part2(lines):
    pass


def main():
    lines = sys.stdin.readlines()
    print("Part1: {}".format(part1(lines)))
    print("Part2: {}".format(part2(lines)))


if __name__ == "__main__":
    main()

